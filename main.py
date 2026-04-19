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
    h = "<html><head><title>MAIA II - 60% DEV</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:'Courier New', monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 30px #0ff;}" 
    h += "details{background:#020202; border:1px solid #333; margin:8px 0; padding:12px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#050505; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre-wrap; font-size:0.85em; margin:10px 0; line-height:1.6; border-radius:3px;}" 
    h += "input{width:60%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em; outline:none;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-voz{background:red; color:#fff;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #f0f; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse; margin-top:15px;} td, th{padding:12px; border:1px solid #1a1a1a;}" 
    h += "th{background:#003333; color:yellow;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. Nexo de ingenieria al 60 por ciento. Desplegando modulos de vision artificial y navegacion autonoma avanzada.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA NIVEL: GLI-DRONE (60%) ]</h1>" 
    h += "<div class='panel'><h2>ESTACION DE TRABAJO: DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Requerimiento tecnico de alto nivel...' value=''>" 
    h += "<button type='submit' class='btn-gen'>DESPLEGAR ARQUITECTURA</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>DOSSIER DE INGENIERIA: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: SYSTEM ARCHITECTURE (60% COMPLETE)</summary><div class='folder'>" 
        h += "<details><summary>?? perception/vision_slam</summary><div class='folder'><details><summary>?? feature_tracker.py</summary><div class='code-view'>import cv2\\n# Algoritmo ORB para odometria visual\\norb = cv2.ORB_create(nfeatures=1500)\\ndef track_points(prev_img, curr_img):\\n    kp1, des1 = orb.detectAndCompute(prev_img, None)\\n    kp2, des2 = orb.detectAndCompute(curr_img, None)\\n    # Matcher por Hamming para tiempo real en Jetson\\n    return bf_matcher.match(des1, des2)</div></details></div></details>" 
        h += "<details><summary>?? navigation/swarm_logic</summary><div class='folder'><details><summary>?? mesh_sync.cpp</summary><div class='code-view'>#include ^SwarmProtocol.h^\\n// Sincronizacion de malla para vuelo cooperativo\\nvoid update_swarm_pos(DroneID id, Vector3 pos) {\\n    m_peer_positions[id] = pos;\\n    adjust_collision_avoidance_vectors();\\n}</div></details></div></details>" 
        h += "<details><summary>?? safety/redundancy</summary><div class='folder'><details><summary>?? health_monitor.py</summary><div class='code-view'>class HealthCheck:\\n    def __init__(self):\\n        self.imu_variance = 0.0\\n    def validate_sensors(self, imu1, imu2):\\n        if abs(imu1.accel - imu2.accel) > THRESHOLD:\\n            self.trigger_sensor_failover()</div></details></div></details>" 
        h += "<details><summary>?? core/os_layer</summary><div class='folder'><details><summary>?? rtos_tasks.c</summary><div class='code-view'>void vTaskFlightControl(void *pvParameters) {\\n    for(;;) {\\n        run_pid_loop();\\n        vTaskDelay(pdMS_TO_TICKS(2)); // Loop de 500Hz\\n    }\\n}</div></details></div></details>" 
        h += "</div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: FULL INDUSTRIAL BOM</summary><div class='folder'>" 
        h += "<table><tr><th>SUBSISTEMA</th><th>COMPONENTE</th><th>INTERFAZ CRITICA</th></tr>" 
        h += "<tr><td>PROCESADOR IA</td><td>NVIDIA Jetson AGX Orin</td><td>NVLink / PCIe Gen4</td></tr>" 
        h += "<tr><td>AVIONICA</td><td>Cube Orange+ Triple Redundant</td><td>Dual CAN Bus</td></tr>" 
        h += "<tr><td>SENSORES</td><td>Lidar Ouster OS1 (128 canales)</td><td>Gigabit Ethernet (GMSL2)</td></tr>" 
        h += "<tr><td>LINK DEFENSA</td><td>Persistent Systems MPU5</td><td>Malla Wave Relay</td></tr></table></div></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: MATRIZ DE ANALISIS TêCNICO</summary><div class='folder'>" 
        h += "<table><tr><td><b>FISICA</b></td><td>MTOW: Dinamico. Centro de masa autocalibrado mediante telemetria.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>Ataques de suplantacion GPS (Mitigacion: Odometria Visual activa).</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>Chasis con aislamiento galvanico y jaula de Faraday interna.</td></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>Certificable bajo estandares DO-178C (Software Aeronautico).</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR DE PROYECTO</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
