# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
except:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def get_strategic_analysis(x): return {}

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
    <html><head><title>MAIA II - KERNEL</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; gap:10px; padding:10px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .btn-ui {{ background:none; border:1px solid #0ff; color:#0ff; padding:6px 12px; cursor:pointer; font-weight:bold; font-size:10px; }}
        #voice-btn {{ background:#f00; color:#fff; border:none; }}
        
        .grid-master {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:88vh; padding:10px; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,12,12,0.9); padding:10px; overflow-y:auto; border-radius:4px; }}
        
        .hw-header {{ display:flex; justify-content:space-between; align-items:center; cursor:pointer; color:#0ff; border-bottom:1px solid #0ff3; padding-bottom:5px; }}
        .hw-item {{ border-left:2px solid #0f0; background:rgba(0,255,0,0.03); padding:8px; margin-bottom:5px; }}
        #proto-container {{ width:100%; height:100%; }}
        .code-box {{ background:#000; color:#39ff14; padding:10px; font-size:10px; border-left:2px solid #f0f; white-space:pre-wrap; overflow-y:auto; height:150px; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b>MAIA II</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' style="background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1;" value='{idea}'>
            <button type='submit' style="background:#0ff; color:#000; font-weight:bold; border:none; padding:0 20px;">DESPLEGAR</button>
        </form>
        <button class='btn-ui' onclick="window.location.href='/'">LIMPIAR</button>
        <button class='btn-ui' onclick="alert('Memoria Sincronizada')">MEMORIA</button>
        <button class='btn-ui' id="voice-btn" onclick="maiaVoice()">VOZ MAIA II: OFF</button>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#f0f;">ESTRATEGIA</h4>
            {"".join([f"<div style='margin-bottom:10px;'><b style='color:#0ff;'>{k}</b><p style='color:#ccc;'>{v}</p></div>" for k,v in strat_data.items()])}
        </div>

        <div class="panel" style="padding:0;">
            <div id="proto-container"></div>
        </div>

        <div class="panel">
            <div class="hw-header" onclick="toggleHW()">
                <h4 style="margin:0;">HARDWARE (8 CATEGORÍAS)</h4>
                <span id="hw-arrow">▼</span>
            </div>
            <div id="hw-section">
                {"".join([f"<div class='hw-item'><b style='color:#0f0; font-size:10px;'>{k}</b><div style='color:#ccc; font-size:9px;'>{v}</div></div>" for k,v in hw_data.items()])}
            </div>
            
            <h4 style="color:#f0f; margin-top:15px;">NODOS SOFTWARE</h4>
            <div style="max-height:80px; overflow-y:auto; border-bottom:1px solid #f0f2; margin-bottom:10px;">
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:10px;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            <div class="code-box">{current_code}</div>
        </div>
    </div>

    <script>
        function toggleHW() {{
            const sec = document.getElementById('hw-section');
            const arr = document.getElementById('hw-arrow');
            if(sec.style.display === 'none') {{
                sec.style.display = 'block';
                arr.innerText = '▼';
            }} else {{
                sec.style.display = 'none';
                arr.innerText = '▶';
            }}
        }}

        function maiaVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.style.background = "#0f0";
            btn.style.color = "#000";
            btn.innerText = "VOZ MAIA II: ON";
            const msg = new SpeechSynthesisUtterance("Bienvenido Alex. Sistema MAIA II activo y blindado. Ingeniería lista para tu comando.");
            msg.lang = 'es-ES';
            window.speechSynthesis.speak(msg);
        }}

        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);
            const droneGroup = new THREE.Group();
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(1, 0), new THREE.MeshStandardMaterial({{color: 0x111111, metalness: 1, roughness: 0.2}}));
            body.scale.set(1, 0.5, 1);
            droneGroup.add(body);
            const core = new THREE.Mesh(new THREE.SphereGeometry(0.15, 16, 16), new THREE.MeshBasicMaterial({{color: 0x00ffff}}));
            droneGroup.add(core);
            scene.add(droneGroup);
            const light = new THREE.PointLight(0x00ffff, 2, 50);
            light.position.set(2, 2, 2);
            scene.add(light);
            scene.add(new THREE.AmbientLight(0xffffff, 0.3));
            camera.position.set(0, 3, 6);
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
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)