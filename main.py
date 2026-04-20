# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance
except:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    
    current_code = db.get(target, "// KERNEL MAIA II ACTIVE") if idea and target else "// ESPERANDO COMANDO TÁCTICO..."

    h = f"""
    <html><head><title>MAIA II - COMMAND CENTER</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Segoe UI', monospace; padding:15px; margin:0; overflow:hidden; }}
        .panel {{ border:1px solid #0ff3; padding:12px; background:rgba(0,10,10,0.9); margin-bottom:10px; border-radius:4px; }}
        .flex {{ display:flex; gap:10px; height: 82vh; }} .col-20 {{ width:20%; }} .col-55 {{ width:55%; }} .col-25 {{ width:25%; }}
        
        /* BARRA DE COMANDO SUPERIOR */
        .cmd-bar {{ display:flex; gap:10px; background:rgba(0,20,20,0.8); padding:15px; border-bottom:2px solid #0ff; margin-bottom:15px; }}
        .input-idea {{ background:#000; color:#0ff; border:1px solid #0ff; padding:12px; flex-grow:1; font-size:1.1em; outline:none; }}
        .btn-gen {{ background:#0ff; color:#000; border:none; padding:0 25px; font-weight:bold; cursor:pointer; text-transform:uppercase; }}

        /* BOTONES DE ESTADO */
        #voice-btn {{ background:#400; color:#f66; border:1px solid #f66; padding:8px 15px; cursor:pointer; font-weight:bold; }}
        #voice-btn.active {{ background:#060; color:#6f6; border-color:#6f6; box-shadow:0 0 10px #0f0; }}
        .btn-ctrl {{ background:none; color:#f0f; border:1px solid #f0f; padding:8px; cursor:pointer; font-size:11px; }}
        .btn-mem {{ background:none; color:#0ff; border:1px solid #0ff; padding:8px; cursor:pointer; font-size:11px; }}
        
        /* CHAT MAIA EXPANDIBLE */
        #chat-maia {{ 
            position: fixed; bottom: 20px; right: 20px; width: 300px; height: 40px; 
            background: rgba(0,30,30,0.95); border: 1px solid #0ff; display: flex; flex-direction: column; 
            z-index:100; transition: height 0.4s ease; overflow:hidden; border-radius: 5px 5px 0 0;
        }}
        #chat-maia.expanded {{ height: 400px; }}
        #chat-header {{ background:#0ff; color:#000; padding:10px; font-weight:bold; cursor:pointer; display:flex; justify-content:space-between; }}
        #chat-log {{ flex-grow: 1; padding: 10px; font-size: 11px; overflow-y: auto; color: #fff; background:#000505; }}
        #chat-input {{ background:#000; border:none; border-top:1px solid #0ff; color:#0ff; padding:12px; outline:none; }}
        
        /* CONTENEDOR 3D */
        #proto-container {{ width:100%; height:100%; min-height:400px; background:radial-gradient(circle, #001 0%, #000 100%); position:relative; }}
        .code-window {{ background:#000; color:#39ff14; padding:10px; border-left:2px solid #f0f; height:250px; overflow-y:auto; font-size:10px; }}
        .hw-card {{ border:1px solid #0ff2; padding:5px; margin-bottom:5px; font-size:0.7em; background:rgba(0,255,255,0.02); }}
    </style>
    </head><body>
    
    <div class='cmd-bar'>
        <div style="display:flex; align-items:center; gap:20px; width:100%;">
            <h2 style='margin:0; font-size:1.2em;'>MAIA II</h2>
            <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
                <input name='drone_idea' class='input-idea' placeholder='DESPLEGAR NUEVA MISIÓN LOGÍSTICA...' value='{idea}'>
                <button type='submit' class='btn-gen'>GENERAR</button>
            </form>
            <div style="display:flex; gap:8px;">
                <button type='button' id='voice-btn' onclick="toggleVoice()">VOICE: OFF</button>
                <button type='button' class='btn-ctrl' onclick="alert('Memoria Sincronizada')">MEMORIA</button>
                <button type='button' class='btn-mem' onclick="window.location.href='/'">LIMPIAR</button>
            </div>
        </div>
    </div>

    <div class='flex'>
        <div class='col-20'>
            <div class='panel' style='height:95%; overflow-y:auto;'>
                <h4 style='color:#f0f; margin:0 0 10px 0;'>ENGINE NODES</h4>
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; width:100%; padding:5px;'>>> {n}</button></form>" for n in sorted(db.keys())])}
            </div>
        </div>

        <div class='col-55'>
            <div class='panel' style='height:95%; padding:0; position:relative; overflow:hidden;'>
                <div id="proto-container"></div>
                <div style="position:absolute; top:10px; left:10px; font-size:10px; color:#0f0; background:rgba(0,0,0,0.6); padding:5px;">
                    SISTEMA: {idea if idea else "STANDBY"} | PROTOCOLO V3.2
                </div>
            </div>
        </div>

        <div class='col-25'>
            <div class='panel' style='height:45%; overflow-y:auto;'>
                <h4 style='color:#0ff; margin-top:0;'>HARDWARE</h4>
                {"".join([f"<div class='hw-card'><b>{k}</b><br>{', '.join(v)}</div>" for k,v in hw_data.items()])}
            </div>
            <div class='panel' style='height:47%;'>
                <h4 style='color:#39ff14; margin-top:0;'>INSPECTOR</h4>
                <div class='code-window'>{current_code}</div>
            </div>
        </div>
    </div>

    <div id="chat-maia">
        <div id="chat-header" onclick="toggleChat()">
            <span>CORE CHAT: MAIA</span>
            <span id="chat-icon">▲</span>
        </div>
        <div id="chat-log">MAIA: Sistema listo. ¿Cuál es nuestra misión, Alex?</div>
        <input type="text" id="chat-input" placeholder="Comando de voz/texto..." onkeydown="if(event.key==='Enter') sendChat()">
    </div>

    <script>
        // CONTROL DEL CHAT
        function toggleChat() {{
            const chat = document.getElementById('chat-maia');
            const icon = document.getElementById('chat-icon');
            chat.classList.toggle('expanded');
            icon.innerText = chat.classList.contains('expanded') ? "▼" : "▲";
        }}

        // VOZ FEMENINA NEUTRAL
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.classList.toggle('active');
            if(btn.classList.contains('active')) {{
                btn.innerText = "VOICE: ON";
                const msg = new SpeechSynthesisUtterance("Hola Alex, ¿en qué puedo ayudarte hoy?");
                msg.lang = 'es-ES'; msg.pitch = 1.0; msg.rate = 1.0;
                window.speechSynthesis.speak(msg);
            }} else {{
                btn.innerText = "VOICE: OFF";
                window.speechSynthesis.cancel();
            }}
        }}

        function sendChat() {{
            const input = document.getElementById('chat-input');
            const log = document.getElementById('chat-log');
            if(!input.value) return;
            log.innerHTML += "<div><b style='color:#f0f;'>ALEX:</b> " + input.value + "</div>";
            setTimeout(() => {{
                log.innerHTML += "<div><b style='color:#0f0;'>MAIA:</b> Comando recibido. Ajustando parámetros de ingeniería para " + '{idea}' + ".</div>";
                log.scrollTop = log.scrollHeight;
            }}, 600);
            input.value = "";
            log.scrollTop = log.scrollHeight;
        }}

        // MOTOR 3D REFORZADO (Three.js)
        if ('{idea}' !== '') {{
            const container = document.getElementById('proto-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matDark = new THREE.MeshStandardMaterial({{color:0x1a1a1a, metalness:0.8, roughness:0.2}});
            const matProp = new THREE.MeshStandardMaterial({{color:0x00ffcc, transparent:true, opacity:0.3, side: THREE.DoubleSide}});

            // CUERPO AERODINÁMICO
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.4, 0), matDark);
            body.scale.y = 0.4;
            droneGroup.add(body);
            
            // BRAZOS Y HÉLICES (X-FRAME)
            const props = [];
            const angles = [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4];
            angles.forEach(a => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.05, 1.3), matDark);
                arm.rotation.z = Math.PI/2;
                arm.rotation.y = a;
                droneGroup.add(arm);

                const motor = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.2), matDark);
                motor.position.set(Math.cos(a)*0.65, 0.1, Math.sin(a)*0.65);
                droneGroup.add(motor);

                const p = new THREE.Mesh(new THREE.CircleGeometry(0.5, 32), matProp);
                p.position.set(Math.cos(a)*0.65, 0.25, Math.sin(a)*0.65);
                p.rotation.x = Math.PI/2;
                droneGroup.add(p);
                props.push(p);
            }});

            // SENSORES LÁSER
            const sensor = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.1, 0.2), new THREE.MeshBasicMaterial({{color:0x00ff00}}));
            sensor.position.set(0, 0, 0.35);
            droneGroup.add(sensor);

            scene.add(droneGroup);
            scene.add(new THREE.AmbientLight(0xffffff, 0.4));
            const light = new THREE.PointLight(0x00ffff, 2, 50);
            light.position.set(5, 5, 5);
            scene.add(light);

            camera.position.set(0, 4, 7);
            camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach((p, i) => p.rotation.z += (i % 2 === 0 ? 0.6 : -0.6));
                const t = Date.now() * 0.001;
                droneGroup.position.y = Math.sin(t*2) * 0.15;
                droneGroup.rotation.y += 0.005;
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