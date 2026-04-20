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
    current_code = db.get(target, "// SISTEMA MAIA V12") if idea and target else "// AGUARDANDO..."

    h = f"""
    <html><head><title>MAIA II - ELITE DASHBOARD</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Courier New', monospace; padding:10px; margin:0; overflow:hidden; }}
        .panel {{ border:1px solid #0ff2; padding:10px; background:rgba(0,12,12,0.9); margin-bottom:8px; border-radius:2px; }}
        .flex {{ display:flex; gap:8px; height: 80vh; }} 
        .col-nodes {{ width:18%; }} .col-render {{ width:52%; }} .col-data {{ width:30%; }}
        
        /* BARRA TÁCTICA */
        .cmd-bar {{ display:flex; gap:10px; background:rgba(0,30,30,0.9); padding:12px; border-bottom:2px solid #0ff; margin-bottom:10px; }}
        .input-idea {{ background:#000; color:#0ff; border:1px solid #0ff; padding:10px; flex-grow:1; font-size:1em; outline:none; }}
        .btn-gen {{ background:#0ff; color:#000; border:none; padding:0 20px; font-weight:bold; cursor:pointer; }}

        /* CONTROL DE VOZ Y MEMORIA */
        #voice-btn {{ background:#300; color:#f55; border:1px solid #f55; padding:8px 12px; cursor:pointer; font-size:11px; }}
        #voice-btn.active {{ background:#040; color:#5f5; border-color:#5f5; box-shadow:0 0 10px #0f0; }}
        .btn-fucsia {{ background:none; color:#f0f; border:1px solid #f0f; padding:8px 12px; cursor:pointer; font-size:11px; }}
        .btn-cyan {{ background:none; color:#0ff; border:1px solid #0ff; padding:8px 12px; cursor:pointer; font-size:11px; }}

        /* HARDWARE GRID (8 CATEGORÍAS) */
        .hw-grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:5px; height: 35vh; overflow-y:auto; }}
        .hw-card {{ border:1px solid #f0f3; padding:6px; font-size:0.65em; background:rgba(255,0,255,0.02); }}
        .hw-card b {{ color:#f0f; display:block; border-bottom:1px solid #f0f2; margin-bottom:3px; }}

        /* CHAT MAIA ELASTIC */
        #chat-maia {{ 
            position: fixed; bottom: 15px; right: 15px; width: 280px; height: 35px; 
            background: rgba(0,25,25,0.98); border: 1px solid #0ff; display: flex; flex-direction: column; 
            z-index:200; transition: height 0.4s cubic-bezier(0.4, 0, 0.2, 1); overflow:hidden;
        }}
        #chat-maia.expanded {{ height: 380px; }}
        #chat-head {{ background:#0ff; color:#000; padding:8px; font-weight:bold; cursor:pointer; font-size:11px; display:flex; justify-content:space-between; }}
        #chat-log {{ flex-grow: 1; padding: 8px; font-size: 10px; overflow-y: auto; color: #fff; }}
        #chat-in {{ background:#000; border:none; border-top:1px solid #0ff; color:#0ff; padding:10px; font-size:11px; outline:none; }}
        
        #proto-container {{ width:100%; height:100%; min-height:450px; background:radial-gradient(circle at center, #001515 0%, #000 100%); }}
        .code-window {{ background:#000; color:#39ff14; padding:8px; border-left:2px solid #f0f; height:28vh; overflow-y:auto; font-size:9px; }}
    </style>
    </head><body>
    
    <div class='cmd-bar'>
        <h3 style='margin:0; color:#0ff; border-right:2px solid #0ff; padding-right:15px;'>MAIA II</h3>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='COMANDO DE MISIÓN...' value='{idea}'>
            <button type='submit' class='btn-gen'>DESPLEGAR ECOSISTEMA</button>
        </form>
        <div style="display:flex; gap:5px;">
            <button type='button' id='voice-btn' onclick="toggleVoice()">VOICE: OFF</button>
            <button type='button' class='btn-fucsia' onclick="alert('Datos Sincronizados')">MEMORIA</button>
            <button type='button' class='btn-cyan' onclick="window.location.href='/'">LIMPIAR</button>
        </div>
    </div>

    <div class='flex'>
        <div class='col-nodes'>
            <div class='panel' style='height:95%; overflow-y:auto;'>
                <h4 style='color:#f0f; font-size:0.7em; margin:0 0 10px 0;'>RTOS NODES</h4>
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.75em; text-align:left; width:100%; padding:4px;'>[RUN] {n}</button></form>" for n in sorted(db.keys())])}
            </div>
        </div>

        <div class='col-render'>
            <div class='panel' style='height:95%; padding:0; position:relative; overflow:hidden; border-color:#0f04;'>
                <div id="proto-container"></div>
                <div style="position:absolute; bottom:10px; left:10px; font-size:9px; color:#0f0; pointer-events:none;">
                    RENDERING: QUAD-ARM STEALH V4 | {get_hardware_integrity_hash()}
                </div>
            </div>
        </div>

        <div class='col-data'>
            <div class='panel'>
                <h4 style='color:#0ff; font-size:0.7em; margin:0 0 8px 0;'>HARDWARE LAYER (8 CAPAS)</h4>
                <div class='hw-grid'>
                    {"".join([f"<div class='hw-card'><b>{k}</b>{', '.join(v)}</div>" for k,v in hw_data.items()])}
                </div>
            </div>
            <div class='panel'>
                <h4 style='color:#39ff14; font-size:0.7em; margin:0 0 8px 0;'>NODE INSPECTOR</h4>
                <div class='code-window'>{current_code}</div>
            </div>
        </div>
    </div>

    <div id="chat-maia">
        <div id="chat-head" onclick="toggleChat()">
            <span>MAIA CORE INTELLIGENCE</span>
            <span id="chat-ico">▲</span>
        </div>
        <div id="chat-log">MAIA: Alex, sistema de 8 capas restaurado. Esperando instrucciones de vuelo.</div>
        <input type="text" id="chat-in" placeholder="Escribir comando..." onkeydown="if(event.key==='Enter') sendChat()">
    </div>

    <script>
        function toggleChat() {{
            const c = document.getElementById('chat-maia');
            c.classList.toggle('expanded');
            document.getElementById('chat-ico').innerText = c.classList.contains('expanded') ? "▼" : "▲";
        }}

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
            const i = document.getElementById('chat-in');
            const l = document.getElementById('chat-log');
            if(!i.value) return;
            l.innerHTML += "<div><b style='color:#f0f;'>ALEX:</b> " + i.value + "</div>";
            setTimeout(() => {{
                l.innerHTML += "<div><b style='color:#0f0;'>MAIA:</b> Comando procesado en Nodo 04. Sincronizando hardware...</div>";
                l.scrollTop = l.scrollHeight;
            }}, 600);
            i.value = "";
            l.scrollTop = l.scrollHeight;
        }}

        if ('{idea}' !== '') {{
            const container = document.getElementById('proto-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(40, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matMetal = new THREE.MeshStandardMaterial({{color:0x0a0a0a, metalness:1, roughness:0.2}});
            const matCyan = new THREE.MeshBasicMaterial({{color:0x00ffff}});
            const matProp = new THREE.MeshStandardMaterial({{color:0x00ff00, transparent:true, opacity:0.3, side: THREE.DoubleSide}});

            // 1. CHASIS AERODINÁMICO COMPLEX
            const body = new THREE.Mesh(new THREE.CapsuleGeometry(0.3, 0.5, 4, 8), matMetal);
            body.rotation.x = Math.PI/2;
            droneGroup.add(body);
            
            // 2. SENSORES DE NAVEGACIÓN (LUCES)
            const lightL = new THREE.Mesh(new THREE.SphereGeometry(0.04), matCyan);
            lightL.position.set(0.15, 0, 0.45);
            const lightR = new THREE.Mesh(new THREE.SphereGeometry(0.04), matCyan);
            lightR.position.set(-0.15, 0, 0.45);
            droneGroup.add(lightL, lightR);

            // 3. BRAZOS Y HÉLICES (X-CONFIGURATION)
            const props = [];
            const angles = [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4];
            angles.forEach(a => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.4), matMetal);
                arm.rotation.z = Math.PI/2;
                arm.rotation.y = a;
                droneGroup.add(arm);

                const motor = new THREE.Mesh(new THREE.CylinderGeometry(0.09, 0.09, 0.25), matMetal);
                motor.position.set(Math.cos(a)*0.7, 0.1, Math.sin(a)*0.7);
                droneGroup.add(motor);

                const p = new THREE.Mesh(new THREE.CircleGeometry(0.55, 32), matProp);
                p.position.set(Math.cos(a)*0.7, 0.25, Math.sin(a)*0.7);
                p.rotation.x = Math.PI/2;
                droneGroup.add(p);
                props.push(p);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.AmbientLight(0xffffff, 0.3));
            const spot = new THREE.SpotLight(0x00ffff, 2); spot.position.set(5, 10, 5);
            scene.add(spot);

            camera.position.set(0, 5, 8);
            camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach((p, i) => p.rotation.z += (i % 2 === 0 ? 0.8 : -0.8));
                const t = Date.now() * 0.001;
                droneGroup.position.y = Math.sin(t*1.5) * 0.2;
                droneGroup.rotation.y += 0.003;
                droneGroup.rotation.z = Math.sin(t) * 0.05;
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