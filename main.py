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
    h = "<html><head><title>MAIA II 40% Real</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 20px #0ff;}" 
    h += "details{background:#020202; border:1px solid #333; margin:8px 0; padding:12px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre-wrap; font-size:0.82em; line-height:1.5;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #0ff; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse; margin:10px 0;} td, th{padding:10px; border:1px solid #222; text-align:left;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Alex, Maia operando al 40 por ciento de realismo en software. Todos los nodos estan activos.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA 40% ]</h1>" 
    h += "<div class='panel'><h2>CONSTRUCTOR DE MISION</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Concepto de dron...' value=''>" 
    h += "<button type='submit' style='background:#0ff; color:#000;'>DESPLEGAR NODOS</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: PRODUCTION STACK (14 NODOS)</summary><div class='folder'>" 
        h += "<details><summary>?? ai/perception</summary><div class='folder'><details><summary>?? thermal_inference.py</summary><div class='code-view'>import torch\\nclass Detector:\\n  def __init__(self):\\n    self.model = torch.jit.load('thermal.pt').eval()\\n  def infer(self, frame):\\n    return self.model(frame)</div></details></div></details>" 
        h += "<details><summary>?? telemetry/mavlink</summary><div class='folder'><details><summary>?? mavlink_handler.py</summary><div class='code-view'>from pymavlink import mavutil\\ndef send_status(conn):\\n  conn.mav.sys_status_send(500, 500, 500, 0, 14000, -1, 0, 0, 0, 0, 0, 0, 0)</div></details></div></details>" 
        h += "<details><summary>?? power/bms</summary><div class='folder'><details><summary>?? smbus_interface.py</summary><div class='code-view'>import smbus\\ndef read_cell_v(bus_id):\\n  bus = smbus.SMBus(bus_id)\\n  return bus.read_word_data(0x0B, 0x09) / 1000.0</div></details></div></details>" 
        h += "<details><summary>?? core/rtos</summary><div class='folder'><details><summary>?? task_scheduler.c</summary><div class='code-view'>void start_scheduler() {\\n  BaseType_t xReady;\\n  xReady = xTaskCreate(vTaskControl, 'CTRL', 256, NULL, 5, NULL);\\n  vTaskStartScheduler();\\n}</div></details></div></details>" 
        h += "<details><summary>?? simulation/gazebo</summary><div class='folder'><details><summary>?? world_config.json</summary><div class='code-view'>{\\n  'gravity': [0, 0, -9.8],\\n  'magnetic_field': [6e-06, 2.3e-05, -4.2e-05],\\n  'atmosphere': {'type': 'adiabatic'}\\n}</div></details></div></details>" 
        h += "<details><summary>?? perception_lidar</summary><div class='folder'><details><summary>?? pointcloud.py</summary><div class='code-view'>import open3d as o3d\\ndef process_cloud(data):\\n  pcd = o3d.geometry.PointCloud()\\n  pcd.points = o3d.utility.Vector3dVector(data)\\n  return pcd.voxel_down_sample(0.05)</div></details></div></details>" 
        h += "<details><summary>?? diagnostics</summary><div class='folder'><details><summary>?? system_test.py</summary><div class='code-view'>def run_diag():\\n  checks = {'imu': test_imu(), 'gnss': test_gps()}\\n  return all(checks.values())</div></details></div></details>" 
        h += "<details><summary>?? mission</summary><div class='folder'><details><summary>?? mission_ctrl.cpp</summary><div class='code-view'>void execute_step(uint8_t cmd) {\\n  if(cmd == MAV_CMD_NAV_WAYPOINT) navigate_to_wp();\\n  else if(cmd == MAV_CMD_NAV_LAND) auto_land();\\n}</div></details></div></details>" 
        h += "<details><summary>?? estimation</summary><div class='folder'><details><summary>?? state_estimator.py</summary><div class='code-view'>def fuse_state(gps, imu):\\n  # Complementary filter for orientation estimation\\n  return alpha * (prev + imu*dt) + (1-alpha) * gps</div></details></div></details>" 
        h += "<details><summary>?? fusion/ekf_core</summary><div class='folder'>?? kalman_filter.cpp</div></details>" 
        h += "<details><summary>?? control/low_level</summary><div class='folder'>?? motor_driver.c</div></details>" 
        h += "<details><summary>?? navigation/astar</summary><div class='folder'>?? pathfinder.py</div></details>" 
        h += "<details><summary>?? safety/redundancy</summary><div class='folder'>?? watchdog.cpp</div></details>" 
        h += "<details><summary>?? communication/mesh</summary><div class='folder'>?? mesh_node.py</div></details>" 
        h += "</div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: BOM & DOM</summary><div class='folder'><table>" 
        h += "<tr><th>SUBSISTEMA</th><th>COMPONENTE</th><th>PROTOCOLO</th></tr>" 
        h += "<tr><td>AVIONICA</td><td>Cube Orange+ H7</td><td>CAN/UART</td></tr>" 
        h += "<tr><td>PROCESADOR IA</td><td>NVIDIA AGX Orin 64GB</td><td>PCIE Gen4</td></tr>" 
        h += "<tr><td>RADIO LINK</td><td>Silvus StreamCaster 4200</td><td>Mesh UDP</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='border:1px solid #f0f; background:transparent; color:#f0f;'>BUSCADOR</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
