# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request

# CARGA DE MOTORES (SOFTWARE, HARDWARE, 3D)
try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance, get_hardware_integrity_hash
    from model3d_engine import get_3d_model_data, get_3d_integrity_hash
except Exception as e:
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
    
    # Procesamiento
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    m3d_data = get_3d_model_data(idea)
    
    current_code = db.get(target, "// SISTEMA OPERATIVO") if idea and target else "// AGUARDANDO MISIÓN..."

    h = f"""
    <html><head><title>MAIA II - CONTROL TOTAL</title>
    <style>
        body{{background:#000808; color:#0ff; font-family:monospace; padding:20px;}}
        .panel{{border:1px solid #0ff; padding:15px; background:rgba(0,15,15,0.9); margin-bottom:15px;}}
        .flex{{display:flex; gap:15px;}} .col-25{{width:25%;}} .col-75{{width:75%;}}
        .code-window{{background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:400px; overflow-y:scroll; white-space:pre-wrap; font-size:11px;}}
        .btn-gen{{background:#0ff; color:#000; padding:12px; font-weight:bold; border:none; cursor:pointer; width:100%;}}
        .btn-util{{background:none; border:1px solid #f0f; color:#f0f; padding:8px; cursor:pointer; margin-top:5px; font-weight:bold;}}
        .calc-bar{{background:#0ff; color:#000; padding:10px; display:flex; justify-content:space-around; font-weight:bold; margin-bottom:10px;}}
        .grid-main{{display:grid; grid-template-columns: 1fr 1fr; gap:15px;}}
        .hw-card{{border:1px solid #f0f; padding:10px; background:rgba(255,0,255,0.05); font-size:0.75em;}}
        .m3d-card{{border:1px solid #0f0; padding:10px; background:rgba(0,255,0,0.05); font-size:0.75em;}}
    </style>
    </head><body>
    
    <div style='float:right; font-size:0.7em; color:#f0f;'>HW:{get_hardware_integrity_hash()} | 3D:{get_3d_integrity_hash()}</div>
    <h1>MAIA II [ INTEGRATED SYSTEM ]</h1>

    <div class='panel'>
        <form method='post'>
            <div style='display:flex; gap:10px;'>
                <input name='drone_idea' placeholder='DESPLEGAR MISIÓN...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:15px; flex-grow:1;'>
                <button type='submit' class='btn-gen' style='width:auto;'>GENERAR ECOSISTEMA</button>
            </div>
            <div style='display:flex; gap:10px;'>
                <button type='button' class='btn-util' onclick="window.location.href='/'">LIMPIAR MEMORIA</button>
                <button type='button' class='btn-util' style='background:#f0f; color:#000; border:none;' onclick="window.speechSynthesis.speak(new SpeechSynthesisUtterance('Alex, ecosistema MAIA 2 sincronizado. Software, Hardware y Modelo 3D en línea.'))">VOZ MAIA</button>
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
        <span>PESO: {calc.get('Peso','-')}</span> <span>EMPUJE: {calc.get('Empuje','-')}</span>
        <span>TWR: {calc.get('TWR','-')}</span> <span>BATERÍA: {calc.get('Vuelo','-')}</span>
    </div>

    <div class='grid-main'>
        <div class='panel'>
            <h2 style='color:#f0f;'>HARDWARE (8 CAPAS)</h2>
            <div style='display:grid; grid-template-columns: 1fr 1fr; gap:5px;'>
                {"".join([f"<div class='hw-card'><h4>{k}</h4><ul style='padding-left:15px;'>"+"".join([f"<li>{i}</li>" for i in v])+"</ul></div>" for k,v in hw_data.items()])}
            </div>
        </div>
        
        <div class='panel'>
            <h2 style='color:#0f0;'>VISUALIZACIÓN 3D TÁCTICA</h2>
            {"<p style='text-align:center;'>AGUARDANDO RENDER...</p>" if not m3d_data else f'''
                <div class='m3d-card'>
                    <h4>CONFIGURACIÓN DE MALLA</h4>
                    <p><b>CHASIS:</b> {m3d_data['GEOMETRÍA_BASE']['Tipo']}</p>
                    <p><b>RESOLUCIÓN:</b> {m3d_data['GEOMETRÍA_BASE']['Vértices']}</p>
                </div>
                <div class='m3d-card' style='margin-top:10px;'>
                    <h4>EFECTOS Y RENDER</h4>
                    <ul>{"".join([f"<li>{x}</li>" for x in m3d_data['RENDER_OPTIONS']])}</ul>
                </div>
                <div class='m3d-card' style='margin-top:10px;'>
                    <h4>VFX ACTIVOS</h4>
                    <ul>{"".join([f"<li>{x}</li>" for x in m3d_data['VFX_TACTICOS']])}</ul>
                </div>
            '''}
        </div>
    </div>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)