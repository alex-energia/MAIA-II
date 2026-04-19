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
    h += "details{background:#020202; border:1px solid #333; margin:8px 0; padding:10px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px;}" 
    h += ".code-view{background:#080808; color:#0f0; padding:20px; border-left:4px solid #0f0; white-space:pre; font-size:0.85em; overflow-x:auto; line-height:1.6;}" 
    h += "input{width:55%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em; outline:none;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-voz{background:red; color:#fff;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #444; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:12px; border:1px solid #222; text-align:left;}" 
    h += "th{background:#002222; color:yellow;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); " 
    h += "if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. He desplegado el nexo de ingenieria completo con arquitectura de archivos real.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA PROFESIONAL ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Escriba su idea de dron...' value=''>" 
    h += "<button type='submit' class='btn-gen'>GENERAR SISTEMA</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>PROYECTO: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: FULL STACK ARCHITECTURE</summary><div class='folder'>" 
        h += "<details><summary>?? ai</summary><div class='folder'><details><summary>?? perception.py</summary><div class='code-view'>import torch\nfrom models.common import DetectMultiBackend\n\nclass Perceptor:\n    def __init__(self, weights):\n        self.model = DetectMultiBackend(weights, device='cuda')\n    def infer(self, im):\n        pred = self.model(im, augment=False, visualize=False)\n        return pred</div></details></div></details>" 
        h += "<details><summary>?? control</summary><div class='folder'><details><summary>?? pid_controller.cpp</summary><div class='code-view'>#include ^PID.h^\nclass FlightController {\npublic:\n    float compute(float target, float current, float dt) {\n        float error = target - current;\n        p_term = kp * error;\n        i_term += ki * error * dt;\n        d_term = kd * (error - last_error) / dt;\n        return clamp(p_term + i_term + d_term, -1.0, 1.0);\n    }\n};</div></details></div></details>" 
        h += "<details><summary>?? core</summary><div class='folder'><details><summary>?? threading_manager.py</summary><div class='code-view'>import threading\nclass CoreManager:\n    def start_tasks(self):\n        threading.Thread(target=self.telemetry_loop).start()\n        threading.Thread(target=self.safety_check).start()</div></details></div></details>" 
        h += "<details><summary>?? navigation</summary><div class='folder'><details><summary>?? pathfinder.py</summary><div class='code-view'>import heapq\ndef a_star(grid, start, goal):\n    open_set = []\n    heapq.heappush(open_set, (0, start))\n    # Logica de navegacion real por malla voxel...</div></details></div></details>" 
        h += "<details><summary>?? main.py</summary><div class='code-view'>from core.threading_manager import CoreManager\nif __name__ == '__main__':\n    system = CoreManager()\n    system.run_mission()</div></details></div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: COMPONENTES PROFESIONALES</summary><div class='folder'>" 
        h += "<table><tr><th>SUBSISTEMA</th><th>CARPETA</th><th>DETALLE TECNICO</th></tr>" 
        h += "<tr><td>AVIONICA</td><td>?? avionics_hub</td><td>Cube Orange+ / MAVLink v2.0</td></tr>" 
        h += "<tr><td>MOTORES</td><td>?? propulsion</td><td>T-Motor U15II KV80 / ESC FOC 12S</td></tr>" 
        h += "<tr><td>SENSORES</td><td>?? sensor_payload</td><td>Lidar Livox + FLIR Boson 640</td></tr></table></div></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: MATRIZ SISTEMICA</summary><div class='folder'>" 
        h += "<table><tr><td><b>FISICA</b></td><td>Analisis de Empuje Dinamico: 2.8:1 MTOW.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>Fallo de comunicacion (Failsafe: RTL activo).</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>Estructura modular con conectores AS150 antiquispas.</td></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>98% - Basado en componentes TRL-9.</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR DE PROYECTO</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
