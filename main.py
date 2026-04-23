# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- BASE DE DATOS INTEGRADA MAIA II ---
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
            "01_BOOT.py": "import os\ndef init():\n    print('MAIA II Online')\n    os.environ['LEVEL'] = '1200'",
            "02_STABILITY.py": "def auto_level(drone_id):\n    '''Control PID de ejes X/Y'''\n    return 'LEVEL_OK'",
            "03_PROPULSION.py": "def set_rpm(motor, value):\n    '''Sincronización de hélices'''\n    pass",
            "04_LIDAR_SCAN.py": "import lidar\ndef run_scan():\n    return lidar.cloud_points()",
            "05_THERMAL_AI.py": "def detect_heat():\n    '''Detección de firmas térmicas'''\n    return True",
            "06_ENCRYPTION.py": "from Crypto import AES\ndef encrypt(data):\n    return AES.new(key).seal(data)",
            "07_GPS_LOCK.py": "def get_coords():\n    return '4.6243N, 75.6732W'",
            "08_BATTERY_MGMT.py": "def check_cell():\n    return 'Voltage_Nominal: 22.2V'",
            "09_AUTO_PILOT.py": "def fly_to(wp):\n    print(f'Navegando a {wp}')",
            "10_OBJECT_AVOID.py": "def sonar_check():\n    '''Evasión de colisiones activa'''\n    return 'CLEAR'",
            "11_TELEMETRY.py": "def push_hud(data):\n    '''Inyección de datos en Interfaz'''\n    return data",
            "12_NEURAL_LINK.py": "def brain_sync():\n    '''Interfaz Cerebro-Máquina v1'''\n    return 1.0",
            "13_STEALTH_MODE.py": "def ghost_protocol():\n    '''Silenciar motores y LEDs'''\n    return 'SILENT'",
            "14_KERNEL_SYS.py": "import sys\ndef sys_check():\n    return sys.version"
        }
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    data = get_maia_data()
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    scroll_pos = request.form.get('scroll_pos', '0')
    
    current_code = data["sw"].get(target, "# KERNEL MAIA II\n# SELECCIONE UN NODO (.py) PARA VER EL CÓDIGO")

    h = f"""
    <html><head><title>MAIA II - KERNEL</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; padding:10px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .grid-master {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:90vh; padding:10px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,10,10,0.95); padding:15px; overflow-y:auto; border-radius:4px; position:relative; }}
        
        .strat-box {{ margin-bottom:15px; border-bottom:1px solid #0ff1; padding-bottom:5px; }}
        .hw-item {{ border-left:2px solid #ffd700; background:rgba(255,215,0,0.05); padding:8px; margin-bottom:5px; font-size:10px; }}
        
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f03; padding:6px; margin-bottom:4px; cursor:pointer; width:100%; text-align:left; font-size:10px; }}
        .node-btn:hover {{ background:rgba(0,255,0,0.1); border-color:#0f0; }}
        .active-node {{ background:rgba(240,0,255,0.2); border-color:#f0f; color:#fff; }}
        
        .code-box {{ background:#050505; color:#39ff14; padding:15px; font-size:11px; border-left:3px solid #f0f; white-space:pre; overflow-x:auto; height:250px; line-height:1.4; border-top:1px solid #333; }}
        #proto-container {{ width:100%; height:100%; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="letter-spacing:3px; color:#0ff;">MAIA II: DRONE CORE</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0 20px;">
            <input name='drone_idea' style="background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1;" value='{idea}'>
            <button type='submit' style="background:#0ff; color:#000; font-weight:bold; border:none; padding:0 20px; cursor:pointer;">ACTUALIZAR KERNEL</button>
        </form>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#f0f; text-transform:uppercase; margin-top:0;">[1] Strategic Engine</h4>
            {"".join([f"<div class='strat-box'><b style='color:#0ff;'>{k}</b><br><span style='color:#ccc;'>{v}</span></div>" for k,v in data["strat"].items()])}
        </div>

        <div class="panel" style="padding:0; overflow:hidden;">
            <div id="proto-container"></div>
        </div>

        <div class="panel" id="panel-derecho">
            <h4 style="color:#ffd700; margin-top:0;">[2] Hardware Specifications</h4>
            {"".join([f"<div class='hw-item'><b>{k}</b>: {v}</div>" for k,v in data["hw"].items()])}
            
            <h4 style="color:#f0f; margin-top:20px;">[3] Software Nodes (.py)</h4>
            <div style="max-height:200px; overflow-y:auto; border:1px solid #333; padding:5px; background:#000;">
                {"".join([f"<form method='post' class='nodo-form' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><input type='hidden' name='scroll_pos' class='scroll-input'><button type='submit' class='node-btn {'active-node' if n == target else ''}'>[SRC] {n}</button></form>" for n in sorted(data["sw"].keys())])}
            </div>
            
            <div style="color:#f0f; font-size:10px; margin:10px 0 5px 0;">EDITOR DE CÓDIGO:</div>
            <div class="code-box">{current_code}</div>
        </div>
    </div>

    <script>
        // FIX: Persistencia de Scroll
        const pDer = document.getElementById('panel-derecho');
        window.onload = () => {{ pDer.scrollTop = {scroll_pos}; }};
        document.querySelectorAll('.nodo-form').forEach(f => {{
            f.onsubmit = () => {{ f.querySelector('.scroll-input').value = pDer.scrollTop; }};
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

        // Cuerpo
        const body = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 1, 0.5, 6), new THREE.MeshPhongMaterial({{color: 0x111111, specular: 0x00ffff}}));
        droneGroup.add(body);
        
        // Núcleo
        const core = new THREE.Mesh(new THREE.SphereGeometry(0.25, 16, 16), new THREE.MeshBasicMaterial({{color: 0x00ffff}}));
        core.position.y = 0.4;
        droneGroup.add(core);

        // Brazos y Hélices
        const pos = [{{x:1.8, z:1.8}}, {{x:-1.8, z:1.8}}, {{x:1.8, z:-1.8}}, {{x:-1.8, z:-1.8}}];
        pos.forEach(p => {{
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