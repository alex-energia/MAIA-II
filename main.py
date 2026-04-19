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
    h = "<html><head><title>MAIA II - NEXO</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:'Courier New', monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 25px rgba(0,255,255,0.3);}" 
    h += "details{background:#020202; border:1px solid #333; margin:10px 0; padding:10px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:8px; text-transform:uppercase; outline:none;}" 
    h += ".code-view{background:#080808; color:#0f0; padding:20px; border-left:4px solid #0f0; white-space:pre-wrap; font-size:0.85em; margin:10px 0; line-height:1.6; border-radius:3px;}" 
    h += "input{width:60%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em; outline:none;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase; transition:0.3s;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-voz{background:red; color:#fff;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #0ff; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:12px; border:1px solid #1a1a1a; text-align:left;}" 
    h += "th{background:#003333; color:yellow;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. Nexo de ingenieria al 40 por ciento. Desplegando firmware de produccion.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA PROFESIONAL ]</h1>" 
    h += "<div class='panel'><h2>ESTACION DE TRABAJO: DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Requerimiento tecnico...' value=''>" 
    h += "<button type='submit' class='btn-gen'>DESPLEGAR SISTEMA</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>PROYECTO: " + idea + "</h2>" 
        h += "<details open><summary>[+] AGENTE 3D: ARQUITECTURA FISICA</summary><div class='folder'>" 
        h += "<pre style='color:#fff; font-size:12px;'>      [MOTOR_1]          [MOTOR_2]\\n          \\\\              /\\n           \\\\  __________  /\\n            \\\\|          |/\\n       [ARM] |  [BODY]  | [ARM]\\n            /|__________|\\\\\\n           /              \\\\\\n      [MOTOR_4]          [MOTOR_3]\\n\\nESTRUCTURA: MONOCASCO FIBRA DE CARBONO 4K TORAY</pre></div></details>" 
        h += "<details><summary>[DIR] AGENTE SOFTWARE: SYSTEM KERNEL (40% PROGRESS)</summary><div class='folder'>" 
        h += "<details><summary>?? estimation/fusion</summary><div class='folder'><details><summary>?? ekf_filter.cpp</summary><div class='code-view'>#include ^Eigen/Dense^\\n// Extended Kalman Filter para fusion GPS/IMU\\nvoid EKF::predict(float dt) {\\n  state_transition_matrix(dt);\\n  x = F * x;\\n  P = F * P * F.transpose() + Q;\\n}</div></details></div></details>" 
        h += "<details><summary>?? comm/mavlink</summary><div class='folder'><details><summary>?? telemetry_handler.py</summary><div class='code-view'>from pymavlink import mavutil\\ndef send_heartbeat(connection):\\n  connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_QUADROTOR,\\n                                 mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOT, 0, 0, 0)</div></details></div></details>" 
        h += "<details><summary>?? control/low_level</summary><div class='folder'><details><summary>?? pwm_driver.c</summary><div class='code-view'>void set_motor_speed(uint8_t motor_id, float throttle) {\\n  uint16_t pulse = (uint16_t)(1000 + (throttle * 1000));\\n  TIM_SetCompare(motor_id, pulse); // Registro de hardware directo</div></details></div></details>" 
        h += "</div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: DOM PROFESIONAL E INDUSTRIAL</summary><div class='folder'>" 
        h += "<table><tr><th>SUBSISTEMA</th><th>COMPONENTE EXPLICITO</th><th>PUERTO/BUS</th></tr>" 
        h += "<tr><td>AVIONICA</td><td>Orange Cube+ H743</td><td>SPI/I2C/CAN</td></tr>" 
        h += "<tr><td>ESC</td><td>Hobbywing XRotor 80A FOC</td><td>PWM/DShot600</td></tr>" 
        h += "<tr><td>POSICION</td><td>Here3+ RTK GPS</td><td>CAN Bus 1</td></tr></table></div></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: ANALISIS DE SISTEMAS</summary><div class='folder'>" 
        h += "<table><tr><td><b>FISICA</b></td><td>Relacion Empuje/Peso 2.9:1. Torque maximo: 4.5Nm.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>EMI (Interferencia Electromagnetica) en cableado de telemetria.</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>Uso de tornilleria de titanio Grado 5 con Loctite 243.</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR DE PROYECTO</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
