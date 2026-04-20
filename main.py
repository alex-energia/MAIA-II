# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request

# CARGA DE MOTORES BLINDADA
try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance, get_hardware_integrity_hash
    from model3d_engine import get_3d_model_data, get_3d_integrity_hash
except Exception as e:
    print(f"ERROR DE CARGA: {e}")
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}
    def get_3d_model_data(x): return {}
    def get_hardware_integrity_hash(): return "RECOVERY"
    def get_3d_integrity_hash(): return "RECOVERY"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    # Procesamiento de Motores
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    m3d_data = get_3d_model_data(idea)
    
    current_code = db.get(target, "// SISTEMA OPERATIVO MAIA") if idea and target else "// AGUARDANDO MISIÓN..."

    h = f"""
    <html><head><title>MAIA II - PROTO PROTOTYPE V vuelo</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body{{background:#000505; color:#0ff; font-family:'Courier New', monospace; padding:20px; margin:0; overflow-x:hidden;}}
        .panel{{border:1px solid #0ff; padding:15px; background:rgba(0,10,10,0.9); margin-bottom:15px; border-radius:2px;}}
        .flex{{display:flex; gap:15px;}} .col-25{{width:25%;}} .col-75{{width:75%;}}
        .code-window{{background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:400px; overflow-y:scroll; white-space:pre-wrap; font-size:11px;}}
        .btn-gen{{background:#0ff; color:#000; padding:15px; font-weight:bold; border:none; cursor:pointer; width:100%; text-transform:uppercase;}}
        .btn-util{{background:none; border:1px solid #f0f; color:#f0f; padding:8px; cursor:pointer; margin-top:5px; font-weight:bold;}}
        .calc-bar{{background:#0ff; color:#000; padding:10px; display:flex; justify-content:space-around; font-weight:bold; margin-bottom:10px;}}
        .grid-eng{{display:grid; grid-template-columns: 1fr 1fr; gap:15px;}}
        .hw-card, .m3d-card{{border:1px solid #f0f; padding:10px; background:rgba(255,0,255,0.03); font-size:0.75em;}}
        .hw-card h4, .m3d-card h4{{color:#f0f; margin:0 0 5px 0; border-bottom:1px solid #f0f;}}
        
        /* Contenedor del Prototipo 3D */
        #proto-container{{
            width:100%; height:500px; border:2px solid #0f0; background:#000; position:relative; overflow:hidden;
            box-shadow: 0 0 20px rgba(0,255,0,0.2);
        }}
        #proto-label{{
            position:absolute; top:10px; left:10px; color:#0f0; font-weight:bold; background:rgba(0,0,0,0.8); padding:5px; border:1px solid #0f0; z-index:10;
        }}
    </style>
    </head><body>
    
    <div style='float:right; font-size:0.7em; color:rgba(0,255,255,0.5);'>HW:{get_hardware_integrity_hash()} | 3D:{get_3d_integrity_hash()}</div>
    <h1>MAIA II <span style='color:#f0f;'>[ PROTOTIPO VISUAL OPERATIVO ]</span></h1>

    <div class='panel'>
        <form method='post' id='main-form'>
            <div style='display:flex; gap:10px;'>
                <input name='drone_idea' placeholder='DEFINA LA MISIÓN DEL PROTOCOLO...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:15px; flex-grow:1; font-size:1.1em;'>
                <button type='submit' class='btn-gen' style='width:auto;'>GENERAR ECOSISTEMA INTEGRAL</button>
            </div>
            <div style='display:flex; gap:10px;'>
                <button type='button' class='btn-util' onclick="window.location.href='/'">LIMPIAR MEMORIA</button>
                <button type='button' class='btn-util' style='background:#f0f; color:#000; border:none;' onclick="window.speechSynthesis.speak(new SpeechSynthesisUtterance('Alex, prototipo visual en línea. Sistema de vuelo normal activado.'))">VOZ MAIA</button>
            </div>
        </form>
    </div>

    <div class='flex'>
        <div class='col-25'>
            <div class='panel' style='height:400px; overflow-y:auto;'>
                <h3 style='color:#f0f;'>NODOS SOFTWARE</h3>
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em; text-align:left; width:100%; padding:4px;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
        </div>
        <div class='col-75'>
            <div class='panel'>
                <h3>EDITOR DE NODO: {target}</h3>
                <div class='code-window'>{current_code}</div>
            </div>
        </div>
    </div>

    <div class='calc-bar'>
        <span>MASA: {calc.get('Peso Total','-')}</span> <span>THRUST: {calc.get('Empuje Máx','-')}</span>
        <span>TWR: {calc.get('Ratio TWR','-')}</span> <span>AIR TIME: {calc.get('Autonomía','-')}</span>
    </div>

    <div class='grid-eng'>
        <div class='panel'>
            <h2 style='color:#f0f;'>HARDWARE BRUTAL (8 CAPAS)</h2>
            <div style='display:grid; grid-template-columns: 1fr 1fr; gap:5px;'>
                {"".join([f"<div class='hw-card'><h4>{k}</h4><ul style='padding-left:15px;'>"+"".join([f"<li>{i}</li>" for i in v])+"</ul></div>" for k,v in hw_data.items()])}
            </div>
        </div>
        
        <div class='panel'>
            <h2 style='color:#0f0;'>ESPECIFICACIONES DEL MODELO 3D</h2>
            {"<p style='text-align:center; padding:40px;'>AGUARDANDO GENERACIÓN DE IDEA...</p>" if not m3d_data else f'''
                <div class='m3d-card'><h4>GEOMETRÍA BASE</h4><p>Config: {m3d_data['CONFIGURACIÓN_GEOMÉTRICA']['Tipo']}</p><p>Material: {m3d_data['CONFIGURACIÓN_GEOMÉTRICA']['Material_Base']}</p></div>
                <div class='m3d-card' style='margin-top:5px;'><h4>ESTADO OPERATIVO</h4><p>Modo: {m3d_data['ESTADO_OPERATIVO']['Modo']}</p><p>RPM: {m3d_data['ESTADO_OPERATIVO']['RPM_Hélices']}</p></div>
                <div class='m3d-card' style='margin-top:5px;'><h4>TECNOLOGÍA DE RENDER</h4><p>Shader: {m3d_data['DATOS_TECNICOS_RENDER']['Shader']}</p></div>
            '''}
        </div>
    </div>

    <div class='panel' style='border-color:#0f0;'>
        <h2 style='color:#0f0; margin-top:0;'>PROTOTIPO VISUAL OPERATIVO (BRAZOS Y HÉLICES)</h2>
        <div id="proto-container">
            <div id="proto-label">ESTADO: VUELO NORMAL (RTOS NODO 01)</div>
        </div>
    </div>

    <script>
        // Variables globales del prototipo
        let scene, camera, renderer, droneBody;
        let propellers = []; // Array para guardar las hélices y animarlas
        const container = document.getElementById('proto-container');

        // Solo iniciar si hay una idea generada
        if ('{idea}' !== '') {{
            init3D();
            animate3D();
        }} else {{
            container.innerHTML = '<div style="color:#555; text-align:center; padding-top:200px;">ESPERANDO IDEA PARA CONSTRUIR PROTOTIPO FÍSICO...</div>';
        }}

        function init3D() {{
            // 1. Escena y Cámara
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
            camera.position.set(0, 1.5, 3);
            camera.lookAt(0, 0, 0);

            // 2. Renderizador Blindado
            renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(container.clientWidth, container.clientHeight);
            renderer.setClearColor(0x000000, 1); // Fondo negro puro
            container.appendChild(renderer.domElement);

            // 3. Iluminación Táctica
            const ambientLight = new THREE.AmbientLight(0x404040, 2);
            scene.add(ambientLight);
            const directionalLight = new THREE.DirectionalLight(0xffffff, 1.5);
            directionalLight.position.set(1, 1, 1);
            scene.add(directionalLight);
            const spotLight = new THREE.SpotLight(0x00ff00, 1); // Luz verde neón de acento
            spotLight.position.set(0, 3, 0);
            scene.add(spotLight);

            // 4. CONSTRUCCIÓN DEL DRON (Basado en Hardware/Software)
            droneBody = new THREE.Group();
            
            // Materiales GLI-5
            const bodyColor = '{m3d_data.get('CONFIGURACIÓN_GEOMÉTRICA', {}).get('Color_Principal', '#222222')}';
            const matBody = new THREE.MeshStandardMaterial({{ color: bodyColor, metalness: 0.9, roughness: 0.2 }});
            const matArms = new THREE.MeshStandardMaterial({{ color: 0x333333, metalness: 1, roughness: 0.1 }});
            const matProps = new THREE.MeshStandardMaterial({{ color: 0x00ff00, transparent: true, opacity: 0.8 }}); // Hélices verdes neón

            // 4a. Cuerpo Central (Ciber-Físico)
            const geoBody = new THREE.BoxGeometry(0.5, 0.15, 0.5);
            const bodyMesh = new THREE.Mesh(geoBody, matBody);
            droneBody.add(bodyMesh);

            // 4b. Brazos (Configuración en X)
            const armLength = 1.0;
            const geoArm = new THREE.CylinderGeometry(0.03, 0.03, armLength);
            geoArm.rotateZ(Math.PI / 2); // Orientar horizontalmente

            const armPositions = [
                {{ pos: [armLength/2, 0, armLength/2], rot: Math.PI / 4 }}, // Front-Right
                {{ pos: [-armLength/2, 0, armLength/2], rot: -Math.PI / 4 }}, // Front-Left
                {{ pos: [armLength/2, 0, -armLength/2], rot: -Math.PI / 4 }}, // Back-Right
                {{ pos: [-armLength/2, 0, -armLength/2], rot: Math.PI / 4 }}  // Back-Left
            ];

            armPositions.forEach(config => {{
                const armGroup = new THREE.Group();
                const armMesh = new THREE.Mesh(geoArm, matArms);
                armMesh.position.set(0, 0, 0);
                armGroup.add(armMesh);
                armGroup.rotation.y = config.rot;
                armGroup.position.set(config.pos[0]/2, 0, config.pos[2]/2);
                droneBody.add(armGroup);

                // 4c. Motores GaN y Hélices (Al final de cada brazo)
                const geoProp = new THREE.BoxGeometry(0.4, 0.01, 0.04); // Hélice simple
                const propMesh = new THREE.Mesh(geoProp, matProps);
                
                // Posicionar hélice al final del brazo
                const propPosFactor = 0.9; // Ajuste fino de posición
                propMesh.position.set(config.pos[0]*propPosFactor, 0.1, config.pos[2]*propPosFactor);
                
                scene.add(propMesh); // Añadir a la escena para rotación independiente
                propellers.push(propMesh); // Guardar para animar
            }});

            scene.add(droneBody);

            // Resiliencia: Ajustar render si cambia la ventana
            window.addEventListener('resize', onWindowResize, false);
        }

        function onWindowResize() {{
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        }}

        function animate3D() {{
            requestAnimationFrame(animate3D);

            // Animación del dron (Vuelo Estacionario - sutil balanceo)
            const time = Date.now() * 0.001;
            droneBody.position.y = Math.sin(time) * 0.05; // Balanceo vertical
            droneBody.rotation.z = Math.sin(time * 0.5) * 0.02; // Balanceo lateral

            // ANIMACIÓN DE HÉLICES (Vuelo Normal)
            const propSpeed = {m3d_data.get('ESTADO_OPERATIVO', {}).get('RPM_Hélices', 4000)} * 0.0001;
            propellers.forEach((prop, index) => {{
                // Hélices opuestas giran en sentidos opuestos (Lógica de Torque)
                if (index === 0 || index === 3) {{
                    prop.rotation.y += propSpeed;
                }} else {{
                    prop.rotation.y -= propSpeed;
                }}
                
                // Sincronizar posición de hélice con el balanceo del cuerpo
                prop.position.y = droneBody.position.y + 0.1;
                // Ajuste sutil de rotación z para seguir el balanceo
                prop.rotation.z = droneBody.rotation.z;
            }});

            renderer.render(scene, camera);
        }
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)