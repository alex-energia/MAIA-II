import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    res = None 
    idea = "" 
    if request.method == 'POST' and 'drone_idea' in request.form: 
        idea = request.form.get('drone_idea', '') 
        res = "active" 
    h = "<html><head><title>MAIA II 60</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px;}" 
    h += "details{background:#050505; border:1px solid #333; margin:5px 0; padding:8px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#000; color:#0f0; padding:15px; border-left:4px solid #f0f; white-space:pre; font-size:0.85em; margin:10px 0; overflow-x:auto;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:2px solid #0ff; padding:12px;}" 
    h += "button{padding:12px 20px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-voz{background:red; color:#fff;}" 
    h += ".folder{margin-left:20px; border-left:1px dashed #555; padding-left:10px;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:10px; border:1px solid #222; text-align:left; font-size:0.9em;}" 
    h += "th{background:#002222; color:yellow;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. Nexo al 60 por ciento activado. Desplegando 14 modulos de ingenieria real.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA PROFESIONAL 60% ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Defina concepto de dron...' value=''>" 
    h += "<button type='submit' class='btn-gen'>DESPLEGAR ARQUITECTURA</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: FULL STACK ARCHITECTURE</summary><div class='folder'>" 
        h += "<details><summary>?? ai</summary><div class='folder'><details><summary>?? perception.py</summary><div class='code-view'>import torch\\n# Inferencia con TensorRT para baja latencia\\nclass AIModel:\\n  def __init__(self):\\n    self.model = torch.jit.load('perception_model.pt')</div></details></div></details>" 
        h += "<details><summary>?? comm</summary><div class='folder'><details><summary>?? mavlink_bridge.cpp</summary><div class='code-view'>#include ^mavlink.h^\\nvoid send_status() {\\n  mavlink_msg_sys_status_pack(sys_id, comp_id, ^msg, sensors, 0, 0, 500);\\n}</div></details></div></details>" 
        h += "<details><summary>?? control</summary><div class='folder'><details><summary>?? pid_inner_loop.c</summary><div class='code-view'>float update_rate(float error) {\\n  return (kp_r * error) + (ki_r * int_e) + (kd_r * deriv);\\n}</div></details></div></details>" 
        h += "<details><summary>?? fusion</summary><div class='folder'><details><summary>?? ekf_main.py</summary><div class='code-view'>import numpy as np\\ndef fuse(gps, imu):\\n  # Filtro de Kalman Extendido (EKF)\\n  return state_vector * K_gain</div></details></div></details>" 
        h += "<details><summary>?? navigation/swarm</summary><div class='folder'><details><summary>?? mesh_node.py</summary><div class='code-view'>def sync_swarm():\\n  # Sincronizacion de red mesh para evitar colisiones entre unidades\\n  broadcast_pos(current_pos)\\n  update_neighbor_matrix()</div></details></div></details>" 
        h += "<details><summary>?? main.py</summary><div class='code-view'>if __name__ == '__main__':\\n  # Punto de entrada del firmware\\n  init_all_systems()\\n  run_flight_os()</div></details>" 
        h += "<details><summary>?? ... (otras 9 carpetas de sistema)</summary><div class='folder'>?? perception, power, safety, simulation, telemetry, etc.</div></details>" 
        h += "</div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: COMPONENTES INDUSTRIALES</summary><div class='folder'>" 
        h += "<table><tr><th>SISTEMA</th><th>CARPETA</th><th>COMPONENTES</th></tr>" 
        h += "<tr><td>PROCESAMIENTO</td><td>?? edge_compute</td><td>NVIDIA Jetson Orin / Cube Orange</td></tr>" 
        h += "<tr><td>PROPULSION</td><td>?? actuators</td><td>ESC FOC 80A / Motores KDE Direct</td></tr>" 
        h += "<tr><td>COMUNICACION</td><td>?? radio_link</td><td>Microhard p900 / Silvus Mesh</td></tr></table></div></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: ANALISIS SISTEMICO</summary><div class='folder'>" 
        h += "<table><tr><td><b>FISICA</b></td><td>MTOW 18.2kg. Relacion Empuje/Peso 2.5:1 optimizada.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>Fallo de GPS. Mitigacion: Odometria visual habilitada.</td></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>95 por ciento - Basado en componentes TRL-8.</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR DE PROYECTO</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
