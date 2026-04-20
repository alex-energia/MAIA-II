# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request

# Importaciones con sistema de rescate
try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs, calculate_performance, get_hardware_integrity_hash
except ImportError:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def calculate_performance(x): return {}
    def get_hardware_integrity_hash(): return "RECOVERY-MODE"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    # Procesamiento Seguro
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    calc = calculate_performance(idea)
    hw_hash = get_hardware_integrity_hash()
    
    # Visor de código con protección contra vacíos
    current_code = db.get(target, "// SELECCIONE UN NODO PARA DESPLEGAR CÓDIGO") if idea and target else "// AGUARDANDO GENERACIÓN ESTRATÉGICA..."

    h = f"""
    <html><head><title>MAIA II - ARQUITECTURA BRUTAL</title>
    <style>
        body{{background:#000505; color:#0ff; font-family:'Courier New', monospace; padding:20px;}}
        .panel{{border:1px solid #0ff; padding:15px; background:rgba(0,15,15,0.9); margin-bottom:15px; border-radius:4px;}}
        .flex{{display:flex; gap:15px;}} .col-tree{{width:25%;}} .col-code{{width:75%;}}
        .code-window{{background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:450px; overflow-y:scroll; white-space:pre-wrap; font-size:12px;}}
        .btn-gen{{background:#0ff; color:#000; padding:12px 25px; font-weight:bold; border:none; cursor:pointer; flex-grow:1;}}
        .btn-util{{background:none; border:1px solid #f0f; color:#f0f; padding:10px; cursor:pointer; margin-top:10px; font-weight:bold;}}
        .btn-node{{background:none; color:#0f0; width:100%; text-align:left; cursor:pointer; border:1px solid transparent; padding:6px; font-size:0.8em;}}
        .calc-bar{{background:#0ff; color:#000; padding:10px; display:flex; justify-content:space-around; font-weight:bold; margin-bottom:10px;}}
        .hw-grid{{display:grid; grid-template-columns: repeat(3, 1fr); gap:12px;}}
        .hw-card{{border:1px solid #f0f; padding:12px; background:rgba(255,0,255,0.05); font-size:0.8em;}}
        .hw-card h4{{color:#f0f; margin:0 0 8px 0; border-bottom:1px solid #f0f; text-transform:uppercase;}}
        ul{{padding-left:15px; margin:0;}} li{{margin-bottom:4px;}}
    </style>
    </head><body>
    
    <div style='float:right; color:#f0f;'>[ HASH: {hw_hash} ]</div>
    <h1>M.A.I.A. II - GLOBAL LOGISTICS INTELLIGENCE</h1>

    <div class='panel'>
        <form method='post'>
            <div style='display:flex; gap:10px;'>
                <input name='drone_idea' placeholder='DEFINA LA MISIÓN DEL DRON...' value='{idea}' style='background:#000; color:#0ff; border:1px solid #0ff; padding:12px; width:70%;'>
                <button type='submit' class='btn-gen'>GENERAR ECOSISTEMA BRUTAL</button>
            </div>
            <div style='display:flex; gap:10px;'>
                <button type='button' class='btn-util' onclick="window.location.href='/'">LIMPIAR SISTEMA</button>
                <button type='button' class='btn-util' style='background:#f0f; color:#000; border:none;' onclick="window.speechSynthesis.speak(new SpeechSynthesisUtterance('Alex, hardware y software sincronizados al nivel exponencial.'))">VOZ MAIA</button>
            </div>
        </form>
    </div>

    <div class='flex'>
        <div class='col-tree'>
            <div class='panel' style='height:490px; overflow-y:auto;'>
                <h3 style='color:#f0f;'>ESTRUCTURA DE NODOS</h3>
    """
    if db:
        for n in sorted(db.keys()):
            h += f"""<form method='post' style='margin:0;'>
                <input type='hidden' name='drone_idea' value='{idea}'>
                <input type='hidden' name='target_node' value='{n}'>
                <button type='submit' class='btn-node'>▶ {n}</button>
            </form>"""
    else:
        h += "<p style='color:#444;'>Esperando idea...</p>"
    
    h += f"""
            </div>
        </div>
        <div class='col-code'>
            <div class='panel'>
                <h3>VISOR TÁCTICO: <span style='color:#f0f;'>{target if target else "STANDBY"}</span></h3>
                <div class='code-window'>{current_code}</div>
            </div>
        </div>
    </div>

    <div class='panel'>
        <h2 style='color:#0ff;'>LISTA DE MATERIALES Y DINÁMICA (V8-BRUTAL)</h2>
    """
    
    if not idea or not hw_data:
        h += "<p style='color:#555; text-align:center;'>EL HARDWARE SE DESPLEGARÁ AL GENERAR LA IDEA.</p>"
    else:
        h += f"""
        <div class='calc-bar'>
            <span>PESO: {calc.get('Peso')}</span>
            <span>EMPUJE: {calc.get('Empuje')}</span>
            <span>RATIO TWR: {calc.get('TWR')}</span>
            <span>AUTONOMÍA: {calc.get('Vuelo')}</span>
        </div>
        <div class='hw-grid'>
            <div class='hw-card'><h4>Estructura</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data.get('ESTRUCTURA_Y_CUERPO', [])]) + """</ul></div>
            <div class='hw-card'><h4>Propulsión</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data.get('PROPULSION_Y_MOTORES', [])]) + """</ul></div>
            <div class='hw-card'><h4>Sensores</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data.get('SENSÓRICA_Y_VISIÓN', [])]) + """</ul></div>
            <div class='hw-card'><h4>Instrumentación</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data.get('INSTRUMENTACIÓN_Y_IA', [])]) + """</ul></div>
            <div class='hw-card'><h4>Táctico/Luces</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data.get('SISTEMA_LUMÍNICO_Y_SOCORRO', [])]) + """</ul></div>
            <div class='hw-card'><h4>Mando</h4><ul>""" + "".join([f"<li>{x}</li>" for x in hw_data.get('MANDO_Y_CONECTIVIDAD', [])]) + """</ul></div>
        </div>
        """

    h += "</div></body></html>"
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)