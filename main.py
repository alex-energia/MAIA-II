import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    res = None 
    user_idea = "" 
    if request.method == 'POST' and 'drone_idea' in request.form: 
        user_idea = request.form.get('drone_idea', '') 
        res = "active" 
    h = "<html><head><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 15px #0ff;}" 
    h += "details{background:#050505; border:1px solid #333; margin:15px 0; padding:12px;}" 
    h += "summary{font-weight:bold; color:yellow; font-size:1.2em; cursor:pointer; padding:5px;}" 
    h += ".code-block{background:#0a0a0a; color:#0f0; padding:20px; border-left:4px solid #0f0; white-space:pre-wrap; font-size:0.9em; margin:10px 0; line-height:1.5; display:block;}" 
    h += "input{width:60%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em; outline:none;}" 
    h += "button{padding:15px 25px; font-weight:bold; cursor:pointer; margin:5px; border:none; transition: 0.3s;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-gen:hover{background:#fff;}" 
    h += ".btn-voz{background:red; color:#fff; border-radius:5px;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:12px; border:1px solid #222; text-align:left;}" 
    h += "th{background:#003333; color:yellow;}" 
    h += "</style><script>" 
    h += "let hablando = false; function toggleVoz(){ let btn=document.getElementById('btnVoz'); " 
    h += "if(!hablando){ btn.style.background='green'; hablando=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. Iniciando procesamiento de ingenieria avanzada.'); " 
    h += "m.lang='es-MX'; m.onend=()=> { btn.style.background='red'; hablando=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); btn.style.background='red'; hablando=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - ESTACION DE INGENIERIA ]</h1>" 
    h += "<div class='panel'><h2>MODULO: DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Escriba su requerimiento tecnico aqui...' value=''>" 
    h += "<button type='submit' class='btn-gen'>GENERAR SISTEMA</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='toggleVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE DE INGENIERIA: " + user_idea + "</h2>" 
        h += "<details open><summary>[+] AGENTE 3D: DISE¥O ESTRUCTURAL</summary>" 
        h += "<pre style='color:#fff; font-size:14px;'>" 
        h += "      [MOTOR_1]          [MOTOR_2]   \\n          \\              /        \\n           \\  __________  /         \\n            \\|          |/          \\n       [ARM] |  [BODY]  | [ARM]     \\n            /|__________|\\          \\n           /              \\         \\n      [MOTOR_4]          [MOTOR_3]  \\n      CONFIGURACION: QUAD-X REFORZADO</pre>" 
        h += "<ul><li><b>Chasis:</b> Monocasco de Fibra de Carbono 4K</li><li><b>Enfriamiento:</b> Disipadores pasivos de Aluminio 7075</li></ul></details>" 
        h += "<details><summary>[+] AGENTE SOFTWARE: ARQUITECTURA DE CONTROL</summary>" 
        h += "<div class='code-block'>// main_control.cpp\\n#include ^FlightCore.h^\\n\\nvoid processNavigation() {\\n    Vector3 pos = getGPSData();\\n    Vector3 target = getMissionWaypoint();\\n    \\n    if (checkObstacles()) {\\n        evadePath();\\n    } else {\\n        applyPID(pos, target);\\n    }\\n}</div>" 
        h += "<div class='code-block'># vision_system.py\\nimport cv2\\n\\ndef ai_analysis(stream):\\n    objects = model.detect(stream)\\n    for obj in objects:\\n        if obj.confidence > 0.85:\\n            log_event(obj.label)\\n            update_mission_priority(obj)</div></details>" 
        h += "<details><summary>[+] AGENTE HARDWARE: BILL OF MATERIALS (BOM)</summary>" 
        h += "<table><tr><th>CATEGORIA</th><th>COMPONENTE</th><th>ESPECIFICACION</th></tr>" 
        h += "<tr><td>PROCESADOR</td><td>NVIDIA Jetson Orin</td><td>IA y Vision Perimetral</td></tr>" 
        h += "<tr><td>MOTORES</td><td>T-Motor Antigravity</td><td>400KV High Efficiency</td></tr>" 
        h += "<tr><td>SENSORES</td><td>Lidar Livox + RTK</td><td>Precision milimetrica</td></tr></table></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: ANALISIS SISTEMICO</summary>" 
        h += "<table><tr><td><b>FISICA</b></td><td>Centro de masa a +2mm del eje central. Ratio empuje 3.2:1</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>Punto critico: Fatiga de material en brazos por vibracion.</td></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>Tecnica: 100% | Escalabilidad: Industrial</td></tr></table></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR DE PROYECTOS</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
