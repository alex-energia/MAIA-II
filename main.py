# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

def evaluate_viability(idea):
    """Análisis de Viabilidad Nivel 1200"""
    score = 0.92
    alt = "Optimización de carga útil"
    if len(idea) < 5: score = 0.3
    return score, alt

def get_maia_v1200_mid(idea):
    idx = idea.upper() or "TOPOGRAPHY_UNIT"
    v_score, v_alt = evaluate_viability(idea)
    
    # --- 15 NODOS: INGENIERÍA DE ESTADO MEDIO (DENSIDAD ALTA) ---
    sw = {
        "01_DMA_CONTROL.py": f"""# DMA de Doble Buffer para {idx}\nimport machine\ndef dma_init():\n    # Configuración de flujo de datos sin intervención de CPU\n    dma = machine.DMA(1)\n    dma.init(mode=machine.DMA.CIRCULAR, fifo=True)\n    dma.config(priority=machine.DMA.HIGH, dest=0x40004404)\n    return "DMA_TRANSFER_ACTIVE_L1200" """,
        
        "02_REGEN_PHASE_15.py": f"""class RegenerativeCore:\n    '''NODO 15: Recuperación por Frenado de Motor en {idx}'''\n    def __init__(self):\n        self.k_regen = 0.085 # Coeficiente de recuperación\n    def compute(self, rpm, throttle):\n        # Lógica de inversión de puente H para carga de batería\n        if throttle < 0.05 and rpm > 5000:\n            current_return = (rpm / 1000) * self.k_regen\n            return f'INJECTING: {{current_return:.2f}}A' \n        return 'IDLE' """,

        "03_SATURATED_MIXER.py": """def flight_mixer(r, p, y, t):\n    '''Mixer con protección contra saturación de motores'''\n    m = [t-p+r+y, t+p-r+y, t-p-r-y, t+p+r-y]\n    max_m = max(m)\n    if max_m > 1.0:\n        m = [x/max_m for x in m]\n    return [max(0, x) for x in m]""",

        "04_ASYNCHRONOUS_SD.py": """class BlackBox:\n    '''Escritura en SD mediante hilos para evitar bloqueos'''\n    def write(self, data):\n        import _thread\n        _thread.start_new_thread(self._save, (data,))\n    def _save(self, d):\n        with open('/sd/data.log', 'a') as f: f.write(d)""",

        "05_KALMAN_FILTER.py": """class Kalman:\n    '''Filtro de 6 ejes para estabilidad en Topografía'''\n    def __init__(self):\n        self.q = 0.001; self.r = 0.03; self.p = 1.0; self.k = 0.0\n    def update(self, val, noise):\n        self.p += self.q; self.k = self.p / (self.p + self.r)\n        return val + self.k * (noise - val)""",

        "06_CAN_BUS_API.py": "def can_send(msg_id, payload): return f'CAN_TX_ID_{{msg_id}}_DATA_{{payload.hex()}}'",
        "07_MESH_RADIO_V3.py": "def freq_hop(): return 'FHSS_ACTIVE_868MHz_ENCRYPTED'",
        "08_BMS_LIPO_6S.py": "def get_cell_v(): return [4.18, 4.19, 4.17, 4.20, 4.18, 4.19]",
        "09_RTK_PRECISION.py": "def get_rtk_fix(): return 'STATUS: FIXED_LAT_LON_ACC_1CM'",
        "10_NEURAL_LINK.py": "def brain_drive(): return 'NEURAL_COMMAND_LATENCY_8MS'",
        "11_THERMAL_AI.py": "def thermal_infer(): return 'AI_HOTSPOT_DETECTED_COORD_X82'",
        "12_GIMBAL_STAB.py": "def lock_horizon(): return 'GIMBAL_PITCH_ROLL_COMPENSATED'",
        "13_BOOT_LOADER.py": f"def sys_boot(): return 'MAIA_II_{idx}_MID_STATE_OK'",
        "14_PARACHUTE_DRV.py": "def deploy(): return 'PYRO_CHARGE_ARMED_ALT_CHECK_OK'",
        "15_ENERGY_MON.py": "def regen_stats(): return 'TOTAL_RECOVERED_342mAh'"
    }

    # --- STRATEGIC PROFUNDO ---
    strat = {
        "VIABILIDAD": f"Puntuación: {v_score*100}%. Viable bajo parámetros de {idx}.",
        "FÍSICA DE VUELO": "Empuje TWR (Thrust-to-Weight) de 2.4:1. Cálculo de Reynolds para hélices de 15'.",
        "PROTOCOLO DE MONTAJE": "Uso de Loctite 243 en pernos de motor. Calibración dinámica de esc por bus CAN.",
        "RIESGOS": "Redundancia de enlace perdida. Fail-safe a 50m AGL con aterrizaje suave.",
        "COSTOS (BOM)": "Electrónica: $1,200. Estructura: $850. Sensores: $3,400. Total: $5,450."
    }

    # --- HARDWARE 8 CAPAS ---
    hw = {
        "CAPA 1: CORE": "STM32H7 480MHz Dual Core con FPU dedicada.",
        "CAPA 2: CHASIS": "Fibra de carbono prensada al vacío, espesor 4mm.",
        "CAPA 3: PROPULSIÓN": "Motores T-Motor MN6007 KV160 + ESC Alpha 60A.",
        "CAPA 4: REGEN": "Circuito de regeneración activo mediante puente de Mosfets GaN.",
        "CAPA 5: VISIÓN": "Sensor LiDAR Velodyne Puck Lite + Cámara Térmica.",
        "CAPA 6: ENERGÍA": "Batería de estado sólido 6S 30000mAh.",
        "CAPA 7: COMMS": "Enlace Herelink 2.4GHz + Telemetría RF 900MHz.",
        "CAPA 8: GPS": "Módulo RTK dual con antena de doble banda L1/L2."
    }

    return {"sw": sw, "strat": strat, "hw": hw, "v_score": v_score}

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    action = request.form.get('action', '')
    scroll_pos = request.form.get('scroll_pos', '0')
    chat_input = request.form.get('chat_input', '')
    
    if action == "clear":
        idea = ""; target = ""; chat_input = ""; is_gen = False
    else:
        is_gen = action == "generate" and idea != ""
        
    data = get_maia_v1200_mid(idea) if is_gen else {"sw": {}, "strat": {}, "hw": {}}
    current_code = data["sw"].get(target, "# MAIA II KERNEL MID-STATE\n# SELECCIONE NODO...")

    h = f"""
    <html><head><title>MAIA II - MID STATE</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; gap:10px; padding:15px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .grid {{ display:grid; grid-template-columns: 25% 40% 35%; gap:10px; height:85vh; padding:10px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,10,10,0.95); padding:15px; overflow-y:auto; position:relative; }}
        .visor {{ background:#050505; color:#39ff14; padding:15px; font-size:11px; border-left:3px solid #f0f; height:320px; overflow:auto; white-space:pre; margin-top:10px; }}
        .btn {{ padding:8px 15px; cursor:pointer; font-weight:bold; border:none; }}
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f02; width:100%; text-align:left; padding:10px; margin-bottom:5px; cursor:pointer; }}
        .active {{ background:rgba(240,0,255,0.2) !important; border-color:#f0f !important; }}
        input[type='text'] {{ background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1; }}
        .chat-area {{ background:#000; border:1px solid #0ff2; height:150px; margin-top:10px; padding:10px; font-size:11px; color:#aaa; overflow-y:auto; }}
        .telemetry {{ position:absolute; top:10; right:10; color:#0f0; font-size:11px; }}
    </style>
    </head><body>
    
    <form method='post' class='header' id="mainForm">
        <input type="text" name="drone_idea" value="{idea}" placeholder="Proyecto Dron...">
        <input type="hidden" name="scroll_pos" id="scroll_pos_val" value="{scroll_pos}">
        <button type='submit' name="action" value="generate" class="btn" style="background:#0ff;">GENERAR</button>
        <button type='submit' name="action" value="clear" class="btn" style="background:#f00; color:#fff;">LIMPIAR</button>
        <button type="button" class="btn" style="background:#ffd700;" onclick="maiaVoice()">VOZ</button>
    </form>

    <div class='grid'>
        <div class="panel">
            <h4 style="color:#f0f; margin-top:0;">[1] STRATEGIC PROFUNDO</h4>
            {"".join([f"<p><b>{k}:</b><br><small style='color:#ccc;'>{v}</small></p>" for k,v in data["strat"].items()])}
            
            <h4 style="color:#0ff;">MAIA CHAT EXPERTO</h4>
            <div class="chat-area">
                MAIA: Sistema en Estado Medio detectado.<br>
                {f"ALEX: {chat_input}<br>MAIA: Procesando registros para {idea}." if chat_input else ""}
            </div>
            <input type="text" name="chat_input" placeholder="Comando directo..." style="width:100%; margin-top:5px;">
        </div>

        <div class="panel" style="padding:0; overflow:hidden; position:relative;">
            <div id="c3d" style="width:100%; height:100%;"></div>
            <div class="telemetry">
                ALT: <span id="alt">0.0</span> m | VEL: <span id="vel">0.0</span> km/h<br>
                POS: 4.6097 N / 74.0817 W
            </div>
        </div>

        <div class="panel" id="nodes-panel">
            <h4 style="color:#ffd700; margin-top:0;">[2] HARDWARE (8 CAPAS)</h4>
            {"".join([f"<div style='margin-bottom:8px; border-left:2px solid #ffd700; padding-left:8px;'><small><b>{k}:</b> {v}</small></div>" for k,v in data["hw"].items()])}
            
            <h4 style="color:#f0f; margin-top:15px;">[3] PRODUCTION NODES (15)</h4>
            <div id="nodes-container" style="max-height:180px; overflow-y:auto; border:1px solid #333; padding:5px;">
                {"".join([f'''<button type="button" class="node-btn {'active' if n == target else ''}" onclick="navNode('{n}')">[FILE] {n}</button>''' for n in sorted(data["sw"].keys())])}
            </div>
            <div class="visor">{current_code}</div>
        </div>
    </div>

    <form id="navForm" method="post">
        <input type="hidden" name="drone_idea" value="{idea}">
        <input type="hidden" name="action" value="generate">
        <input type="hidden" name="target_node" id="target_node_val">
        <input type="hidden" name="scroll_pos" id="scroll_pos_node">
    </form>

    <script>
        const pNodes = document.getElementById('nodes-panel');
        window.onload = () => {{ pNodes.scrollTop = {scroll_pos}; }};

        function navNode(node) {{
            document.getElementById('target_node_val').value = node;
            document.getElementById('scroll_pos_node').value = pNodes.scrollTop;
            document.getElementById('navForm').submit();
        }}

        function maiaVoice() {{
            const m = new SpeechSynthesisUtterance("Alex, sistema {idea} listo para despliegue medio.");
            m.lang = 'es-ES'; window.speechSynthesis.speak(m);
        }}

        // MOTOR 3D - MOVIMIENTO DE INGENIERÍA
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth*0.4/(window.innerHeight*0.8), 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(window.innerWidth*0.4, window.innerHeight*0.8);
        document.getElementById('c3d').appendChild(renderer.domElement);

        const drone = new THREE.Group();
        if({ "true" if is_gen else "false" }) {{
            const core = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.2, 0.8), new THREE.MeshPhongMaterial({{color:0x333333}}));
            drone.add(core);
            const rtk = new THREE.Mesh(new THREE.CylinderGeometry(0.15, 0.15, 0.3), new THREE.MeshPhongMaterial({{color:0x00ffff}}));
            rtk.position.y = 0.2; drone.add(rtk);

            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(a => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 1.2), new THREE.MeshPhongMaterial({{color:0xffd700}}));
                arm.rotation.z = Math.PI/2; arm.rotation.y = a; drone.add(arm);
                const p = new THREE.Mesh(new THREE.BoxGeometry(0.7, 0.01, 0.1), new THREE.MeshBasicMaterial({{color:0x00ffff, transparent:true, opacity:0.6}}));
                p.position.set(Math.cos(a)*0.6, 0.15, Math.sin(a)*0.6); p.name="p"; drone.add(p);
            }});
        }}
        scene.add(drone);
        scene.add(new THREE.AmbientLight(0xffffff, 0.8));
        camera.position.set(5, 5, 5); camera.lookAt(0,0,0);

        let t = 0;
        function anim() {{
            requestAnimationFrame(anim);
            t += 0.03;
            if({ "true" if is_gen else "false" }) {{
                drone.position.y = Math.sin(t) * 0.8 + 2;
                drone.rotation.x = Math.cos(t*0.5) * 0.15;
                drone.rotation.z = Math.sin(t*0.5) * 0.15;
                document.getElementById('alt').innerText = (drone.position.y * 12.5).toFixed(2);
                document.getElementById('vel').innerText = (Math.abs(Math.sin(t))*38.2).toFixed(1);
                drone.children.forEach(c => {{ if(c.name==="p") c.rotation.y += 1.0; }});
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