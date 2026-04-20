# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
    from scout_engine import get_market_scout, get_scout_status # INTEGRACIÓN SCOUT
except:
    def get_market_scout(): return []
    def get_scout_status(): return "OFFLINE"
    # ... (otras funciones de recuperación)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    show_scout = request.form.get('action') == 'scout'
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    market_data = get_market_scout() if show_scout else []

    h = f"""
    <html><head><title>MAIA II - GLOBAL ASSET SCOUT</title>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Segoe UI', sans-serif; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; gap:12px; padding:15px; background:rgba(0,35,35,0.98); border-bottom:3px solid #0ff; box-shadow:0 0 20px #0ff4; }}
        .main-layout {{ display:grid; grid-template-columns: 30% 70%; gap:10px; height:85vh; padding:10px; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,12,12,0.95); padding:15px; overflow-y:auto; }}
        
        /* TARJETAS DE ACTIVOS */
        .asset-card {{ border:1px solid #0f0; background:rgba(0,255,0,0.02); padding:15px; margin-bottom:15px; border-radius:4px; border-left:5px solid #0f0; }}
        .asset-tag {{ background:#0f0; color:#000; padding:2px 6px; font-weight:bold; font-size:9px; border-radius:2px; margin-right:5px; }}
        .asset-price {{ color:#f0f; font-weight:bold; font-size:1.1em; }}
        .asset-source {{ color:#0ff; font-style:italic; font-size:0.8em; margin-top:5px; }}
        
        .btn-proj {{ background:none; color:#f0f; border:1px solid #f0f; padding:10px 15px; cursor:pointer; font-size:10px; font-weight:bold; }}
        .btn-action {{ background:#0ff; color:#000; border:none; padding:10px 20px; font-weight:bold; cursor:pointer; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.4em; letter-spacing:1px;">MAIA II <span style="color:#f0f;">[SCOUT]</span></b>
        <form method='post' style="margin:0; display:flex; gap:10px;">
            <input type='hidden' name='action' value='scout'>
            <button type='submit' class='btn-proj'>BUSCADOR DE PROYECTOS / ACTIVOS</button>
        </form>
        <button type='button' class='btn-proj' style="color:#0f0; border-color:#0f0;" onclick="window.location.href='/'">NUEVO PROYECTO DRON</button>
        <div style="flex-grow:1;"></div>
        <div style="font-size:9px; color:#0f0;">STATUS: {get_scout_status()}</div>
    </div>

    <div class='main-layout'>
        {"".join([f'''
        <div class="panel" style="grid-column: span 2;">
            <h2 style="color:#0f0; border-bottom:1px solid #0f03; padding-bottom:10px;">INTELIGENCIA DE MERCADO GLOBAL (VIGENCIA: 30 DÍAS)</h2>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:15px;">
                {"".join([f'''
                <div class="asset-card">
                    <div style="display:flex; justify-content:space-between; align-items:start;">
                        <div>
                            <span class="asset-tag">{a['Categoria']}</span>
                            <span class="asset-tag" style="background:#f0f; color:#fff;">{a['Estado']}</span>
                            <h3 style="margin:8px 0; color:#fff;">{a['Nombre']}</h3>
                        </div>
                        <div class="asset-price">{a['Valor']}</div>
                    </div>
                    <p style="color:#ccc; font-size:0.9em;">{a['Descripcion']}</p>
                    <div style="margin:10px 0;">
                        <b>📍 UBICACIÓN:</b> {a['Ubicacion']}<br>
                        <b>🔗 FUENTE:</b> <span class="asset-source">{a['Fuente']}</span><br>
                        <b>📅 DETECTADO:</b> {a['Fecha']}
                    </div>
                    <div style="background:rgba(0,255,255,0.05); padding:10px; border:1px dashed #0ff4; font-size:0.85em;">
                        <b style="color:#0ff;">INFO CONTACTO DIRECTO:</b><br>
                        {a['Contacto']}
                    </div>
                </div>
                ''' for a in market_data])}
            </div>
        </div>
        ''' if show_scout else f'''
        <div class="panel">
            <h4 style="color:#0ff;">ESTRATEGIA DRON</h4>
            <div style="font-size:0.8em; color:#ccc;">Seleccione un proyecto o regrese al diseño de dron.</div>
        </div>
        <div class="panel" style="background:#000;">
            <div style="display:flex; align-items:center; justify-content:center; height:100%; color:#0ff1; font-size:5em; font-weight:bold;">MAIA II</div>
        </div>
        '''])}
    </div>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)