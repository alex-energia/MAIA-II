# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance, get_hardware_integrity_hash
    from model3d_engine import get_3d_model_data
except:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}
    def get_3d_model_data(x): return {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    
    current_code = db.get(target, "// NODO SELECCIONADO") if idea and target else "// AGUARDANDO..."

    h = f"""
    <html><head><title>MAIA II - PROTOCOLO V11</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000808; color:#0ff; font-family:monospace; padding:20px; }}
        .panel {{ border:1px solid #0ff; padding:15px; background:rgba(0,15,15,0.9); margin-bottom:15px; }}
        .flex {{ display:flex; gap:15px; }} .col-25 {{ width:25%; }} .col-75 {{ width:75%; }}
        .code-window {{ background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:350px; overflow-y:scroll; white-space:pre-wrap; font-size:11px; }}
        
        #voice-btn {{ 
            background:#ff0000; color:white; border:none; padding:10px 20px; 
            cursor:pointer; font-weight:bold; border-radius:4px; transition: 0.3s;
        }}
        #voice-btn.active {{ background:#00ff00; color:black; box-shadow:0 0 15px #00ff00; }}
        
        .hw-grid {{ display:grid; grid-template-columns: repeat(4, 1fr); gap:10px; margin-top:10px; }}
        .hw-card {{ border:1px solid #f0f; padding:8px; background:rgba(255,0,255,0.05); font-size:0.7em; }}
        #proto-container {{ width:100%; height:450px; border:1px solid #0f0; background:#000; position:relative; }}
    </style>
    </head><body>
    
    <h1>MAIA II [ GLOBAL LOGISTICS INTELLIGENCE ]</h1>

    <div class='panel'>
        <form method='post'>
            <input name='drone_idea' placeholder='DEFINA MISIÓN...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:12px; width:60%;'>
            <button type='submit' style='background:#0ff; padding:12px; font-weight:bold; border:none; cursor:pointer;'>GENERAR ECOSISTEMA</button>
            <button type='button' id='voice-btn' onclick="toggleVoice()">VOZ MAIA: OFF</button>
            <button type='button' style='background:none; color:#f0f; border:1px solid #f0f; padding:10px; cursor:pointer;' onclick="window.location.href='/'">LIMPIAR</button>
        </form>
    </div>

    <div class='flex'>
        <div class='col-25'>
            <div class='panel' style='height:350px; overflow-y:auto;'>
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; width:100%;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
        </div>
        <div class='col-75'><div class='panel'><div class='code-window'>{current_code}</div></div></div>
    </div>

    <div class='panel'>
        <h3 style='color:#0ff;'>ESPECIFICACIONES DE HARDWARE</h3>
        <div class='hw-grid'>
            {"".join([f"<div class='hw-card'><h4>{k}</h4><ul>"+"".join([f"<li>{i}</li>" for i in v])+"</ul></div>" for k,v in hw_data.items()])}
        </div>
    </div>

    <div class='panel' style='border-color:#0f0;'>
        <h3 style='color:#0f0;'>PROTOTIPO DINÁMICO (BRAZOS Y HÉLICES)</h3>
        <div id="proto-container"></div>
    </div>

    <script>
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.classList.toggle('active');
            if(btn.classList.contains('active')) {{
                btn.innerText = "VOZ MAIA: ON";
                const msg = new SpeechSynthesisUtterance("Hola Alex, en qué puedo ayudarte hoy");
                msg.lang = 'es-ES';
                window.speechSynthesis.speak(msg);
            }} else {{
                btn.innerText = "VOZ MAIA: OFF";
                window.speechSynthesis.cancel();
            }}
        }}

        if ('{idea}' !== '') {{
            const container = document.getElementById('proto-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            // Cuerpo
            const body = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.2, 0.6), new THREE.MeshStandardMaterial({{color:0x333333}}));
            droneGroup.add(body);

            // Brazos y Hélices
            const props = [];
            const armCoords = [[0.5, 0.5], [-0.5, 0.5], [0.5, -0.5], [-0.5, -0.5]];
            armCoords.forEach(coord => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 0.8), new THREE.MeshStandardMaterial({{color:0x555555}}));
                arm.rotation.z = Math.PI/2;
                arm.rotation.y = Math.atan2(coord[1], coord[0]);
                droneGroup.add(arm);

                const prop = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.01, 0.05), new THREE.MeshStandardMaterial({{color:0x00ff00}}));
                prop.position.set(coord[0], 0.15, coord[1]);
                droneGroup.add(prop);
                props.push(prop);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.AmbientLight(0xffffff, 0.8));
            camera.position.set(0, 2, 3);
            camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach(p => p.rotation.y += 0.3);
                droneGroup.position.y = Math.sin(Date.now()*0.002)*0.1;
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
