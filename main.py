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
    h += "details{background:#050505; border:1px solid #333; margin:8px 0; padding:12px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre; font-size:0.82em; margin:10px 0; overflow-x:auto; line-height:1.4; font-weight:bold;}" 
    h += "input{width:55%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em;}" 
    h += "button{padding:15px 22px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".folder{margin-left:25px; border-left:1px dashed #0ff; padding-left:15px;}" 
    h += "table{width:100%; border-collapse:collapse; margin-top:10px;} td, th{padding:12px; border:1px solid #222; text-align:left;}" 
    h += "</style><script>" 
    h += "let v=false; function tVoz(){ let b=document.getElementById('btnVoz'); if(!v){ b.style.background='green'; v=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex. Maia elevando realismo al ochenta por ciento. Desplegando firmware de grado aeroespacial y analisis de hardware.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; v=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; v=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA PROFESIONAL 80% ]</h1>" 
    h += "<div class='panel'><h2>ESTACION DE TRABAJO: DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Especifique mision...' value=''>" 
    h += "<button type='submit' style='background:#0ff; color:#000;'>GENERAR ARQUITECTURA GLI-80</button>" 
    h += "<button type='button' style='background:#555; color:#fff;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>EXPEDIENTE: " + idea + "</h2>" 
        h += "<details open><summary>[+] AGENTE 3D: ESTRUCTURA FISICA</summary><div class='folder'><pre style='color:#fff;'>" 
        h += "      [M1]  (CCW)      [M2] (CW)\\n          \\\\            /\\n           \\\\__________/\\n           |          |\\n     [LIDAR]--[CORE]--[BMS]\\n           |__________|\\n          /            \\\\\\n         /              \\\\\\n      [M4] (CW)        [M3] (CCW)\\n\\nMATERIAL: Monocasco Fibra de Carbono 4K Toray + Titanio Grado 5</pre></div></details>" 
        h += "<details><summary>[DIR] AGENTE SOFTWARE: PRODUCTION KERNEL</summary><div class='folder'>" 
        h += "<details><summary>?? ai/perception</summary><div class='folder'><details><summary>?? thermal_inference.py</summary><div class='code-view'>import torch\\nimport cv2\\nclass ThermalDetector:\\n    def __init__(self, model_path):\\n        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\\n        self.model = torch.jit.load(model_path).to(self.device).eval()\\n    @torch.no_grad()\\n    def process_frame(self, frame):\\n        tensor = torch.from_numpy(frame).permute(2,0,1).unsqueeze(0).float() / 255.0\\n        prediction = self.model(tensor.to(self.device))\\n        return self.non_max_suppression(prediction)</div></details></div></details>" 
        h += "<details><summary>?? fusion/ekf_core</summary><div class='folder'><details><summary>?? kalman_filter.cpp</summary><div class='code-view'>#include ^Eigen/Dense^\\nusing namespace Eigen;\\nvoid EKF::update(const VectorXd& z) {\\n    MatrixXd H = get_measurement_jacobian();\\n    MatrixXd S = H * P * H.transpose() + R;\\n    MatrixXd K = P * H.transpose() * S.inverse();\\n    x = x + K * (z - H * x);\\n    P = (MatrixXd::Identity(9,9) - K * H) * P;\\n}</div></details></div></details>" 
        h += "<details><summary>?? control/low_level</summary><div class='folder'><details><summary>?? motor_driver.c</summary><div class='code-view'>#include ^stm32h7xx.h^\\nvoid set_esc_pulse(uint8_t ch, float throttle) {\\n    uint32_t compare_val = 1000 + (uint32_t)(throttle * 1000);\\n    switch(ch) {\\n        case 1: TIM1->CCR1 = compare_val; break;\\n        case 2: TIM1->CCR2 = compare_val; break;\\n        default: log_error('Invalid CH');\\n    }\\n}</div></details></div></details>" 
        h += "<details><summary>?? navigation/astar</summary><div class='folder'><details><summary>?? path_manager.py</summary><div class='code-view'>import heapq\\nclass AStar:\\n    def solve(self, start, goal, grid):\\n        open_list = []\\n        heapq.heappush(open_list, (0, start))\\n        came_from = {start: None}\\n        while open_list:\\n            current = heapq.heappop(open_list)[1]\\n            if current == goal: break\\n            for neighbor in grid.get_neighbors(current):\\n                # Logica de costo heuristico Euclidiano</div></details></div></details>" 
        h += "<details><summary>?? safety/redundancy</summary><div class='folder'><details><summary>?? watchdog.cpp</summary><div class='code-view'>void monitor_vitals() {\\n    if(imu_divergence() > 0.05f) {\\n        switch_to_secondary_imu();\\n        trigger_warning('IMU_FAILOVER');\\n    }\\n    if(get_battery_pct() < 15.0f) start_rtl();\\n}</div></details></div></details>" 
        h += "</div></details>" 
        h += "<details><summary>[DIR] AGENTE HARDWARE: BOM & DOM INDUSTRIAL</summary><div class='folder'><table><tr><th>SISTEMA</th><th>COMPONENTE</th><th>INTERFAZ</th></tr>" 
        h += "<tr><td>AVIONICA</td><td>Orange Cube+ (STM32H7)</td><td>Dual CAN Bus</td></tr>" 
        h += "<tr><td>IA EDGE</td><td>NVIDIA Jetson Orin 64GB</td><td>GMSL2 / PCIe</td></tr>" 
        h += "<tr><td>POD TERMICO</td><td>FLIR Boson 640</td><td>USB-C / MIPI</td></tr></table></div></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: ANALISIS DE SISTEMAS</summary><div class='folder'><table>" 
        h += "<tr><td><b>FISICA</b></td><td>MTOW 19.5kg. Empuje max 48kg. Relacion 2.4:1.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>Interferencia RF en entornos urbanos densos. Mitigacion: FHSS.</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>Tornilleria Titanio Torx T10 con Loctite 243.</td></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>TRL-8: Listo para pruebas en entorno operativo.</td></tr></table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='border:1px solid #f0f; background:transparent; color:#f0f;'>BUSCADOR DE PROYECTO</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
