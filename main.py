# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
    from scout_engine import get_market_scout, get_countries_list
except Exception as e:
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
    pais_seleccionado = request.form.get('pais_filtro', 'TODOS')
    
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    market_data = get_market_scout(pais_seleccionado)
    paises = get_countries_list()

    h = f"""
    <html><head><title>MAIA II - BLINDAJE ESTRATÉGICO</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Segoe UI', monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; gap:12px; padding:12px; background:rgba(0,30,30,0.98); border-bottom:3px solid #0ff; z-index:100; }}
        .main-layout {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:85vh; padding:10px; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,12,12,0.95); padding:12px; overflow-y:auto; border-radius:4px; }}
        
        /* BOTONES */
        .btn-ui {{ background:none; border:1px solid #0ff; color:#0ff; padding:8px 12px; cursor:pointer; font-weight:bold; font-size:10px; text-transform:uppercase; }}
        .btn-active {{ background:#0ff; color:#000; border:none; padding:8px 15px; font-weight:bold; cursor:pointer; }}
        .btn-scout {{ border-color:#f0f; color:#f0f; }}
        
        /* SCOUT OVERLAY */
        #scout-overlay {{ 
            display: {'block' if show_scout else 'none'};
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,8,8,0.98); border: 2px solid #f0f; z-index: 1000; padding: 25px; box-sizing: border-box;
        }}
        .scout-controls {{ display:flex; gap:10px; margin-bottom:20px; background:rgba(255,0,255,0.05); padding:15px; border-radius:4px; border:1px solid #f0f3; }}
        .asset-grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:15px; }}
        .asset-card {{ border:1px solid #0f0; background:rgba(0,255,0,0.02); padding:15px; border-radius:4px; }}
        
        select.btn-ui {{ background:#000; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.2em; color:#0ff;">MAIA II</b>
        <form method='post' style="margin:0; display:flex; gap:10px; flex-grow:1;">
            <input name='drone_idea' class='btn-ui' style="flex-grow:1; text-align:left;" placeholder='DEFINIR MISIÓN...' value='{idea}'>
            <button type='submit' class='btn-active'>DESPLEGAR CORE</button>
        </form>
        <form method='post' style="margin:0;">
            <input type="hidden" name="show_scout" value="true">
            <button type="submit" class='btn-ui btn-scout'>BUSCADOR DE ACTIVOS</button>
        </form>
        <button class='btn-ui' onclick="window.location.href='/'">NUEVO PROYECTO</button>
    </div>

    <div id="scout-overlay">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
            <h2 style="color:#f0f; margin:0;">GLOBAL ASSET INTEL - VIGENCIA 30 DÍAS</h2>
            <form method="post" style="margin:0;"><button type="submit" class="btn-ui" style="border-color:#f66; color:#f66;">CERRAR BUSCADOR [X]</button></form>
        </div>

        <div class="scout-controls">
            <form method="post" style="display:flex; gap:10px; margin:0; flex-grow:1;">
                <input type="hidden" name="show_scout" value="true">
                <input type="hidden" name="drone_idea" value="{idea}">
                
                <select name="pais_filtro" class="btn-ui" style="width:200px;">
                    <option value="TODOS">-- SELECCIONAR PAÍS --</option>
                    {"".join([f'<option value="{p}" {"selected" if pais_seleccionado==p else ""}>{p}</option>' for p in paises])}
                </select>
                
                <button type="submit" class="btn-active">FILTRAR PAÍS</button>
                <button type="button" class="btn-ui" style="border-color:#0f0; color:#0f0;" onclick="alert('Memoria de activos sincronizada con el servidor central')">MEMORIA</button>
                <button type="button" class="btn-ui" onclick="window.location.href='/?show_scout=true'">LIMPIAR FILTROS</button>
            </form>
        </div>

        <div class="asset-grid">
            {"".join([f'''
            <div class="asset-card">
                <div style="display:flex; justify-content:space-between;">
                    <b style="color:#0f0; font-size:1.1em;">{a['Nombre']}</b>
                    <span style="color:#f0f; font-weight:bold;">{a['Valor']}</span>
                </div>
                <p style="color:#ccc;">{a['Descripcion']}</p>
                <div style="font-size:0.9em; border-top:1px solid #0f02; padding-top:10px; display:grid; grid-template-columns: 1fr 1fr;">
                    <div>
                        <b>📍 PAÍS:</b> {a['Ubicacion']}<br>
                        <b>🔗 FUENTE:</b> {a['Fuente']}
                    </div>
                    <div style="background:rgba(0,255,255,0.05); padding:5px; border-radius:2px;">
                        <b style="color:#0ff;">CONTACTO:</b><br>{a['Contacto']}
                    </div>
                </div>
            </div>
            ''' for a in market_data])}
        </div>
    </div>

    <div class='main-layout'>
        <div class="panel">
            <h4 style="color:#f0f;">ESTRATEGIA</h4>
            {"".join([f"<div><b style='font-size:0.8em; color:#0ff;'>{k}</b><p style='font-size:0.8em; color:#ccc;'>{v}</p></div>" for k,v in strat_data.items()])}
        </div>
        <div class="panel" style="padding:0;"><div id="proto-container" style="width:100%; height:100%;"></div></div>
        <div class="panel">
            <h4 style="color:#0ff; margin-top:0;">HARDWARE LAYER</h4>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:4px; font-size:0.7em;">
                {"".join([f"<div style='border:1px solid #f0f2; padding:2px;'>{k}</div>" for k in hw_data.keys()])}
            </div>
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
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.5, 0), new THREE.MeshStandardMaterial({{color:0x111111}}));
            body.scale.y = 0.4; droneGroup.add(body);
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