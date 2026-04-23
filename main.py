# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

def get_empty_state():
    return {"strat": {}, "hw": {}, "sw": {}, "code": "# SISTEMA EN ESPERA...\n# PRESIONE 'GENERAR' PARA DESPLEGAR MAIA II"}

def get_full_data():
    return {
        "strat": {
            "MISIÓN TÁCTICA": "Infiltración y mapeo de activos críticos industriales mediante enjambre de drones.",
            "VIABILIDAD": "Alta. Retorno de inversión estimado en 14 meses mediante optimización de mantenimiento predictivo.",
            "RIESGO OPERATIVO": "Nivel 2 (Bajo). Mitigación mediante protocolos de sigilo y cifrado AES-256.",
            "ESTADO DE RED": "Nodo central sincronizado. Capa 2 operativa bajo estándar Nivel 1200.",
            "ACCESO": "Root Alex - Autorización de Nivel 5 concedida."
        },
        "hw": {
            "CHASIS": "Estructura hexagonal de fibra de carbono T800 con refuerzo de titanio en puntos de torsión.",
            "MOTORES": "4x Brushless Cobra 2400KV con ESC de 60A y refrigeración líquida pasiva.",
            "ÓPTICA/SCAN": "Sensor LiDAR Velodyne Puck v2 + Cámara térmica Flir Boson 640p.",
            "NÚCLEO": "Unidad de procesamiento neuronal MAIA-Core con 128 núcleos para IA en el borde.",
            "ENERGÍA": "Baterías de estado sólido de grafeno 6S (22.2V) con autonomía de 55 minutos."
        },
        "sw": {
            "01_BOOT_KERNEL.py": "import os\nimport sys\nimport logging\n\nclass MaiaKernel:\n    def __init__(self):\n        self.version = '1.2.0.0'\n        self.mode = 'STEALTH'\n\n    def launch(self):\n        try:\n            logging.info(f'Iniciando MAIA II v{self.version}')\n            os.environ['MAIA_AUTH'] = 'ALEX_ROOT'\n            return True\n        except Exception as e:\n            return f'CRITICAL_ERROR: {e}'",
            
            "02_PID_STABILITY.py": "class FlightController:\n    def __init__(self, kp, ki, kd):\n        self.p, self.i, self.d = kp, ki, kd\n        self.last_error = 0\n\n    def compute_correction(self, target, current):\n        error = target - current\n        p_out = self.p * error\n        i_out = (self.i * error) + self.last_error\n        d_out = self.d * (error - self.last_error)\n        self.last_error = error\n        return p_out + i_out + d_out",
            
            "03_LIDAR_MAPPING.py": "import numpy as np\nfrom sensors import LidarScanner\n\ndef generate_asset_cloud(range_max=200):\n    scanner = LidarScanner(mode='HD')\n    raw_points = scanner.get_buffer()\n    # Filtrar puntos fuera de rango y ruido\n    processed = np.delete(raw_points, np.where(raw_points > range_max))\n    return processed.reshape(-1, 3)",
            
            "04_AES_CRYPTO.py": "from Crypto.Cipher import AES\nfrom Crypto.Util import Counter\n\ndef encrypt_telemetry(payload, secret_key):\n    ctr = Counter.new(128)\n    cipher = AES.new(secret_key, AES.MODE_CTR, counter=ctr)\n    return cipher.encrypt(payload)",
            
            "05_THERMAL_DETECT.py": "import cv2\n\ndef identify_heat_leak(frame):\n    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)\n    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\n    return [cv2.boundingRect(c) for c in contours]",
            
            "06_SWARM_LOGIC.py": "def sync_drone_position(drone_id, swarm_map):\n    '''Algoritmo de cohesión y separación para enjambres'''\n    my_pos = swarm_map[drone_id]\n    neighbors = [p for id, p in swarm_map.items() if id != drone_id]\n    # Calcular vector de repulsión\n    repulsion = sum([1/(my_pos - n) for n in neighbors])\n    return my_pos + repulsion",
            
            "07_GPS_LOCK_V2.py": "import gnss_api\n\ndef get_precision_fix():\n    fix = gnss_api.get_location(constellation=['GPS', 'GLONASS', 'GALILEO'])\n    if fix.hdop < 1.0:\n        return fix.coords\n    return 'WAITING_FOR_SATELLITES'",
            
            "08_POWER_MGMT.py": "def check_battery_health(cells_v):\n    '''Análisis de balanceo de celdas 6S'''\n    avg_v = sum(cells_v) / 6\n    deviation = max([abs(v - avg_v) for v in cells_v])\n    if deviation > 0.05:\n        return 'CELL_IMBALANCE_DETECTED'\n    return 'BATTERY_NOMINAL'",
            
            "09_AUTO_PILOT.py": "@autopilot_decorator\ndef mission_execute(path):\n    for waypoint in path:\n        if not obstacle_ahead():\n            move_to(waypoint)\n        else:\n            recalculate_route(waypoint)",
            
            "10_SONAR_AVOID.py": "import RPi.GPIO as GPIO\n\ndef get_distance():\n    GPIO.output(TRIG, True)\n    # Medir tiempo de eco\n    while GPIO.input(ECHO) == 0: start = time.time()\n    while GPIO.input(ECHO) == 1: end = time.time()\n    return (end - start) * 17150",
            
            "11_TELEMETRY_API.py": "import json\nfrom flask import jsonify\n\ndef broadcast_status(drone_obj):\n    data = {\n        'id': drone_obj.id,\n        'telemetry': drone_obj.get_full_stats(),\n        'auth': 'SECURE_V1200'\n    }\n    return json.dumps(data)",
            
            "12_NEURAL_LINK.py": "import brain_interface as bi\n\ndef sync_neural_stream():\n    if bi.check_handshake('ALEX_ALPHA_WAVE'):\n        return bi.connect_motor_cortex(drone_id=0)\n    return False",
            
            "13_GHOST_PROTOCOL.py": "def stealth_activation():\n    '''Modo de baja visibilidad para infiltración'''\n    motors.set_esc_timing('silent')\n    lights.all_off()\n    rf.set_low_power_mode()\n    return 'GHOST_MODE_ACTIVE'",
            
            "14_SYSTEM_CHECK.py": "import psutil\n\ndef get_core_load():\n    cpu = psutil.cpu_percent(interval=1)\n    ram = psutil.virtual_memory().percent\n    return f'CPU: {cpu}% | RAM: {ram}% | DISK: OK'"
        }
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    is_generated = request.form.get('generated') == 'true'
    action = request.form.get('action', '')
    
    # Manejo de estados (Vacío o Generado)
    if is_generated and action != 'clear':
        data = get_full_data()
    else:
        data = get_empty_state()
        is_generated = False

    target = request.form.get('target_node', '')
    scroll_pos = request.form.get('scroll_pos', '0')
    current_code = data["sw"].get(target, "# MAIA II: ESPERANDO DESPLIEGUE\n# Seleccione un archivo .py para inspección de ingeniería.") if is_generated else data["code"]

    h = f"""
    <html><head><title>MAIA II - KERNEL v1200</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; padding:10px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .grid-master {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:90vh; padding:10px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,10,10,0.95); padding:15px; overflow-y:auto; border-radius:4px; }}
        
        .strat-box {{ margin-bottom:15px; border-bottom:1px solid #0ff1; padding-bottom:5px; }}
        .hw-item {{ border-left:2px solid #ffd700; background:rgba(255,215,0,0.05); padding:8px; margin-bottom:5px; font-size:10px; }}
        
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f03; padding:6px; margin-bottom:4px; cursor:pointer; width:100%; text-align:left; font-size:10px; display:block; }}
        .node-btn:hover {{ background:rgba(0,255,0,0.1); }}
        .active-node {{ background:rgba(240,0,255,0.25) !important; border: 1px solid #f0f !important; color:#fff !important; }}
        
        .code-box {{ background:#050505; color:#39ff14; padding:15px; font-size:11px; border-left:3px solid #f0f; white-space:pre; overflow-x:auto; height:240px; line-height:1.4; border-top:1px solid #333; }}
        .btn-main {{ background:#0ff; color:#000; border:none; padding:8px 15px; font-weight:bold; cursor:pointer; margin-right:5px; }}
        .btn-clear {{ background:#f00; color:#fff; border:none; padding:8px 15px; cursor:pointer; }}
        .btn-chat {{ background:#f0f; color:#fff; border:none; padding:8px 15px; cursor:pointer; }}
        #proto-container {{ width:100%; height:100%; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="letter-spacing:3px; color:#0ff; margin-right:20px;">MAIA II: DRONE INTERFACE</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input type="hidden" name="generated" value="true">
            <button type='submit' name="action" value="generate" class="btn-main">GENERAR MAIA II</button>
            <button type='submit' name="action" value="clear" class="btn-clear">LIMPIAR</button>
            <button type="button" class="btn-chat" onclick="alert('CHAT MAIA: En espera de comandos de Alex...')">CHAT MAIA</button>
            <button type="button" id="voice-btn" class="btn-main" style="background:#ffd700;" onclick="speakMaia()">VOZ MAIA</button>
        </form>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#f0f; margin-top:0;">[1] STRATEGIC ENGINE</h4>
            {"".join([f"<div class='strat-box'><b style='color:#0ff;'>{k}</b><br><span style='color:#ccc;'>{v}</span></div>" for k,v in data["strat"].items()])}
        </div>

        <div class="panel" style="padding:0; overflow:hidden;">
            <div id="proto-container"></div>
        </div>

        <div class="panel" id="panel-derecho">
            <h4 style="color:#ffd700; margin-top:0;">[2] HARDWARE SPECS</h4>
            {"".join([f"<div class='hw-item'><b>{k}</b>: {v}</div>" for k,v in data["hw"].items()])}
            
            <h4 style="color:#f0f; margin-top:20px;">[3] SOFTWARE NODES (.py)</h4>
            <div style="max-height:180px; overflow-y:auto; border:1px solid #333; padding:5px; background:#000; margin-bottom:10px;">
                {"".join([f'''<form method="post" class="nodo-form" style="margin:0;">
                    <input type="hidden" name="generated" value="true">
                    <input type="hidden" name="target_node" value="{n}">
                    <input type="hidden" name="scroll_pos" class="scroll-input">
                    <button type="submit" class="node-btn {'active-node' if n == target else ''}">[SRC] {n}</button>
                </form>''' for n in sorted(data["sw"].keys())])}
            </div>
            <div class="code-box">{current_code}</div>
        </div>
    </div>

    <script>
        function speakMaia() {{
            const msg = new SpeechSynthesisUtterance("{'Alex, sistema MAIA II desplegado y listo para infiltración.' if is_generated else 'Esperando orden de generación, Alex.'}");
            msg.lang = 'es-ES'; window.speechSynthesis.speak(msg);
        }}

        const panelR = document.getElementById('panel-derecho');
        window.onload = () => {{ panelR.scrollTop = {scroll_pos}; }};
        document.querySelectorAll('.nodo-form').forEach(f => {{
            f.onsubmit = () => {{ f.querySelector('.scroll-input').value = panelR.scrollTop; }};
        }});

        const container = document.getElementById('proto-container');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(renderer.domElement);

        const droneGroup = new THREE.Group();
        const props = [];

        if({ "true" if is_generated else "false" }) {{
            const body = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 1, 0.5, 6), new THREE.MeshPhongMaterial({{color: 0x111111, specular: 0x00ffff}}));
            droneGroup.add(body);
            const core = new THREE.Mesh(new THREE.SphereGeometry(0.25, 16, 16), new THREE.MeshBasicMaterial({{color: 0x00ffff}}));
            core.position.y = 0.4;
            droneGroup.add(core);

            const armCoords = [{{x:1.8, z:1.8}}, {{x:-1.8, z:1.8}}, {{x:1.8, z:-1.8}}, {{x:-1.8, z:-1.8}}];
            armCoords.forEach(p => {{
                const arm = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.15, 0.15), new THREE.MeshPhongMaterial({{color: 0xffd700}}));
                arm.position.set(p.x/2, 0, p.z/2);
                arm.rotation.y = -Math.atan2(p.z, p.x);
                droneGroup.add(arm);
                const prop = new THREE.Group();
                const blade = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.02, 0.15), new THREE.MeshBasicMaterial({{color: 0x00ffff, transparent:true, opacity:0.8}}));
                const blade2 = blade.clone(); blade2.rotation.y = Math.PI/2;
                prop.add(blade, blade2);
                prop.position.set(p.x, 0.3, p.z);
                props.push(prop);
                droneGroup.add(prop);
            }});
        }}

        scene.add(droneGroup);
        const light = new THREE.PointLight(0x00ffff, 2, 50);
        light.position.set(5, 5, 5);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0xffffff, 0.2));
        camera.position.set(0, 5, 10); camera.lookAt(0,0,0);

        function animate() {{
            requestAnimationFrame(animate);
            if({ "true" if is_generated else "false" }) {{
                droneGroup.position.y = Math.sin(Date.now() * 0.002) * 0.25;
                droneGroup.rotation.y += 0.005;
                props.forEach(p => p.rotation.y += 0.6);
            }}
            renderer.render(scene, camera);
        }}
        animate();
    </script>
    </body></html>
    """
    return render_template_string(h, scroll_pos=scroll_pos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
