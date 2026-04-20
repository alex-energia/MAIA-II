# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

# Importaciones blindadas
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
    
    # Procesamiento Seguro
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    
    # Kernel Inspector
    current_code = db.get(target, "// SISTEMA MAIA V13 ACTIVATED") if idea and target else "// AGUARDANDO COMANDO TÁCTICO..."

    h = f"""
    <html><head><title>MAIA II - V13 EXPONENCIAL & BLINDADA</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000101; color:#0ff; font-family:'Courier New', monospace; margin:0; overflow:hidden; font-size:12px; }}
        .panel {{ border:1px solid #0f02; background:rgba(0,10,10,0.92); border-radius:2px; padding:10px; margin-bottom:5px; }}
        .flex-main {{ display:flex; gap:10px; height: 83vh; padding:10px; box-sizing:border-box; }}
        
        /* CABECERA TÁCTICA */
        .header {{ display:flex; align-items:center; gap:15px; padding:15px; background:rgba(0,30,30,0.98); border-bottom:3px solid #0ff; box-shadow:0 0 15px #0ff5; }}
        .input-idea {{ background:#000; color:#0ff; border:2px solid #0ff; padding:12px; flex-grow:1; outline:none; font-size:1.1em; }}
        .btn-gen {{ background:#0ff; color:#000; border:none; padding:12px 25px; font-weight:bold; cursor:pointer; text-transform:uppercase; letter-spacing:1px; }}

        /* ESTADOS DE MEMORIA Y VOZ */
        #voice-btn {{ background:#300; color:#f66; border:1px solid #f66; padding:10px; cursor:pointer; font-weight:bold; width:120px; }}
        #voice-btn.active {{ background:#050; color:#6f6; border-color:#6f6; box-shadow:0 0 10px #0f0; }}
        .btn-mem {{ background:none; color:#f0f; border:1px solid #f0f; padding:10px; cursor:pointer; font-weight:bold; }}
        .btn-clr {{ background:none; color:#0ff; border:1px solid #0ff; padding:10px; cursor:pointer; font-weight:bold; }}

        /* RENDERIZADO EXPANENCIAL BLINDADO */
        #proto-container {{ width:100%; height:100%; position:relative; background:#000000; overflow:hidden; border:2px solid #0f0; box-shadow:0 0 20px #0f04; }}
        #status-label {{ position:absolute; bottom:10px; left:10px; color:#0f0; background:rgba(0,0,0,0.8); padding:5px; border:1px solid #0f0; font-size:9px; z-index:10; pointer-events:none; }}
        
        /* HARDWARE GRID BLINDADO */
        .hw-grid {{ display:grid; grid-template-columns: repeat(2, 1fr); gap:6px; }}
        .hw-card {{ border:1px solid #f0f3; padding:6px; font-size:0.68em; background:rgba(255,0,255,0.02); }}
        .hw-card b {{ color:#f0f; display:block; border-bottom:1px solid #f0f3; margin-bottom:3px; }}
        
        /* CHAT ELÁSTICO MAIA */
        #chat-maia {{ position:fixed; bottom:10px; right:10px; width:300px; height:40px; background:rgba(0,25,25,0.98); border:2px solid #0ff; transition:0.4s cubic-bezier(0.4, 0, 0.2, 1); z-index:999; overflow:hidden; }}
        #chat-maia.open {{ height:400px; box-shadow:0 0 25px #0ff6; }}
        #chat-head {{ background:#0ff; color:#000; padding:10px; font-weight:bold; cursor:pointer; display:flex; justify-content:space-between; }}
        #chat-log {{ padding:10px; font-size:11px; height:290px; overflow-y:auto; color:#fff; background:#000505; }}
        #chat-in {{ width:100%; background:#000; color:#0ff; border:none; border-top:1px solid #0ff; padding:12px; outline:none; font-size:11px; }}
        
        /* SCROLLBARS */
        ::-webkit-scrollbar {{ width: 5px; height: 5px; }}
        ::-webkit-scrollbar-track {{ background: #000; }}
        ::-webkit-scrollbar-thumb {{ background: #0ff; border-radius: 5px; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.3em; letter-spacing:2px; color:#0ff;">MAIA II <span style="color:#0f0;font-size:0.8em;">[V13-EXP]</span></b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='COMANDO DE MISIÓN OESTRATEGIA LOGÍSTICA...' value='{idea}'>
            <button type='submit' class='btn-gen'>DESPLEGAR</button>
        </form>
        <button type='button' id='voice-btn' onclick="toggleVoice()">VOICE: OFF</button>
        <button type='button' class='btn-mem' onclick="alert('Datos Sincronizados al 100%')">MEMORIA</button>
        <button type='button' class='btn-clr' onclick="window.location.href='/'">LIMPIAR</button>
    </div>

    <div class='flex-main'>
        <div style="width:20%; overflow-y:auto;" class="panel">
            <h4 style="color:#f0f; font-size:0.8em; text-align:center; border-bottom:1px solid #f0f3; padding-bottom:5px; margin-top:0;">RTOS NODES</h4>
            {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; padding:6px; width:100%; border-bottom:1px solid #0f01;'>> {n}</button></form>" for n in sorted(db.keys())])}
        </div>

        <div style="width:50%;" class="panel">
            <div id="proto-container">
                <div id="status-label">PROTO: MAIA-II_STEALTH_V4 | HASH: {hex(id(idea)) if idea else "0x000"} | FW:V13</div>
            </div>
        </div>

        <div style="width:30%; overflow-y:auto; display:flex; flex-direction:column; gap:10px;" class="panel">
            <div>
                <h4 style="color:#0ff; font-size:0.8em; margin-top:0;">HARDWARE LAYER (8 CAPAS BLINDADAS)</h4>
                <div class='hw-grid'>
                    {"".join([f"<div class='hw-card'><b>{k}</b>{', '.join(v)}</div>" for k,v in hw_data.items()])}
                </div>
            </div>
            <div>
                <h4 style="color:#39ff14; font-size:0.8em; margin-top:0;">KERNEL INSPECTOR: {target if target else "STANDBY"}</h4>
                <div style="background:#000; color:#39ff14; padding:12px; font-size:10px; height:200px; overflow-y:auto; border-left:3px solid #f0f; border-radius:2px; white-space:pre-wrap;">{current_code}</div>
            </div>
        </div>
    </div>

    <div id="chat-maia">
        <div id="chat-head" onclick="this.parentElement.classList.toggle('open')">
            <span>MAIA CORE INTEL</span><span>▲</span>
        </div>
        <div id="chat-log">MAIA: Alex, sistema de 8 capas operativo. Dron V13 blindado y visible al 100%.</div>
        <input type="text" id="chat-in" placeholder="Escribir comando..." onkeydown="if(event.key==='Enter') sendChat(this)">
    </div>

    <script>
        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.classList.toggle('active');
            if(btn.classList.contains('active')) {{
                btn.innerText = "VOICE: ON";
                const msg = new SpeechSynthesisUtterance("Hola Alex, ¿en qué puedo ayudarte hoy?");
                msg.lang = 'es-ES'; msg.pitch = 1.1; msg.rate = 1.0;
                window.speechSynthesis.speak(msg);
            }} else {{ btn.innerText = "VOICE: OFF"; window.speechSynthesis.cancel(); }}
        }}

        function sendChat(i) {{
            const log = document.getElementById('chat-log');
            if(!i.value) return;
            log.innerHTML += "<div><b style='color:#f0f;'>ALEX:</b> "+i.value+"</div>";
            setTimeout(() => {{ log.innerHTML += "<div><b style='color:#0f0;'>MAIA:</b> Comando procesado. Optimizando parámetros de vuelo para " + '{idea}' + ".</div>"; log.scrollTop = log.scrollHeight; }}, 600);
            i.value = "";
            log.scrollTop = log.scrollHeight;
        }}

        // MOTOR 3D EXPONENCIAL Y BLINDADO (Three.js V13)
        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            // Cámara ajustada para resaltar el dron
            const camera = new THREE.PerspectiveCamera(40, container.clientWidth / container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true, logarithmicDepthBuffer: true }});
            renderer.setSize(container.clientWidth, container.clientHeight);
            renderer.setPixelRatio(window.devicePixelRatio); // Calidad exponencial
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            
            // MATERIALES PBR (FÍSICOS AVANZADOS)
            const matCarbon = new THREE.MeshStandardMaterial({{ color: 0x010101, metalness: 1.0, roughness: 0.05, envMapIntensity: 2.0 }});
            const matGlow = new THREE.MeshBasicMaterial({{ color: 0x00ff00 }});
            const matProp = new THREE.MeshStandardMaterial({{ color: 0x00ffff, transparent: true, opacity: 0.35, side: THREE.DoubleSide, blending: THREE.AdditiveBlending }});

            // 1. CHASIS COMPLEJO EXPONENCIAL
            // Cuerpo Octaédrico de Carbono Brillante
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.55, 0), matCarbon);
            body.scale.y = 0.5;
            body.rotation.y = Math.PI/8;
            droneGroup.add(body);
            
            // Detalle de núcleo de energía neón
            const coreGlow = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 0.2, 8), matGlow);
            droneGroup.add(coreGlow);

            // 2. SENSORES LÁSER (OJOS IA)
            const sensorL = new THREE.Mesh(new THREE.SphereGeometry(0.045), matGlow);
            sensorL.position.set(0.18, 0, 0.45);
            const sensorR = new THREE.Mesh(new THREE.SphereGeometry(0.045), matGlow);
            sensorR.position.set(-0.18, 0, 0.45);
            droneGroup.add(sensorL, sensorR);

            // 3. BRAZOS DOBLES REFORZADOS
            const props = [];
            const angles = [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4];
            angles.forEach((a, index) => {{
                const armGroup = new THREE.Group();
                // Brazo tubular reforzado
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.05, 1.4), matCarbon);
                arm.rotation.z = Math.PI/2;
                armGroup.add(arm);

                // Detalle de motorGaN metálico
                const motor = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 0.25, 16), matCarbon);
                motor.position.set(0.7, 0.08, 0);
                armGroup.add(motor);

                // Hélice Efecto Neón
                const p = new THREE.Mesh(new THREE.CircleGeometry(0.55, 32), matProp);
                p.position.set(0.7, 0.25, 0);
                p.rotation.x = Math.PI/2;
                armGroup.add(p);
                props.push(p);

                armGroup.rotation.y = a;
                droneGroup.add(armGroup);
            }});

            // 4. TREN DE ATERRIZAJE EXPONENCIAL
            const leg = new THREE.Mesh(new THREE.BoxGeometry(0.02, 0.4, 0.1), matCarbon);
            const legL = leg.clone(); legL.position.set(0.2, -0.3, 0); legL.rotation.x = 0.2;
            const legR = leg.clone(); legR.position.set(-0.2, -0.3, 0); legR.rotation.x = 0.2;
            droneGroup.add(legL, legR);

            droneGroup.rotation.x = 0.2; // Inclinación inicial para vista táctica
            scene.add(droneGroup);
            
            // ILUMINACIÓN EXPONENCIAL
            const ambient = new THREE.AmbientLight(0xffffff, 0.2); // Sutil ambiente
            const spot1 = new THREE.SpotLight(0x00ffff, 2.5); spot1.position.set(5, 5, 5); // Luz cian táctica
            const spot2 = new THREE.SpotLight(0xff00ff, 1.5); spot2.position.set(-5, -5, 5); // Luz magenta táctica
            const point = new THREE.PointLight(0x00ff00, 1, 10); point.position.set(0, 0.5, 0.6); // Luz verde frontal

            scene.add(ambient, spot1, spot2, point);

            camera.position.set(0, 3, 7.5); // Cámara ajustada
            camera.lookAt(0, 0, 0);

            // BLINDAJE DE REDIMENSIÓN TOTAL (ResizeObserver)
            function adjustRender() {{
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            }}

            // Observador de redimensionamiento dinámico
            new ResizeObserver(adjustRender).observe(container);
            window.addEventListener('load', adjustRender); // Forzar ajuste inicial

            function animate() {{
                requestAnimationFrame(animate);
                // Hélices giran a alta frecuencia neón
                props.forEach((p, i) => p.rotation.z += (i % 2 === 0 ? 0.9 : -0.9));
                const t = Date.now() * 0.001;
                // Efecto de vuelo orgánico (Hover táctico)
                droneGroup.position.y = Math.sin(t*1.8) * 0.18;
                droneGroup.rotation.y += 0.003;
                droneGroup.rotation.z = Math.sin(t*0.5) * 0.05;
                
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