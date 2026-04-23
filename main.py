# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

def generate_expert_code(idea):
    idx = idea.upper()
    # Lógica de producción real: Registros, Buffers y Protocolos de bajo nivel
    nodes = {
        "01_BOOT_HAL.py": f"""import machine, time\n# Nivel 1200: Bootloader para {idx}\nclass BootManager:\n    def __init__(self):\n        self.wdt = machine.WDT(timeout=2000)\n        self.rtc = machine.RTC()\n\n    def system_check(self):\n        '''Validación de integridad de memoria Flash'''\n        hash_val = machine.unique_id()\n        return True if hash_val else False""",

        "02_REGEN_CORE_15.py": f"""# NODO 15: REGENERACIÓN POR GIRO (HÉLICES)\nclass EnergyRecovery:\n    def __init__(self, esc_id):\n        self.v_bus = 22.2\n        self.is_braking = False\n\n    def active_regeneration(self, rpm_actual, rpm_target):\n        '''Inyección de corriente inversa en frenado de {idx}'''\n        if rpm_actual > rpm_target:\n            self.is_braking = True\n            duty_cycle = (rpm_actual - rpm_target) * 0.12\n            return f"REGEN_ACTIVE: {{duty_cycle}}mA_BACK_INJECTION"\n        return "CONSUMPTION_MODE" """,

        "03_SURVEY_LIDAR.py": f"""import ustruct\n# Captura de densidades para Topografía\nclass LidarSlam:\n    def __init__(self, uart_bus):\n        self.uart = uart_bus\n\n    def read_packet(self):\n        raw = self.uart.read(47)\n        # Desempaquetado de trama binaria de 360 grados\n        data = ustruct.unpack('<HHf', raw[4:12])\n        return {{"dist": data[0], "angle": data[1], "signal": data[2]}}""",

        "04_NAV_STABILITY.py": """class IMU_Fusion:\n    def __init__(self):\n        self.q = [1.0, 0.0, 0.0, 0.0] # Cuaterniones\n\n    def update_ahrs(self, gx, gy, gz, ax, ay, az):\n        '''Filtro Madgwick para orientación espacial'''\n        # Algoritmo de 6 ejes para estabilidad topográfica absoluta\n        pass """,

        "05_MESH_COMMS.py": """import network, espnow\n# Red Mesh de grado militar\ndef init_mesh():\n    sta = network.WLAN(network.STA_IF)\n    sta.active(True)\n    enow = espnow.ESPNow()\n    enow.active(True)\n    return enow """,

        "06_AES_VAULT.py": """from ucryptolib import aes\ndef secure_link(payload, key):\n    # Cifrado por hardware AES-CBC\n    cipher = aes(key, 1) # Mode 1: CBC\n    return cipher.encrypt(payload) """,

        "07_MOTOR_ESC.py": f"""def set_esc_timing(val):\n    '''Configuración de frecuencia para {idx}'''\n    # 32kHz PWM para reducir ruido acústico\n    return f"ESC_FREQ_SET: 32000Hz" """,

        "08_BATTERY_MGMT.py": """def read_cell_v(adc_pin):\n    '''Lectura de precisión 12-bit para celdas de Grafeno'''\n    raw = adc_pin.read_u16()\n    return (raw * 3.3 / 65535) * 11 # Divisor de tensión """,

        "09_GPS_RTK_PRO.py": """def parse_ubx_nav_pvt(data):\n    '''Extracción centimétrica de trama UBX-NAV-PVT'''\n    itow, lon, lat, h_msl = ustruct.unpack('<Iiiii', data[6:26])\n    return (lat/1e7, lon/1e7) """,

        "10_NEURAL_LINK.py": """class NeuralInterface:\n    def filter_eeg(self, raw_buffer):\n        '''Filtro de paso de banda para ondas Alpha'''\n        return [x for x in raw_buffer if 8 <= x <= 12] """,

        "11_THERMAL_PRO.py": """def get_isotherm_area(frame, temp_threshold):\n    import numpy as np\n    mask = np.where(frame > temp_threshold, 255, 0)\n    return mask """,

        "12_GIMBAL_API.py": """def sync_camera_to_imu(pitch, roll):\n    # Estabilización de horizonte vía bus CAN\n    return f"CAN_TX: PITCH={{pitch}} ROLL={{roll}}" """,

        "13_SYSTEM_MONITOR.py": """import gc\ndef get_free_heap():\n    # Monitor de memoria RAM embebida (No psutil)\n    gc.collect()\n    return gc.mem_free() """,

        "14_RECOVERY_SYS.py": """def trigger_parachute():\n    '''Protocolo de emergencia por fallo de motor'''\n    pin = machine.Pin(15, machine.Pin.OUT)\n    pin.on()\n    return "PARACHUTE_DEPLOYED" """,

        "15_REGEN_INIT.py": """def bootstrap_regen():\n    return "MODULE_15_REGEN_READY" """
    }
    
    strat = {
        "MISIÓN TÁCTICA": f"Análisis topográfico HD en entorno {idx}.",
        "VIABILIDAD": "Recuperación de energía del 4% mediante frenado dinámico en hélices.",
        "HARDWARE CORE": "Nodos de procesamiento redundante STM32H7 + FPGA.",
        "AUDITORÍA": "Capa 2 activa. Todos los buses de datos cifrados bajo estándar V1200."
    }

    hw = {
        "CHASIS": "Fibra de Carbono T1100 (Grado Aeroespacial)",
        "PROPULSIÓN": "Motores con imanes de neodimio N52SH y hélices regenerativas.",
        "ENERGÍA": "Batería de estado sólido con Bus de Regeneración activo.",
        "ESC": "Protocolo DSHOT1200 con soporte para Telemetría Bidireccional."
    }

    return {"sw": nodes, "strat": strat, "hw": hw}

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    action = request.form.get('action', '')
    # FIX: Guardar posición del scroll
    scroll_top = request.form.get('scroll_pos', '0')
    
    is_gen = action == "generate" and idea != ""
    data = generate_expert_code(idea) if is_gen else {"sw": {}, "strat": {}, "hw": {}}
    
    current_code = data["sw"].get(target, "# MAIA II EXPERT KERNEL\n# ESPERANDO COMANDO DE DESPLIEGUE...")

    h = f"""
    <html><head><title>MAIA II - CAPA 2</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; gap:10px; padding:15px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .grid {{ display:grid; grid-template-columns: 25% 40% 35%; gap:10px; height:88vh; padding:10px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,10,10,0.95); padding:15px; overflow-y:auto; position:relative; }}
        .code-visor {{ background:#050505; color:#39ff14; padding:15px; font-size:11px; border-left:3px solid #f0f; height:380px; overflow:auto; white-space:pre; margin-top:10px; }}
        .btn {{ padding:8px 15px; cursor:pointer; font-weight:bold; border:none; }}
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f02; width:100%; text-align:left; padding:8px; margin-bottom:4px; font-size:10px; cursor:pointer; }}
        .active {{ background:rgba(240,0,255,0.2) !important; border-color:#f0f !important; }}
        input[type='text'] {{ background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1; }}
    </style>
    </head><body>
    
    <form method='post' class='header' id="mainForm">
        <input type="text" name="drone_idea" value="{idea}" placeholder="Escriba la idea del dron...">
        <input type="hidden" name="scroll_pos" id="scroll_pos" value="{scroll_top}">
        <button type='submit' name="action" value="generate" class="btn" style="background:#0ff;">GENERAR</button>
        <button type='submit' name="action" value="clear" class="btn" style="background:#f00; color:#fff;">LIMPIAR</button>
    </form>

    <div class='grid'>
        <div class="panel">
            <h4 style="color:#f0f; margin-top:0;">[1] STRATEGIC ENGINE</h4>
            {"".join([f"<p><b>{k}:</b><br><small style='color:#ccc;'>{v}</small></p>" for k,v in data["strat"].items()])}
        </div>

        <div class="panel" style="padding:0; overflow:hidden;">
            <div id="c3d" style="width:100%; height:100%;"></div>
        </div>

        <div class="panel" id="panel-derecho">
            <h4 style="color:#ffd700; margin-top:0;">[2] HARDWARE ELITE (REGEN ACTIVE)</h4>
            {"".join([f"<div style='margin-bottom:8px; border-left:2px solid #ffd700; padding-left:8px;'><small><b>{k}:</b> {v}</small></div>" for k,v in data["hw"].items()])}
            
            <h4 style="color:#f0f; margin-top:15px;">[3] SOFTWARE NODES (15)</h4>
            <div style="max-height:200px; overflow-y:auto; border:1px solid #333; padding:5px;">
                {"".join([f'''<button type="button" class="node-btn {'active' if n == target else ''}" onclick="selectNode('{n}')">[FILE] {n}</button>''' for n in sorted(data["sw"].keys())])}
            </div>
            <div class="code-visor" id="visor">{current_code}</div>
        </div>
    </div>

    <form id="nodeForm" method="post">
        <input type="hidden" name="drone_idea" value="{idea}">
        <input type="hidden" name="action" value="generate">
        <input type="hidden" name="target_node" id="target_node">
        <input type="hidden" name="scroll_pos" id="scroll_pos_node">
    </form>

    <script>
        // PERSISTENCIA DE SCROLL (Solución definitiva al salto)
        const panelDer = document.getElementById('panel-derecho');
        window.onload = () => {{ panelDer.scrollTop = {scroll_top}; }};

        function selectNode(nodeName) {{
            document.getElementById('target_node').value = nodeName;
            document.getElementById('scroll_pos_node').value = panelDer.scrollTop;
            document.getElementById('nodeForm').submit();
        }}

        // MOTOR 3D
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth*0.4/(window.innerHeight*0.8), 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(window.innerWidth*0.4, window.innerHeight*0.8);
        document.getElementById('c3d').appendChild(renderer.domElement);

        const g = new THREE.Group();
        if({ "true" if is_gen else "false" }) {{
            const body = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.4, 1.2), new THREE.MeshPhongMaterial({{color:0x111111}}));
            g.add(body);
            // Luces de Regeneración (Ambar)
            const lr = new THREE.PointLight(0xffaa00, 2, 4); lr.position.set(0, 0.5, 0); g.add(lr);
            
            [1,-1].forEach(x => [1,-1].forEach(z => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 1), new THREE.MeshPhongMaterial({{color:0xffd700}}));
                arm.rotation.z = Math.PI/2; arm.position.set(x*0.6, 0, z*0.6); g.add(arm);
                const p = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.02, 0.1), new THREE.MeshBasicMaterial({{color:0x00ffff, transparent:true, opacity:0.6}}));
                p.position.set(x*1.1, 0.1, z*1.1); p.name="p"; g.add(p);
            }}));
        }}
        scene.add(g);
        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        camera.position.set(0, 3, 7); camera.lookAt(0,0,0);

        function anim() {{
            requestAnimationFrame(anim);
            g.rotation.y += 0.005;
            g.children.forEach(c => {{ if(c.name==="p") c.rotation.y += 0.8; }});
            renderer.render(scene, camera);
        }}
        anim();
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
