import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    res = None 
    idea = "" 
    if request.method == 'POST': 
        idea = request.form.get('drone_idea', '') 
        res = "active" 
    h = "<html><head><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px;}" 
    h += "details{background:#050505; border:1px solid #333; margin:10px 0; padding:10px; cursor:pointer;}" 
    h += "summary{font-weight:bold; color:yellow; font-size:1.2em; padding:5px;}" 
    h += ".code-view{background:#0a0a0a; color:#0f0; padding:15px; border-left:3px solid #0f0; white-space:pre; font-size:0.85em; overflow-x:auto; margin:10px 0;}" 
    h += "input{width:60%; background:#000; color:#0ff; border:1px solid #0ff; padding:10px;}" 
    h += "button{background:#0ff; border:none; padding:10px 20px; font-weight:bold; cursor:pointer;}" 
    h += ".folder{margin-left:20px; border-left:1px dashed #444; padding-left:10px;}" 
    h += "</style></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO MULTIAGENTE ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Idea de dron...' value='\"+idea+\"'>" 
    h += "<button type='submit'>GENERAR PROYECTO</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE TECNICO: " + idea + "</h2>" 
        h += "<details><summary>[DIR] AGENTE IA: SOFTWARE (REAL_CODE)</summary><div class='folder'>" 
        h += "<details><summary>src/thermal_vision.py</summary><div class='code-view'>import cv2\nimport numpy as np\n\ndef detect_fire(frame):\n    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)\n    lower_fire = np.array([0, 120, 70])\n    upper_fire = np.array([10, 255, 255])\n    mask = cv2.inRange(hsv, lower_fire, upper_fire)\n    return np.sum(mask) > 500</div></details>" 
        h += "<details><summary>src/flight_control.cpp</summary><div class='code-view'>#include ^PitchRoll.h^\nvoid updatePID() {\n  error = target_angle - current_angle;\n  integral += error * dt;\n  derivative = (error - last_error) / dt;\n  output = (Kp*error) + (Ki*integral) + (Kd*derivative);\n}</div></details></div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: ESPECIFICACIONES</summary><div class='folder'>" 
        h += "<ul><li><b>Procesador:</b> NVIDIA Jetson Orin Nano (Analisis IA en tiempo real)</li>" 
        h += "<li><b>Sensores:</b> FLIR Lepton 3.5 (Termica) + GPS RTK (Precision 1cm)</li>" 
        h += "<li><b>Propulsion:</b> Motores T-Motor U10II + ESC 100A 12S (Carga pesada)</li></ul></div></details>" 
        h += "<details><summary>[DIR] AGENTE 3D: ARQUITECTURA</summary><div class='folder'>" 
        h += "<p><b>Visualizador:</b> Prototipo Quad-X Industrial 850mm</p>" 
        h += "<pre style='color:#555;'>      /\\      \n  [M1]--[M2]  \n   |  ||  |   \n  [M4]--[M3]  \n      \\/      </pre></div></details>" 
        h += "<details><summary>[DIR] AGENTE EXPERTO: ANALISIS SISTEMICO</summary><div class='folder'>" 
        h += "<table><tr><td><b>Fisica:</b></td><td>Resistencia a vientos de 45km/h. Empuje total: 18kg.</td></tr>" 
        h += "<tr><td><b>Riesgos:</b></td><td>Degradacion termica de componentes (Necesita recubrimiento Kapton).</td></tr>" 
        h += "<tr><td><b>Viabilidad:</b></td><td>Tecnica: 95% | Financiera: Dependiente de sensores FLIR.</td></tr></table>" 
        h += "</div></details></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
