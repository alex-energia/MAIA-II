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
    <html><head><title>MAIA II - ELITE INTERFACE</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Segoe UI', monospace; padding:15px; margin:0; overflow:hidden; }}
        .panel {{ border:1px solid #0ff3; padding:12px; background:rgba(0,10,10,0.9); margin-bottom:10px; border-radius:4px; }}
        .flex {{ display:flex; gap:10px; height: 85vh; }} .col-20 {{ width:20%; }} .col-50 {{ width:50%; }} .col-30 {{ width:30%; }}
        .code-window {{ background:#000; color:#39ff14; padding:15px; border-left:3px solid #f0f; height:300px; overflow-y:auto; font-size:10px; border-radius:4px; }}
        
        /* BOTONES */
        #voice-btn {{ background:#400; color:#f66; border:1px solid #f66; padding:8px 15px; cursor:pointer; font-weight:bold; }}
        #voice-btn.active {{ background:#060; color:#6f6; border-color:#6f6; box-shadow:0 0 10px #0f0; }}
        .btn-ctrl {{ background:none; color:#f0f; border:1px solid #f0f; padding:8px; cursor:pointer; font-size:11px; }}
        .btn-mem {{ background:none; color:#0ff; border:1px solid #0ff; padding:8px; cursor:pointer; font-size:11px; }}
        
        /* CHAT BOX */
        #chat-maia {{ 
            position: fixed; bottom: 20px; right: 20px; width: 280px; height: 350px; 
            background: rgba(0,20,20,0.95); border: 1px solid #0ff; display: flex; flex-direction: column; z-index:100;
        }}
        #chat-log {{ flex-grow: 1; padding: 10px; font-size: 11px; overflow-y: auto; color: #fff; }}
        #chat-input {{ background:#000; border:none; border-top:1px solid #0ff; color:#0ff; padding:10px; outline:none; }}
        
        #proto-container {{ width:100%; height:100%; background:radial-gradient(circle, #001 0%, #000 100%); }}
        .hw-card {{ border:1px solid #0ff2; padding:5px; margin-bottom:5px; font-size:0.7em; background:rgba(0,255,255,0.02); }}
    </style>
    </head><body>
    
    <div style='display:flex; justify-content:space-between; align-items:center; padding-bottom:10px;'>
        <h2 style='margin:0; letter-spacing:3px;'>MAIA II <span style='color:#f0f; font-size:0.6em;'>[ V3 BRUTAL-SPEC ]</span></h2>
        <div>
            <button type='button' id='voice-btn' onclick="toggleVoice()">VOICE: OFF</button>
            <button type='button' class='btn-ctrl' onclick="alert('Memoria Sincronizada')">MEMORIA</button>
            <button type='button' class='btn-mem' onclick="window.location.href='/'">LIMPIAR</button>
        </div>
    </div>

    <div class='flex'>
        <div class='col-20'>
            <div class='panel' style='height:90%; overflow-y:auto;'>
                <h4 style='color:#f0f; margin:0 0 10px 0;'>ENGINE NODES</h4>
                {"".join([f"<form method='post'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; width:100%; padding:5px;'>>> {n}</button></form>" for n in sorted(db.keys())])}
            </div>
        </div>

        <div class='col-50'>
            <div class='panel' style='height:90%; padding:0; position:relative;'>
                <div id="proto-container"></div>
                <div style="position:absolute; top:10px; left:10px; font-size:10px; background:rgba(0,0,0,0.7); padding:5px; border:1px solid #0f0;">
                    STATUS: FLIGHT_READY | HASH: {hex(id(idea)) if idea else "0x0"}
                </div>
            </div>
        </div>

        <div class='col-30'>
            <div class='panel' style='height:40%; overflow-y:auto;'>
                <h4 style='color:#0ff;'>HARDWARE LAYER</h4>
                {"".join([f"<div class='hw-card'><b>{k}</b>: {', '.join(v)}</div>" for k,v in hw_data.items()])}
            </div>
            <div class='panel' style='height:45%;'>
                <h4 style='color:#39ff14;'>NODE INSPECTOR</h4>
                <div class='code-window'>{current_code}</div>
            </div>
        </div>
    </div>

    <div id="chat-maia">
        <div style="background:#0ff; color:#000; padding:5px; font-weight:bold; font-size:12px;">CORE CHAT: MAIA</div>
        <div id="chat-log">MAIA: Sistema listo. ¿Cuál es nuestra misión, Alex?</div>
        <input type="text" id="chat-input" placeholder="Escribir comando..." onkeydown="if(event.key==='Enter') sendChat()">
    </div>

    <script>
        // SISTEMA DE VOZ NEUTRAL
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

        // CHAT DINÁMICO
        function sendChat() {{
            const input = document.getElementById('chat-input');
            const log = document.getElementById('chat-log');
            if(!input.value) return;
            log.innerHTML += "<div><b>ALEX:</b> " + input.value + "</div>";
            
            // Simulación de respuesta IA
            setTimeout(() => {{
                log.innerHTML += "<div style='color:#0f0'><b>MAIA:</b> Comando procesado. Optimizando parámetros de vuelo...</div>";
                log.scrollTop = log.scrollHeight;
            }}, 800);
            
            input.value = "";
            log.scrollTop = log.scrollHeight;
        }}

        // RENDERIZADO DRON V3 BRUTAL
        if ('{idea}' !== '') {{
            const container = document.getElementById('proto-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matMetal = new THREE.MeshStandardMaterial({{color:0x222222, metalness:1, roughness:0.2}});
            const matCarbon = new THREE.MeshStandardMaterial({{color:0x111111, metalness:0.5, roughness:0.5}});
            const matLight = new THREE.MeshBasicMaterial({{color:0x00ff00}});
            const matProp = new THREE.MeshStandardMaterial({{color:0x00ff00, transparent:true, opacity:0.3, side: THREE.DoubleSide}});

            // CUERPO REFORZADO
            const body = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.4, 0.25, 8), matMetal);
            droneGroup.add(body);
            
            // BRAZOS REFORZADOS (4)
            const props = [];
            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(angle => {{
                const armGroup = new THREE.Group();
                // Brazo tubular
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.2), matCarbon);
                arm.rotation.z = Math.PI/2;
                armGroup.add(arm);
                
                // Motor Detail
                const motor = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.2, 16), matMetal);
                motor.position.set(0.6, 0.05, 0);
                armGroup.add(motor);
                
                // Hélice
                const prop = new THREE.Mesh(new THREE.CircleGeometry(0.5, 32), matProp);
                prop.position.set(0.6, 0.2, 0);
                prop.rotation.x = Math.PI/2;
                armGroup.add(prop);
                props.push(prop);

                armGroup.rotation.y = angle;
                droneGroup.add(armGroup);
            }});

            // TREN DE ATERRIZAJE TÁCTICO
            const legGeo = new THREE.BoxGeometry(0.05, 0.5, 0.05);
            const l1 = new THREE.Mesh(legGeo, matMetal); l1.position.set(0.2, -0.3, 0.2); l1.rotation.x = 0.3;
            const l2 = new THREE.Mesh(legGeo, matMetal); l2.position.set(-0.2, -0.3, 0.2); l2.rotation.x = 0.3;
            droneGroup.add(l1, l2);

            scene.add(droneGroup);
            
            // LUCES
            const ambient = new THREE.AmbientLight(0xffffff, 0.4);
            const spot = new THREE.SpotLight(0x00ffff, 2); spot.position.set(2,5,2);
            scene.add(ambient, spot);

            camera.position.set(0, 3, 6);
            camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach(p => p.rotation.z += 0.4);
                const t = Date.now() * 0.001;
                droneGroup.position.y = Math.sin(t*2) * 0.2;
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
