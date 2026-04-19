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
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px;}" 
    h += "details{background:#050505; border:1px solid #333; margin:10px 0; padding:10px; cursor:pointer;}" 
    h += "summary{font-weight:bold; color:yellow; font-size:1.1em; padding:5px;}" 
    h += ".code-view{background:#0a0a0a; color:#0f0; padding:15px; border-left:3px solid #0f0; white-space:pre; font-size:0.85em; overflow-x:auto;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:1px solid #0ff; padding:10px;}" 
    h += "button{padding:10px 15px; font-weight:bold; cursor:pointer; margin:5px; border:none;}" 
    h += ".btn-gen{background:#0ff; color:#000;}" 
    h += ".btn-mem{background:#555; color:#fff;}" 
    h += ".btn-clr{background:#a00; color:#fff;}" 
    h += ".btn-voz{background:red; color:#fff; transition: 0.3s;}" 
    h += ".folder{margin-left:20px; border-left:1px dashed #444; padding-left:15px;}" 
    h += "</style><script>" 
    h += "function hablar(){ let btn=document.getElementById('btnVoz'); btn.style.background='green'; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia en que puedo ayudarte'); " 
    h += "m.lang='es-MX'; window.speechSynthesis.speak(m); }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Idea de dron...' value='\"+idea+\"'>" 
    h += "<button type='submit' class='btn-gen'>GENERAR</button>" 
    h += "<button type='button' class='btn-mem'>MEMORIA</button>" 
    h += "<button type='reset' class='btn-clr'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='hablar()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE: " + idea + "</h2>" 
        h += "<details><summary>[DIR] AGENTE SOFTWARE (SISTEMA OPERATIVO)</summary><div class='folder'>" 
        h += "<details><summary>drivers/imu_sensor.cpp</summary><div class='code-view'>#include ^I2C.h^\\nvoid readIMU() { ax = readReg(0x3B); ay = readReg(0x3D); az = readReg(0x3F); }</div></details>" 
        h += "<details><summary>src/navigation/ekf_filter.py</summary><div class='code-view'>import numpy as np\\ndef update_state(x, P, z):\\n  F = np.eye(4)\\n  x = F @ x\\n  P = F @ P @ F.T + Q</div></details>" 
        h += "<details><summary>ai/vision_thermal.py</summary><div class='code-view'>import cv2\\ndef thermal_detect(frame):\\n  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\\n  (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)\\n  return maxLoc</div></details></div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE (COMPONENTES)</summary><div class='folder'>" 
        h += "<ul><li><b>Poder:</b> Lipo 6S 22.2V 10000mAh 95C</li><li><b>Control:</b> Pixhawk 6C + Raspberry Pi 5 (Companion)</li></ul></div></details>" 
        h += "<details><summary>[DIR] AGENTE EXPERTO (MATRIZ DE VIABILIDAD)</summary><div class='folder'>" 
        h += "<table><tr><td><b>Fisica:</b></td><td>Estabilidad aerodinamica certificada. Centro de gravedad (CoG) optimizado.</td></tr>" 
        h += "<tr><td><b>Riesgos:</b></td><td>Interferencia RF, Degradacion de bateria por temperatura extrema.</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR PROYECTOS</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
