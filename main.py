# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request
from software_engine import get_node_library

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Lógica de inicio en blanco: Si no hay POST, los valores son vacíos
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    # Solo obtenemos la librería si hay una idea escrita
    db = get_node_library(idea) if idea else {f"{i:02}_NODO": "// Esperando generación..." for i in range(1, 15)}
    
    # El visor permanece vacío si no se ha seleccionado un nodo
    current_code = db.get(target, "// VISOR BLOQUEADO: Ingrese idea y seleccione un nodo") if target else "// ESPERANDO ACCIÓN..."

    h = """
    <html><head><title>MAIA II - COMMAND CENTER</title>
    <style>
        body{background:#020202; color:#0ff; font-family:'Courier New', monospace; padding:20px; text-transform: uppercase;}
        .panel{border:1px solid #0ff; padding:15px; background:rgba(0,17,17,0.8); margin-bottom:10px; box-shadow: 0 0 10px #0ff;}
        .flex{display:flex; gap:15px;} .col-tree{width:30%;} .col-code{width:70%;}
        .code-window{background:#000; color:#39ff14; padding:20px; border-left:4px solid #f0f; height:600px; overflow-y:scroll; white-space:pre-wrap; font-size:12px; line-height:1.5;}
        
        input, button { font-family: monospace; }
        .input-idea {width:50%; background:#000; color:#0ff; border:1px solid #0ff; padding:12px; font-size:1.1em;}
        
        .btn-gen{background:#0ff; color:#000; padding:10px 20px; cursor:pointer; font-weight:bold; border:none;}
        .btn-gen:hover{background:#fff;}
        
        .btn-node{background:none; color:#0f0; width:100%; text-align:left; cursor:pointer; border:1px solid transparent; padding:5px; transition: 0.3s;}
        .btn-node:hover{background:rgba(0,255,0,0.1); border:1px solid #0f0;}
        
        .action-btns { display: flex; gap: 10px; margin-top: 10px; }
        .btn-util { background:#000; border:1px solid #f0f; color:#f0f; padding:5px 15px; cursor:pointer; }
        .btn-util:hover { background:#f0f; color:#000; }
        
        .hw-spec{background:rgba(0,255,255,0.05); border:1px solid #0ff; padding:10px; display:flex; justify-content: space-between; font-size: 0.9em;}
        h1, h2, h3 { margin-top: 0; color: #f0f; text-shadow: 2px 2px #000; }
        ::-webkit-scrollbar { width: 5px; } ::-webkit-scrollbar-thumb { background: #f0f; }
    </style>
    </head><body>
    
    <h1><span style='color:#0ff;'>▶</span> M.A.I.A. II - GLOBAL LOGISTICS INTELLIGENCE</h1>
    
    <div class='panel'>
        <h2>GENERACION ESTRATEGICA</h2>
        <form method='post' id='main_form'>
            <input name='drone_idea' class='input-idea' placeholder='INGRESE CONCEPTO BRUTAL DE DRON...' value='""" + idea + """'>
            <button type='submit' class='btn-gen'>GENERAR EXPEDIENTE</button>
            
            <div class='action-btns'>
                <button type='button' class='btn-util' onclick="window.location.href='/'">LIMPIAR INTERFAZ</button>
                <button type='button' class='btn-util' onclick="alert('Accediendo a Memoria de Nodos... Transfiriendo datos GLI')">MEMORIA</button>
                <button type='button' style='background:#f0f; color:#000; border:none; padding:5px 15px; font-weight:bold;' onclick="window.speechSynthesis.speak(new SpeechSynthesisUtterance('Alex, sistema cargado. Motor de ingeniería listo.'))">VOZ MAIA</button>
            </div>
        </form>
    </div>

    <div class='panel'>
        <h2>MODULO DE CONSTRUCCION (ENSAMBLAJE DINÁMICO)</h2>
        <div class='hw-spec'>
            <span><b>CHASIS:</b> CARBONO M40J ESTRUCTURAL</span>
            <span><b>PROPULSION:</b> KDE DIRECT HIGH-TORQUE</span>
            <span><b>POWER:</b> 12S INTELLIGENT ENERGY</span>
            <span><b>CORE:</b> STM32H7 DUAL-CORE</span>
        </div>
    </div>

    <div class='flex'>
        <div class='col-tree'>
            <div class='panel'>
                <h3>14 NODOS DE INGENIERÍA</h3>
                <div style='max-height: 400px; overflow-y: auto;'>
    """
    # Renderizar botones de nodos
    for n in sorted(db.keys()):
        h += f"""
        <form method='post' style='margin:0;'>
            <input type='hidden' name='drone_idea' value='{idea}'>
            <input type='hidden' name='target_node' value='{n}'>
            <button type='submit' class='btn-node'>[MOD] {n}</button>
        </form>
        """
    
    h += """
                </div>
            </div>
            <div class='panel'>
                <h3>PROJECT LAB</h3>
                <button style='background:#f0f; color:#000; width:100%; font-weight:bold; padding:10px;'>BUSCADOR TÁCTICO</button>
            </div>
        </div>

        <div class='col-code'>
            <div class='panel' style='height: 100%;'>
                <h3>VISOR DE CÓDIGO: """ + (target if target else "STANDBY") + """</h3>
                <div class='code-window'>""" + current_code + """</div>
            </div>
        </div>
    </div>

    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)