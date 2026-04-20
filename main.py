# -*- coding: utf-8 -*-
# main.py - RESTAURACIÓN DE INGENIERÍA MAIA II
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
    
    current_code = db.get(target, "// SISTEMA MAIA II: LISTO") if idea and target else "// AGUARDANDO COMANDO DE INGENIERÍA..."

    h = f"""
    <html><head><title>MAIA II - INGENIERÍA BLINDADA</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Segoe UI', monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; gap:12px; padding:15px; background:rgba(0,40,40,0.98); border-bottom:3px solid #0ff; }}
        .input-idea {{ background:#000; color:#0ff; border:2px solid #0ff; padding:10px; flex-grow:1; outline:none; font-size:1em; }}
        .btn-action {{ background:#0ff; color:#000; border:none; padding:10px 20px; font-weight:bold; cursor:pointer; text-transform:uppercase; }}
        
        .grid-master {{ display:grid; grid-template-columns: 28% 42% 30%; gap:10px; height:85vh; padding:10px; box-sizing:border-box; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,15,15,0.95); padding:12px; overflow-y:auto; border-radius:4px; display:flex; flex-direction:column; }}
        
        .strat-card {{ margin-bottom:12px; border-left:3px solid #f0f; padding-left:10px; background:rgba(255,0,255,0.02); }}
        .code-window {{ background:#000; color:#39ff14; padding:10px; border-left:3px solid #f0f; flex-grow:1; overflow-y:auto; font-size:10px; white-space:pre-wrap; }}
        #proto-container {{ width:100%; height:100%; background:radial-gradient(circle, #001 0%, #000 100%); }}
        .hw-item {{ border:1px solid #0ff3; padding:5px; margin:2px; font-size:9px; background:rgba(0,255,255,0.03); }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.5em; letter-spacing:2px;">MAIA II</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='DESCRIBA LA MISIÓN DEL DRON...' value='{idea}'>
            <button type='submit' class='btn-action'>GENERAR INGENIERÍA</button>
        </form>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#0ff; border-bottom:1px solid #0ff3; margin-top:0;">INTELIGENCIA ESTRATÉGICA</h4>
            {"".join([f"<div class='strat-card'><b style='color:#f0f; font-size:10px;'>{k}</b><p style='color:#ccc; margin:3px 0;'>{v}</p></div>" for k,v in strat_data.items()])}
        </div>

        <div class="panel" style="padding:0; position:relative;">
            <div id="proto-container"></div>
            <div style="position:absolute; bottom:10px; left:10px; color:#0f0; font-size:10px; background:rgba(0,0,0,0.7); padding:5px;">MODELO_V14_CORE</div>
        </div>

        <div class="panel">
            <h4 style="color:#0ff; margin:0 0 10px 0;">HARDWARE (8 CAPAS)</h4>
            <div style="display:grid; grid-template-columns:1fr 1fr; margin-bottom:15px;">
                {"".join([f"<div class='hw-item'>{k}</div>" for k in hw_data.keys()])}
            </div>
            
            <h4 style="color:#f0f; margin:0 0 5px 0;">NODOS DE SOFTWARE</h4>
            <div style="max-height:120px; overflow-y:auto; margin-bottom:10px; border-bottom:1px solid #f0f2;">
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:11px; padding:2px;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            
            <div class='code-window'>{current_code}</div>
        </div>
    </div>

    <script>
        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const mat = new THREE.MeshStandardMaterial({{color:0x151515, metalness:1, roughness:0.2}});
            
            const body = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.2, 0.6), mat);
            droneGroup.add(body);

            [0,1,2,3].forEach(i => {{
                const x = i<2 ? 0.7 : -0.7;
                const z = i%2==0 ? 0.7 : -0.7;
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 0.5), mat);
                arm.position.set(x/2, 0, z/2);
                arm.rotation.z = Math.PI/2; arm.rotation.y = Math.atan2(z, x);
                droneGroup.add(arm);
                
                const prop = new THREE.Mesh(new THREE.TorusGeometry(0.3, 0.02, 16, 100), new THREE.MeshBasicMaterial({{color:0x00ff00, transparent:true, opacity:0.4}}));
                prop.position.set(x, 0.1, z); prop.rotation.x = Math.PI/2;
                droneGroup.add(prop);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.PointLight(0x00ffff, 2, 100));
            camera.position.set(0, 4, 8); camera.lookAt(0,0,0);

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