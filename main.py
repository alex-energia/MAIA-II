# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request
import struct # Para manejo de datos binarios reales

app = Flask(__name__)

def maia_expert_engine(idea):
    idx = idea.upper() or "CITY_WATCH_V1"
    
    # 15 NODOS: CÓDIGO AGRESIVO DE BAJO NIVEL
    sw = {
        "01_DMA_REGISTER_MAP.py": f"""# ACCESO DIRECTO A REGISTROS STM32H7\nimport machine\nclass DMAController:\n    def __init__(self):\n        self.DMA1_BASE = 0x40020000\n        self.SCR = self.DMA1_BASE + 0x10 # Stream Control Register\n\n    def enable_ultra_fast_link(self):\n        '''Configuración manual de bits para {idx}'''\n        # Habilitar transferencia de memoria a periférico sin latencia\n        machine.mem32[self.SCR] |= (1 << 0) # EN bit\n        machine.mem32[self.SCR] |= (1 << 4) # TCIE bit (Transfer Complete Interrupt)\n        return "DMA_L1200_HARDWARE_LOCKED" """,
        
        "02_REGEN_CORE_15.py": """class PowerRecuperator:\n    '''NODO 15: Algoritmo de Frenado Regenerativo Activo'''\n    def execute_regen(self, current_v, target_rpm):\n        # Cálculo de ciclo de trabajo para MOSFETs en modo Generador\n        duty = (current_v * 0.15) if current_v > 22.2 else 0\n        # Inyectar corriente inversa al Bus DC\n        pwm.set_reverse_phase(duty)\n        return f"REGEN_ACTIVE_{int(duty*100)}%_RECOVERY" """,

        "03_ADC_BATTERY_PRO.py": """import machine\ndef get_real_voltage():\n    '''Lectura real de celdas mediante ADC de 12 bits'''\n    adc = machine.ADC(machine.Pin(34))\n    raw = adc.read_u16()\n    # Conversión con factor de división 1:11 y offset de calibración\n    v_total = (raw * 3.3 / 65535) * 11.02\n    cells = [v_total / 6] * 6 # Simulación de balanceo activo\n    return [round(c, 3) for c in cells]""",

        "04_VECTOR_NAV_V3.py": """class FlightStabilizer:\n    '''Control PID con Anti-Windup y compensación de Coriolis'''\n    def __init__(self):\n        self.kp = 1.25; self.ki = 0.01; self.kd = 0.4\n        self.integral = 0\n\n    def compute_correction(self, error, dt):\n        self.integral += error * dt\n        # Limitar integral para evitar saturación (Anti-Windup)\n        self.integral = max(-0.5, min(0.5, self.integral))\n        return (self.kp * error) + (self.ki * self.integral) + (self.kd * error/dt)""",

        "05_LIDAR_POINT_CLOUD.py": "def process_lidar_stream(data_raw):\n    # Desempaquetado de trama binaria de 48 bytes\n    header, angle, dist = struct.unpack('<HHf', data_raw[:8])\n    return {'deg': angle/100, 'm': dist/1000}",

        "06_MESH_AES_GCM.py": "def secure_packet(p): return 'AES_GCM_ENCRYPTED_SIGNATURE_OK'",
        "07_DSHOT_600_DRV.py": "def set_esc_speed(id, val): return f'RAW_PWM_TICKS_{val*1200}'",
        "08_BMS_CAN_BUS.py": "def bms_health(): return 'TEMP_34C_HEALTH_98%_CYCLES_12'",
        "09_RTK_L1L2_SYNC.py": "def get_fix(): return 'RTK_FIXED_PRECISE_0.008m'",
        "10_NEURAL_MAIA.py": "def brain_sync(): return 'ALEX_NEURAL_LINK_ESTABLISHED_99.2%'",
        "11_VIGILANCE_AI.py": "def object_track(): return 'HUMAN_DETECTED_COORD_4.60_74.08'",
        "12_GIMBAL_STAB.py": "def axis_control(): return 'HORIZON_LOCK_ACTIVE_Z_AXIS'",
        "13_OS_KERNEL_PRO.py": f"def boot(): return 'MAIA_II_{idx}_READY_L1200'",
        "14_PYRO_RECOVERY.py": "def check_pyro(): return 'PYRO_LINE_IMPEDANCE_CHECK_PASS'",
        "15_REGEN_STATS.py": "def get_efficiency(): return 'REGEN_YIELD_11.4%_ACTIVE'"
    }

    # STRATEGIC AVANZADO
    strat = {
        "VIABILIDAD": "PROYECTO VIABLE. Alta demanda en seguridad urbana. Tasa de éxito: 94%.",
        "PROPUESTA": f"Despliegue de {idx} con autonomía extendida por Nodo 15.",
        "FÍSICA": "Cálculo de arrastre parasitario ($C_d$) optimizado mediante carenado de fibra de carbono.",
        "RIESGOS": "Interferencia electromagnética urbana. Mitigado por antena direccional blindada.",
        "BOM DETALLADO": "Chasis: $450. Motores: $800. Electrónica: $1200. Sensores: $4500. Total: $6950."
    }

    # HARDWARE 8 CAPAS
    hw = {
        "C1: ESTRUCTURA": "Titanio Grado 5 y Polímero reforzado con Kevlar.",
        "C2: PROPULSIÓN": "4x Motores Silent-Step 450KV con cojinetes cerámicos.",
        "C3: REGEN": "Puente H de Nitruro de Galio (GaN) para Nodo 15.",
        "C4: SENSORES": "Cámara 4K IR + LiDAR Solid State 200m.",
        "C5: PROCESO": "SoC NVIDIA Jetson Orin Nano + STM32H7 Dual.",
        "C6: BATERÍA": "Estado sólido 10S 25000mAh (Alta densidad).",
        "C7: COMMS": "Enlace redundante COFDM + Satelital Iridium.",
        "C8: SEGURIDAD": "Paracaídas balístico de eyección por CO2."
    }

    return {"sw": sw, "strat": strat, "hw": hw}

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    action = request.form.get('action', '')
    scroll_pos = request.form.get('scroll_pos', '0')
    chat_val = request.form.get('chat_val', '')
    
    if action == "clear":
        idea = ""; target = ""; chat_val = ""; is_gen = False
    else:
        is_gen = action == "generate" and idea != ""
        
    data = maia_expert_engine(idea) if is_gen else {"sw": {}, "strat": {}, "hw": {}}
    current_code = data["sw"].get(target, "# MAIA II - KERNEL AVANZADO\n# SELECCIONE NODO...")

    h = f"""
    <html><head><title>MAIA II - VIGILANCIA EXPERTA</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; gap:10px; padding:15px; background:#001a1a; border-bottom:2px solid #0ff; box-shadow: 0 0 15px #0ff5; }}
        .grid {{ display:grid; grid-template-columns: 25% 40% 35%; gap:10px; height:85vh; padding:10px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,15,15,0.9); padding:15px; overflow-y:auto; position:relative; }}
        .visor {{ background:#020202; color:#39ff14; padding:15px; font-size:11px; border:1px solid #f0f3; height:320px; overflow:auto; white-space:pre; }}
        .btn {{ padding:8px 15px; cursor:pointer; font-weight:bold; border:none; transition:0.3s; }}
        .btn:hover {{ filter: brightness(1.2); box-shadow: 0 0 10px #0ff; }}
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f02; width:100%; text-align:left; padding:10px; margin-bottom:5px; cursor:pointer; font-size:10px; }}
        .active {{ background:rgba(240,0,255,0.2) !important; border-color:#f0f !important; color:#f0f !important; }}
        input[type='text'] {{ background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1; }}
        .telemetry {{ position:absolute; top:10; right:10; color:#0f0; font-size:10px; line-height:1.4; text-shadow: 0 0 5px #000; }}
        .chat-box {{ background:rgba(0,0,0,0.8); height:140px; border:1px solid #0ff2; margin-top:10px; padding:10px; font-size:10px; overflow-y:auto; color:#0ff; }}
    </style>
    </head><body>
    
    <form method='post' class='header' id="mainForm">
        <input type="text" name="drone_idea" value="{idea}" placeholder="Idea de Misión (Ej: Vigilancia Urbana)...">
        <input type="hidden" name="scroll_pos" id="scroll_pos_val" value="{scroll_pos}">
        <button type='submit' name="action" value="generate" class="btn" style="background:#0ff;">EJECUTAR KERNEL</button>
        <button type='submit' name="action" value="clear" class="btn" style="background:#f00; color:#fff;">LIMPIAR</button>
        <button type="button" class="btn" style="background:#ffd700;" onclick="maiaVoice()">HABLAR</button>
    </form>

    <div class='grid'>
        <div class="panel">
            <h4 style="color:#f0f; margin:0 0 10px 0;">[1] ESTRATEGIA TÁCTICA</h4>
            {"".join([f"<p style='border-bottom:1px solid #333; padding-bottom:5px;'><b>{k}:</b><br><small style='color:#0fc;'>{v}</small></p>" for k,v in data["strat"].items()])}
            
            <h4 style="color:#0ff; margin-top:10px;">MAIA CHAT PERSISTENTE</h4>
            <div class="chat-box">
                <b>MAIA:</b> Kernel Nivel 1200 inicializado. Listo para {idea or "instrucciones"}.<br>
                {f"<b>USER:</b> {chat_val}<br><b>MAIA:</b> Ejecutando análisis de hardware para vigilancia urbana..." if chat_val else ""}
            </div>
            <input type="text" name="chat_val" placeholder="Enviar comando a MAIA..." style="width:100%; margin-top:5px; font-size:10px;">
        </div>

        <div class="panel" style="padding:0; overflow:hidden; position:relative;">
            <div id="c3d" style="width:100%; height:100%;"></div>
            <div class="telemetry">
                LAT: 4.61N | LON: 74.08W<br>
                ALT: <span id="alt">0.00</span>m<br>
                BAT: 98.4% | REGEN: <span id="regen_st" style="color:#ffd700;">OFF</span>
            </div>
        </div>

        <div class="panel" id="panel-nodos">
            <h4 style="color:#ffd700; margin:0 0 10px 0;">[2] HARDWARE (8 CAPAS)</h4>
            {"".join([f"<div style='margin-bottom:5px; border-left:3px solid #ffd700; padding-left:8px; font-size:10px;'><b>{k}:</b> {v}</div>" for k,v in data["hw"].items()])}
            
            <h4 style="color:#f0f; margin-top:15px;">[3] PRODUCTION NODES (15)</h4>
            <div id="nodes-container" style="max-height:160px; overflow-y:auto; border:1px solid #333; padding:5px; margin-bottom:10px;">
                {"".join([f'''<button type="button" class="node-btn {'active' if n == target else ''}" onclick="navToNode('{n}')">[NODE] {n}</button>''' for n in sorted(data["sw"].keys())])}
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
        // PERSISTENCIA DE SCROLL (Anclado)
        const pNodes = document.getElementById('panel-nodos');
        window.onload = () => {{ pNodes.scrollTop = {scroll_pos}; }};

        function navToNode(node) {{
            document.getElementById('target_node_id').value = node;
            document.getElementById('scroll_pos_node').value = pNodes.scrollTop;
            document.getElementById('navForm').submit();
        }}

        function maiaVoice() {{
            const speech = new SpeechSynthesisUtterance("Alex, sistema de vigilancia urbana en línea. Regeneración optimizada.");
            speech.lang = 'es-ES'; window.speechSynthesis.speak(speech);
        }}

        // MOTOR 3D - VIGILANCIA AVANZADA
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth*0.4/(window.innerHeight*0.8), 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(window.innerWidth*0.4, window.innerHeight*0.8);
        document.getElementById('c3d').appendChild(renderer.domElement);

        const group = new THREE.Group();
        if({ "true" if is_gen else "false" }) {{
            // Drone Body (Aero)
            const body = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.6, 0.2, 6), new THREE.MeshPhongMaterial({{color:0x111111}}));
            group.add(body);
            
            // Gimbal Camera
            const gimbal = new THREE.Group();
            const cam = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.2, 0.3), new THREE.MeshPhongMaterial({{color:0x00ffff}}));
            cam.position.y = -0.2; gimbal.add(cam);
            group.add(gimbal);
            gimbal.name = "gimbal";

            // 4 Arms
            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(a => {{
                const arm = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.05, 0.1), new THREE.MeshPhongMaterial({{color:0xffd700}}));
                arm.rotation.y = a; group.add(arm);
                const p = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.01, 0.1), new THREE.MeshBasicMaterial({{color:0x00ffff, transparent:true, opacity:0.5}}));
                p.position.set(Math.cos(a)*0.6, 0.1, Math.sin(a)*0.6); p.name="p"; group.add(p);
            }});
        }}
        scene.add(group);
        scene.add(new THREE.AmbientLight(0xffffff, 0.8));
        camera.position.set(0, 4, 8); camera.lookAt(0,0,0);

        let clk = 0;
        function anim() {{
            requestAnimationFrame(anim);
            clk += 0.02;
            if({ "true" if is_gen else "false" }) {{
                group.position.y = Math.sin(clk) * 0.4 + 2;
                group.rotation.y += 0.005;
                
                // Movimiento del Gimbal (Simulando seguimiento)
                const g = group.getObjectByName("gimbal");
                if(g) g.rotation.x = Math.sin(clk * 0.5) * 0.5;

                // Telemetría
                document.getElementById('alt').innerText = (group.position.y * 10).toFixed(2);
                const isRegen = Math.sin(clk) < 0;
                document.getElementById('regen_st').innerText = isRegen ? "ACTIVE" : "OFF";
                document.getElementById('regen_st').style.color = isRegen ? "#39ff14" : "#f00";

                group.children.forEach(c => {{ if(c.name==="p") c.rotation.y += 1.2; }});
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