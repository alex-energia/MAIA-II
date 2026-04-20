# -*- coding: utf-8 -*-
# main.py - NÚCLEO MAESTRO MAIA II [FASE DE BLINDAJE TOTAL]
from flask import Flask, render_template_string, request

# Importaciones de los 3 Agentes Blindados
try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance
    from strategic_engine import get_strategic_analysis
except Exception as e:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}
    def get_strategic_analysis(x): return {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    # Ejecución de Ecosistema
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    
    current_code = db.get(target, "// KERNEL MAIA II EN LÍNEA") if idea and target else "// AGUARDANDO COMANDO..."

    h = f"""
    <html><head><title>MAIA II - BLINDAJE NIVEL 14</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Segoe UI', monospace; margin:0; overflow:hidden; font-size:12px; }}
        .panel {{ border:1px solid #0f02; background:rgba(0,15,15,0.95); border-radius:4px; padding:12px; overflow:hidden; display:flex; flex-direction:column; }}
        
        /* CABECERA DE CONTROL SUPERIOR (BLINDADA) */
        .header {{ display:flex; align-items:center; gap:12px; padding:12px 20px; background:rgba(0,40,40,0.98); border-bottom:3px solid #0ff; box-shadow:0 0 20px #0ff5; z-index:100; }}
        .input-idea {{ background:#000; color:#0ff; border:2px solid #0ff; padding:10px; flex-grow:1; outline:none; font-size:1em; border-radius:2px; }}
        
        /* BOTONERA TÁCTICA */
        .btn-action {{ background:#0ff; color:#000; border:none; padding:10px 18px; font-weight:bold; cursor:pointer; text-transform:uppercase; font-size:10px; }}
        .btn-proj {{ background:none; color:#f0f; border:1px solid #f0f; padding:10px 15px; cursor:pointer; font-size:10px; font-weight:bold; }}
        .btn-new {{ background:none; color:#0f0; border:1px solid #0f0; padding:10px 15px; cursor:pointer; font-size:10px; font-weight:bold; }}
        
        /* ESTADOS MAIA */
        #voice-btn {{ background:#200; color:#f66; border:1px solid #f66; padding:10px; cursor:pointer; font-weight:bold; font-size:10px; }}
        #voice-btn.active {{ background:#040; color:#6f6; border-color:#6f6; box-shadow:0 0 10px #0f0; }}

        /* GRID DE INTERFAZ */
        .main-layout {{ display:grid; grid-template-columns: 28% 42% 30%; gap:10px; height:84vh; padding:10px; box-sizing:border-box; }}
        
        /* ESTRATEGIA (IZQUIERDA) */
        .strat-scroll {{ overflow-y:auto; flex-grow:1; }}
        .strat-card {{ margin-bottom:12px; border-left:3px solid #0ff; padding-left:10px; background:rgba(0,255,255,0.02); padding-top:5px; padding-bottom:5px; }}
        .strat-title {{ color:#f0f; font-weight:bold; font-size:0.85em; text-transform:uppercase; }}
        .strat-desc {{ color:#ccc; font-size:0.8em; line-height:1.4; text-align:justify; }}

        /* RENDER (CENTRO) */
        #proto-container {{ width:100%; height:100%; position:relative; background:radial-gradient(circle, #001 0%, #000 100%); border:1px solid #0f02; }}

        /* HW & SW (DERECHA) */
        .hw-grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:5px; margin-bottom:10px; }}
        .hw-card {{ border:1px solid #f0f2; padding:5px; font-size:0.65em; background:rgba(255,0,255,0.02); }}
        .code-window {{ background:#000; color:#39ff14; padding:10px; border-left:3px solid #f0f; flex-grow:1; overflow-y:auto; font-size:9px; white-space:pre-wrap; border-radius:0 0 4px 4px; }}

        /* CHAT ELÁSTICO */
        #chat-maia {{ position:fixed; bottom:15px; right:15px; width:280px; height:38px; background:rgba(0,25,25,0.98); border:2px solid #0ff; transition:0.4s; z-index:1000; overflow:hidden; border-radius:4px 4px 0 0; }}
        #chat-maia.open {{ height:350px; box-shadow:0 0 25px #0ff5; }}
        #chat-head {{ background:#0ff; color:#000; padding:10px; font-weight:bold; cursor:pointer; display:flex; justify-content:space-between; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.3em; letter-spacing:1px; color:#0ff;">MAIA II</b>
        
        <button type='button' class='btn-proj' onclick="alert('Abriendo buscador de proyectos...')">BUSCADOR PROYECTOS</button>
        <button type='button' class='btn-new' onclick="window.location.href='/'">NUEVO PROYECTO</button>

        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='DEFINIR MISIÓN ESTRATÉGICA...' value='{idea}'>
            <button type='submit' class='btn-action'>GENERAR</button>
        </form>

        <button type='button' id='voice-btn' onclick="toggleVoice()">VOICE: OFF</button>
        <button type='button' class='btn-proj' style="color:#0ff; border-color:#0ff;" onclick="alert('Memoria Sincronizada')">MEMORIA</button>
    </div>

    <div class='main-layout'>
        <div class="panel">
            <h4 style="color:#0ff; border-bottom:1px solid #0ff3; padding-bottom:5px; margin-top:0;">INTELIGENCIA ESTRATÉGICA</h4>
            <div class="strat-scroll">
                {"".join([f"<div class='strat-card'><div class='strat-title'>{k}</div><div class='strat-desc'>{v}</div></div>" for k,v in strat_data.items()])}
            </div>
        </div>

        <div class="panel" style="padding:0; position:relative; border-color:#0f04;">
            <div id="proto-container"></div>
            <div style="position:absolute; bottom:10px; right:10px; font-size:9px; color:#0f0; background:rgba(0,0,0,0.6); padding:4px;">MAIA_DRONE_V14_BLINDADO</div>
        </div>

        <div class="panel">
            <h4 style="color:#0ff; margin-top:0; font-size:0.85em;">HARDWARE (8 CAPAS)</h4>
            <div class='hw-grid'>
                {"".join([f"<div class='hw-card'><b>{k}</b></div>" for k in hw_data.keys()])}
            </div>
            
            <h4 style="color:#f0f; margin-top:5px; font-size:0.85em;">SOFTWARE NODES</h4>
            <div style="max-height:100px; overflow-y:auto; margin-bottom:10px; border-bottom:1px solid #f0f2;">
                {"".join([f"<form method='post' style='margin:1px;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.85em; text-align:left; width:100%;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            
            <h4 style="color:#39ff14; font-size:0.8em; margin:0; background:#000; padding:5px; border:1px solid #39ff1433; border-bottom:none;">INSPECTOR: {target if target else "SYSTEM"}</h4>
            <div class='code-window'>{current_code}</div>
        </div>
    </div>

    <div id="chat-maia">
        <div id="chat-head" onclick="this.parentElement.classList.toggle('open')">
            <span>MAIA CORE INTEL</span><span>▲</span>
        </div>
        <div style="padding:10px; font-size:10px; height:245px; overflow-y:auto;" id="chat-log">MAIA: Alex, proyecto blindado. Módulos de gestión restaurados.</div>
        <input type="text" id="chat-in" style="width:100%; background:#000; color:#0ff; border:none; border-top:1px solid #0ff; padding:10px;" placeholder="Comando..." onkeydown="if(event.key==='Enter') sendChat(this)">
    </div>

    <script>
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.classList.toggle('active');
            if(btn.classList.contains('active')) {{
                btn.innerText = "VOICE: ON";
                const msg = new SpeechSynthesisUtterance("Protocolo de blindaje V14 activo. ¿Iniciamos la misión?");
                msg.lang = 'es-ES'; window.speechSynthesis.speak(msg);
            }} else {{ btn.innerText = "VOICE: OFF"; window.speechSynthesis.cancel(); }}
        }}

        function sendChat(i) {{
            const log = document.getElementById('chat-log');
            if(!i.value) return;
            log.innerHTML += "<div><b style='color:#f0f;'>Alex:</b> "+i.value+"</div>";
            setTimeout(() => {{ log.innerHTML += "<div><b style='color:#0f0;'>MAIA:</b> Procesado.</div>"; log.scrollTop = log.scrollHeight; }}, 500);
            i.value = "";
        }}

        // RENDER V14 BLINDADO
        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matCarbon = new THREE.MeshStandardMaterial({{color:0x080808, metalness:1, roughness:0.1}});
            const matCyan = new THREE.MeshBasicMaterial({{color:0x00ffff}});
            
            // CHASIS
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.5, 0), matCarbon);
            body.scale.y = 0.4;
            droneGroup.add(body);

            // BRAZOS Y HÉLICES (NEÓN)
            const props = [];
            const matProp = new THREE.MeshStandardMaterial({{color:0x00ff00, transparent:true, opacity:0.35, side:THREE.DoubleSide}});
            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(a => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.4), matCarbon);
                arm.rotation.z = Math.PI/2; arm.rotation.y = a;
                droneGroup.add(arm);
                const p = new THREE.Mesh(new THREE.CircleGeometry(0.5, 32), matProp);
                p.position.set(Math.cos(a)*0.7, 0.2, Math.sin(a)*0.7); p.rotation.x = Math.PI/2;
                droneGroup.add(p); props.push(p);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.AmbientLight(0xffffff, 0.3));
            const light = new THREE.PointLight(0x00ffff, 2, 100); light.position.set(5, 5, 5);
            scene.add(light);
            camera.position.set(0, 4, 8); camera.lookAt(0,0,0);

            // AUTO-AJUSTE
            new ResizeObserver(() => {{
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            }}).observe(container);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach(p => p.rotation.z += 0.8);
                droneGroup.rotation.y += 0.005;
                droneGroup.position.y = Math.sin(Date.now()*0.002) * 0.15;
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