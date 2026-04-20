# -*- coding: utf-8 -*-
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
    
    current_code = db.get(target, "// NODO SELECCIONADO") if idea and target else "// AGUARDANDO COMANDO..."

    h = f"""
    <html><head><title>MAIA II - GLI V10</title>
    <style>
        body{{background:#000d0d; color:#0ff; font-family:monospace; padding:20px;}}
        .panel{{border:1px solid #0ff; padding:15px; background:rgba(0,20,20,0.9); margin-bottom:15px;}}
        .flex{{display:flex; gap:15px;}} .col-tree{{width:20%;}} .col-code{{width:80%;}}
        .code-window{{background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:400px; overflow-y:scroll; white-space:pre-wrap; font-size:11px;}}
        .btn-gen{{background:#0ff; color:#000; padding:12px; font-weight:bold; border:none; cursor:pointer; width:100%;}}
        .calc-bar{{background:#0ff; color:#000; padding:10px; display:flex; justify-content:space-around; font-weight:bold; margin-bottom:15px;}}
        .hw-grid{{display:grid; grid-template-columns: repeat(4, 1fr); gap:10px;}}
        .hw-card{{border:1px solid #f0f; padding:10px; background:rgba(255,0,255,0.05); font-size:0.7em;}}
        .hw-card h4{{color:#f0f; margin:0 0 5px 0; border-bottom:1px solid #f0f; text-transform:uppercase;}}
        .btn-node{{background:none; color:#0f0; width:100%; text-align:left; cursor:pointer; border:1px solid transparent; padding:4px; font-size:0.8em;}}
    </style>
    </head><body>
    
    <div style='text-align:right; font-size:0.7em; color:#f0f;'>HASH: {hw_hash}</div>
    <h1>M.A.I.A. II [ GLOBAL LOGISTICS INTELLIGENCE ]</h1>

    <div class='panel'>
        <form method='post'>
            <input name='drone_idea' placeholder='IDEA DEL DRON...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:12px; width:70%;'>
            <button type='submit' class='btn-gen' style='width:25%;'>GENERAR</button>
        </form>
    </div>

    <div class='flex'>
        <div class='col-tree'>
            <div class='panel' style='height:400px; overflow-y:auto;'>
                <h3 style='color:#f0f; font-size:0.8em;'>NODOS SOFTWARE</h3>
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
                <h3>VISOR: {target if target else "STANDBY"}</h3>
                <div class='code-window'>{current_code}</div>
            </div>
        </div>
    </div>

    <div class='panel'>
        <div class='calc-bar'>
            <span>PESO: {calc['Peso']}</span> <span>EMPUJE: {calc['Empuje']}</span>
            <span>TWR: {calc['TWR']}</span> <span>VUELO: {calc['Vuelo']}</span>
        </div>

        <div class='hw-grid'>
    """
    if not idea:
        h += "<div style='grid-column: span 4; text-align:center;'>ESPERANDO MISIÓN...</div>"
    else:
        for category, items in hw_data.items():
            h += f"<div class='hw-card'><h4>{category}</h4><ul style='padding-left:15px;'>"
            h += "".join([f"<li>{item}</li>" for item in items])
            h += "</ul></div>"

    h += "</div></div></body></html>"
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)