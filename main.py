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
    h = "<html><head><title>MAIA II GLI-60/40</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 30px #0ff;}" 
    h += "details{background:#020202; border:1px solid #333; margin:8px 0; padding:12px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre-wrap; font-size:0.82em; line-height:1.4;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #f0f; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse; margin:10px 0;} td, th{padding:10px; border:1px solid #222; text-align:left;}" 
    h += "th{background:#003333; color:yellow;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Alex, elevando realismo. Software al sesenta y hardware al cuarenta por ciento. Arquitectura lista para inversion.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - SISTEMA INTEGRADO 60/40 ]</h1>" 
    h += "<div class='panel'><h2>ESTACION DE TRABAJO</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Requerimiento tecnico...' value=''>" 
    h += "<button type='submit' style='background:#0ff; color:#000;'>GENERAR EXPEDIENTE</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: PRODUCTION STACK (60% REAL)</summary><div class='folder'>" 
        h += "<details><summary>?? fusion/ekf_core</summary><div class='folder'><details><summary>?? kalman_filter.cpp</summary><div class='code-view'>#include ^Eigen/Dense^\\nvoid EKF::predict(const VectorXd& u, float dt) {\\n  // Prediccion de estado no lineal\\n  x = transition_model(x, u, dt);\\n  MatrixXd F = compute_jacobian_f(x, u, dt);\\n  P = F * P * F.transpose() + Q;\\n  // Normalizacion de Cuaterniones\\n  x.segment(6, 4).normalize();\\n}</div></details></div></details>" 
        h += "<details><summary>?? control/low_level</summary><div class='folder'><details><summary>?? motor_driver.c</summary><div class='code-view'>#include ^stm32h7xx_hal.h^\\nvoid set_motor_speed(uint16_t esc_id, float throttle) {\\n  uint32_t pulse = (uint32_t)(1000 + (throttle * 1000));\\n  __HAL_TIM_SET_COMPARE(&htim1, esc_id, pulse);\\n  // Telemetria DSHOT600 opcional\\n  if(use_dshot) send_dshot_frame(esc_id, pulse);\\n}</div></details></div></details>" 
        h += "<details><summary>?? navigation/astar</summary><div class='folder'><details><summary>?? pathfinder.py</summary><div class='code-view'>import heapq\\nclass PathPlanner:\\n  def __init__(self, octomap_res):\\n    self.res = octomap_res\\n  def compute(self, start, goal):\\n    neighbors = self.get_valid_voxels(current)\\n    # Costo = Distancia + Riesgo Proximidad\\n    f_score = g_score + self.heuristic(neighbor, goal)\\n    heapq.heappush(self.open_set, (f_score, neighbor))</div></details></div></details>" 
        h += "<details><summary>?? safety/redundancy</summary><div class='folder'><details><summary>?? watchdog.cpp</summary><div class='code-view'>void check_system_integrity() {\\n  if(get_cpu_load() > 90.0) kill_non_critical_tasks();\\n  if(check_vibration_levels() > 2.5g) emergency_hover();\\n  // Verificacion de IMU triple redundante\\n  if(imu_primary_fail()) switch_to_imu(IMU_SECONDARY);\\n}</div></details></div></details>" 
        h += "<details><summary>?? communication/mesh</summary><div class='folder'><details><summary>?? mesh_node.py</summary><div class='code-view'>import asyncio\\nasync def mesh_heartbeat():\\n  while True:\\n    msg = {'id': DRONE_ID, 'pos': current_gps, 'status': 'ALIVE'}\\n    await broadcast_udp(msg, port=5005)\\n    await asyncio.sleep(0.1) # 10Hz Swarm Sync</div></details></div></details>" 
        h += "</div></details>" 
        h += "<details open><summary>[DIR] AGENTE HARDWARE: BOM & DOM (40% REAL)</summary><div class='folder'><table>" 
        h += "<tr><th>MODULO</th><th>ESPECIFICACION TECNICA</th><th>INTERFAZ / POTENCIA</th></tr>" 
        h += "<tr><td><b>PROCESAMIENTO</b></td><td>NVIDIA AGX Orin (275 TOPS, 64GB LPDDR5)</td><td>2x GMSL2 Camera / 60W Max</td></tr>" 
        h += "<tr><td><b>PROPULSION</b></td><td>T-Motor U15 II (KV80) + ESC Flame 180A</td><td>12S LiPo / 48V Nominal</td></tr>" 
        h += "<tr><td><b>ESTRUCTURA</b></td><td>Monocasco Fibra de Carbono 4K + Resina Epoxy</td><td>Resistencia: 15G Impacto</td></tr>" 
        h += "<tr><td><b>ENERGIA</b></td><td>Smart BMS 12S 200A (Protocolo SMBus/CAN)</td><td>Celdas Solid-State 350Wh/kg</td></tr>" 
        h += "<tr><td><b>DATALINK</b></td><td>Silvus SC4200 (MIMO 2x2, 20Mbps AES256)</td><td>Ethernet Bridge / 10W RF</td></tr>" 
        h += "</table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button>BUSCADOR</button><button style='background:#f0f;'>CREAR PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
