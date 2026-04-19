import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    result = None 
    idea = "" 
    if request.method == 'POST' and 'drone_idea' in request.form: 
        idea = request.form.get('drone_idea') 
        result = { 
            "software": ["Controlador PID en C++", "Protocolo de comunicacion MAVLink", "Algoritmo de evision de obstaculos IA"], 
            "hardware": ["Procesador STM32F4", "Sensores IMU Bosch BNO055", "Modulos de telemetria 915MHz"], 
            "modelo_3d": ["Chasis optimizado en Fibra de Carbono", "Soportes de motor con amortiguacion", "Carcasa aerodinamica"], 
            "expert": ["Analisis de Viabilidad: 92%", "Calculo de Fisica: Empuje/Peso 2.5:1", "Riesgos: Interferencia electromagnetica baja"] 
        } 
    h = "<html><head><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px;}" 
    h += "details{background:#050505; border:1px solid #333; margin:10px 0; padding:10px; cursor:pointer;}" 
    h += "summary{font-weight:bold; color:yellow; font-size:1.2em;}" 
    h += ".code-view{background:#111; color:#0f0; padding:10px; border-left:3px solid #0f0; white-space:pre; font-size:0.9em; margin-top:5px;}" 
    h += "input{width:70%; background:#000; color:#0ff; border:1px solid #0ff; padding:10px;}" 
    h += "button{background:#0ff; border:none; padding:10px 20px; font-weight:bold; cursor:pointer;}" 
    h += "</style></head><body>" 
    h += "<h1> [ M.A.I.A. II - SISTEMA MULTIAGENTE ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Describa su idea de dron...' value='\"+idea+\"'>" 
    h += "<button type='submit'>GENERAR</button></form></div>" 
    if result: 
        h += "<div class='panel'><h2 style='color:white;'>PROYECTO: \"+idea+\"</h2>" 
        h += "<details><summary>[+] AGENTE IA: SOFTWARE</summary>" 
        h += "<div class='code-view'>// Kernel de Vuelo v1.0\\nvoid setup() { init_sensors(); }\\nvoid loop() { calculate_PID(); stable_flight(); }</div></details>" 
        h += "<details><summary>[+] AGENTE HARDWARE: COMPONENTES</summary><ul>" 
        for item in result['hardware']: h += f"<li>{item}</li>" 
        h += "</ul></details>" 
        h += "<details><summary>[+] AGENTE 3D: ESTRUCTURA</summary><ul>" 
        for item in result['modelo_3d']: h += f"<li>{item}</li>" 
        h += "</ul></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: ANALISIS SISTEMICO</summary><ul>" 
        for item in result['expert']: h += f"<li>{item}</li>" 
        h += "</ul></details></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == "__main__": 
    port = int(os.environ.get(\"PORT\", 10000)) 
    app.run(host=\"0.0.0.0\", port=port) 
