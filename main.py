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
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 30px #0ff;}" 
    h += "details{background:#020202; border:1px solid #333; margin:8px 0; padding:10px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#080808; color:#0f0; padding:20px; border-left:4px solid #0f0; white-space:pre; font-size:0.85em; overflow-x:auto; line-height:1.6; font-weight:bold;}" 
    h += "input{width:55%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em; outline:none;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-voz{background:red; color:#fff;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #0ff; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:12px; border:1px solid #222; text-align:left;}" 
    h += "th{background:#002222; color:yellow;}" 
    h += ".status-bar{background:#333; color:#fff; padding:5px; font-size:10px; text-align:right; border-top:1px solid #0ff;}" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); " 
    h += "if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. El sistema ha alcanzado el nivel de arquitectura avanzada 0.9. Los bloques de codigo son ahora de grado industrial.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA NIVEL: GLI-DRONE ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Especifique idea para despliegue tecnico...' value=''>" 
    h += "<button type='submit' class='btn-gen'>DESPLEGAR ARQUITECTURA</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>PROYECTO: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: PRODUCTION-READY ARCHITECTURE</summary><div class='folder'>" 
        h += "<details><summary>?? ai/perception</summary><div class='folder'><details><summary>?? thermal_segmentation.py</summary><div class='code-view'>import numpy as np\nimport segmentation_models_pytorch as smp\n\nclass ThermalAnalyzer:\n    def __init__(self, encoder='resnet34'):\n        self.model = smp.Unet(encoder_name=encoder, classes=1, activation='sigmoid')\n    def get_hotspot_mask(self, thermal_frame):\n        tensor = self.preprocess(thermal_frame)\n        return self.model.predict(tensor) > 0.85</div></details></div></details>" 
        h += "<details><summary>?? control/stabilization</summary><div class='folder'><details><summary>?? attitude_control.cpp</summary><div class='code-view'>#include ^mavlink.h^\n#include ^Eigen/Dense^\n\nvoid updateAttitude(const Eigen::Quaternionf& target_q) {\n    Eigen::Quaternionf current_q = imu.get_quaternion();\n    Eigen::Quaternionf error_q = target_q * current_q.inverse();\n    // Control por torque para evitar Gimbal Lock\n    Vector3f torque = (2.0f / dt) * error_q.vec();\n    motors.applyTorque(torque);\n}</div></details></div></details>" 
        h += "<details><summary>?? core/safety</summary><div class='folder'><details><summary>?? failsafe_manager.py</summary><div class='code-view'>import time\nclass Failsafe:\n    def check_vitals(self, battery, link_rssi):\n        if battery < 15.0 or link_rssi < -95:\n            print('[CRITICAL] RTL INITIATED')\n            self.trigger_return_to_launch()</div></details></div></details>" 
        h += "<details><summary>?? mission/logic</summary><div class='folder'><details><summary>?? waypoint_engine.py</summary><div class='code-view'>from collections import deque\nclass MissionEngine:\n    def __init__(self):\n        self.waypoints = deque()\n    def execute_next(self):\n        target = self.waypoints.popleft()\n        nav.move_to(target.lat, target.lon, target.alt)</div></details></div></details>" 
        h += "</div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: FULL BOM INDUSTRIAL</summary><div class='folder'>" 
        h += "<table><tr><th>SUBSISTEMA</th><th>COMPONENTE</th><th>INTERFAZ</th></tr>" 
        h += "<tr><td>AVIONICA</td><td>Orange Cube+ (Triple IMU)</td><td>MAVLink / CAN Bus</td></tr>" 
        h += "<tr><td>IA EDGE</td><td>NVIDIA Jetson Orin Nano</td><td>MIPI-CSI / Ethernet</td></tr>" 
        h += "<tr><td>TELEMETRIA</td><td>Microhard p900</td><td>UART / 900MHz FHSS</td></tr></table></div></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: ANALISIS SISTEMICO</summary><div class='folder'>" 
        h += "<table><tr><td><b>FISICA</b></td><td>MTOW: 18.5kg. Factor de carga max: 4.5G.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>Interferencia de cenizas en sensores opticos (Requiere Lidar).</td></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>TRL-8 (System complete and qualified).</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR DE PROYECTO</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
