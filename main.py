# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

# Importaciones de los 3 Agentes Blindados
try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance
    from strategic_engine import get_strategic_analysis
except Exception as e:
    print(f"Error de importación: {e}")
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}
    def get_strategic_analysis(x): return {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    # Ejecución de Agentes
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    strat_data = get_strategic_analysis(idea)
    
    current_code = db.get(target, "// SISTEMA MAIA V13 ACTIVATED") if idea and target else "// AGUARDANDO COMANDO TÁCTICO..."

    h = f"""
    <html><head><title>MAIA II - ECOSISTEMA INTEGRAL BLINDADO</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Segoe UI', monospace; margin:0; overflow:hidden; font-size:12px; }}
        .panel {{ border:1px solid #0f02; background:rgba(0,12,12,0.95); border-radius:4px; padding:12px; overflow-y:auto; }}
        
        /* CABECERA TÁCTICA */
        .header {{ display:flex; align-items:center; gap:15px; padding:15px; background:rgba(0,35,35,0.98); border-bottom:3px solid #0ff; box-shadow:0 0 20px #0ff4; }}
        .input-idea {{ background:#000; color:#0ff; border:2px solid #0ff; padding:12px; flex-grow:1; outline:none; font-size:1em; }}
        .btn-gen {{ background:#0ff; color:#000; border:none; padding:12px 25px; font-weight:bold; cursor:pointer; text-transform:uppercase; }}

        /* BOTONES DE CONTROL */
        #voice-btn {{ background:#300; color:#f66; border:1px solid #f66; padding:10px; cursor:pointer; font-weight:bold; }}
        #voice-btn.active {{ background:#050; color:#6f6; border-color:#6f6; box-shadow:0 0 10px #0f0; }}
        .btn-mem {{ background:none; color:#f0f; border:1px solid #f0f; padding:10px; cursor:pointer; font-weight:bold; }}
        .btn-clr {{ background:none; color:#0ff; border:1px solid #0ff; padding:10px; cursor:pointer; font-weight:bold; }}

        /* GRID PRINCIPAL */
        .grid-layout {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:82vh; padding:10px; box-sizing:border-box; }}
        
        /* COLUMNA IZQUIERDA: ESTRATEGIA */
        .strat-card {{ margin-bottom:12px; border-left:3px solid #0ff; padding-left:10px; }}
        .strat-title {{ color:#f0f; font-weight:bold; font-size:0.85em; text-transform:uppercase; }}
        .strat-desc {{ color:#ccc; font-size:0.8em; line-height:1.3; text-align:justify; margin-top:3px; }}

        /* COLUMNA CENTRAL: DRON */
        #proto-container {{ width:100%; height:100%; position:relative; background:#000; border:1px solid #0f02; overflow:hidden; }}

        /* COLUMNA DERECHA: HW & SW */
        .hw-grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:5px; margin-bottom:15px; }}
        .hw-card {{ border:1px solid #f0f3; padding:5px; font-size:0.65em; background:rgba(255,0,255,0.02); }}
        .code-window {{ background:#000; color:#39ff14; padding:10px; border-left:3px solid #f0f; height:250px; overflow-y:auto; font-size:9px; white-space:pre-wrap; }}

        /* CHAT MAIA */
        #chat-maia {{ position:fixed; bottom:15px; right:15px; width:280px; height:38px; background:rgba(0,25,25,0.98); border:2px solid #0ff; transition:0.4s; z-index:1000; overflow:hidden; border-radius:4px 4px 0 0; }}
        #chat-maia.open {{ height:350px; box-shadow:0 0 25px #0ff5; }}
        #chat-head {{ background:#0ff; color:#000; padding:10px; font-weight:bold; cursor:pointer; display:flex; justify-content:space-between; }}
        #chat-log {{ padding:10px; font-size:10px; height:245px; overflow-y:auto; }}
        #chat-in {{ width:100%; background:#000; color:#0ff; border:none; border-top:1px solid #0ff; padding:10px; outline:none; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.4em; letter-spacing:2px;">MAIA II <span style="color:#0f0;">[V13-COMPLETE]</span></b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='DESPLEGAR ESTRATEGIA...' value='{idea}'>
            <button type='submit' class='btn-gen'>GENERAR ECOSISTEMA</button>
        </form>
        <button type='button' id='voice-btn' onclick="toggleVoice()">VOICE: OFF</button>
        <button type='button' class='btn-mem' onclick="alert('Sync de Memoria Finalizado')">MEMORIA</button>
        <button type='button' class='btn-clr' onclick="window.location.href='/'">LIMPIAR</button>
    </div>

    <div class='grid-layout'>
        <div class="panel">
            <h4 style="color:#0ff; border-bottom:1px solid #0ff3; padding-bottom:5px; margin-top:0;">INTELIGENCIA ESTRATÉGICA</h4>
            {"".join([f"<div class='strat-card'><div class='strat-title'>{k}</div><div class='strat-desc'>{v}</div></div>" for k,v in strat_data.items()])}
        </div>

        <div class="panel" style="padding:0; position:relative;">
            <div id="proto-container"></div>
            <div style="position:absolute; top:10px; left:10px; background:rgba(0,0,0,0.7); padding:5px; border:1px solid #0f0; font-size:9px; color:#0f0;">RENDER: ACTIVE | V13_BLINDADO</div>
        </div>

        <div class="panel">
            <h4 style="color:#0ff; margin-top:0;">HARDWARE (8 CAPAS)</h4>
            <div class='hw-grid'>
                {"".join([f"<div class='hw-card'><b>{k}</b>{', '.join(v)}</div>" for k,v in hw_data.items()])}
            </div>
            
            <h4 style="color:#f0f; margin-top:10px;">SOFTWARE RTOS NODES</h4>
            <div style="margin-bottom:10px; max-height:120px; overflow-y:auto;">
                {"".join([f"<form method='post' style='margin:2px;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; width:100%;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            
            <h4 style="color:#39ff14; font-size:0.8em;">INSPECTOR: {target if target else "NULL"}</h4>
            <div class='code-window'>{current_code}</div>
        </div>
    </div>

    <div id="chat-maia">
        <div id="chat-head" onclick="document.getElementById('chat-maia').classList.toggle('open')">
            <span>MAIA CORE INTEL</span><span>▲</span>
        </div>
        <div id="chat-log">MAIA: Alex, todos los sistemas blindados están en línea.</div>
        <input type="text" id="chat-in" placeholder="Escribir comando..." onkeydown="if(event.key==='Enter') sendChat(this)">
    </div>

    <script>
        // CONTROL DE VOZ
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.classList.toggle('active');
            if(btn.classList.contains('active')) {{
                btn.innerText = "VOICE: ON";
                const msg = new SpeechSynthesisUtterance("Hola Alex, ecosistema completo y blindado en línea.");
                msg.lang = 'es-ES'; window.speechSynthesis.speak(msg);
            }} else {{ btn.innerText = "VOICE: OFF"; window.speechSynthesis.cancel(); }}
        }}

        function sendChat(i) {{
            const log = document.getElementById('chat-log');
            if(!i.value) return;
            log.innerHTML += "<div><b style='color:#f0f;'>Alex:</b> "+i.value+"</div>";
            setTimeout(() => {{ log.innerHTML += "<div><b style='color:#0f0;'>MAIA:</b> Nodo sincronizado.</div>"; log.scrollTop = log.scrollHeight; }}, 500);
            i.value = "";
        }}

        // MOTOR 3D V13 BLINDADO
        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matCarbon = new THREE.MeshStandardMaterial({{color:0x050505, metalness:1, roughness:0.1}});
            const matCyan = new THREE.MeshBasicMaterial({{color:0x00ffff}});
            const matProp = new THREE.MeshStandardMaterial({{color:0x00ff00, transparent:true, opacity:0.3, side: THREE.DoubleSide}});

            // CUERPO AERODINÁMICO
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.5, 0), matCarbon);
            body.scale.y = 0.4;
            droneGroup.add(body);
            
            // OJOS LÁSER
            const eye = new THREE.Mesh(new THREE.SphereGeometry(0.04), matCyan);
            const eyeL = eye.clone(); eyeL.position.set(0.2, 0, 0.4);
            const eyeR = eye.clone(); eyeR.position.set(-0.2, 0, 0.4);
            droneGroup.add(eyeL, eyeR);

            // BRAZOS Y HÉLICES
            const props = [];
            const angles = [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4];
            angles.forEach(a => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.4), matCarbon);
                arm.rotation.z = Math.PI/2; arm.rotation.y = a;
                droneGroup.add(arm);

                const p = new THREE.Mesh(new THREE.CircleGeometry(0.5, 32), matProp);
                p.position.set(Math.cos(a)*0.7, 0.2, Math.sin(a)*0.7); p.rotation.x = Math.PI/2;
                droneGroup.add(p); props.push(p);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.AmbientLight(0xffffff, 0.3));
            const light = new THREE.SpotLight(0x00ffff, 2); light.position.set(5, 5, 5);
            scene.add(light);

            camera.position.set(0, 4, 8); camera.lookAt(0,0,0);

            // AUTO-AJUSTE BLINDADO
            new ResizeObserver(() => {{
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            }}).observe(container);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach(p => p.rotation.z += 0.8);
                droneGroup.rotation.y += 0.005;
                droneGroup.position.y = Math.sin(Date.now()*0.002) * 0.2;
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