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
    h = "<html><head><title>MAIA II GLI-80</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 35px #0ff;}" 
    h += "details{background:#050505; border:1px solid #333; margin:5px 0; padding:10px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre-wrap; font-size:0.85em; margin:10px 0; overflow-x:auto; line-height:1.6;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #0ff; padding-left:15px;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex. Maia operando al ochenta por ciento. Arquitectura de catorce nodos desplegada.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA PROFESIONAL 80% ]</h1>" 
    h += "<div class='panel'><h2>ESTACION DE TRABAJO: DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Requerimiento tecnico...' value=''>" 
    h += "<button type='submit' style='background:#0ff; color:#000;'>GENERAR FIRMWARE GLI-80</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: PRODUCTION STACK (80% FUNCTIONAL)</summary><div class='folder'>" 
        h += "<details><summary>?? ai</summary><div class='folder'><details><summary>?? perception.py</summary><div class='code-view'>import torch\\nclass ThermalAI:\\n    def __init__(self):\\n        self.model = torch.jit.load('model.pt')\\n    def detect(self, img):\\n        return self.model(img)</div></details></div></details>" 
        h += "<details><summary>?? comm</summary><div class='folder'><details><summary>?? radio_protocol.cpp</summary><div class='code-view'>void transmit() {\\n    uint16_t crc = calc_crc(buffer);\\n    Serial.write(buffer, len);\\n    Serial.write(crc);\\n}</div></details></div></details>" 
        h += "<details><summary>?? control</summary><div class='folder'><details><summary>?? pid_core.hpp</summary><div class='code-view'>template ^typename T^ class PID {\\n    T update(T error, float dt) {\\n        integral += error * dt;\\n        return (kp*error) + (ki*integral);\\n    }\\n};</div></details></div></details>" 
        h += "<details><summary>?? navigation</summary><div class='folder'><details><summary>?? astar.py</summary><div class='code-view'>import heapq\\ndef search(grid, start, goal):\\n    queue = [(0, start)]\\n    while queue:\\n        cost, node = heapq.heappop(queue)\\n        if node == goal: return True</div></details></div></details>" 
        h += "<details><summary>?? power</summary><div class='folder'><details><summary>?? bms_comm.py</summary><div class='code-view'>def read_bms():\\n    data = i2c.read(0x42, 16)\\n    return {'v': data[0], 'i': data[1]}</div></details></div></details>" 
        h += "<details><summary>?? safety</summary><div class='folder'><details><summary>?? failsafe.cpp</summary><div class='code-view'>void check_health() {\\n    if (link_lost()) trigger(RTL);\\n    if (low_bat()) trigger(LAND);\\n}</div></details></div></details>" 
        h += "<details><summary>?? telemetry</summary><div class='folder'><details><summary>?? mavlink.py</summary><div class='code-view'>from pymavlink import mavutil\\ndef heartbeat(c):\\n    c.mav.heartbeat_send(1, 1, 0, 0, 0)</div></details></div></details>" 
        h += "<details><summary>?? simulation</summary><div class='folder'><details><summary>?? gazebo_conf.json</summary><div class='code-view'>{'world': 'forest', 'physics': 'ode', 'step': 0.001}</div></details></div></details>" 
        h += "<details><summary>?? core</summary><div class='folder'><details><summary>?? kernel.py</summary><div class='code-view'>import threading\\ndef start_kernel():\\n    threading.Thread(target=control_loop).start()</div></details></div></details>" 
        h += "<details><summary>?? mission</summary><div class='folder'><details><summary>?? planner.cpp</summary><div class='code-view'>void run_mission() {\\n    for(auto& wp : list) goto(wp);\\n}</div></details></div></details>" 
        h += "<details><summary>?? perception_lidar</summary><div class='folder'><details><summary>?? lidar_proc.py</summary><div class='code-view'>def filter_cloud(pc):\\n    return pc.remove_outliers()</div></details></div></details>" 
        h += "<details><summary>?? diagnostics</summary><div class='folder'><details><summary>?? hw_test.py</summary><div class='code-view'>def self_test():\\n    return 'OK' if bus_check() else 'ERR'</div></details></div></details>" 
        h += "<details><summary>?? fusion</summary><div class='folder'><details><summary>?? kalman.cpp</summary><div class='code-view'>void predict() {\\n    x = F * x;\\n    P = F * P * Ft + Q;\\n}</div></details></div></details>" 
        h += "<details><summary>?? estimation</summary><div class='folder'><details><summary>?? state.py</summary><div class='code-view'>def get_state(imu, gps):\\n    return fuse_sensors(imu, gps)</div></details></div></details>" 
        h += "</div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button>BUSCADOR</button><button style='background:#f0f;'>CREAR PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
