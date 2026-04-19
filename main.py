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
    h = "<html><head><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 20px #0ff;}" 
    h += "details{background:#020202; border:1px solid #333; margin:5px 0; padding:10px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px;}" 
    h += ".code-view{background:#080808; color:#0f0; padding:20px; border-left:4px solid #0f0; white-space:pre; font-size:0.9em; margin:10px 0; line-height:1.5;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em;}" 
    h += "button{padding:15px 20px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-voz{background:red; color:#fff;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #444; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:12px; border:1px solid #222; text-align:left;}" 
    h += "th{background:#002222; color:yellow;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); " 
    h += "if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. El sistema multiagente ha desplegado la arquitectura completa del proyecto.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA PROFESIONAL ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Describa su idea de dron...' value=''>" 
    h += "<button type='submit' class='btn-gen'>GENERAR SISTEMA</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>PROYECTO: " + idea + "</h2>" 
        h += "<details open><summary>[+] AGENTE 3D: PROTOTIPO VISUAL</summary><div class='folder'>" 
        h += "<pre style='color:#fff; font-size:12px;'>      [M1]----[M2]\\n        \\  ||  /\\n         \\ || /\\n    <----[ BODY ]----->\\n         / || \\\\n        /  ||  \\\\n      [M4]----[M3]\\n CONFIGURACION: X-LAYOUT INDUSTRIAL</pre></div></details>" 
        h += "<details><summary>[DIR] AGENTE SOFTWARE: FULL STACK ARCHITECTURE</summary><div class='folder'>" 
        h += "<details><summary>?? ai</summary><div class='folder'><details><summary>?? perception.py</summary><div class='code-view'>import cv2\\ndef detect_objects(frame):\\n  model = load_yolo_weights()\\n  return model.predict(frame)</div></details></div></details>" 
        h += "<details><summary>?? control</summary><div class='folder'><details><summary>?? pid_controller.cpp</summary><div class='code-view'>float compute(float e) {\\n  integral += e * dt;\\n  return (Kp*e) + (Ki*integral) + (Kd*(e-last)/dt);\\n}</div></details></div></details>" 
        h += "<details><summary>?? fusion</summary><div class='folder'><details><summary>?? kalman_filter.py</summary><div class='code-view'>import numpy as np\\ndef predict(x, P):\\n  x = F @ x\\n  P = F @ P @ F.T + Q\\n  return x, P</div></details></div></details>" 
        h += "<details><summary>?? main.py</summary><div class='code-view'>if __name__ == '__main__':\\n  init_hardware()\\n  start_flight_loop()</div></details></div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: DOM PROFESIONAL</summary><div class='folder'>" 
        h += "<table><tr><th>SUBSISTEMA</th><th>CARPETA</th><th>DETALLE</th></tr>" 
        h += "<tr><td>AVIONICA</td><td>?? avionics_core</td><td>Pixhawk 6X + Raspberry Pi 5</td></tr>" 
        h += "<tr><td>MOTORES</td><td>?? propulsion_sys</td><td>T-Motor U15II KV80</td></tr>" 
        h += "<tr><td>ENERGIA</td><td>?? power_mgmt</td><td>Lipo 12S 22000mAh SmartBMS</td></tr></table></div></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: ANALISIS SISTEMICO</summary><div class='folder'>" 
        h += "<table><tr><td><b>FISICA</b></td><td>MTOW: 25kg. Centro de gravedad optimizado en eje Z.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>Interferencia de radio, Fallo de sensor IMU redundante.</td></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>Tecnica: 98% | Tiempo de ensamble: 40 horas.</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>Esquema de conexionado en serie para redundancia de poder.</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR DE PROYECTO</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
