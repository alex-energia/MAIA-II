# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request
import os

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
except:
    # Mantener blindaje aunque no existan los archivos externos
    def get_node_library(x): return {"SISTEMA_Vuelo": "// Kernel de Estabilidad Activo", "IA_Escaneo": "// Red Neuronal en espera"}
    def get_hardware_specs(x): return {"CHASIS": "Fibra de Carbono Reforzada", "MOTORES": "Brushless 2400KV", "SENSORES": "LiDAR de barrido 360", "BATERÍA": "LiPo 6S 5000mAh"}
    def get_strategic_analysis(x): return {"OBJETIVO": "Infiltración y Reconocimiento", "RIESGO": "Bajo (Blindaje v1000)"}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    current_code = db.get(target, "// KERNEL MAIA II") if idea and target else "// AGUARDANDO COMANDO..."

    h = f"""
    <html><head><title>MAIA II - KERNEL INTEGRADO</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; gap:10px; padding:10px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .btn-ui {{ background:none; border:1px solid #0ff; color:#0ff; padding:6px 12px; cursor:pointer; font-weight:bold; font-size:10px; }}
        #voice-btn {{ background:#f00; color:#fff; border:none; }}
        
        .grid-master {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:88vh; padding:10px; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,12,12,0.9); padding:10px; overflow-y:auto; border-radius:4px; position:relative; }}
        
        .hw-header {{ display:flex; justify-content:space-between; align-items:center; cursor:pointer; color:#0ff; border-bottom:1px solid #0ff3; padding-bottom:5px; }}
        .hw-item {{ border-left:2px solid #0f0; background:rgba(0,255,0,0.03); padding:8px; margin-bottom:5px; }}
        #proto-container {{ width:100%; height:100%; position:relative; }}
        .code-box {{ background:#000; color:#39ff14; padding:10px; font-size:10px; border-left:2px solid #f0f; white-space:pre-wrap; overflow-y:auto; height:150px; }}
        
        /* Overlay de Telemetría sobre el 3D */
        .telemetry {{ position:absolute; top:10px; right:10px; font-size:9px; color:#ffd700; pointer-events:none; text-align:right; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="letter-spacing:2px;">MAIA II</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' placeholder="Ingresa Comando de Diseño..." style="background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1;" value='{idea}'>
            <button type='submit' style="background:#0ff; color:#000; font-weight:bold; border:none; padding:0 20px; cursor:pointer;">DESPLEGAR SISTEMA</button>
        </form>
        <button class='btn-ui' onclick="window.location.href='/'">LIMPIAR</button>
        <button class='btn-ui' id="voice-btn" onclick="maiaVoice()">VOZ MAIA II: OFF</button>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#f0f; border-bottom:1px solid #f0f3; padding-bottom:5px;">STRATEGIC ENGINE</h4>
            {"".join([f"<div style='margin-bottom:15px;'><b style='color:#0ff; font-size:10px;'>[{k}]</b><p style='color:#ccc; margin:5px 0;'>{v}</p></div>" for k,v in strat_data.items()])}
            <div style="margin-top:20px; border-top:1px solid #222; padding-top:10px; color:#555; font-size:9px;">BLINDAJE DE SEGURIDAD NIVEL 1100 ACTIVO</div>
        </div>

        <div class="panel" style="padding:0; overflow:hidden;">
            <div id="proto-container">
                <div class="telemetry" id="stat-3d">DRONE_STATUS: STANDBY</div>
            </div>
        </div>

        <div class="panel">
            <div class="hw-header" onclick="toggleHW()">
                <h4 style="margin:0;">HARDWARE SPECS</h4>
                <span id="hw-arrow">▼</span>
            </div>
            <div id="hw-section" style="margin-top:10px;">
                {"".join([f"<div class='hw-item'><b style='color:#ffd700; font-size:10px;'>{k}</b><div style='color:#ccc; font-size:9px;'>{v}</div></div>" for k,v in hw_data.items()])}
            </div>
            
            <h4 style="color:#f0f; margin-top:20px; border-bottom:1px solid #f0f3; padding-bottom:5px;">SOFTWARE NODES</h4>
            <div style="max-height:120px; overflow-y:auto; margin-bottom:10px; background:rgba(0,0,0,0.5);">
                {"".join([f"<form method='post' style='margin:0; padding:2px;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:10px; text-align:left; width:100%;'> [▶] {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            <div class="code-box" id="editor">{current_code}</div>
        </div>
    </div>

    <script>
        function toggleHW() {{
            const sec = document.getElementById('hw-section');
            const arr = document.getElementById('hw-arrow');
            sec.style.display = (sec.style.display === 'none') ? 'block' : 'none';
            arr.innerText = (sec.style.display === 'none') ? '▶' : '▼';
        }}

        function maiaVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.style.background = "#0f0"; btn.style.color = "#000"; btn.innerText = "VOZ MAIA II: ON";
            const msg = new SpeechSynthesisUtterance("Alex, sistema MAIA II reconfigurado. Dron industrial listo para inspección de activos.");
            msg.lang = 'es-ES'; window.speechSynthesis.speak(msg);
        }}

        // --- MOTOR 3D MAIA II (DRON COMPLETO) ---
        const container = document.getElementById('proto-container');
        if (container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const props = [];

            // 1. Cuerpo del Dron (Hexagonal con color vivo)
            const body = new THREE.Mesh(
                new THREE.CylinderGeometry(0.8, 1, 0.4, 6),
                new THREE.MeshPhongMaterial({{color: 0x111111, specular: 0x00ffff, shininess: 100}})
            );
            droneGroup.add(body);

            // Núcleo central brillante
            const core = new THREE.Mesh(
                new THREE.SphereGeometry(0.25, 16, 16),
                new THREE.MeshBasicMaterial({{color: 0x00ffff}})
            );
            core.position.y = 0.3;
            droneGroup.add(core);

            // 2. Brazos y Hélices (X4)
            const armPositions = [
                {{x:1.5, z:1.5}}, {{x:-1.5, z:1.5}},
                {{x:1.5, z:-1.5}}, {{x:-1.5, z:-1.5}}
            ];

            armPositions.forEach(pos => {{
                // Brazo (Color Oro Vivo)
                const armGroup = new THREE.Group();
                const arm = new THREE.Mesh(
                    new THREE.BoxGeometry(1.8, 0.15, 0.15),
                    new THREE.MeshPhongMaterial({{color: 0xffd700}})
                );
                const angle = Math.atan2(pos.z, pos.x);
                arm.rotation.y = -angle;
                arm.position.set(pos.x/2, 0, pos.z/2);
                armGroup.add(arm);

                // Motor
                const motor = new THREE.Mesh(
                    new THREE.CylinderGeometry(0.2, 0.2, 0.3, 12),
                    new THREE.MeshPhongMaterial({{color: 0x333333}})
                );
                motor.position.set(pos.x, 0.1, pos.z);
                armGroup.add(motor);

                // Hélice (Cian Neón)
                const prop = new THREE.Group();
                const blade = new THREE.Mesh(
                    new THREE.BoxGeometry(1.4, 0.02, 0.15),
                    new THREE.MeshBasicMaterial({{color: 0x00ffff, transparent: true, opacity: 0.8}})
                );
                const blade2 = blade.clone(); blade2.rotation.y = Math.PI/2;
                prop.add(blade, blade2);
                prop.position.set(pos.x, 0.3, pos.z);
                
                armGroup.add(prop);
                props.push(prop);
                droneGroup.add(armGroup);
            }});

            scene.add(droneGroup);

            // Iluminación
            const pLight = new THREE.PointLight(0x00ffff, 1.5, 50);
            pLight.position.set(5, 5, 5);
            scene.add(pLight);
            scene.add(new THREE.AmbientLight(0xffffff, 0.2));

            camera.position.set(0, 4, 8);
            camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                
                // Levitación y rotación suave
                droneGroup.position.y = Math.sin(Date.now() * 0.002) * 0.2;
                droneGroup.rotation.y += 0.005;
                
                // Hélices a alta velocidad
                props.forEach(p => p.rotation.y += 0.5);

                renderer.render(scene, camera);
                
                // Actualizar Telemetría en pantalla
                document.getElementById('stat-3d').innerText = 
                    "ALTITUD_ESTABLE: OK\\nPROPULSIÓN: " + (Math.random()*100).toFixed(0) + "%\\nRADAR: ACTIVO";
            }}
            animate();
            
            window.addEventListener('resize', () => {{
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            }});
        }}
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
