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
    h += "summary{font-weight:bold; color:yellow; font-size:1.1em; padding:10px; border-bottom:1px solid #222;}" 
    h += ".code-view{background:#0a0a0a; color:#0f0; padding:20px; border-left:4px solid #0f0; white-space:pre; font-size:0.85em; overflow-x:auto; line-height:1.4;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:1px solid #0ff; padding:12px; font-size:1em;}" 
    h += "button{padding:12px 20px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;}" 
    h += ".btn-voz{background:red; color:#fff;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #0ff; padding-left:15px; margin-top:10px;}" 
    h += "table{width:100%; border-collapse:collapse; margin-top:10px;} td{padding:10px; border:1px solid #333;}" 
    h += "</style><script>" 
    h += "function hablar(){ let btn=document.getElementById('btnVoz'); btn.style.background='green'; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. Iniciando calculos de ingenieria avanzada para tu proyecto.'); " 
    h += "m.lang='es-MX'; m.rate=0.9; window.speechSynthesis.speak(m); }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA BRUTAL ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Escribe cualquier idea (Aereo, Maritimo, Espacial)...' value='\"+idea+\"'>" 
    h += "<button type='submit' class='btn-gen'>GENERAR SISTEMA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='hablar()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE MAESTRO: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE 3D: PROTOTIPO ESTRUCTURAL</summary><div class='folder'>" 
        h += "<pre style='color:#0f0; font-size:12px; line-height:1;'>" 
        h += "      [M1]  __  [M2]      \\n        \\  /  /  /       \\n         \\/  /  /        \\n    ----[ BODY ]----     \\n         /  /  \\         \\n        /  /  / \\        \\n      [M4]      [M3]      \\n   ESTADO: CONFIGURADO X8 </pre>" 
        h += "<ul><li><b>Material:</b> Fibra de Carbono 3K Toray (Alta densidad)</li><li><b>Brazos:</b> Tubulares 25mm con amortiguacion mecanica</li></ul></div></details>" 
        h += "<details><summary>[DIR] AGENTE SOFTWARE: FULL STACK FLIGHT CONTROL</summary><div class='folder'>" 
        h += "<details><summary>drivers/gnss_rtk.py</summary><div class='code-view'>import serial\\ndef get_rtk_precision():\\n  # Protocolo NMEA High Precision\\n  ser = serial.Serial('/dev/ttyAMA0', 115200)\\n  while True:\\n    line = ser.readline()\\n    if '$GNGGA' in str(line):\\n      return parse_fix_quality(line) # Precision 0.01m</div></details>" 
        h += "<details><summary>src/stability/pid_controller.cpp</summary><div class='code-view'>float calculatePID(float target, float current) {\\n  static float last_error, integral;\\n  float error = target - current;\\n  integral += error * dt;\\n  float derivative = (error - last_error) / dt;\\n  last_error = error;\\n  return (Kp * error) + (Ki * integral) + (Kd * derivative);\\n}</div></details></div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: LISTA DE MATERIALES (BOM)</summary><div class='folder'>" 
        h += "<table><tr><td><b>Propulsion</b></td><td>Motores T-Motor MN6007 KV160 + Helices 21pulg</td></tr>" 
        h += "<tr><td><b>Energia</b></td><td>Sistema Dual Battery Solid State 30000mAh</td></tr>" 
        h += "<tr><td><b>Mision</b></td><td>Lidar Livox Avia + Camara Sony A7R IV</td></tr></table></div></details>" 
        h += "<details><summary>[DIR] AGENTE EXPERTO: ANALISIS DE FACTIBILIDAD</summary><div class='folder'>" 
        h += "<table><tr><td><b>Fisica</b></td><td>MTOW: 12.5kg | Tiempo Vuelo: 45min | Viento Max: 55km/h</td></tr>" 
        h += "<tr><td><b>Riesgos</b></td><td>Vibracion armonica en brazos (Solucion: dampers silicona).</td></tr>" 
        h += "<tr><td><b>Normativa</b></td><td>Cumplimiento Categoria Especifica (SORA) - Nivel de Riesgo II.</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR PROYECTOS</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
