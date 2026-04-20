# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance
    from strategic_engine import get_strategic_analysis # NUEVO AGENTE
except:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}
    def get_strategic_analysis(x): return {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    strat_data = get_strategic_analysis(idea) # Llamada al agente estratégico
    
    current_code = db.get(target, "// SISTEMA MAIA V13 ACTIVATED") if idea and target else "// AGUARDANDO..."

    h = f"""
    <html><head><title>MAIA II - ESTRATEGIA Y CONTROL</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:'Segoe UI', sans-serif; margin:0; overflow:hidden; }}
        .header {{ display:flex; align-items:center; gap:15px; padding:15px; background:rgba(0,30,30,0.98); border-bottom:3px solid #0ff; }}
        .flex-main {{ display:flex; gap:10px; height: 85vh; padding:10px; overflow:hidden; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,10,10,0.9); padding:10px; overflow-y:auto; border-radius:3px; }}
        
        /* ESTILOS DE TEXTO PROFESIONAL */
        .strat-card {{ margin-bottom:15px; border-left:3px solid #0ff; padding-left:10px; }}
        .strat-title {{ color:#f0f; font-weight:bold; font-size:0.9em; text-transform:uppercase; margin-bottom:5px; }}
        .strat-desc {{ color:#ccc; font-size:0.85em; line-height:1.4; text-align:justify; }}
        
        .input-idea {{ background:#000; color:#0ff; border:2px solid #0ff; padding:10px; flex-grow:1; outline:none; }}
        .btn-gen {{ background:#0ff; color:#000; border:none; padding:10px 20px; font-weight:bold; cursor:pointer; }}
        #proto-container {{ width:100%; height:350px; background:#000; border:1px solid #0f03; }}
        
        #chat-maia {{ position:fixed; bottom:10px; right:10px; width:300px; height:35px; background:rgba(0,25,25,0.98); border:1px solid #0ff; transition:0.4s; z-index:999; overflow:hidden; }}
        #chat-maia.open {{ height:400px; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b>MAIA II [CORE]</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='DEFINA MISIÓN...' value='{idea}'>
            <button type='submit' class='btn-gen'>ANALIZAR ECOSISTEMA</button>
        </form>
        <button type='button' style="background:none; color:#f0f; border:1px solid #f0f; padding:8px;" onclick="window.location.href='/'">LIMPIAR</button>
    </div>

    <div class='flex-main'>
        <div style="width:30%;" class="panel">
            <h4 style="color:#0ff; border-bottom:1px solid #0ff3; padding-bottom:5px;">INTELIGENCIA ESTRATÉGICA</h4>
            {"".join([f"<div class='strat-card'><div class='strat-title'>{k}</div><div class='strat-desc'>{v}</div></div>" for k,v in strat_data.items()])}
        </div>

        <div style="width:40%; display:flex; flex-direction:column; gap:10px;">
            <div class="panel" style="flex-grow:1; padding:0;">
                <div id="proto-container"></div>
            </div>
            <div class="panel" style="height:35%;">
                <h4 style="color:#0ff; margin-top:0;">LAYER DE HARDWARE</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:5px;">
                    {"".join([f"<div style='font-size:0.7em; border:1px solid #f0f2; padding:3px;'><b>{k}</b></div>" for k in hw_data.keys()])}
                </div>
            </div>
        </div>

        <div style="width:30%;" class="panel">
            <h4 style="color:#f0f;">ENGINE NODES</h4>
            <div style="background:#000; color:#39ff14; padding:10px; font-size:10px; height:80%; overflow-y:auto; border-left:2px solid #f0f;">{current_code}</div>
        </div>
    </div>

    <script>
        // MOTOR 3D BLINDADO V13
        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matCarbon = new THREE.MeshStandardMaterial({{color:0x111111, metalness:1, roughness:0.1}});
            const body = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.2, 0.8), matCarbon);
            droneGroup.add(body);

            const props = [];
            [[0.5, 0.5], [-0.5, 0.5], [0.5, -0.5], [-0.5, -0.5]].forEach(pos => {{
                const p = new THREE.Mesh(new THREE.CircleGeometry(0.4, 32), new THREE.MeshBasicMaterial({{color:0x00ff00, transparent:true, opacity:0.3}}));
                p.position.set(pos[0], 0.2, pos[1]); p.rotation.x = Math.PI/2;
                droneGroup.add(p); props.push(p);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.PointLight(0x00ffff, 2, 100));
            camera.position.set(0, 3, 6); camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach(p => p.rotation.z += 0.5);
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
