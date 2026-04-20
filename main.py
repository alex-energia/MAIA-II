# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

# Importaciones Blindadas
try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
    from scout_engine import get_market_scout, get_countries_list
except Exception as e:
    print(f"ERROR_CORE: {e}")
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def get_strategic_analysis(x): return {}
    def get_market_scout(p): return []
    def get_countries_list(): return []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    show_scout = request.form.get('show_scout') == 'true'
    pais_sel = request.form.get('pais_filtro', 'TODOS')
    
    # Procesamiento de Agentes
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    market_data = get_market_scout(pais_sel)
    paises = get_countries_list()
    
    current_code = db.get(target, "// KERNEL MAIA II ACTIVE") if idea and target else "// AGUARDANDO..."

    h = f"""
    <html><head><title>MAIA II - ECOSISTEMA INTEGRAL BLINDADO</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; font-size:12px; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,15,15,0.9); padding:10px; overflow-y:auto; border-radius:4px; }}
        
        /* CABECERA */
        .header {{ display:flex; align-items:center; gap:10px; padding:10px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .btn-ui {{ background:none; border:1px solid #0ff; color:#0ff; padding:6px 12px; cursor:pointer; font-weight:bold; font-size:10px; }}
        .btn-active {{ background:#0ff; color:#000; border:none; padding:7px 15px; font-weight:bold; cursor:pointer; }}
        .input-idea {{ background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1; }}

        /* LAYOUT */
        .grid-master {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:88vh; padding:10px; }}

        /* SCOUT OVERLAY BLINDADO */
        #scout-overlay {{ 
            display: {'block' if show_scout else 'none'};
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,5,5,0.98); border: 3px solid #f0f; z-index: 2000; padding: 20px; box-sizing:border-box;
        }}
        .asset-card {{ border:1px solid #0f0; background:rgba(0,255,0,0.02); padding:12px; margin-bottom:10px; border-radius:3px; }}

        /* DRON RENDER */
        #proto-container {{ width:100%; height:100%; background:radial-gradient(circle, #001 0%, #000 100%); }}
    </style>
    </head><body>
    
    <div class='header'>
        <b>MAIA II [V16]</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='MISIÓN DRON...' value='{idea}'>
            <button type='submit' class='btn-active'>DESPLEGAR</button>
        </form>
        <form method='post' style="margin:0;">
            <input type="hidden" name="show_scout" value="true">
            <button type="submit" class='btn-ui' style="border-color:#f0f; color:#f0f;">BUSCADOR ACTIVOS</button>
        </form>
        <button class='btn-ui' onclick="window.location.href='/'">NUEVO</button>
    </div>

    <div id="scout-overlay">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #f0f3; padding-bottom:10px;">
            <h2 style="color:#f0f; margin:0;">INTELIGENCIA DE ACTIVOS ENERGÉTICOS</h2>
            <form method="post" style="margin:0;"><button type="submit" class="btn-ui">CERRAR [X]</button></form>
        </div>
        
        <form method="post" style="padding:15px 0; display:flex; gap:10px;">
            <input type="hidden" name="show_scout" value="true">
            <select name="pais_filtro" class="btn-ui" style="background:#000;">
                <option value="TODOS">-- PAÍS --</option>
                {"".join([f'<option value="{p}" {"selected" if pais_sel==p else ""}>{p}</option>' for p in paises])}
            </select>
            <button type="submit" class="btn-active">FILTRAR</button>
            <button type="button" class="btn-ui" onclick="alert('Memoria Sincronizada')">MEMORIA</button>
            <button type="button" class="btn-ui" onclick="window.location.href='/?show_scout=true'">LIMPIAR</button>
        </form>

        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
            {"".join([f'''
            <div class="asset-card">
                <div style="display:flex; justify-content:space-between; border-bottom:1px solid #0f03;">
                    <b style="color:#0f0;">{a['Nombre']}</b>
                    <b style="color:#f0f;">{a['Valor']}</b>
                </div>
                <p style="font-size:11px;">{a['Descripcion']}</p>
                <div style="font-size:10px; color:#0ff;">📍 {a['Ubicacion']} | 🔗 {a['Fuente']}</div>
                <div style="margin-top:8px; padding:5px; background:rgba(0,255,255,0.05); font-size:10px;"><b>CONTACTO:</b> {a['Contacto']}</div>
            </div>
            ''' for a in market_data])}
        </div>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#f0f; border-bottom:1px solid #f0f2;">ESTRATEGIA</h4>
            {"".join([f"<div><b style='color:#0ff;'>{k}</b><p style='color:#ccc; font-size:11px;'>{v}</p></div>" for k,v in strat_data.items()])}
        </div>

        <div class="panel" style="padding:0; position:relative;">
            <div id="proto-container"></div>
            <div style="position:absolute; top:10px; left:10px; color:#0f0; font-size:9px;">RENDER: V16_STABLE</div>
        </div>

        <div class="panel">
            <h4 style="color:#0ff; margin-top:0;">HARDWARE (8 CAPAS)</h4>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:4px;">
                {"".join([f"<div style='border:1px solid #f0f2; padding:3px; font-size:9px;'>{k}</div>" for k in hw_data.keys()])}
            </div>
            <h4 style="color:#f0f; margin-top:10px;">SOFTWARE NODES</h4>
            <div style="max-height:100px; overflow-y:auto; border-bottom:1px solid #f0f2;">
                {"".join([f"<form method='post'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:10px;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            <div style="background:#000; color:#39ff14; padding:10px; font-size:9px; border-left:2px solid #f0f; margin-top:10px; white-space:pre-wrap;">{current_code}</div>
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
            const mat = new THREE.MeshStandardMaterial({{color:0x111111, metalness:1, roughness:0.1}});
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.5, 0), mat);
            body.scale.y = 0.4; droneGroup.add(body);
            [0,1,2,3].forEach(i => {{
                const p = new THREE.Mesh(new THREE.CircleGeometry(0.4, 32), new THREE.MeshBasicMaterial({{color:0x00ff00, transparent:true, opacity:0.3}}));
                p.position.set(i<2?0.6:-0.6, 0.1, i%2?0.6:-0.6); p.rotation.x = Math.PI/2;
                droneGroup.add(p);
            }});
            scene.add(droneGroup); scene.add(new THREE.PointLight(0x00ffff, 2, 100));
            camera.position.set(0, 4, 8); camera.lookAt(0,0,0);
            function animate() {{ requestAnimationFrame(animate); droneGroup.rotation.y += 0.005; renderer.render(scene, camera); }}
            animate();
        }}
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
