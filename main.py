# -*- coding: utf-8 -*- 
import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    res = None 
    if request.method == 'POST' and 'drone_idea' in request.form: 
        res = "active" 
    h = "<html><head><title>MAIA II - SOFTWARE ARCHITECTURE</title><style>" 
    h += "body{background:#0a0a0a; color:#0ff; font-family: 'Courier New', monospace; padding:20px;}" 
    h += ".panel{border:1px solid #0ff; padding:20px; background:#001111; margin-bottom:20px;}" 
    h += ".tree-container{background:#050505; border-left: 2px solid #f0f; padding:10px 20px;}" 
    h += "details{margin:5px 0;}" 
    h += "summary{cursor:pointer; color:#ffff00; font-weight:bold; list-style:none; padding:5px; border-bottom:1px solid #222;}" 
    h += "summary:hover{background:#003333;}" 
    h += "summary::before{content: '?? ';}" 
    h += ".file{color:#0f0; margin-left:25px; padding:3px; display:block; text-decoration:none; font-size:0.9em;}" 
    h += ".file::before{content: '?? ';}" 
    h += ".code-window{background:#000; color:#0f0; padding:20px; border:1px solid #333; border-left:5px solid #f0f; height:600px; overflow-y:scroll; overflow-x:hidden; white-space:pre; line-height:1.6; margin-top:10px; width:100%;}" 
    h += "h2{border-bottom:2px solid #f0f; display:inline-block; padding-bottom:5px;}" 
    h += "</style></head><body>" 
    h += "<h1>[ M.A.I.A. II - ARQUITECTURA DE SOFTWARE ]</h1>" 
    h += "<div class='panel'><h2>SISTEMA DE ARCHIVOS (14 NODOS)</h2>" 
    h += "<div class='tree-container'>" 
    h += "<details><summary>01_CORE_RTOS</summary><a class='file'>os_kernel.c</a><a class='file'>tasks_priority.h</a></details>" 
    h += "<details><summary>02_CONTROL_ATTITUDE</summary><a class='file'>mahony_filter.py</a><a class='file'>pid_controller.cpp</a></details>" 
    h += "<details><summary>03_NAVIGATION_ASTAR</summary><a class='file'>voxel_grid.cpp</a><a class='file'>path_optimizer.py</a></details>" 
    h += "<details><summary>04_PERCEPTION_THERMAL</summary><a class='file'>radiometric_proc.py</a><a class='file'>target_tracking.py</a></details>" 
    h += "<details><summary>05_PERCEPTION_LIDAR</summary><a class='file'>ouster_driver.py</a><a class='file'>point_cloud_filter.cpp</a></details>" 
    h += "<details><summary>06_TELEMETRY_MAVLINK</summary><a class='file'>mavlink_v2_encoder.py</a><a class='file'>status_packets.h</a></details>" 
    h += "<details><summary>07_POWER_BMS</summary><a class='file'>can_bms_driver.cpp</a><a class='file'>energy_management.py</a></details>" 
    h += "<details><summary>08_COMM_SILVUS</summary><a class='file'>mesh_network.py</a><a class='file'>encryption_aes256.c</a></details>" 
    h += "<details><summary>09_DIAGNOSTICS_HEALTH</summary><a class='file'>system_monitor.py</a><a class='file'>failsafe_logic.cpp</a></details>" 
    h += "<details><summary>10_SIMULATION_SITL</summary><a class='file'>gazebo_bridge.py</a><a class='file'>physics_model.py</a></details>" 
    h += "<details><summary>11_MISSION_PLANNER</summary><a class='file'>waypoint_manager.py</a><a class='file'>geofencing.cpp</a></details>" 
    h += "<details><summary>12_HARDWARE_HAL</summary><a class='file'>gpio_map.h</a><a class='file'>i2c_bus_config.c</a></details>" 
    h += "<details><summary>13_AI_INFERENCE</summary><a class='file'>tensorrt_engine.py</a><a class='file'>object_detection.py</a></details>" 
    h += "<details><summary>14_FILESYSTEM_LOGS</summary><a class='file'>blackbox_logger.c</a><a class='file'>data_sync.py</a></details>" 
    h += "</div></div>" 
    h += "<div class='panel'><h2>EDITOR DE C‡DIGO VERTICAL</h2>" 
    h += "<div class='code-window'>" 
    h += "// ARCHIVO: control/mahony_filter.py\\n// DESCRIPCI‡N: Fusi¢n sensorial para estimaci¢n de actitud.\\n\\nimport numpy as np\\n\\nclass MahonyIMU:\\n    def __init__(self, Kp=2.0, Ki=0.005, freq=400):\\n        self.q = np.array([1.0, 0.0, 0.0, 0.0])\\n        self.e_int = np.zeros(3)\\n        self.dt = 1.0 / freq\\n\\n    def update(self, gyro, acc):\\n        # 1. Normalizar aceler¢metro\\n        a_norm = np.linalg.norm(acc)\\n        if a_norm < 0.01: return\\n        acc /= a_norm\\n\\n        # 2. Estimar direcci¢n de gravedad basada en cuaterni¢n actual\\n        v = np.array([\\n            2*(self.q[1]*self.q[3] - self.q[0]*self.q[2]),\\n            2*(self.q[0]*self.q[1] + self.q[2]*self.q[3]),\\n            self.q[0]**2 - self.q[1]**2 - self.q[2]**2 + self.q[3]**2\\n        ])\\n\\n        # 3. Error: producto vectorial entre aceleraci¢n medida y estimada\\n        error = np.cross(acc, v)\\n\\n        # 4. TÇrmino Integral\\n        self.e_int += error * self.dt\\n\\n        # 5. Correcci¢n de Velocidad Angular\\n        gyro_corr = gyro + 2.0 * error + 0.005 * self.e_int\\n\\n        # 6. Integraci¢n de Cuaterni¢n (Regla de la mano derecha)\\n        q_dot = 0.5 * self.q_multiply(self.q, [0, *gyro_corr])\\n        self.q = self.q + q_dot * self.dt\\n        self.q /= np.linalg.norm(self.q)\\n\\n    def q_multiply(self, q, p):\\n        w1, x1, y1, z1 = q\\n        w2, x2, y2, z2 = p\\n        return np.array([\\n            w1*w2 - x1*x2 - y1*y2 - z1*z2,\\n            w1*x2 + x1*w2 + y1*z2 - z1*y2,\\n            w1*y2 - x1*z2 + y1*w2 + z1*x2,\\n            w1*z2 + x1*y2 - y1*x2 + z1*w2\\n        ])\\n\\n// --- FIN DEL M‡DULO ---</div></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
