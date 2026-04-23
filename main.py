# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

def get_maia_v6_industrial(idea):
    # --- 25 NODOS DE SOFTWARE DE ALTO IMPACTO ---
    sw = {
        "01_RTOS_SYSTICK.py": "def init(): machine.mem32[0xE000E010] = 0x07 # Configura reloj de sistema 1kHz",
        "02_EKF_QUATERNION.py": "def predict(q, g, dt): q_dot = 0.5 * q @ g; return q + q_dot * dt # Integración 4D",
        "03_REGEN_NODO_15.py": "def regen(rpm, v): return (rpm * 0.0038 / v) * 4095 if rpm > 5500 else 0",
        "04_CAN_FD_BUS.py": "def tx(id, data): can.send(id=0x123, dlc=64, data=data) # 8Mbps Industrial",
        "05_AES_256_GCM.py": "def secure(p): return aes.gcm_encrypt(p, key=SYS_KEY) # Encriptación militar",
        "06_DMA_ADC_BMS.py": "def read_cells(): return [adc.read(i) for i in range(12)] # Monitoreo 12S",
        "07_RTK_GNSS_L5.py": "def get_fix(): return 'L1_L2_L5_TRIPLE_BAND_FIXED' # Precisión 5mm",
        "08_SLAM_OCTOMAP.py": "def update_grid(scan): return voxel.insert(scan) # Mapeo 3D tiempo real",
        "09_PID_WINDUP.py": "def pid(err): self.integ = clamp(self.integ + err, -limit, limit) # Anti-saturación",
        "10_NEURAL_ORIN.py": "def detect(): return engine.inference(camera_stream) # IA en NVIDIA Orin Nano",
        "11_THERMAL_GAUGE.py": "def cool(): return fan.set_pwm(temp * 1.5) # Gestión térmica dinámica",
        "12_BLACKBOX_LFS.py": "def log(data): lfs.write('mission.log', data) # LittleFS redundante",
        "13_SECURE_BOOT.py": "def verify(): return sha256.check(firmware_hash) # Arranque verificado",
        "14_PYRO_SAFETY.py": "def arm(): return pyro.check_impedance(0.4) # Actuador de paracaídas",
        "15_REGEN_STATS.py": "def yield(): return f'{regen_current * v_bus} Wh Recovered' # Análisis Nodo 15",
        "16_STARLINK_LINK.py": "def sat_sync(): return starlink.get_status() # Enlace satelital global",
        "17_DSHOT_1200.py": "def write_esc(v): return dshot.send_frame(v) # Protocolo digital de motores",
        "18_GIMBAL_3AXIS.py": "def stabilize(): return imu.get_rotation() @ gimbal.inverse() # Horizonte fijo",
        "19_GEO_FENCE_3D.py": "def check(): return poly.contains(gps.pos) # Perímetro esférico de seguridad",
        "20_AUTO_LAND_CV.py": "def find_pad(): return cv.find_corners(landing_marker) # Aterrizaje visual",
        "21_SDR_JAM_PROT.py": "def hop(): return sdr.set_frequency(random.randint(2400, 2500)) # Anti-jamming",
        "22_H2_FUEL_CTRL.py": "def h2_flow(): return solenoid.set_open(0.85) # Gestión de Hidrógeno",
        "23_SWARM_MESH.py": "def mesh_sync(): return esp_now.sync_nodes() # Coordinación de enjambre",
        "24_API_SYS_HEALTH.py": "def check_all(): return [n.status for n in all_nodes] # Diagnóstico total",
        "25_DEBUG_DUMP.py": "def crash_dump(): return core.dump_registers() # Análisis post-vuelo"
    }

    # --- HARDWARE DE 8 CAPAS + DOM ---
    hw = {
        "CAPA 1: CÓMPUTO": "STM32H7 (Vuelo) + NVIDIA Orin (IA Vision).",
        "CAPA 2: SENSORES": "LiDAR 360 Solid State + Cámara 4K 60fps.",
        "CAPA 3: POTENCIA": "Inversores GaN para recuperación Nodo 15.",
        "CAPA 4: ESTRUCTURA": "Fibra de Carbono T1200 de alta densidad.",
        "CAPA 5: ENERGÍA": "Baterías de Estado Sólido 450 Wh/kg.",
        "CAPA 6: COMMS": "SDR + SatLink (Starlink/Iridium).",
        "CAPA 7: NAV": "Triple IMU + GNSS Triple Banda (L1/L2/L5).",
        "CAPA 8: SEGURIDAD": "Paracaídas Pirotécnico de acción rápida.",
        "MÓDULO DOM": "Digital Operations Module: IA y Caja Negra Independiente."
    }

    # --- STRATEGIC INDUSTRIAL ---
    strat = {
        "MISIÓN": f"Despliegue de {idea} en entorno crítico.",
        "AUTONOMÍA": "Estimada 45 min con recuperación Nodo 15 activa.",
        "SEGURIDAD": "Certificación SIL3 para operación en zonas urbanas.",
        "CAPACIDAD": "Carga útil modular de hasta 4.5kg con balanceo activo."
    }

    return {"sw": sw, "hw": hw, "strat": strat}

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    action = request.form.get('action', '')
    scroll_pos = request.form.get('scroll_pos', '0')
    
    is_gen = action == "generate" and idea != ""
    if action == "clear": idea = ""; target = ""; is_gen = False

    data = get_maia_v6_industrial(idea) if is_gen else {"sw": {}, "hw": {}, "strat": {}}
    current_code = data["sw"].get(target, "# MAIA II INDUSTRIAL KERNEL\n# LISTO PARA AUDITORÍA...")

    h = f"""
    <html><head><title>MAIA II - INDUSTRIAL EXPERT</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; gap:15px; padding:15px; background:#001a1a; border-bottom:3px solid #0ff; }}
        .grid {{ display:grid; grid-template-columns: 20% 50% 30%; gap:15px; height:88vh; padding:15px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,10,10,0.9); padding:15px; overflow-y:auto; border-radius:5px; }}
        
        /* SCROLLBAR VISOR */
        .visor-box {{ height: 400px; overflow-y: scroll; background:#000; padding:20px; border-left:4px solid #f0f; border-radius:5px; }}
        ::-webkit-scrollbar {{ width: 14px; }}
        ::-webkit-scrollbar-track {{ background: #001a1a; }}
        ::-webkit-scrollbar-thumb {{ background: #0ff; border-radius: 10px; border: 3px solid #001a1a; }}
        
        /* CHAT FLOTANTE LIMPIO */
        .chat-widget {{ position:fixed; bottom:20px; left:20px; width:300px; border:2px solid #0ff; background:#000; border-radius:8px; z-index:100; }}
        .chat-header {{ background:#0ff; color:#000; padding:10px; cursor:pointer; font-weight:bold; }}
        .chat-body {{ height:150px; padding:10px; display:none; overflow-y:auto; font-size:11px; }}
        .chat-input-box {{ border-top:1px solid #0ff3; display:none; padding:5px; }}
        .chat-input-box input {{ width:100%; background:transparent; border:none; color:#0ff; font-family:monospace; outline:none; }}

        .node-btn {{ background:none; color:#0f0; border:1px solid #0f02; width:100%; text-align:left; padding:10px; margin-bottom:5px; cursor:pointer; font-size:11px; }}
        .active {{ background:rgba(240,0,255,0.2) !important; border-color:#f0f !important; }}
        .telemetry {{ position:absolute; top:20; right:20; color:#0f0; font-size:12px; text-align:right; }}
    </style>
    </head><body>
    
    <form method='post' class='header'>
        <input type="text" name="drone_idea" value="{idea}" style="background:#000; color:#0ff; border:1px solid #0ff; padding:10px; flex-grow:1;" placeholder="MISIÓN INDUSTRIAL...">
        <input type="hidden" name="scroll_pos" id="scroll_pos_val" value="{scroll_pos}">
        <button type='submit' name="action" value="generate" style="background:#0ff; padding:10px 20px; cursor:pointer; font-weight:bold;">INICIALIZAR MAIA II</button>
    </form>

    <div class='grid'>
        <div class="panel">
            <h3 style="color:#f0f; margin-top:0;">[1] STRATEGIC</h3>
            {"".join([f"<p style='font-size:11px;'><b>{k}:</b><br><span style='color:#ccc;'>{v}</span></p>" for k,v in data["strat"].items()])}
        </div>

        <div class="panel" style="padding:0; overflow:hidden; position:relative;">
            <div id="c3d" style="width:100%; height:100%;"></div>
            <div class="telemetry">
                MODO: SOBERANÍA TOTAL<br>
                ALT: <span id="alt">0.00</span> m | DOM: <span style="color:#0f0;">ONLINE</span><br>
                LiDAR: ACTIVE | REGEN: 14.8%
            </div>
        </div>

        <div class="panel" id="nodes-panel">
            <h3 style="color:#ffd700; margin-top:0;">[2] HARDWARE (8 CAPAS + DOM)</h3>
            {"".join([f"<div style='font-size:10px; margin-bottom:5px; border-left:2px solid #ffd700; padding-left:8px;'><b>{k}:</b> {v}</div>" for k,v in data["hw"].items()])}
            
            <h3 style="color:#f0f; margin-top:20px;">[3] SOFTWARE (25 NODOS)</h3>
            <div style="max-height:150px; overflow-y:auto; margin-bottom:10px; border:1px solid #333; padding:5px;">
                {"".join([f'''<button type="button" class="node-btn {'active' if n == target else ''}" onclick="navToNode('{n}')">{n}</button>''' for n in sorted(data["sw"].keys())])}
            </div>
            <div class="visor-box"><code style="color:#39ff14;">{current_code}</code></div>
        </div>
    </div>

    <div class="chat-widget">
        <div class="chat-header" onclick="toggleChat()">MAIA COMMS</div>
        <div class="chat-body" id="chatBody"><b>MAIA II:</b> Kernel v6.0 listo. DOM verificado.</div>
        <div class="chat-input-box" id="chatInput"><input type="text" placeholder="Digitar comando..."></div>
    </div>

    <form id="navForm" method="post">
        <input type="hidden" name="drone_idea" value="{idea}">
        <input type="hidden" name="action" value="generate">
        <input type="hidden" name="target_node" id="target_node_id">
        <input type="hidden" name="scroll_pos" id="scroll_pos_node">
    </form>

    <script>
        function toggleChat() {{
            const b = document.getElementById('chatBody'), i = document.getElementById('chatInput');
            const show = b.style.display === 'block' ? 'none' : 'block';
            b.style.display = show; i.style.display = show;
        }}
        function navToNode(node) {{
            document.getElementById('target_node_id').value = node;
            document.getElementById('scroll_pos_node').value = document.getElementById('nodes-panel').scrollTop;
            document.getElementById('navForm').submit();
        }}

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, (window.innerWidth*0.5)/(window.innerHeight*0.8), 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(window.innerWidth*0.5, window.innerHeight*0.8);
        document.getElementById('c3d').appendChild(renderer.domElement);

        const group = new THREE.Group();
        if({ "true" if is_gen else "false" }) {{
            const mat = new THREE.MeshPhongMaterial({{color:0x111111, shininess:100}});
            // Fuselaje Aero-X
            const body = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.2, 1.4), mat);
            group.add(body);
            // MÓDULO DOM (Módulo de Operaciones Digitales en el frente)
            const dom = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.15, 0.4), new THREE.MeshPhongMaterial({{color:0x333333}}));
            dom.position.set(0, 0, -0.8); group.add(dom);
            // Sensores LiDAR / Cámaras
            const cam = new THREE.Mesh(new THREE.SphereGeometry(0.1, 16, 16), new THREE.MeshPhongMaterial({{color:0x00ffff}}));
            cam.position.set(0, -0.15, -0.7); group.add(cam);
            
            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(a => {{
                const arm = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.05, 0.1), mat);
                arm.rotation.y = a; group.add(arm);
                const p = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.01, 16), new THREE.MeshBasicMaterial({{color:0x00ffff, transparent:true, opacity:0.3}}));
                p.position.set(Math.cos(a)*0.8, 0.15, Math.sin(a)*0.8); p.name="p"; group.add(p);
            }});
        }}
        scene.add(group);
        scene.add(new THREE.PointLight(0xffffff, 1).position.set(5,5,5));
        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        camera.position.set(0, 5, 10); camera.lookAt(0,0,0);

        function anim() {{
            requestAnimationFrame(anim);
            if({ "true" if is_gen else "false" }) {{
                group.rotation.y += 0.003;
                group.position.y = Math.sin(Date.now()*0.001) * 0.2 + 1;
                document.getElementById('alt').innerText = (group.position.y * 12.5).toFixed(2);
                group.children.forEach(c => {{ if(c.name==="p") c.rotation.y += 2.0; }});
            }}
            renderer.render(scene, camera);
        }}
        anim();
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
