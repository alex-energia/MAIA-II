
# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request
import os

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
except:
    # BLINDAJE: Inyección de código REAL en los nodos
    def get_node_library(x): 
        return {
            "ESTABILIDAD_VUELO.py": "import time\nimport drone_api\n\ndef stabilize(drone_id):\n    '''Controlador PID para nivelación de chasis'''\n    target_alt = 12.4\n    while True:\n        current_alt = drone_api.get_telemetry(drone_id).alt\n        error = target_alt - current_alt\n        # Ajuste de potencia motores 1-4\n        drone_api.set_throttle(drone_id, power=0.85 + (error * 0.1))\n        time.sleep(0.01)",
            
            "ESCANEO_LIDAR.py": "from maia_vision import LidarScanner\n\ndef run_surface_scan():\n    '''Inicia barrido de Capa 2 para activos industriales'''\n    scanner = LidarScanner(resolution='high', range=200)\n    point_cloud = scanner.capture_3d()\n    # Filtrado de estructuras metálicas\n    assets = point_cloud.filter_by_material('steel')\n    return assets.export_json()",
            
            "SEGURIDAD_AES.py": "import hashlib\nfrom Crypto.Cipher import AES\n\ndef encrypt_comms(data, key):\n    '''Cifrado de grado militar para enlace satelital'''\n    cipher = AES.new(key, AES.MODE_EAX)\n    nonce = cipher.nonce\n    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))\n    return ciphertext, nonce"
        }
    def get_hardware_specs(x): 
        return {"CHASIS": "Fibra de Carbono T800", "LIDAR": "Velodyne v2", "COMMS": "Sat-Link AES-256"}
    def get_strategic_analysis(x): 
        return {"MISION": "Escaneo Activos", "ESTADO": "Operativo"}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    # Recuperar posición de scroll para evitar el salto
    scroll_pos = request.form.get('scroll_pos', '0')
    
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    current_code = db.get(target, "# KERNEL MAIA II\n# SELECCIONE UN NODO .py PARA DESPLEGAR")

    h = f"""
    <html><head><title>MAIA II - KERNEL</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; gap:10px; padding:10px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .grid-master {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:88vh; padding:10px; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,12,12,0.9); padding:10px; overflow-y:auto; border-radius:4px; }}
        #proto-container {{ width:100%; height:100%; }}
        /* Estilo del editor de código real */
        .code-box {{ background:#050505; color:#39ff14; padding:15px; font-size:11px; border:1px solid #f0f4; border-left:3px solid #f0f; white-space:pre; overflow-x:auto; height:250px; font-family:'Courier New', monospace; line-height:1.4; }}
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f03; padding:8px; margin-bottom:4px; cursor:pointer; width:100%; text-align:left; font-size:10px; display:block; text-decoration:none; }}
        .node-btn:hover {{ background:rgba(0,255,0,0.1); border-color:#0f0; }}
        .active-node {{ background:rgba(240,0,255,0.1); border-color:#f0f; color:#fff; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="letter-spacing:2px;">MAIA II</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' style="background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1;" value='{idea}'>
            <button type='submit' style="background:#0ff; color:#000; font-weight:bold; border:none; padding:0 20px;">DESPLEGAR</button>
        </form>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#f0f;">ESTRATEGIA</h4>
            {"".join([f"<div style='margin-bottom:10px;'><b style='color:#0ff;'>{k}</b><p style='color:#ccc;'>{v}</p></div>" for k,v in strat_data.items()])}
        </div>

        <div class="panel" style="padding:0;">
            <div id="proto-container"></div>
        </div>

        <div class="panel" id="right-panel">
            <h4 style="color:#ffd700;">HARDWARE SPECS</h4>
            {"".join([f"<div style='border-left:2px solid #0f0; padding:5px; margin-bottom:5px; font-size:10px;'><b>{k}</b>: {v}</div>" for k,v in hw_data.items()])}
            
            <h4 style="color:#f0f; margin-top:20px;">NODOS DE SOFTWARE (.py)</h4>
            <div style="margin-bottom:10px;">
                {"".join([f"<form method='post' class='node-form' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><input type='hidden' name='scroll_pos' class='scroll-input'><button type='submit' class='node-btn {'active-node' if n == target else ''}'>[FILE] {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            
            <div style="color:#f0f; font-size:10px; margin-bottom:5px;">EDITOR DE KERNEL:</div>
            <div class="code-box">{current_code}</div>
        </div>
    </div>

    <script>
        // SOLUCIÓN AL SALTO: Guardar y restaurar el scroll
        const rightPanel = document.getElementById('right-panel');
        
        // Al cargar la página, restaurar la posición del scroll
        window.onload = function() {{
            rightPanel.scrollTop = {scroll_pos};
        }};

        // Antes de enviar cualquier formulario de nodo, capturar el scroll actual
        document.querySelectorAll('.node-form').forEach(form => {{
            form.onsubmit = function() {{
                const currentScroll = rightPanel.scrollTop;
                form.querySelector('.scroll-input').value = currentScroll;
            }};
        }});

        // --- MODELO 3D (Se mantiene blindado) ---
        const container = document.getElementById('proto-container');
        if (container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);
            
            const droneGroup = new THREE.Group();
            const body = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 1, 0.4, 6), new THREE.MeshPhongMaterial({{color: 0x111111, specular: 0x00ffff}}));
            droneGroup.add(body);
            
            // Brazos Oro
            [1, -1].forEach(x => [1, -1].forEach(z => {{
                const arm = new THREE.Mesh(new THREE.BoxGeometry(2, 0.1, 0.1), new THREE.MeshPhongMaterial({{color: 0xffd700}}));
                arm.position.set(x, 0, z);
                arm.rotation.y = Math.PI/4 * x * z;
                droneGroup.add(arm);
            }}));

            scene.add(droneGroup);
            const light = new THREE.PointLight(0x00ffff, 2, 50);
            light.position.set(2, 2, 2);
            scene.add(light);
            scene.add(new THREE.AmbientLight(0xffffff, 0.3));
            camera.position.set(0, 4, 8);
            camera.lookAt(0,0,0);
            
            function animate() {{
                requestAnimationFrame(animate);
                droneGroup.rotation.y += 0.005;
                renderer.render(scene, camera);
            }}
            animate();
        }}
    </script>
    </body></html>
    """
    return render_template_string(h, scroll_pos=scroll_pos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)