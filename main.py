# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
    from scout_engine import get_market_scout
except:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def get_strategic_analysis(x): return {}
    def get_market_scout(): return []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    show_scout = request.form.get('show_scout') == 'true'
    
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    market_data = get_market_scout()

    h = f"""
    <html><head><title>MAIA II - BLINDAJE TOTAL V15</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:'Segoe UI', monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; align-items:center; gap:12px; padding:12px; background:rgba(0,30,30,0.98); border-bottom:3px solid #0ff; z-index:100; }}
        .main-layout {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:85vh; padding:10px; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,12,12,0.95); padding:12px; overflow-y:auto; border-radius:4px; }}
        
        /* BOTONES BLINDADOS */
        .btn-ui {{ background:none; border:1px solid #0ff; color:#0ff; padding:8px 12px; cursor:pointer; font-weight:bold; font-size:10px; }}
        .btn-scout {{ border-color:#f0f; color:#f0f; }}
        .btn-active {{ background:#0ff; color:#000; }}

        /* BUSCADOR DE ACTIVOS (OVERLAY) */
        #scout-overlay {{ 
            display: {'block' if show_scout else 'none'};
            position: fixed; top: 70px; left: 10px; right: 10px; bottom: 10px;
            background: rgba(0,10,10,0.98); border: 2px solid #f0f; z-index: 500; padding: 20px; overflow-y: auto;
        }}
        .asset-card {{ border:1px solid #0f0; padding:15px; margin-bottom:15px; display:grid; grid-template-columns: 1fr 1fr; gap:20px; background:rgba(0,255,0,0.03); }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.2em; color:#0ff;">MAIA II</b>
        <form method='post' style="margin:0; display:flex; gap:10px; flex-grow:1;">
            <input name='drone_idea' class='btn-ui' style="flex-grow:1; text-align:left;" placeholder='MISIÓN DRON...' value='{idea}'>
            <input type="hidden" name="show_scout" value="{'true' if show_scout else 'false'}">
            <button type='submit' class='btn-active'>DESPLEGAR</button>
        </form>
        <button class='btn-ui btn-scout' onclick="toggleScout()">BUSCADOR DE ACTIVOS</button>
        <button class='btn-ui' onclick="window.location.href='/'">NUEVO PROYECTO</button>
        <button class='btn-ui' id="voice-btn">VOICE: OFF</button>
    </div>

    <div id="scout-overlay">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h2 style="color:#f0f; margin:0;">INTELIGENCIA DE ACTIVOS ENERGÉTICOS GLOBAL</h2>
            <button class="btn-ui" onclick="toggleScout()">[ X ] CERRAR</button>
        </div>
        <hr style="border:1px solid #f0f2; margin:15px 0;">
        {"".join([f'''
        <div class="asset-card">
            <div>
                <h3 style="color:#0f0; margin-top:0;">{a['Nombre']}</h3>
                <p><b>Descripción:</b> {a['Descripcion']}</p>
                <p><b>Estado:</b> <span style="color:#f0f;">{a['Estado']}</span></p>
                <p><b>Ubicación:</b> {a['Ubicacion']}</p>
            </div>
            <div style="border-left:1px solid #0f03; padding-left:20px;">
                <p style="font-size:1.2em;"><b>VALOR:</b> <span style="color:#0ff;">{a['Valor']}</span></p>
                <p><b>Fuente:</b> {a['Fuente']}</p>
                <p style="background:rgba(0,255,255,0.1); padding:10px;">
                    <b>CONTACTO DIRECTO:</b><br>{a['Contacto']}
                </p>
            </div>
        </div>
        ''' for a in market_data])}
    </div>

    <div class='main-layout'>
        <div class="panel">
            <h4 style="color:#f0f; border-bottom:1px solid #f0f3;">INTELIGENCIA ESTRATÉGICA</h4>
            {"".join([f"<div><b style='font-size:0.8em; color:#0ff;'>{k}</b><p style='font-size:0.8em; color:#ccc;'>{v}</p></div>" for k,v in strat_data.items()])}
        </div>

        <div class="panel" style="padding:0; position:relative;">
            <div id="proto-container" style="width:100%; height:100%;"></div>
            <div style="position:absolute; top:10px; left:10px; font-size:9px; color:#0f0;">DRONE_ENGINE: ACTIVE</div>
        </div>

        <div class="panel">
            <h4 style="color:#0ff; margin-top:0;">HARDWARE LAYER</h4>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:4px; font-size:0.7em;">
                {"".join([f"<div style='border:1px solid #f0f2; padding:2px;'>{k}</div>" for k in hw_data.keys()])}
            </div>
            <h4 style="color:#f0f; margin-top:15px;">SOFTWARE RTOS</h4>
            {"".join([f"<form method='post'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:0.8em;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            <div style="background:#000; color:#39ff14; padding:10px; font-size:9px; border-left:2px solid #f0f; margin-top:10px;">{current_code}</div>
        </div>
    </div>

    <script>
        function toggleScout() {{
            const overlay = document.getElementById('scout-overlay');
            overlay.style.display = overlay.style.display === 'none' ? 'block' : 'none';
        }}

        // RENDERIZADO 3D RESTAURADO
        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            const matCarbon = new THREE.MeshStandardMaterial({{color:0x111111, metalness:1, roughness:0.2}});
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.5, 0), matCarbon);
            body.scale.y = 0.4; droneGroup.add(body);

            const props = [];
            [0,1,2,3].forEach(i => {{
                const p = new THREE.Mesh(new THREE.CircleGeometry(0.4, 32), new THREE.MeshBasicMaterial({{color:0x00ff00, transparent:true, opacity:0.3}}));
                p.position.set(i<2?0.6:-0.6, 0.2, i%2?0.6:-0.6); p.rotation.x = Math.PI/2;
                droneGroup.add(p); props.push(p);
            }});

            scene.add(droneGroup);
            scene.add(new THREE.PointLight(0x00ffff, 2, 100));
            camera.position.set(0, 4, 8); camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                props.forEach(p => p.rotation.z += 0.8);
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