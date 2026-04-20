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
    current_code = db.get(target, "// SISTEMA MAIA V12 PROTECTED") if idea and target else "// AGUARDANDO..."

    h = f"""
    <html><head><title>MAIA II - ARQUITECTURA BLINDADA</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:'Courier New', monospace; margin:0; overflow:hidden; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,15,15,0.9); margin-bottom:5px; border-radius:2px; padding:10px; }}
        .flex-main {{ display:flex; gap:10px; height: 82vh; padding:10px; }}
        
        /* CABECERA */
        .header {{ display:flex; align-items:center; gap:15px; padding:15px; background:rgba(0,30,30,0.95); border-bottom:2px solid #0ff; }}
        .input-idea {{ background:#000; color:#0ff; border:1px solid #0ff; padding:10px; flex-grow:1; outline:none; }}
        .btn-gen {{ background:#0ff; color:#000; border:none; padding:10px 20px; font-weight:bold; cursor:pointer; }}

        /* ESTADOS */
        #voice-btn {{ background:#300; color:#f55; border:1px solid #f55; padding:8px 15px; cursor:pointer; font-weight:bold; }}
        #voice-btn.active {{ background:#040; color:#5f5; border-color:#5f5; box-shadow:0 0 10px #0f0; }}
        .btn-mem {{ background:none; color:#f0f; border:1px solid #f0f; padding:8px; cursor:pointer; }}
        .btn-clr {{ background:none; color:#0ff; border:1px solid #0ff; padding:8px; cursor:pointer; }}

        /* RENDERIZADO BLINDADO */
        #proto-container {{ width:100%; height:100%; position:relative; background:#000; overflow:hidden; border:1px solid #0f02; }}
        
        .hw-grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:5px; }}
        .hw-card {{ border:1px solid #f0f3; padding:5px; font-size:0.7em; background:rgba(255,0,255,0.03); }}
        
        /* CHAT */
        #chat-maia {{ position:fixed; bottom:10px; right:10px; width:280px; height:35px; background:rgba(0,25,25,0.98); border:1px solid #0ff; transition:0.3s; z-index:999; }}
        #chat-maia.open {{ height:350px; }}
        #chat-head {{ background:#0ff; color:#000; padding:8px; font-weight:bold; cursor:pointer; display:flex; justify-content:space-between; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.2em;">MAIA II</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='COMANDO DE MISIÓN...' value='{idea}'>
            <button type='submit' class='btn-gen'>GENERAR</button>
        </form>
        <button type='button' id='voice-btn' onclick="toggleVoice()">VOICE: OFF</button>
        <button type='button' class='btn-mem' onclick="alert('Sync OK')">MEMORIA</button>
        <button type='button' class='btn-clr' onclick="window.location.href='/'">LIMPIAR</button>
    </div>

    <div class='flex-main'>
        <div style="width:20%; overflow-y:auto;" class="panel">
            <h4 style="color:#f0f; font-size:0.7em;">NODOS DE SOFTWARE</h4>
            {"".join([f"<form method='post'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; padding:5px;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
        </div>

        <div style="width:50%;" class="panel">
            <div id="proto-container"></div>
        </div>

        <div style="width:30%; overflow-y:auto;" class="panel">
            <h4 style="color:#0ff; font-size:0.7em;">ESPECIFICACIONES HARDWARE</h4>
            <div class='hw-grid'>
                {"".join([f"<div class='hw-card'><b>{k}</b><br>{', '.join(v)}</div>" for k,v in hw_data.items()])}
            </div>
            <h4 style="color:#39ff14; font-size:0.7em; margin-top:15px;">KERNEL INSPECTOR</h4>
            <div style="background:#000; color:#39ff14; padding:10px; font-size:9px; height:200px; overflow-y:auto; border-left:2px solid #f0f;">{current_code}</div>
        </div>
    </div>

    <div id="chat-maia">
        <div id="chat-head" onclick="this.parentElement.classList.toggle('open')">
            <span>MAIA CHAT</span><span>▲</span>
        </div>
        <div style="padding:10px; font-size:11px; height:260px; overflow-y:auto;" id="chat-log">MAIA: Sistema 3D blindado y operativo.</div>
        <input type="text" style="width:100%; background:#000; color:#0ff; border:none; border-top:1px solid #0ff; padding:10px;" placeholder="Mensaje..." onkeydown="if(event.key==='Enter') sendChat(this)">
    </div>

    <script>
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.classList.toggle('active');
            if(btn.classList.contains('active')) {{
                btn.innerText = "VOICE: ON";
                const msg = new SpeechSynthesisUtterance("Hola Alex, ¿en qué puedo ayudarte hoy?");
                msg.lang = 'es-ES'; window.speechSynthesis.speak(msg);
            }} else {{ btn.innerText = "VOICE: OFF"; window.speechSynthesis.cancel(); }}
        }}

        function sendChat(i) {{
            const log = document.getElementById('chat-log');
            log.innerHTML += "<div><b>Alex:</b> "+i.value+"</div>";
            setTimeout(() => {{ log.innerHTML += "<div style='color:#0f0'><b>MAIA:</b> Comando procesado.</div>"; }}, 500);
            i.value = "";
        }}

        // MOTOR 3D BLINDADO
        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(50, container.clientWidth / container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matMetal = new THREE.MeshStandardMaterial({{ color: 0x222222, metalness: 1, roughness: 0.2 }});
            const matProp = new THREE.MeshStandardMaterial({{ color: 0x00ff00, transparent: true, opacity: 0.4 }});

            // CUERPO CENTRAL (Octaedro Blindado)
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.5, 0), matMetal);
            body.scale.y = 0.5;
            droneGroup.add(body);

            // BRAZOS Y HÉLICES
            const props = [];
            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(a => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.4), matMetal);
                arm.rotation.z = Math.PI/2;
                arm.rotation.y = a;
                droneGroup.add(arm);

                const p = new THREE.Mesh(new THREE.CircleGeometry(0.5, 32), matProp);
                p.position.set(Math.cos(a)*0.7, 0.2, Math.sin(a)*0.7);
                p.rotation.x = Math.PI/2;
                droneGroup.add(p);
                props.push(p);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.AmbientLight(0xffffff, 0.5));
            const light = new THREE.PointLight(0x00ffff, 2, 100);
            light.position.set(5, 5, 5);
            scene.add(light);

            camera.position.set(0, 3, 7);
            camera.lookAt(0, 0, 0);

            // BLINDAJE DE REDIMENSIÓN
            window.addEventListener('resize', () => {{
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            }});

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach(p => p.rotation.z += 0.5);
                droneGroup.rotation.y += 0.005;
                droneGroup.position.y = Math.sin(Date.now() * 0.002) * 0.2;
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