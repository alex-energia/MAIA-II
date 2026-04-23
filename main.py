# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- BASE DE DATOS DE INGENIERÍA MAIA II ---
def get_maia_data():
    return {
        "strat": {
            "MISIÓN": "Infiltración y Reconocimiento Industrial",
            "OBJETIVO": "Escaneo de Activos en Tiempo Real",
            "ESTADO": "Kernel Blindado - Nivel 1200",
            "PRIORIDAD": "Máxima (Alex Root Access)",
            "PROTOCOLO": "Capa 2 / Barrido Global"
        },
        "hw": {
            "CHASIS": "Fibra de Carbono T800 Hexagonal",
            "MOTORES": "4x Brushless 2400KV Alta Respuesta",
            "SENSORES": "LiDAR Velodyne v2 + Térmica 4K",
            "ENERGÍA": "Batería de Grafeno 6S 8000mAh",
            "NÚCLEO": "Procesador Octa-Core MAIA Neural",
            "COMMS": "Enlace Satelital AES-256"
        },
        "sw": {
            "01_BOOT.py": "import os\nimport sys\n\ndef initialize_maia():\n    '''Carga de protocolos de seguridad v1200'''\n    status = 'BOOT_SEQUENCE_COMPLETE'\n    return status",
            "02_STABILITY.py": "import time\n\ndef auto_level(gyro_data):\n    '''Controlador PID para ejes X e Y'''\n    correction = (gyro_data * 0.15)\n    return correction",
            "03_PROPULSION.py": "def sync_motors(rpm_target):\n    '''Sincronización de los 4 motores brushless'''\n    for i in range(4):\n        power_up_motor(i, rpm_target)\n    return True",
            "04_LIDAR_SCAN.py": "from maia_vision import Lidar\n\ndef run_active_scan():\n    '''Mapeo 3D de activos industriales'''\n    scanner = Lidar(range=200)\n    return scanner.capture_3d()",
            "05_THERMAL_AI.py": "import cv2\n\ndef analyze_thermal_signature():\n    '''Detección de calor en núcleos de energía'''\n    raw_feed = get_cam_feed()\n    return process_heat_map(raw_feed)",
            "06_ENCRYPTION.py": "from Crypto.Cipher import AES\n\ndef seal_packet(data):\n    '''Cifrado de telemetría grado militar'''\n    cipher = AES.new(SECRET_KEY, AES.MODE_GCM)\n    return cipher.encrypt(data)",
            "07_GPS_LOCK.py": "def sync_satellites():\n    '''Triangulación GPS/GLONASS de alta precisión'''\n    lat, lon = 4.6243, -75.6732\n    return (lat, lon)",
            "08_BATTERY_MGMT.py": "def cell_balancer():\n    '''Gestión de descarga para celdas de Grafeno'''\n    if voltage < 3.2:\n        trigger_rtlh() # Return to Launch Site\n    return 'OK'",
            "09_AUTO_PILOT.py": "def navigate_waypoints(points):\n    '''Navegación autónoma evasiva'''\n    for p in points:\n        fly_to(p, mode='Stealth')\n    return 'FINISHED'",
            "10_OBJECT_AVOID.py": "def proximity_sensor():\n    '''Evasión de colisiones por ultrasonido'''\n    dist = read_sonar()\n    if dist < 1.5:\n        evade_left()\n    return dist",
            "11_TELEMETRY.py": "def stream_to_hud():\n    '''Envío de datos a la interfaz de Alex'''\n    stats = get_all_sensors()\n    return format_for_web(stats)",
            "12_NEURAL_LINK.py": "def neural_handshake():\n    '''Sincronización de interfaz cerebro-máquina'''\n    signal_quality = 0.98\n    return signal_quality",
            "13_STEALTH_MODE.py": "def activate_ghost():\n    '''Protocolo de baja observabilidad'''\n    set_leds(False)\n    mute_esc_frequency(True)\n    return 'GHOST_ON'",
            "14_KERNEL_SYS.py": "import sys\n\ndef maia_core_status():\n    '''Estado crítico del núcleo del sistema'''\n    return f'Uptime: {sys.uptime()}'"
        }
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    data = get_maia_data()
    # Captura de inputs
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    scroll_pos = request.form.get('scroll_pos', '0')
    
    # LÓGICA DE VISUALIZACIÓN DE CÓDIGO
    # Si hay un target_node en el POST, buscamos su código, si no, mostramos el placeholder.
    current_code = data["sw"].get(target, "# KERNEL MAIA II - VISOR DE CÓDIGO\n# SELECCIONE UN ARCHIVO .py A LA DERECHA")

    h = f"""
    <html><head><title>MAIA II - KERNEL v1200</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; padding:10px; background:#001a1a; border-bottom:1px solid #0ff; }}
        .grid-master {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:90vh; padding:10px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,10,10,0.95); padding:15px; overflow-y:auto; border-radius:4px; }}
        
        .strat-box {{ margin-bottom:15px; border-bottom:1px solid #0ff1; padding-bottom:5px; }}
        .hw-item {{ border-left:2px solid #ffd700; background:rgba(255,215,0,0.05); padding:8px; margin-bottom:5px; font-size:10px; }}
        
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f03; padding:6px; margin-bottom:4px; cursor:pointer; width:100%; text-align:left; font-size:10px; display:block; }}
        .node-btn:hover {{ background:rgba(0,255,0,0.1); border-color:#0f0; }}
        .active-node {{ background:rgba(240,0,255,0.25) !important; border: 1px solid #f0f !important; color:#fff !important; font-weight:bold; }}
        
        .code-box {{ background:#050505; color:#39ff14; padding:15px; font-size:11px; border-left:3px solid #f0f; white-space:pre; overflow-x:auto; height:240px; line-height:1.4; border-top:1px solid #333; font-family:'Courier New', monospace; }}
        #proto-container {{ width:100%; height:100%; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="letter-spacing:3px; color:#0ff; margin-right:20px;">MAIA II: DRONE CORE</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' style="background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1;" value='{idea}' placeholder="Comandos de ingeniería...">
            <button type='submit' style="background:#0ff; color:#000; font-weight:bold; border:none; padding:0 20px; cursor:pointer;">ACTUALIZAR</button>
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
            <div style="max-height:200px; overflow-y:auto; border:1px solid #333; padding:5px; background:#000; margin-bottom:10px;">
                {"".join([f'''<form method="post" class="nodo-form" style="margin:0;">
                    <input type="hidden" name="drone_idea" value="{idea}">
                    <input type="hidden" name="target_node" value="{n}">
                    <input type="hidden" name="scroll_pos" class="scroll-input">
                    <button type="submit" class="node-btn {'active-node' if n == target else ''}">[FILE] {n}</button>
                </form>''' for n in sorted(data["sw"].keys())])}
            </div>
            
            <div style="color:#f0f; font-size:10px; margin-bottom:5px;">EDITOR DE CÓDIGO KERNEL:</div>
            <div class="code-box">{current_code}</div>
        </div>
    </div>

    <script>
        // Sincronización de Scroll
        const panelR = document.getElementById('panel-derecho');
        window.onload = () => {{ panelR.scrollTop = {scroll_pos}; }};
        document.querySelectorAll('.nodo-form').forEach(f => {{
            f.onsubmit = () => {{ f.querySelector('.scroll-input').value = panelR.scrollTop; }};
        }});

        // --- MOTOR 3D MAIA II ---
        const container = document.getElementById('proto-container');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(container.clientWidth, container.clientHeight);
        container.appendChild(renderer.domElement);

        const droneGroup = new THREE.Group();
        const props = [];

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

        scene.add(droneGroup);
        const light = new THREE.PointLight(0x00ffff, 2, 50);
        light.position.set(5, 5, 5);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0xffffff, 0.2));
        camera.position.set(0, 5, 10);
        camera.lookAt(0,0,0);

        function animate() {{
            requestAnimationFrame(animate);
            droneGroup.position.y = Math.sin(Date.now() * 0.002) * 0.25;
            droneGroup.rotation.y += 0.005;
            props.forEach(p => p.rotation.y += 0.6);
            renderer.render(scene, camera);
        }}
        animate();
    </script>
    </body></html>
    """
    return render_template_string(h, scroll_pos=scroll_pos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)