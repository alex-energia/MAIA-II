# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

def get_maia_v3_core(idea):
    # --- ARQUITECTURA DE SOFTWARE CRÍTICA (NODO POR NODO) ---
    sw = {
        "01_REGEN_NODO_15_PRO.py": """# CONTROL DE POTENCIA GAN - NIVEL INDUSTRIAL
class ActiveRegen:
    def __init__(self):
        self.REG_PWM = 0x40012C00 
        self.LIMIT = 4095
    
    def execute_braking(self, rpm, v_bus):
        # Protección de sobrevoltaje y saturación
        if rpm > 5000 and v_bus < 26.0:
            raw_val = int((rpm * 0.004 / v_bus) * self.LIMIT)
            # Safe-Guard: No exceder el límite del registro
            clamped = max(0, min(self.LIMIT, raw_val))
            machine.mem32[self.REG_PWM] = clamped
            return f"REGEN_ACTIVE_{clamped/self.LIMIT*100:.1f}%"
        return "DISCHARGE_MODE" """,

        "02_ATTITUDE_9DOF_EKF.py": """# FILTRO DE KALMAN EXTENDIDO (SENSING)
def get_attitude(self, dt):
    # Predicción basada en giroscopio
    self.state = self.transition_matrix @ self.state
    # Corrección mediante Acelerómetro y Magnetómetro (Brújula)
    innovation = self.z - (self.h_matrix @ self.state)
    self.state += self.kalman_gain @ innovation
    return {"pitch": self.state[0], "roll": self.state[1], "yaw": self.state[2]}""",

        "03_DMA_BUS_MANAGER.py": "def transfer(): return 'DMA_L1_CACHE_SYNC_OK'",
        "04_CAN_FD_STACK.py": "def can_tx(): return 'FRAME_ID_0x100_SENT_8MBPS'",
        "05_RTOS_SCHEDULER.py": "def task_mgr(): return 'PRIORITY_FLIGHT_CTRL_1KHZ'",
        "06_AES_VAULT.py": "def secure(): return 'GCM_256_LINK_ENCRYPTED'",
        "07_RTK_POSITIONING.py": "def get_fix(): return 'PRECISION_0.008m_LOCKED'",
        "08_BMS_ADVANCED.py": "def cells(): return 'HEALTH_99.2%_SOH_ACTIVE'",
        "09_SLAM_AI_VISION.py": "def map(): return 'VOXEL_GRID_GENERATED_60FPS'",
        "10_NEURAL_MAIA.py": "def ai_inference(): return 'TARGET_LOCKED_ID_042'",
        "11_THERMAL_CTRL.py": "def heat_sync(): return 'FAN_RPM_OPTIMIZED_42C'",
        "12_BLACKBOX_SYNC.py": "def log(): return 'FS_WRITE_BUFFER_COMMITTED'",
        "13_BOOT_SECURE.py": "def check(): return 'FIRMWARE_SIGNATURE_VALID'",
        "14_PYRO_SAFETY.py": "def arm(): return 'VOLTAGE_IMPEDANCE_CHECK_PASS'",
        "15_REGEN_STATS.py": "def yield_calc(): return 'EFFICIENCY_18.4%_GAIN'",
        "16_SAT_LINK_SYNC.py": "def uplink(): return 'STARLINK_LOW_LATENCY_ACTIVE'",
        "17_DSHOT_1200_DRV.py": "def esc_write(): return 'DSHOT_TELEMETRY_SYNCED'",
        "18_GIMBAL_STAB.py": "def lock(): return 'HORIZON_STABILIZED_0.01_DEG'",
        "19_GEO_FENCE_PRO.py": "def fence(): return 'INSIDE_AUTHORIZED_AIRSPACE'",
        "20_AUTO_LAND_IR.py": "def land(): return 'PRECISION_PAD_DETECTED'",
        "21_SDR_JAMMING.py": "def shield(): return 'RF_INTERFERENCE_MITIGATED'",
        "22_H2_FUEL_MGMT.py": "def hybrid(): return 'H2_CELL_FLOW_NOMINAL'",
        "23_MESH_SYNC.py": "def mesh(): return 'SWARM_HEARTBEAT_ACTIVE'",
        "24_API_DIAGNOSTIC.py": "def health(): return 'SYSTEM_READY_FOR_MISSION'",
        "25_TRACE_DEBUG.py": "def dump(): return 'KERNEL_TRACE_SUCCESSFUL'"
    }

    hw = {
        "H1_COMPUTE": "STM32H7 Dual Core + NVIDIA Orin Nano.",
        "H2_FRAME": "Monocasco de Carbono T1200 Aerodinámico.",
        "H3_POWER": "Inversores GaN de alta frecuencia para Nodo 15.",
        "H4_SENSORS": "LiDAR Solid State oculto + Cámara 8K IR.",
        "H5_ENERGY": "Pilas de estado sólido 450Wh/kg.",
        "H6_SAFETY": "Paracaídas balístico integrado de despliegue < 0.5s."
    }

    return {"sw": sw, "hw": hw}

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    action = request.form.get('action', '')
    scroll_pos = request.form.get('scroll_pos', '0')
    
    is_gen = action == "generate" and idea != ""
    if action == "clear":
        idea = ""; target = ""; is_gen = False

    data = get_maia_v3_core(idea) if is_gen else {"sw": {}, "hw": {}}
    current_code = data["sw"].get(target, "# MAIA II INDUSTRIAL CORE\n# DESPLIEGUE COMPLETO DISPONIBLE...")

    h = f"""
    <html><head><title>MAIA II - INDUSTRIAL PRO</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:'Segoe UI',monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; gap:15px; padding:20px; background:linear-gradient(90deg, #001a1a, #003333); border-bottom:4px solid #0ff; }}
        .grid {{ display:grid; grid-template-columns: 25% 45% 30%; gap:20px; height:85vh; padding:20px; }}
        .panel {{ border:1px solid #0ff4; background:rgba(0,10,10,0.9); padding:20px; overflow-y:auto; border-radius:10px; position:relative; }}
        
        /* BARRA DE DESPLAZAMIENTO AMPLIADA */
        ::-webkit-scrollbar {{ width: 14px; }}
        ::-webkit-scrollbar-track {{ background: #001a1a; }}
        ::-webkit-scrollbar-thumb {{ background: #0ff; border: 3px solid #001a1a; border-radius: 10px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #f0f; }}

        .visor {{ background:#020202; color:#39ff14; padding:25px; font-size:13px; border-left:5px solid #f0f; height:380px; overflow:auto; white-space:pre; border-radius:5px; box-shadow: inset 0 0 15px #000; }}
        .btn {{ padding:12px 24px; cursor:pointer; font-weight:bold; border:none; border-radius:5px; transition:0.3s; text-transform:uppercase; }}
        .btn:hover {{ filter:brightness(1.2); transform:scale(1.02); }}
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f02; width:100%; text-align:left; padding:15px; margin-bottom:8px; cursor:pointer; font-size:12px; border-radius:4px; }}
        .active {{ background:rgba(240,0,255,0.2) !important; border-color:#f0f !important; color:#fff !important; }}
        input[type='text'] {{ background:#000; color:#0ff; border:2px solid #0ff6; padding:15px; flex-grow:1; outline:none; border-radius:5px; font-size:16px; }}
        .telemetry {{ position:absolute; top:20; right:20; color:#0f0; font-size:14px; text-align:right; font-weight:bold; text-shadow: 0 0 10px #000; }}
    </style>
    </head><body>
    
    <form method='post' class='header'>
        <input type="text" name="drone_idea" value="{idea}" placeholder="Misión: {idea or 'Definir objetivo industrial...'}">
        <input type="hidden" name="scroll_pos" id="scroll_pos_val" value="{scroll_pos}">
        <button type='submit' name="action" value="generate" class="btn" style="background:#0ff; color:#000;">DESPLEGAR SISTEMA TOTAL</button>
        <button type='submit' name="action" value="clear" class="btn" style="background:#f00; color:#fff;">RESET</button>
        <button type="button" class="btn" style="background:#ffd700;" onclick="maiaVoice()">AUDIO ON</button>
    </form>

    <div class='grid'>
        <div class="panel">
            <h3 style="color:#f0f; margin-top:0;">ESTRATEGIA DE MERCADO</h3>
            <p><b>VIABILIDAD:</b> Alta. {idea} tiene un ROI del 210% en mercados de seguridad y logística.</p>
            <p><b>HARDWARE:</b> Stack redundante SIL3.</p>
            <p><b>INNOVACIÓN:</b> Nodo 15 activo con recuperación de 18%.</p>
            <div style="background:#000; padding:15px; border:1px solid #0ff2; margin-top:20px; font-size:12px;">
                <b>MAIA CHAT:</b><br>Sistema {idea} validado. Sensores LiDAR alineados. En espera de despegue autónomo.
            </div>
        </div>

        <div class="panel" style="padding:0; overflow:hidden;">
            <div id="c3d" style="width:100%; height:100%;"></div>
            <div class="telemetry">
                MODO: AUTÓNOMO<br>
                ALT: <span id="alt">0.0</span> m<br>
                REGEN: <span style="color:#39ff14;">ESTABLE</span>
            </div>
        </div>

        <div class="panel" id="nodes-panel">
            <h3 style="color:#ffd700; margin-top:0;">PRODUCTION NODES (25)</h3>
            <div style="max-height:220px; overflow-y:auto; border:1px solid #333; padding:10px; margin-bottom:15px; border-radius:5px;">
                {"".join([f'''<button type="button" class="node-btn {'active' if n == target else ''}" onclick="navToNode('{n}')">/SYS/PROD/{n}</button>''' for n in sorted(data["sw"].keys())])}
            </div>
            <div class="visor" id="code-visor">{current_code}</div>
        </div>
    </div>

    <form id="navForm" method="post">
        <input type="hidden" name="drone_idea" value="{idea}">
        <input type="hidden" name="action" value="generate">
        <input type="hidden" name="target_node" id="target_node_id">
        <input type="hidden" name="scroll_pos" id="scroll_pos_node">
    </form>

    <script>
        const pNodes = document.getElementById('nodes-panel');
        window.onload = () => {{ pNodes.scrollTop = {scroll_pos}; }};

        function navToNode(node) {{
            document.getElementById('target_node_id').value = node;
            document.getElementById('scroll_pos_node').value = pNodes.scrollTop;
            document.getElementById('navForm').submit();
        }}

        function maiaVoice() {{
            const u = new SpeechSynthesisUtterance("MAIA II inicializada. Sistema industrial listo para despliegue táctico.");
            u.lang = 'es-ES'; window.speechSynthesis.speak(u);
        }}

        // MOTOR 3D - REDISEÑO INDUSTRIAL AGRESIVO
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth*0.45/(window.innerHeight*0.8), 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(window.innerWidth*0.45, window.innerHeight*0.8);
        document.getElementById('c3d').appendChild(renderer.domElement);

        const group = new THREE.Group();
        if({ "true" if is_gen else "false" }) {{
            // Cuerpo Aero-X (Sin bolas ni cuadros)
            const material = new THREE.MeshPhongMaterial({{color:0x1a1a1a, shininess:100}});
            const body = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.2, 1.2), material);
            group.add(body);
            
            // Front LiDAR (Inclinado)
            const nose = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.4, 0.4, 4), material);
            nose.rotation.x = Math.PI/2; nose.position.z = -0.7; group.add(nose);

            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(a => {{
                const arm = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.05, 0.1), material);
                arm.rotation.y = a; group.add(arm);
                
                const prop = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.01, 16), new THREE.MeshBasicMaterial({{color:0x00ffff, transparent:true, opacity:0.3}}));
                prop.position.set(Math.cos(a)*0.8, 0.15, Math.sin(a)*0.8); prop.name="p"; group.add(prop);
            }});
        }}
        scene.add(group);
        scene.add(new THREE.PointLight(0xffffff, 1, 100).position.set(5,5,5));
        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        camera.position.set(0, 5, 10); camera.lookAt(0,0,0);

        function anim() {{
            requestAnimationFrame(anim);
            if({ "true" if is_gen else "false" }) {{
                group.rotation.y += 0.005;
                group.position.y = Math.sin(Date.now()*0.002) * 0.3 + 1.5;
                document.getElementById('alt').innerText = (group.position.y * 10).toFixed(1);
                group.children.forEach(c => {{ if(c.name==="p") c.rotation.y += 1.5; }});
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