# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request
from software_engine import get_node_library
from hardware_engine import get_hardware_specs, calculate_performance, get_hardware_integrity_hash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    hw_hash = get_hardware_integrity_hash()
    
    current_code = db.get(target, "// SISTEMA LISTO") if idea and target else "// ESPERANDO GENERACIÓN..."

    h = f"""
    <html><head><title>MAIA II - ARQUITECTURA BRUTAL</title>
    <style>
        body{{background:#000808; color:#0ff; font-family:'Courier New', monospace; padding:20px;}}
        .panel{{border:1px solid #0ff; padding:15px; background:rgba(0,15,15,0.9); margin-bottom:15px;}}
        .flex{{display:flex; gap:15px;}} .col-tree{{width:25%;}} .col-code{{width:75%;}}
        .code-window{{background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:400px; overflow-y:scroll; white-space:pre-wrap; font-size:12px;}}
        .btn-gen{{background:#0ff; color:#000; padding:12px 25px; font-weight:bold; border:none; cursor:pointer; width:100%;}}
        .btn-node{{background:none; color:#0f0; width:100%; text-align:left; cursor:pointer; border:1px solid transparent; padding:6px; font-size:0.8em;}}
        .hw-grid{{display:grid; grid-template-columns: repeat(3, 1fr); gap:10px; margin-top:10px;}}
        .hw-card{{border:1px solid #f0f; padding:10px; background:rgba(255,0,255,0.05); font-size:0.75em;}}
        .hw-card h4{{color:#f0f; margin:0 0 5px 0; text-transform:uppercase; border-bottom:1px solid #f0f;}}
        .calc-bar{{background:#0ff; color:#000; padding:10px; display:flex; justify-content:space-around; font-weight:bold; margin-bottom:10px; border-radius:2px;}}
        .tag{{color:#f0f; font-size:0.8em;}}
    </style>
    </head><body>
    
    <div style='float:right;' class='tag'>INTEGRITY-HASH: {hw_hash}</div>
    <h1>[ M.A.I.A. II - DATA CONTEXT: BRUTAL HARDWARE ]</h1>

    <div class='panel'>
        <form method='post'>
            <div style='display:flex; gap:10px;'>
                <input name='drone_idea' placeholder='INGRESE MISIÓN PARA CALCULAR HARDWARE...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:12px; flex-grow:1;'>
                <button type='submit' class='btn-gen' style='width:auto;'>GENERAR EXPEDIENTE</button>
            </div>
            <div style='margin-top:10px;'>
                <button type='button' style='background:none; border:1px solid red; color:red; padding:8px;' onclick="window.location.href='/'">RESETEAR</button>
                <button type='button' style='background:#f0f; color:#000; padding:8px; border:none; font-weight:bold;' onclick="window.speechSynthesis.speak(new SpeechSynthesisUtterance('Alex, hardware brutal sincronizado.'))">VOZ MAIA</button>
            </div>
        </form>
    </div>

    <div class='flex'>
        <div class='col-tree'>
            <div class='panel' style='height:440px; overflow-y:auto;'>
                <h3 style='color:#f0f; font-size:0.9em;'>NODOS DE SOFTWARE</h3>
    """
    for n in sorted(db.keys()):
        h += f"""<form method='post' style='margin:0;'>
            <input type='hidden' name='drone_idea' value='{idea}'>
            <input type='hidden' name='target_node' value='{n}'>
            <button type='submit' class='btn-node'>▶ {n}</button>
        </form>"""
    
    h += f"""
            </div>
        </div>
        <div class='col-code'>
            <div class='panel'>
                <h3 style='color:#f0f; font-size:0.9em;'>VISOR DE CÓDIGO: {target if target else "STANDBY"}</h3>
                <div class='code-window'>{current_code}</div>
            </div>
        </div>
    </div>

    <div class='panel'>
        <h2 style='margin-top:0;'>ESPECIFICACIONES FÍSICAS EXPONENCIALES</h2>
    """
    
    if not idea or not hw_data:
        h += "<p style='color:#444; text-align:center;'>--- SISTEMA FÍSICO DESCONECTADO ---</p>"
    else:
        h += f"""
        <div class='calc-bar'>
            <span>MASA: {calc.get('Peso')}</span>
            <span>THRUST: {calc.get('Empuje')}</span>
            <span>TWR: {calc.get('TWR')}</span>
            <span>AIR TIME: {calc.get('Vuelo')}</span>
        </div>
        <div class='hw-grid'>
            <div class='hw-card'><h4>Estructura</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data['ESTRUCTURA_Y_CHASIS']]) + """</ul></div>
            <div class='hw-card'><h4>Propulsión</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data['PROPULSION_BRUTA']]) + """</ul></div>
            <div class='hw-card'><h4>Instru. & IA</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data['INSTRUMENTACION_Y_IA']]) + """</ul></div>
            <div class='hw-card'><h4>Visión & Sensores</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data['SENSORS_Y_CAMARAS']]) + """</ul></div>
            <div class='hw-card'><h4>Táctico & Luces</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data['ILUMINACION_Y_TACTICO']]) + """</ul></div>
            <div class='hw-card'><h4>Mando & Link</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data['SISTEMA_DE_MANDO']]) + """</ul></div>
        </div>
        """

    h += "</div></body></html>"
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
