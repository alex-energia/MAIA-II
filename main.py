# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance, get_hardware_integrity_hash
except:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}
    def get_hardware_integrity_hash(): return "RECOVERY"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    
    current_code = db.get(target, "// SISTEMA OPERATIVO MAIA") if idea and target else "// AGUARDANDO MISIÓN..."

    h = f"""
    <html><head><title>MAIA II - INTERFAZ BRUTAL</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000505; color:#0ff; font-family:'Courier New', monospace; padding:20px; }}
        .panel {{ border:1px solid #0ff; padding:15px; background:rgba(0,15,15,0.9); margin-bottom:15px; }}
        .flex {{ display:flex; gap:15px; }} .col-25 {{ width:25%; }} .col-75 {{ width:75%; }}
        .code-window {{ background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:350px; overflow-y:scroll; white-space:pre-wrap; font-size:11px; }}
        
        #voice-btn {{ 
            background:#ff0000; color:white; border:none; padding:12px 20px; 
            cursor:pointer; font-weight:bold; border-radius:4px; transition: 0.3s;
        }}
        #voice-btn.active {{ background:#00ff00; color:black; box-shadow:0 0 20px #00ff00; }}
        
        .btn-memoria {{ background:none; color:#f0f; border:1px solid #f0f; padding:10px; cursor:pointer; font-weight:bold; }}
        .hw-grid {{ display:grid; grid-template-columns: repeat(4, 1fr); gap:10px; margin-top:10px; }}
        .hw-card {{ border:1px solid #f0f; padding:8px; background:rgba(255,0,255,0.05); font-size:0.7em; }}
        #proto-container {{ width:100%; height:500px; border:1px solid #0f0; background:#000; position:relative; overflow:hidden; }}
    </style>
    </head><body>
    
    <h1>MAIA II <span style='color:#f0f;'>[ GLOBAL LOGISTICS INTELLIGENCE ]</span></h1>

    <div class='panel'>
        <form method='post'>
            <div style='display:flex; gap:10px;'>
                <input name='drone_idea' placeholder='DEFINA LA MISIÓN...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:15px; flex-grow:1;'>
                <button type='submit' style='background:#0ff; padding:15px; font-weight:bold; border:none; cursor:pointer;'>GENERAR ECOSISTEMA</button>
            </div>
            <div style='display:flex; gap:10px; margin-top:10px;'>
                <button type='button' id='voice-btn' onclick="toggleVoice()">VOZ MAIA: OFF</button>
                <button type='button' class='btn-memoria' onclick="window.location.href='/'">LIMPIAR MEMORIA</button>
            </div>
        </form>
    </div>

    <div class='flex'>
        <div class='col-25'>
            <div class='panel' style='height:350px; overflow-y:auto; border-color:#f0f;'>
                <h3 style='color:#f0f; font-size:0.8em;'>SOFTWARE (NODOS)</h3>
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; width:100%; padding:4px;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
        </div>
        <div class='col-75'><div class='panel'><div class='code-window'>{current_code}</div></div></div>
    </div>

    <div class='panel'>
        <h3 style='color:#0ff;'>HARDWARE INTEGRADO</h3>
        <div class='hw-grid'>
            {"".join([f"<div class='hw-card'><h4>{k}</h4><ul>"+"".join([f"<li>{i}</li>" for i in v])+"</ul></div>" for k,v in hw_data.items()])}
        </div>
    </div>

    <div class='panel' style='border-color:#0f0;'>
        <h3 style='color:#0f0;'>PROTOTIPO DINÁMICO MAIA-II [ ALTA RESOLUCIÓN ]</h3>
        <div id="proto-container"></div>
    </div>

    <script>
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.classList.toggle('active');
            if(btn.classList.contains('active')) {{
                btn.innerText = "VOZ MAIA: ON";
                const msg = new SpeechSynthesisUtterance("Hola Alex, ¿en qué puedo ayudarte hoy?");
                
                // Configuración de voz femenina neutral
                const voices = window.speechSynthesis.getVoices();
                msg.voice = voices.find(v => v.lang.includes('es') && (v.name.includes('Google') || v.name.includes('Female')));
                msg.pitch = 1.1;
                msg.rate = 1.0;
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
            const camera = new THREE.PerspectiveCamera(60, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matBlack = new THREE.MeshStandardMaterial({{color:0x111111, metalness:0.9, roughness:0.1}});
            const matGlow = new THREE.MeshBasicMaterial({{color:0x00ff00}});
            const matProp = new THREE.MeshStandardMaterial({{color:0x00ff00, transparent:true, opacity:0.4, side: THREE.DoubleSide}});

            // 1. Cuerpo Hexagonal
            const body = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.5, 0.15, 6), matBlack);
            droneGroup.add(body);

            // 2. Sensores Frontales
            const s1 = new THREE.Mesh(new THREE.SphereGeometry(0.04, 8, 8), matGlow);
            s1.position.set(0.15, 0.05, 0.35);
            const s2 = new THREE.Mesh(new THREE.SphereGeometry(0.04, 8, 8), matGlow);
            s2.position.set(-0.15, 0.05, 0.35);
            droneGroup.add(s1, s2);

            // 3. Brazos y Motores Detallados
            const props = [];
            const armAngles = [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4];
            
            armAngles.forEach(angle => {{
                // Brazos tubulares
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.025, 0.025, 1.1), matBlack);
                arm.rotation.z = Math.PI/2;
                arm.rotation.y = angle;
                droneGroup.add(arm);

                // Motores cilíndricos
                const motor = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 0.12, 16), matBlack);
                motor.position.set(Math.cos(angle)*0.55, 0.05, Math.sin(angle)*0.55);
                droneGroup.add(motor);

                // Hélices (Efecto disco)
                const prop = new THREE.Mesh(new THREE.CircleGeometry(0.4, 32), matProp);
                prop.position.set(Math.cos(angle)*0.55, 0.15, Math.sin(angle)*0.55);
                prop.rotation.x = Math.PI/2;
                droneGroup.add(prop);
                props.push(prop);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.AmbientLight(0xffffff, 0.5));
            const light = new THREE.PointLight(0x00ffff, 2, 10);
            light.position.set(2, 2, 2);
            scene.add(light);

            camera.position.set(0, 2, 4);
            camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach(p => p.rotation.z += 0.5);
                const t = Date.now() * 0.001;
                droneGroup.position.y = Math.sin(t*2) * 0.1;
                droneGroup.rotation.x = Math.sin(t) * 0.05;
                droneGroup.rotation.z = Math.cos(t) * 0.05;
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