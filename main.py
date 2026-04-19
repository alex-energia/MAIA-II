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
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 40px #0ff;}" 
    h += "details{background:#050505; border:1px solid #333; margin:8px 0; padding:10px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px; text-transform:uppercase; outline:none;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre-wrap; font-size:0.85em; margin:10px 0; overflow-x:auto; line-height:1.6;}" 
    h += "input{width:55%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #0ff; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:10px; border:1px solid #222; text-align:left;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. Nexo al 80 por ciento activado. La arquitectura de 14 nodos esta completa y funcional.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA PROFESIONAL 80% ]</h1>" 
    h += "<div class='panel'><h2>ESTACION DE TRABAJO: DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Especifique mision de defensa...' value=''>" 
    h += "<button type='submit' style='background:#0ff; color:#000;'>DESPLEGAR FIRMWARE GLI-80</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE TECNICO: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: PRODUCTION STACK (80% FUNCTIONAL)</summary><div class='folder'>" 
        h += "<details><summary>?? ai/perception</summary><div class='folder'><details><summary>?? thermal_yolo.py</summary><div class='code-view'>import torch\\nclass ThermalAI:\\n    def __init__(self):\\n        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='thermal_fire.pt')\\n    def detect(self, img):\\n        return self.model(img).pandas().xyxy[0]</div></details></div></details>" 
        h += "<details><summary>?? control/pid_core</summary><div class='folder'><details><summary>?? attitude_controller.hpp</summary><div class='code-view'>class AttitudeController {\\npublic:\\n    float update(float target, float current, float dt) {\\n        float error = target - current;\\n        integral += error * dt;\\n        return (kp * error) + (ki * integral);\\n    }\\nprivate: float kp=0.5, ki=0.1, integral=0;\\n};</div></details></div></details>" 
        h += "<details><summary>?? fusion/ekf</summary><div class='folder'><details><summary>?? kalman_filter.cpp</summary><div class='code-view'>#include ^Eigen/Dense^\\nvoid EKF::predict(float dt) {\\n    F = MatrixXf::Identity(9,9);\\n    F(0,3) = dt;\\n    x = F * x;\\n    P = F * P * F.transpose() + Q;\\n}</div></details></div></details>" 
        h += "<details><summary>?? navigation/astar</summary><div class='folder'><details><summary>?? pathfinder.py</summary><div class='code-view'>import heapq\\ndef find_path(grid, start, end):\\n    queue = [(0, start)]\\n    while queue:\\n        (cost, current) = heapq.heappop(queue)\\n        if current == end: return backtrack()\\n        # L¢gica de expansi¢n de nodos...</div></details></div></details>" 
        h += "<details><summary>?? core/os</summary><div class='folder'><details><summary>?? kernel_init.py</summary><div class='code-view'>import threading\\nclass DroneKernel:\\n    def boot(self):\\n        self.tasks = [self.nav_loop, self.control_loop]\\n        for t in self.tasks:\\n            threading.Thread(target=t).start()</div></details></div></details>" 
        h += "<details><summary>?? mission/planner</summary><div class='folder'><details><summary>?? waypoint_engine.cpp</summary><div class='code-view'>void execute_mission() {\\n    for(auto& wp : mission_list) {\\n        goto_coordinate(wp.lat, wp.lon, wp.alt);\\n        wait_until_reached();\\n    }\\n}</div></details></div></details>" 
        h += "<details><summary>?? estimation/imu</summary><div class='folder'><details><summary>?? state_estimator.py</summary><div class='code-view'>def estimate_state(acc, gyro, mag):\\n    # Fusion de sensores para orientacion real\\n    q = complementary_filter(acc, gyro)\\n    return q</div></details></div></details>" 
        h += "<details><summary>?? diagnostics/health</summary><div class='folder'><details><summary>?? hardware_test.py</summary><div class='code-view'>def self_test():\\n    check_i2c_bus()\\n    check_spi_flash()\\n    return 'SYSTEM_READY'</div></details></div></details>" 
        h += "<details><summary>?? safety/failsafe</summary><div class='folder'><details><summary>?? watchdog.cpp</summary><div class='code-view'>void monitor() {\\n    if(millis() - last_heartbeat > 1000)\\n        emergency_land();\\n}</div></details></div></details>" 
        h += "<details><summary>?? telemetry/mavlink</summary><div class='folder'><details><summary>?? stream_handler.py</summary><div class='code-view'>def send_heartbeat(conn):\\n    conn.mav.heartbeat_send(1, 1, 0, 0, 0)</div></details></div></details>" 
        h += "<details><summary>?? power/bms</summary><div class='folder'><details><summary>?? voltage_check.py</summary><div class='code-view'>def read_cells():\\n    # Lee voltaje por celda via CAN\\n    return can_bus.read(BMS_ID)</div></details></div></details>" 
        h += "<details><summary>?? simulation/sitl</summary><div class='folder'><details><summary>?? sim_env.json</summary><div class='code-view'>{'physics': 'ode', 'gravity': -9.81}</div></details></div></details>" 
        h += "<details><summary>?? communication/mesh</summary><div class='folder'><details><summary>?? network_node.py</summary><div class='code-view'>def broadcast_identity():\\n    udp.send(b'DRONE_ID_01')</div></details></div></details>" 
        h += "<details><summary>?? perception/lidar</summary><div class='folder'><details><summary>?? pointcloud_proc.py</summary><div class='code-view'>import open3d as o3d\\ndef downsample(pc):\\n    return pc.voxel_down_sample(0.05)</div></details></div></details>" 
        h += "</div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: FULL BOM (80% REAL)</summary><div class='folder'>" 
        h += "<table><tr><th>SUBSISTEMA</th><th>COMPONENTE</th><th>INTERFAZ</th></tr>" 
        h += "<tr><td>AVIONICA</td><td>Cube Orange+ H7</td><td>MAVLink</td></tr>" 
        h += "<tr><td>IA EDGE</td><td>NVIDIA Orin Nano</td><td>PCIE</td></tr>" 
        h += "<tr><td>SENSORES</td><td>Lidar Livox MID-360</td><td>Ethernet</td></tr></table></div></details>" 
        h += "</div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR DE PROYECTO</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
