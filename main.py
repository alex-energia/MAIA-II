# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance
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
    
    current_code = db.get(target, "// SISTEMA MAIA V11") if idea and target else "// AGUARDANDO..."

    h = f"""
    <html><head><title>MAIA II - VISTA TÁCTICA</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Courier New', monospace; padding:20px; }}
        .panel {{ border:1px solid #0ff; padding:15px; background:rgba(0,10,10,0.95); margin-bottom:15px; box-shadow: inset 0 0 10px #0ff2; }}
        .flex {{ display:flex; gap:15px; }} .col-25 {{ width:25%; }} .col-75 {{ width:75%; }}
        .code-window {{ background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:350px; overflow-y:scroll; white-space:pre-wrap; font-size:11px; }}
        
        #voice-btn {{ 
            background:#900; color:white; border:none; padding:12px 25px; 
            cursor:pointer; font-weight:bold; border-radius:2px; transition: 0.4s;
        }}
        #voice-btn.active {{ background:#0f0; color:black; box-shadow:0 0 20px #0f0; }}
        
        .hw-grid {{ display:grid; grid-template-columns: repeat(4, 1fr); gap:10px; }}
        .hw-card {{ border:1px solid #f0f; padding:8px; background:rgba(255,0,255,0.05); font-size:0.7em; }}
        #proto-container {{ width:100%; height:550px; border:1px solid #0f0; background:radial-gradient(circle, #001 0%, #000 100%); }}
    </style>
    </head><body>
    
    <h1 style='letter-spacing: 5px;'>MAIA II <span style='color:#f0f;'>[ PROTOCOLO DE INGENIERÍA ]</span></h1>

    <div class='panel'>
        <form method='post'>
            <input name='drone_idea' placeholder='COMANDO DE MISIÓN...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:15px; width:50%;'>
            <button type='submit' style='background:#0ff; padding:15px; font-weight:bold; border:none; cursor:pointer;'>INICIALIZAR</button>
            <button type='button' id='voice-btn' onclick="toggleVoice()">MAIA VOICE: OFF</button>
            <button type='button' style='background:none; color:#f0f; border:1px solid #f0f; padding:14px; cursor:pointer;' onclick="window.location.href='/'">CLEAN</button>
        </form>
    </div>

    <div class='flex'>
        <div class='col-25'>
            <div class='panel' style='height:350px; overflow-y:auto; border-color:#f0f;'>
                <h4 style='color:#f0f; margin-top:0;'>NODOS DE VUELO</h4>
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; width:100%; padding:5px; border-bottom:1px solid #0f02;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
        </div>
        <div class='col-75'><div class='panel'><div class='code-window'>{current_code}</div></div></div>
    </div>

    <div class='panel' style='border-color:#f0f;'>
        <div class='hw-grid'>
            {"".join([f"<div class='hw-card'><h4 style='margin:0;color:#f0f;'>{k}</h4><ul style='padding-left:15px;'>"+"".join([f"<li>{i}</li>" for i in v])+"</ul></div>" for k,v in hw_data.items()])}
        </div>
    </div>

    <div class='panel' style='border-color:#0f0;'>
        <h3 style='color:#0f0; margin-top:0;'>RENDERIZADO DE ACTIVOS 3D [ ALTA RESOLUCIÓN ]</h3>
        <div id="proto-container"></div>
    </div>

    <script>
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.classList.toggle('active');
            if(btn.classList.contains('active')) {{
                btn.innerText = "MAIA VOICE: ON";
                const msg = new SpeechSynthesisUtterance("Hola Alex, en qué puedo ayudarte hoy");
                msg.lang = 'es-ES';
                window.speechSynthesis.speak(msg);
            }} else {{
                btn.innerText = "MAIA VOICE: OFF";
                window.speechSynthesis.cancel();
            }}
        }}

        if ('{idea}' !== '') {{
            const container = document.getElementById('proto-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(50, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            
            // MATERIALES AVANZADOS
            const matDark = new THREE.MeshStandardMaterial({{color:0x111111, metalness:1, roughness:0.2}});
            const matGlow = new THREE.MeshBasicMaterial({{color:0x00ff00}});
            const matProp = new THREE.MeshStandardMaterial({{color:0x00ff00, transparent:true, opacity:0.4, side: THREE.DoubleSide}});

            // 1. CHASIS CENTRAL (Diseño Angular)
            const body = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.5, 0.2, 6), matDark);
            droneGroup.add(body);

            // 2. SENSORES FRONTALES (Ojos IA)
            const eye1 = new THREE.Mesh(new THREE.SphereGeometry(0.05, 16, 16), matGlow);
            eye1.position.set(0.15, 0.05, 0.4);
            const eye2 = new THREE.Mesh(new THREE.SphereGeometry(0.05, 16, 16), matGlow);
            eye2.position.set(-0.15, 0.05, 0.4);
            droneGroup.add(eye1, eye2);

            // 3. BRAZOS TUBULARES Y MOTORES
            const props = [];
            const angles = [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4];
            
            angles.forEach(angle => {{
                // Brazo
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 1.2), matDark);
                arm.rotation.z = Math.PI/2;
                arm.rotation.y = angle;
                droneGroup.add(arm);

                // Motor
                const motor = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.15, 16), matDark);
                motor.position.set(Math.cos(angle)*0.6, 0.05, Math.sin(angle)*0.6);
                droneGroup.add(motor);

                // Hélice (Disco de rotación)
                const prop = new THREE.Mesh(new THREE.CircleGeometry(0.45, 32), matProp);
                prop.position.set(Math.cos(angle)*0.6, 0.15, Math.sin(angle)*0.6);
                prop.rotation.x = Math.PI/2;
                droneGroup.add(prop);
                props.push(prop);
            }});

            // 4. TREN DE ATERRIZAJE
            const leg1 = new THREE.Mesh(new THREE.BoxGeometry(0.02, 0.3, 0.6), matDark);
            leg1.position.set(0.2, -0.2, 0);
            const leg2 = new THREE.Mesh(new THREE.BoxGeometry(0.02, 0.3, 0.6), matDark);
            leg2.position.set(-0.2, -0.2, 0);
            droneGroup.add(leg1, leg2);

            scene.add(droneGroup);

            // ILUMINACIÓN
            const light1 = new THREE.PointLight(0x00ffff, 2, 10);
            light1.position.set(2, 2, 2);
            const light2 = new THREE.PointLight(0xff00ff, 1, 10);
            light2.position.set(-2, -2, 2);
            scene.add(light1, light2, new THREE.AmbientLight(0xffffff, 0.3));

            camera.position.set(0, 3, 5);
            camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                // Animación de hélices
                props.forEach(p => p.rotation.z += 0.5);
                
                // Efecto de vuelo (Hover)
                const t = Date.now() * 0.002;
                droneGroup.position.y = Math.sin(t) * 0.15;
                droneGroup.rotation.x = Math.sin(t * 0.5) * 0.05;
                droneGroup.rotation.z = Math.cos(t * 0.5) * 0.05;
                
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