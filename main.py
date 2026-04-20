# -*- coding: utf-8 -*- 
import os 
from flask import Flask, render_template_string, request 
from software_engine import get_node_library 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    idea = request.form.get('drone_idea', 'DRON DE PRUEBA') 
    target = request.form.get('target_node', '01_CORE_RTOS') 
    db = get_node_library(idea) 
    current_code = db.get(target, '// Selecciona un nodo') 
    h = "<html><head><title>MAIA II - MODULAR</title><style>" 
    h += "body{background:#050505; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:1px solid #0ff; padding:15px; background:#001111; margin-bottom:10px;}" 
    h += ".flex{display:flex; gap:10px;} .col-tree{width:30%;} .col-code{width:70%;}" 
    h += ".code-window{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; height:500px; overflow-y:scroll; white-space:pre-wrap;}" 
    h += "button{padding:8px; cursor:pointer; font-weight:bold; margin:2px; border:none;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-node{background:none; color:#0f0; width:100%; text-align:left; cursor:pointer;}" 
    h += ".hw-spec{background:rgba(0,255,255,0.05); border:1px solid #0ff; padding:10px; margin-bottom:10px;}" 
    h += "</style></head><body>" 
    h += "<h1>[ M.A.I.A. II - ARQUITECTURA MODULAR ]</h1>" 
    h += "<div class='panel'><h2>GENERACION ESTRATEGICA</h2>" 
    h += "<form method='post'><input name='drone_idea' value='" + idea + "' style='width:40%; background:#000; color:#0ff; border:1px solid #0ff; padding:10px;'>" 
    h += "<button type='submit' class='btn-gen'>GENERAR EXPEDIENTE</button>" 
    h += "<button type='button' style='background:red; color:white;' onclick=\\\"window.speechSynthesis.speak(new SpeechSynthesisUtterance('Alex, motor de software cargado.'))\\\">VOZ MAIA</button></form></div>" 
    h += "<div class='panel'><h2>MODULO DE CONSTRUCCION</h2>" 
    h += "<div class='hw-spec'><b>CHASIS:</b> Carbono M40J | <b>PROPULSION:</b> KDE Direct | <b>POWER:</b> 12S</div></div>" 
    h += "<div class='flex'><div class='col-tree'><div class='panel'><h3>14 NODOS</h3>" 
    for n in db.keys(): 
        h += f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button class='btn-node'>?? {n}</button></form>" 
    h += "</div><div class='panel'><h3>PROJECT LAB</h3><button style='background:#f0f;'>BUSCADOR</button></div></div>" 
    h += "<div class='col-code'><div class='panel'><h3>VISOR: " + target + "</h3><div class='code-window'>" + current_code + "</div></div></div></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=10000) 
