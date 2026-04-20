# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request
from software_engine import get_node_library
from hardware_engine import get_hardware_specs, get_hardware_integrity_hash

app = Flask(__name__)

# --- SELLO DE SEGURIDAD MAIA ---
SOFTWARE_LOCKED = True  # Blindaje activado

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    hw = get_hardware_specs()
    hw_hash = get_hardware_integrity_hash()
    db = get_node_library(idea)
    
    current_code = db.get(target, "// SISTEMA SELLADO: SELECCIONE NODO") if idea and target else "// AGUARDANDO COMANDO ESTRATÉGICO..."

    h = f"""
    <html><head><title>MAIA II - GLI INTERFACE</title>
    <style>
        body{{background:#010a0a; color:#0ff; font-family:monospace; padding:20px;}}
        .panel{{border:1px solid #0ff; padding:15px; background:rgba(0,30,30,0.9); margin-bottom:10px;}}
        .flex{{display:flex; gap:15px;}} .col-tree{{width:30%;}} .col-code{{width:70%;}}
        .code-window{{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; height:500px; overflow-y:scroll; white-space:pre-wrap;}}
        .btn-gen{{background:#0ff; color:#000; padding:10px 20px; font-weight:bold; border:none; cursor:pointer;}}
        .btn-node{{background:none; color:#0f0; width:100%; text-align:left; cursor:pointer; border:1px solid transparent; padding:8px;}}
        .hw-grid{{display:grid; grid-template-columns: 1fr 1fr; gap:10px; font-size:0.8em; color:#f0f;}}
        .status-tag{{background:#0ff; color:#000; padding:2px 5px; font-size:0.7em;}}
    </style>
    </head><body>
    
    <div style='display:flex; justify-content:space-between; align-items:center;'>
        <h1>M.A.I.A. II <span style='color:#f0f;'>[ GLI HARDWARE READY ]</span></h1>
        <div>
            <span class='status-tag'>SW: LOCKED</span>
            <span class='status-tag' style='background:#f0f;'>HW HASH: {hw_hash}</span>
        </div>
    </div>

    <div class='panel'>
        <h3>HARDWARE ESTRATÉGICO (MÓDULO EXTRAÍDO)</h3>
        <div class='hw-grid'>
            <div><b>CHASIS:</b> {hw['FRAME']['model']}</div>
            <div><b>PROPULSIÓN:</b> {hw['PROPULSION_GLI']['motors']}</div>
            <div><b>AVIÓNICA:</b> {hw['AVIONICS_ELITE']['cpu_master']}</div>
            <div><b>COMUNICACIONES:</b> {hw['AVIONICS_ELITE']['comms']}</div>
        </div>
    </div>

    <div class='panel'>
        <form method='post'>
            <input name='drone_idea' placeholder='DEFINA EL PROPÓSITO...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:10px; width:50%;'>
            <button type='submit' class='btn-gen'>GENERAR EXPEDIENTE</button>
            <button type='button' style='background:none; border:1px solid #f0f; color:#f0f; padding:9px;' onclick="window.location.href='/'">LIMPIAR</button>
            <button type='button' style='background:#f0f; color:#000; padding:10px;' onclick="alert('Sello de integridad validado: No se permiten cambios en el kernel.')">INTEGRIDAD</button>
        </form>
    </div>

    <div class='flex'>
        <div class='col-tree'>
            <div class='panel' style='height:500px; overflow-y:auto;'>
                <h3 style='color:#f0f;'>NODOS DE SOFTWARE</h3>
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
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)