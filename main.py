# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

def get_engineering_db(idea):
    """Generador de Ingeniería Densa Nivel 1200 - 14 Nodos Independientes"""
    i = idea.upper()
    # Diccionario de lógica para los 14 nodos (Densidad de producción)
    sw_nodes = {
        "01_KERNEL_CORE.py": f"""import os, sys, time\nfrom typing import Final\n\n# Core de {i}\nSYS_ID: Final = "{random.randint(1000,9999)}"\n\nclass MaiaKernel:\n    def __init__(self):\n        self.is_auth = False\n        self.boot_time = time.time()\n\n    def verify_checksum(self) -> bool:\n        '''Valida integridad de binarios en Capa 2'''\n        return os.access('/proc/self/exe', os.R_OK)\n\n    def launch(self):\n        if self.verify_checksum():\n            print(f"MAIA II [{i}] ONLINE")\n            self.is_auth = True""",

        "02_HARDWARE_HAL.py": f"""import ctypes\n\ndef set_pwm_freq(channel: int, freq: int):\n    '''Capa de Abstracción de Hardware para motores de {i}'''\n    # Acceso directo a registros de memoria para baja latencia\n    _lib = ctypes.CDLL('/usr/lib/libmaiahw.so')\n    return _lib.pwm_write(channel, freq)""",

        "03_FLIGHT_PID.py": f"""class FlightPID:\n    def __init__(self, kp: float, ki: float, kd: float):\n        self.p, self.i, self.d = kp, ki, kd\n        self.error_sum = 0.0\n        self.prev_err = 0.0\n\n    def compute(self, target: float, current: float, dt: float) -> float:\n        '''Algoritmo de estabilidad para {i}'''\n        error = target - current\n        self.error_sum += error * dt\n        der = (error - self.prev_err) / dt\n        self.prev_err = error\n        return (self.p * error) + (self.i * self.error_sum) + (self.d * der)""",

        "04_LIDAR_FUSION.py": f"""import numpy as np\n\ndef point_cloud_filter(raw_data: np.ndarray):\n    '''Filtro de densidad para mapeo de {i}'''\n    # Eliminación de ruido estadístico (SOR)\n    mean = np.mean(raw_data, axis=0)\n    dist = np.linalg.norm(raw_data - mean, axis=1)\n    return raw_data[dist < np.percentile(dist, 95)]""",

        "05_THERMAL_AI.py": f"""import cv2\n\ndef detect_anomalies(frame):\n    '''Inferencia de IA Térmica para {i}'''\n    net = cv2.dnn.readNetFromTensorflow('maia_v1200.pb')\n    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300))\n    net.setInput(blob)\n    return net.forward()""",

        "06_ENCRYPT_GCM.py": """from cryptography.hazmat.primitives.ciphers.aead import AESGCM\n\ndef secure_tx(data: bytes, key: bytes):\n    '''Cifrado de grado militar AES-256-GCM'''\n    aes = AESGCM(key)\n    nonce = os.urandom(12)\n    return aes.encrypt(nonce, data, b"MAIA_AUTH")""",

        "07_MESH_ROUTING.py": f"""import socket\n\ndef init_mesh_node(node_id: int):\n    '''Protocolo de enjambre dinámico para {i}'''\n    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)\n    return s""",

        "08_BATTERY_BMS.py": f"""def balance_cells(voltages: list):\n    '''Gestión de celdas de Grafeno para {i}'''\n    target = sum(voltages)/len(voltages)\n    return [v - target for v in voltages if abs(v-target) > 0.01]""",

        "09_GPS_RTK.py": """def get_precise_fix():\n    '''Posicionamiento centimétrico RTK L1/L2'''\n    from gnss_lib import RTKEngine\n    engine = RTKEngine(port='/dev/ttyAMA0', baud=921600)\n    return engine.get_solution()""",

        "10_SONAR_EVASION.py": """def collision_avoidance(dist: float):\n    '''Lógica de evasión ultrasónica activa'''\n    if dist < 1.5:\n        throttle_cut()\n        execute_yaw_evasion(direction='left')\n    return 'PATH_CLEAR'""",

        "11_TELEMETRY_HUD.py": """def update_ui_stream(stats: dict):\n    '''Inyección de telemetría en tiempo real'''\n    import json\n    return json.dumps({**stats, "status": "OPERATIONAL_V1200"})""",

        "12_NEURAL_INTERFACE.py": f"""def bridge_brain_wave(wave_data):\n    '''Control por interfaz neuronal para {i}'''\n    alpha_threshold = 0.75\n    return "EXECUTE" if wave_data > alpha_threshold else "IDLE" """,

        "13_STEALTH_MODE.py": """def ghost_protocol_on():\n    '''Reducción de firma acústica y térmica'''\n    set_motor_khz(48) # Frecuencia ultrasónica\n    led_array.off()\n    return True""",

        "14_SYSTEM_AUDIT.py": """import psutil\n\ndef full_audit():\n    '''Reporte crítico de hardware y carga de CPU'''\n    return {\n        "cpu": psutil.cpu_percent(),\n        "mem": psutil.virtual_memory().percent,\n        "temp": psutil.sensors_temperatures()\n    }"""
    }

    # ESTRATEGIA Y HARDWARE ELITE
    strat = {
        "ANÁLISIS ESTRATÉGICO": f"Implementación de arquitectura descentralizada para '{i}'. Redundancia de misión N+2.",
        "VIABILIDAD TÉCNICA": "ROI calculado en 1.2 años. Eficiencia energética optimizada mediante algoritmos de flujo laminar.",
        "PROTOCOLO DE SEGURIDAD": "Cifrado de extremo a extremo con rotación de llaves cada 300 segundos.",
        "OBJETIVOS TÁCTICOS": f"Infiltración y recolección de datos en entorno '{i}' con latencia inferior a 8ms."
    }
    
    hw = {
        "CHASIS": "Monocasco de Fibra de Carbono T800 y refuerzos de Kevlar en nodos de impacto.",
        "PROPULSIÓN": "Motores de levitación magnética con sensores Hall integrados para control de RPM absoluto.",
        "ÓPTICA": "Sensor multiespectral 8K con estabilización mecánica mediante gimbal de 4 ejes.",
        "NÚCLEO": "Procesador dedicado MAIA-V1200 con aceleración por hardware para visión artificial."
    }

    return {"sw": sw_nodes, "strat": strat, "hw": hw}

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    action = request.form.get('action', '')
    chat_msg = request.form.get('chat_msg', '')
    
    is_gen = action == "generate" and idea != ""
    data = get_engineering_db(idea) if is_gen else {"sw": {}, "strat": {}, "hw": {}}
    
    current_code = data["sw"].get(target, "# MAIA II KERNEL\n# SELECCIONE NODO PARA INSPECCIÓN.") if is_gen else "# SISTEMA APAGADO"

    h = f"""
    <html><head><title>MAIA II - KERNEL v1200</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; gap:10px; padding:15px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .grid {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:88vh; padding:10px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,10,10,0.95); padding:15px; overflow-y:auto; border-radius:5px; }}
        .code {{ background:#050505; color:#39ff14; padding:15px; font-size:11px; border-left:3px solid #f0f; height:350px; overflow:auto; white-space:pre; }}
        .btn {{ padding:8px 15px; cursor:pointer; font-weight:bold; border:none; }}
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f02; width:100%; text-align:left; padding:6px; margin-bottom:3px; font-size:10px; }}
        .active {{ background:rgba(240,0,255,0.2) !important; border-color:#f0f !important; }}
        input[type='text'] {{ background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1; }}
        .chat-box {{ background:#000; border:1px solid #0ff2; height:100px; margin-top:10px; padding:5px; font-size:10px; overflow-y:auto; color: #aaa; }}
    </style>
    </head><body>
    
    <form method='post' class='header'>
        <input type="text" name="drone_idea" value="{idea}" placeholder="Idea del Dron (Ej: Vigilancia Urbana, Inspección Térmica...)">
        <button type='submit' name="action" value="generate" class="btn" style="background:#0ff;">GENERAR</button>
        <button type='submit' name="action" value="clear" class="btn" style="background:#f00; color:#fff;">LIMPIAR</button>
        <button type="button" class="btn" style="background:#ffd700;" onclick="speak()">VOZ MAIA</button>
    </form>

    <div class='grid'>
        <div class="panel">
            <h4 style="color:#f0f; margin-top:0;">[1] STRATEGIC ANALYSIS</h4>
            {"".join([f"<p><b>{k}:</b><br><small style='color:#ccc;'>{v}</small></p>" for k,v in data["strat"].items()])}
            
            <div style="margin-top:20px;">
                <h4 style="color:#0ff;">CHAT DE MAIA</h4>
                <div class="chat-box" id="chat">MAIA: Esperando comandos de Alex...<br>{f"USER: {chat_msg}<br>MAIA: Procesando ingeniería para {idea}" if chat_msg else ""}</div>
                <input type="text" name="chat_msg" placeholder="Hablar con MAIA..." style="width:100%; margin-top:5px;">
            </div>
        </div>

        <div class="panel" style="padding:0; position:relative;">
            <div id="c3d" style="width:100%; height:100%;"></div>
            <div style="position:absolute; bottom:10; left:10; color:#0f0; font-size:10px;">GPS: LOCK | AEAD: ON | V1200</div>
        </div>

        <div class="panel">
            <h4 style="color:#ffd700; margin-top:0;">[2] HARDWARE ELITE</h4>
            {"".join([f"<div style='margin-bottom:10px; border-left:2px solid #ffd700; padding-left:10px;'><small><b>{k}:</b> {v}</small></div>" for k,v in data["hw"].items()])}
            
            <h4 style="color:#f0f; margin-top:20px;">[3] PRODUCTION NODES (14)</h4>
            <div style="max-height:180px; overflow-y:auto; border:1px solid #333; padding:5px; margin-bottom:10px;">
                {"".join([f'''<form method="post" style="margin:0;">
                    <input type="hidden" name="drone_idea" value="{idea}">
                    <input type="hidden" name="action" value="generate">
                    <input type="hidden" name="target_node" value="{n}">
                    <button type="submit" class="node-btn {'active' if n == target else ''}">[SRC] {n}</button>
                </form>''' for n in sorted(data["sw"].keys())])}
            </div>
            <div class="code">{current_code}</div>
        </div>
    </div>

    <script>
        function speak() {{
            const m = new SpeechSynthesisUtterance("{f'Sistema de {idea} generado con éxito.' if is_gen else 'En espera de idea.'}");
            m.lang = 'es-ES'; window.speechSynthesis.speak(m);
        }}

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth*0.45/(window.innerHeight*0.8), 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(window.innerWidth*0.45, window.innerHeight*0.8);
        document.getElementById('c3d').appendChild(renderer.domElement);

        const g = new THREE.Group();
        if({ "true" if is_gen else "false" }) {{
            const body = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.3, 1.2), new THREE.MeshPhongMaterial({{color:0x111111}}));
            g.add(body);
            // LUCES ESTROBOSCÓPICAS
            const l1 = new THREE.PointLight(0xff0000, 2, 5); l1.position.set(0.6, 0.2, 0.6); g.add(l1);
            const l2 = new THREE.PointLight(0x0000ff, 2, 5); l2.position.set(-0.6, 0.2, 0.6); g.add(l2);
            // SENSORES Y LENTES
            const s = new THREE.Mesh(new THREE.SphereGeometry(0.2, 16, 16), new THREE.MeshPhongMaterial({{color:0x333333}}));
            s.position.set(0, -0.3, 0.5); g.add(s);
            
            [1,-1].forEach(x => [1,-1].forEach(z => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 1), new THREE.MeshPhongMaterial({{color:0xffd700}}));
                arm.rotation.z = Math.PI/2; arm.position.set(x*0.6, 0, z*0.6); g.add(arm);
                const p = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.02, 0.1), new THREE.MeshBasicMaterial({{color:0x00ffff, transparent:true, opacity:0.5}}));
                p.position.set(x*1.1, 0.1, z*1.1); p.name="p"; g.add(p);
            }}));
        }}
        scene.add(g);
        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        const pl = new THREE.PointLight(0x00ffff, 1, 20); pl.position.set(5, 5, 5); scene.add(pl);
        camera.position.set(0, 3, 7); camera.lookAt(0,0,0);

        function anim() {{
            requestAnimationFrame(anim);
            g.rotation.y += 0.005;
            g.children.forEach(c => {{ if(c.name==="p") c.rotation.y += 0.5; }});
            renderer.render(scene, camera);
        }}
        anim();
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)