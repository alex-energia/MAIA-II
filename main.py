# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance, get_hardware_integrity_hash
    from model3d_engine import get_3d_model_data, get_3d_integrity_hash
except Exception as e:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}
    def get_3d_model_data(x): return {}
    def get_hardware_integrity_hash(): return "RECOVERY"
    def get_3d_integrity_hash(): return "RECOVERY"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    m3d_data = get_3d_model_data(idea)
    current_code = db.get(target, "// SISTEMA MAIA") if idea and target else "// AGUARDANDO..."

    # El HTML usa {{ y }} para escapar de la f-string de Python
    h = f"""
    <html><head><title>MAIA II - VOICE INTERFACE</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000505; color:#0ff; font-family:monospace; padding:20px; }}
        .panel {{ border:1px solid #0ff; padding:15px; background:rgba(0,10,10,0.9); margin-bottom:15px; }}
        .flex {{ display:flex; gap:15px; }} .col-25 {{ width:25%; }} .col-75 {{ width:75%; }}
        .code-window {{ background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:350px; overflow-y:scroll; white-space:pre-wrap; font-size:11px; }}
        .btn-gen {{ background:#0ff; color:#000; padding:15px; font-weight:bold; border:none; cursor:pointer; width:100%; }}
        
        /* BOTÓN DE VOZ MAIA - DINÁMICO */
        #voice-btn {{
            background: #ff0000; color: #fff; border: none; padding: 10px 20px; 
            font-weight: bold; cursor: pointer; border-radius: 5px; transition: 0.3s;
        }}
        #voice-btn.active {{ background: #00ff00; color: #000; box-shadow: 0 0 15px #00ff00; }}
        
        .calc-bar {{ background:#0ff; color:#000; padding:10px; display:flex; justify-content:space-around; font-weight:bold; margin-bottom:10px; }}
        #proto-container {{ width:100%; height:400px; border:1px solid #0f0; background:#000; }}
    </style>
    </head><body>
    
    <h1>MAIA II <span style='color:#f0f;'>[ VOICE & 3D ]</span></h1>

    <div class='panel'>
        <form method='post' id='main-form'>
            <div style='display:flex; gap:10px;'>
                <input name='drone_idea' placeholder='MISIÓN...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:12px; flex-grow:1;'>
                <button type='submit' class='btn-gen' style='width:auto;'>GENERAR</button>
            </div>
            <div style='display:flex; gap:10px; margin-top:10px;'>
                <button type='button' id='voice-btn' onclick="toggleVoice()">VOZ MAIA: OFF</button>
                <button type='button' style='background:none; border:1px solid #0ff; color:#0ff; cursor:pointer;' onclick="window.location.href='/'">LIMPIAR</button>
            </div>
        </form>
    </div>

    <div class='flex'>
        <div class='col-25'>
            <div class='panel' style='height:350px; overflow-y:auto;'>
                {"".join([f"<form method='post'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; width:100%; text-align:left;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
        </div>
        <div class='col-75'><div class='panel'><div class='code-window'>{current_code}</div></div></div>
    </div>

    <div class='panel' style='border-color:#0f0;'>
        <div id="proto-container"></div>
    </div>

    <script>
        let isListening = false;
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            isListening = !isListening;
            
            if (isListening) {{
                btn.classList.add('active');
                btn.innerText = "VOZ MAIA: ON";
                // Saludo inicial
                const msg = new SpeechSynthesisUtterance("Hola Alex, ¿en qué puedo ayudarte hoy?");
                msg.lang = 'es-ES';
                window.speechSynthesis.speak(msg);
                console.log("Escuchando...");
            }} else {{
                btn.classList.remove('active');
                btn.innerText = "VOZ MAIA: OFF";
                window.speechSynthesis.cancel();
            }}
        }}

        // Lógica Simple de Three.js para el Dron
        if ('{idea}' !== '') {{
            const container = document.getElementById('proto-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);
            
            const geometry = new THREE.BoxGeometry(1, 0.2, 1);
            const material = new THREE.MeshStandardMaterial({{color: 0x00ff00}});
            const drone = new THREE.Mesh(geometry, material);
            scene.add(drone);
            
            const light = new THREE.PointLight(0xffffff, 1, 100);
            light.position.set(5, 5, 5);
            scene.add(light);
            camera.position.z = 3;

            function animate() {{
                requestAnimationFrame(animate);
                drone.rotation.y += 0.01;
                renderer.render(scene, camera);
            }}
            animate();
        }}
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)