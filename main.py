# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = os.urandom(2048)

# --- MÓDULOS BLINDADOS (SOFTWARE / HARDWARE / STRATEGY) ---
class MaiaCore:
    def get_strategic_status(self):
        return {"status": "Escaneando Activos", "nivel": 1200, "blindaje": "Máximo"}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'history' not in session: session['history'] = []
    view = request.form.get('view_state', 'model_3d')
    
    # Lógica de persistencia de módulos estratégicos
    core = MaiaCore()
    strategy = core.get_strategic_status()

    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>MAIA II - DRONE INTERFACE</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>
            :root { --cian: #00ffff; --gold: #ffd700; --bg: #050505; }
            body { margin: 0; background: var(--bg); color: #fff; font-family: monospace; overflow: hidden; }
            
            /* UI Overlay */
            #ui-layer { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10; }
            .panel { position: absolute; padding: 20px; background: rgba(0,0,0,0.7); border: 1px solid #222; pointer-events: auto; }
            .top-left { top: 20px; left: 20px; border-left: 4px solid var(--cian); }
            .bottom-right { bottom: 20px; right: 20px; border-right: 4px solid var(--gold); text-align: right; }
            
            .nav-btn { background: none; border: 1px solid var(--cian); color: var(--cian); padding: 10px; cursor: pointer; margin-top: 10px; font-weight: bold; }
            .nav-btn:hover { background: var(--cian); color: #000; }

            /* Contenedor 3D */
            #canvas-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }
        </style>
    </head>
    <body>

    <div id="ui-layer">
        <div class="panel top-left">
            <h2 style="color:var(--cian); margin:0;">MAIA II - CORE</h2>
            <div style="font-size:10px; margin-top:5px;">SISTEMA: V.1200 / DRONE MODEL</div>
            <div style="margin-top:15px;">
                <b>ESTADO:</b> <span style="color:var(--gold);">""" + strategy['status'] + """</span><br>
                <b>STRATEGY:</b> BLINDADO<br>
                <b>HARDWARE:</b> ACTIVO
            </div>
            <form method="POST">
                <button type="submit" name="view_state" value="scout" class="nav-btn">BARRIDO DE ACTIVOS</button>
            </form>
        </div>

        <div class="panel bottom-right">
            <div style="color:var(--cian);">TELEMETRÍA 3D</div>
            <div id="coords">X: 0.00 Y: 0.00 Z: 0.00</div>
            <div style="margin-top:10px; font-size:9px; color:#555;">BRAZOS Y HÉLICES: SINCRONIZADOS</div>
        </div>
    </div>

    <div id="canvas-container"></div>

    <script>
        let scene, camera, renderer, drone, props = [];

        function init() {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 8;
            camera.position.y = 3;

            renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('canvas-container').appendChild(renderer.domElement);

            // Luces
            const light = new THREE.PointLight(0x00ffff, 1, 100);
            light.position.set(10, 10, 10);
            scene.add(light);
            scene.add(new THREE.AmbientLight(0x404040, 2));

            // --- CONSTRUCCIÓN DEL DRON MAIA II ---
            drone = new THREE.Group();

            // 1. Cuerpo Central (Hexágono)
            const bodyGeo = new THREE.CylinderGeometry(1.2, 1.5, 0.6, 6);
            const bodyMat = new THREE.MeshPhongMaterial({ color: 0x111111, specular: 0x00ffff, shininess: 100 });
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            drone.add(body);

            // Detalle de color vivo en el centro
            const coreGeo = new THREE.SphereGeometry(0.4, 32, 32);
            const coreMat = new THREE.MeshBasicMaterial({ color: 0x00ffff });
            const core = new THREE.Mesh(coreGeo, coreMat);
            core.position.y = 0.4;
            drone.add(core);

            // 2. Brazos y Hélices (X4)
            const armColor = 0xffd700; // Oro
            const propColor = 0x00ffff; // Cian
            const positions = [
                { x: 2, z: 2 }, { x: -2, z: 2 },
                { x: 2, z: -2 }, { x: -2, z: -2 }
            ];

            positions.forEach((pos, index) => {
                // Brazo
                const armGeo = new THREE.BoxGeometry(2.5, 0.2, 0.2);
                const armMat = new THREE.MeshPhongMaterial({ color: armColor });
                const arm = new THREE.Mesh(armGeo, armMat);
                
                // Rotar brazo hacia la esquina
                const angle = Math.atan2(pos.z, pos.x);
                arm.rotation.y = -angle;
                arm.position.set(pos.x / 2, 0, pos.z / 2);
                drone.add(arm);

                // Motor (al final del brazo)
                const motorGeo = new THREE.CylinderGeometry(0.3, 0.3, 0.4, 16);
                const motorMat = new THREE.MeshPhongMaterial({ color: 0x333333 });
                const motor = new THREE.Mesh(motorGeo, motorMat);
                motor.position.set(pos.x, 0.2, pos.z);
                drone.add(motor);

                // Hélice
                const propGroup = new THREE.Group();
                const bladeGeo = new THREE.BoxGeometry(1.8, 0.05, 0.2);
                const bladeMat = new THREE.MeshBasicMaterial({ color: propColor, transparent: true, opacity: 0.8 });
                const blade1 = new THREE.Mesh(bladeGeo, bladeMat);
                const blade2 = blade1.clone();
                blade2.rotation.y = Math.PI / 2;
                
                propGroup.add(blade1);
                propGroup.add(blade2);
                propGroup.position.set(pos.x, 0.5, pos.z);
                
                drone.add(propGroup);
                props.push(propGroup); // Guardar para animar
            });

            scene.add(drone);

            // Grid de fondo
            const grid = new THREE.GridHelper(20, 20, 0x00ffff, 0x111111);
            grid.position.y = -2;
            scene.add(grid);

            animate();
        }

        function animate() {
            requestAnimationFrame(animate);

            // Movimiento suave del dron (levitación)
            drone.position.y = Math.sin(Date.now() * 0.002) * 0.2;
            drone.rotation.y += 0.005; // Rotación lenta del modelo completo
            drone.rotation.x = Math.sin(Date.now() * 0.001) * 0.05;

            // Rotación de hélices (Velocidad alta)
            props.forEach(p => {
                p.rotation.y += 0.4;
            });

            // Actualizar Telemetría
            document.getElementById('coords').innerText = 
                `X: ${drone.position.x.toFixed(2)} Y: ${drone.position.y.toFixed(2)} Z: ${drone.rotation.y.toFixed(2)}`;

            renderer.render(scene, camera);
        }

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        init();
    </script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
