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
    h += "details{background:#020202; border:1px solid #0ff; margin:15px 0; padding:15px;}" 
    h += "summary{font-weight:bold; color:yellow; font-size:1.3em; cursor:pointer; text-transform:uppercase;}" 
    h += ".code-block{background:#000; color:#0f0; padding:25px; border-left:5px solid #0f0; white-space:pre-wrap; font-size:0.95em; margin:15px 0; line-height:1.7;}" 
    h += "input{width:65%; background:#000; color:#0ff; border:2px solid #0ff; padding:18px; font-size:1.2em;}" 
    h += "button{padding:18px 30px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-voz{background:red; color:#fff;}" 
    h += "table{width:100%; border-collapse:collapse; margin-top:20px;} td, th{padding:15px; border:1px solid #333;}" 
    h += "th{background:#002222; color:yellow; border:1px solid #0ff;} .status{color:#f0f; font-weight:bold;}" 
    h += "</style><script>" 
    h += "let h=false; function tVoz(){ let b=document.getElementById('btnVoz'); " 
    h += "if(!h){ b.style.background='green'; h=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. El expediente para inversionistas esta listo. Los datos de sigilo acustico han sido verificados por mi motor experto.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; h=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; h=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - DEFENSE & AEROSPACE MODULE ]</h1>" 
    h += "<div class='panel'><h2>ESTACION DE TRABAJO: DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Especifique mision de defensa...' value=''>" 
    h += "<button type='submit' class='btn-gen'>GENERAR DOSSIER TECNICO</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>DORSSIER: " + idea + "</h2><p class='status'>ESTADO: CLASIFICADO - CONFIDENCIAL</p>" 
        h += "<details open><summary>[+] AGENTE 3D: ARQUITECTURA DE SIGILO</summary><div>" 
        h += "<ul><li><b>Geometria:</b> Stealth X-Wing con carenado toroidal en motores para reducir ruido de punta.</li>" 
        h += "<li><b>Materiales:</b> Compuestos de grafeno y nucleo de Nomex para absorcion de vibraciones ultrasonicas.</li>" 
        h += "<li><b>Propulsion:</b> Helices 'Owl-Design' (bio-inspiradas) con bordes serrados.</li></ul></div></details>" 
        h += "<details><summary>[+] AGENTE SOFTWARE: KERNEL DE VUELO SILENCIOSO</summary>" 
        h += "<div class='code-block'>// silent_motor_driver.cpp\n#include ^FOC_Controller.h^\nvoid stealth_drive() {\n    // Field Oriented Control (FOC) para eliminar el ruido electromagnetico\n    apply_sinusoidal_current(motor_A, target_rpm);\n    modulate_frequency(18000); // Frecuencia fuera del espectro audible humano\n    monitor_vibration_nodes(accelerometer_feedback);\n}</div>" 
        h += "<div class='code-block'># signature_control.py\ndef analyze_acoustic_footprint(self):\n    db_level = self.hydro_sensor.get_noise_floor()\n    if db_level > THRESHOLD:\n        self.lower_altitude_and_rpm()\n        self.activate_active_noise_cancellation()</div></details>" 
        h += "<details><summary>[+] AGENTE HARDWARE: COMPONENTES DE GRADO MILITAR</summary>" 
        h += "<table><tr><th>SISTEMA</th><th>COMPONENTE</th><th>DATOS DE RENDIMIENTO</th></tr>" 
        h += "<tr><td>PROCESADOR</td><td>NVIDIA Jetson AGX Orin</td><td>275 TOPS (IA para sigilo activo)</td></tr>" 
        h += "<tr><td>MOTORES</td><td>KDE Direct Industrial</td><td>Bajo ruido / Alta densidad magnetica</td></tr>" 
        h += "<tr><td>ENLACE</td><td>Silvus StreamCaster 4200</td><td>Malla MIMO encriptada AES-256</td></tr></table></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: ANALISIS DE SUPERVIVENCIA</summary>" 
        h += "<table><tr><td><b>ACUSTICA</b></td><td>Firma sonora reducida en -15dB vs configuracion estandar.</td></tr>" 
        h += "<tr><td><b>RADAR</b></td><td>Seccion Transversal de Radar (RCS) optimizada mediante pintura RAM.</td></tr>" 
        h += "<tr><td><b>AUTONOMIA</b></td><td>Celdas de Hidrogeno para 4 horas de loitering silencioso.</td></tr></table></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB: GESTION DE CAPITAL</h2>" 
    h += "<button style='background:#f0f; color:#fff;'>CALCULAR ROI DEL PROYECTO</button>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>PREPARAR PITCH DE INVERSION</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
