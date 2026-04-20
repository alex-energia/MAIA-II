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
    
    # Carga de Motores
    db = get_node_library(idea)
    hw_list = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    hw_hash = get_hardware_integrity_hash()
    
    current_code = db.get(target, "// SELECCIONE NODO...") if idea and target else "// ESPERANDO GENERACIÓN..."

    h = f"""
    <html><head><title>MAIA II - COMMAND CENTER</title>
    <style>
        body{{background:#010505; color:#0ff; font-family:'Courier New', monospace; padding:20px;}}
        .panel{{border:1px solid #0ff; padding:15px; background:rgba(0,20,20,0.9); margin-bottom:15px;}}
        .flex{{display:flex; gap:15px;}} .col-tree{{width:30%;}} .col-code{{width:70%;}}
        .code-window{{background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:450px; overflow-y:scroll; white-space:pre-wrap; font-size:12px;}}
        .btn-gen{{background:#0ff; color:#000; padding:12px 25px; font-weight:bold; border:none; cursor:pointer;}}
        .btn-node{{background:none; color:#0f0; width:100%; text-align:left; cursor:pointer; border:1px solid transparent; padding:8px;}}
        .hw-grid{{display:grid; grid-template-columns: repeat(3, 1fr); gap:15px; margin-top:10px;}}
        .hw-card{{border:1px solid #f0f; padding:10px; background:rgba(255,0,255,0.05); font-size:0.8em;}}
        .calc-bar{{background:#0ff; color:#000; padding:10px; display:flex; justify-content:space-around; font-weight:bold; margin-bottom:10px;}}
        .hash-tag{{color:#f0f; font-size:0.8em; float:right;}}
    </style>
    </head><body>
    
    <span class='hash-tag'>GLI-HASH: {hw_hash}</span>
    <h1>[ M.A.I.A. II - GLOBAL LOGISTICS ]</h1>

    <div class='panel'>
        <form method='post'>
            <input name='drone_idea' placeholder='IDEA DEL DRON...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:12px; width:40%;'>
            <button type='submit' class='btn-gen'>GENERAR SISTEMA COMPLETO</button>
            <button type='button' style='background:none; border:1px solid red; color:red; padding:10px;' onclick="window.location.href='/'">LIMPIAR</button>
        </form>
    </div>

    <div class='flex'>
        <div class='col-tree'>
            <div class='panel' style='height:490px; overflow-y:auto;'>
                <h3 style='color:#f0f;'>14 NODOS DE SOFTWARE</h3>
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
                <h3>VISOR TÁCTICO: {target if target else "STANDBY"}</h3>
                <div class='code-window'>{current_code}</div>
            </div>
        </div>
    </div>

    <div class='panel'>
        <h2>ESPECIFICACIONES DE HARDWARE BRUTAL</h2>
    """
    
    if not idea:
        h += "<p style='color:#444;'>SISTEMA FÍSICO EN ESPERA...</p>"
    else:
        h += f"""
        <div class='calc-bar'>
            <span>MASA: {calc['Peso Total']}</span>
            <span>THRUST: {calc['Empuje Máximo']}</span>
            <span>TWR: {calc['Ratio TWR']}</span>
            <span>FLIGHT TIME: {calc['Autonomía']}</span>
        </div>
        <div class='hw-grid'>
            <div class='hw-card'><b style='color:#f0f;'>CHASIS:</b><br>{hw_list['ESTRUCTURA']['Cuerpo']}</div>
            <div class='hw-card'><b style='color:#f0f;'>MOTORES:</b><br>{hw_list['PROPULSION']['Motores']}</div>
            <div class='hw-card'><b style='color:#f0f;'>BATERÍA:</b><br>{hw_list['ENERGÍA']['Baterías']}</div>
            <div class='hw-card'><b style='color:#f0f;'>SENSOR:</b><br>{hw_list['SENSÓRICA Y CÁMARAS']['Lidar']}</div>
            <div class='hw-card'><b style='color:#f0f;'>CÁMARA:</b><br>{hw_list['SENSÓRICA Y CÁMARAS']['Cámara Principal']}</div>
            <div class='hw-card'><b style='color:#f0f;'>ENLACE:</b><br>{hw_list['MANDO Y COMUNICACIONES']['Control Remoto']}</div>
        </div>
        """

    h += """
    </div>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)