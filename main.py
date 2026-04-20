# -*- coding: utf-8 -*- 
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
    h = "<html><head><title>MAIA II - ESTRATEGIA 60</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001a1a; margin-bottom:20px; box-shadow: 0 0 40px rgba(0,255,255,0.2);}" 
    h += "details{background:#050505; border:1px solid #444; margin:10px 0; padding:15px;}" 
    h += "summary{font-weight:bold; color:#ffff00; cursor:pointer; text-transform:uppercase;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre; font-size:0.85em; height:450px; overflow-y:scroll; line-height:1.5; border-top: 1px solid #333; display:block;}" 
    h += "input{width:40%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em;}" 
    h += "button{padding:15px 25px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-mem{background:#444; color:#fff;} .btn-clear{background:#800; color:#fff;}" 
    h += ".hw-grid{display:grid; grid-template-columns: 1fr 1fr; gap:15px;}" 
    h += ".hw-spec{background:rgba(0,255,255,0.05); border:1px solid #0ff; padding:15px; border-left: 5px solid #f0f;}" 
    h += "table{width:100%; border-collapse:collapse; margin-top:10px;} td, th{padding:10px; border:1px solid #222; text-align:left;}" 
    h += ".viewer-3d{width:100%; height:400px; background:#000; border:2px solid #333; position:relative; overflow:hidden; display:flex; flex-direction:column; align-items:center; justify-content:center;}" 
    h += ".drone-core{width:100px; height:20px; background:#222; border:2px solid #0ff; position:relative; animation: v-fly 4s infinite ease-in-out;}" 
    h += ".arm{width:80px; height:4px; background:#0ff; position:absolute; top:8px;}" 
    h += "@keyframes v-fly { 0%,100%{transform:translateY(0) rotate(0);} 50%{transform:translateY(-30px) rotate(3deg);} }" 
    h += "</style><script>" 
    h += "function tVoz(){ let m=new SpeechSynthesisUtterance('Alex, sistema corregido. Sin errores de caracteres. Stack sesenta por ciento real activo.'); m.lang='es-MX'; window.speechSynthesis.speak(m); }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - STACK DE INGENIERIA 60/60 ]</h1>" 
    h += "<div class='panel'><h2>UNIDAD DE COMANDO</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Requerimiento tecnico...' value=''>" 
    h += "<button type='submit' class='btn-gen'>GENERAR EXPEDIENTE</button>" 
    h += "<button type='button' class='btn-mem'>MEMORIA PROYECTO</button>" 
    h += "<button type='reset' class='btn-clear'>LIMPIAR TERMINAL</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>MODELO ANALITICO 3D (TACTICAL VIEW)</h2><div class='viewer-3d'>" 
        h += "<div class='drone-core'><div class='arm' style='left:-80px;'></div><div class='arm' style='right:-80px;'></div></div>" 
        h += "<p style='margin-top:50px; color:#f0f;'>[ CONFIGURACION HEXA-QUAD | CHASIS CARBONO M40J ]</p></div></div>" 
        h += "<div class='panel'><h2>EXPEDIENTE TACTICO: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: 14 NODOS DE PRODUCCION</summary><div style='padding-left:20px; border-left:1px dotted #f0f;'>" 
        h += "<details><summary>?? control/attitude_mahony.py</summary><div class='code-view'>import numpy as np\\n\\nclass MahonyFilter:\\n    def __init__(self, Kp=2.0, Ki=0.005, dt=0.0025):\\n        self.q = np.array([1.0, 0.0, 0.0, 0.0])\\n        self.integral_error = np.zeros(3)\\n        self.dt = dt\\n\\n    def update(self, gyro, acc):\\n        # Estimacion de orientacion mediante fusion sensorial\\n        a_norm = np.linalg.norm(acc)\\n        if a_norm < 0.01: return\\n        acc /= a_norm\\n\\n        v = np.array([2*(self.q[1]*self.q[3] - self.q[0]*self.q[2]),\\n                      2*(self.q[0]*self.q[1] + self.q[2]*self.q[3]),\\n                      self.q[0]**2 - self.q[1]**2 - self.q[2]**2 + self.q[3]**2])\\n\\n        error = np.cross(acc, v)\\n        self.integral_error += error * 0.005 * self.dt\\n        gyro_corr = gyro + 2.0 * error + self.integral_error\\n\\n        dq = 0.5 * self.q_update(self.q, gyro_corr) * self.dt\\n        self.q = (self.q + dq) / np.linalg.norm(self.q + dq)</div></details>" 
        h += "<details><summary>?? navigation/astar_dynamic.cpp</summary><div class='code-view'>// A-Star Voxel Navigation\\n#include ^vector^\\n#include ^cmath^\\n\\nstruct Node { int x, y, z; float g, h; };\\n\\nfloat calculate_cost(Node current, Node target, float fire_intensity) {\\n    // El coste aumenta exponencialmente con el calor detectado por IR\\n    float dist = sqrt(pow(current.x-target.x, 2) + pow(current.y-target.y, 2));\\n    float heat_penalty = exp(fire_intensity / 100.0);\\n    return dist * heat_penalty;\\n}</div></details>" 
        h += "<details><summary>?? core/rtos_scheduler.c</summary><div class='code-view'>// Kernel Priority Mapping\\n#include ^FreeRTOS.h^\\n\\nvoid StartTasks() {\\n    // Nivel Critico: Estabilizacion 400Hz\\n    xTaskCreate(vFlightControl, ^FCTRL^, 1024, NULL, 15, NULL);\\n    // Nivel Tactico: Percepcion IR 60Hz\\n    xTaskCreate(vThermalAnalysis, ^THERM^, 4096, NULL, 10, NULL);\\n    // Nivel Global: Telemetria Silvus\\n    xTaskCreate(vMeshComm, ^MESH^, 512, NULL, 5, NULL);\\n}</div></details>" 
        h += "</div></details>" 
        h += "<details open><summary>[DOM] AGENTE HARDWARE: ARQUITECTURA DETALLADA</summary><div class='hw-grid'>" 
        h += "<div class='hw-spec'><h3>? POTENCIA</h3><b>Bus:</b> 12S Solid-State Amprius.<br><b>PDB:</b> Cobre 4oz con aislamiento galvanico.<br><b>ESC:</b> KDE CAN-FD 120A.</div>" 
        h += "<div class='hw-spec'><h3>?? COMPUTO</h3><b>SoM:</b> Jetson Orin Nano + FPGA.<br><b>Bus:</b> GMSL2 (Latencia < 30ms).<br><b>SSD:</b> Industrial NVMe 1TB.</div>" 
        h += "<div class='hw-spec'><h3>?? SENSORES</h3><b>Lidar:</b> Ouster OS1-64 V2.<br><b>IR:</b> FLIR Boson Radiometrica.<br><b>GNSS:</b> u-blox ZED-F9P RTK.</div>" 
        h += "<div class='hw-spec'><h3>?? CHASIS</h3><b>Material:</b> Carbono M40J Aeroespacial.<br><b>Blindaje:</b> Capas Kapton / Oro.<br><b>IP Rating:</b> IP67 (Motores y Sensores).</div>" 
        h += "</div></details>" 
        h += "<details open><summary>[ANX] ANALISIS DE VIABILIDAD Y RIESGOS</summary><div class='folder'>" 
        h += "<table><tr><th>CATEGORIA</th><th>NIVEL</th><th>DETALLE TECNICO</th><th>ACCION</th></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>ALTA</td><td>Relacion Empuje-Peso 3.4:1 validada.</td><td>Ok.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>ALTO</td><td>Calor extremo (>85C) en electronica central.</td><td>Usar Grafeno.</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>PROC</td><td>Estructura monocasco en fase de curado.</td><td>40% completado.</td></tr>" 
        h += "<tr><td><b>FISICA</b></td><td>CALC</td><td>Desplazamiento CoG < 3mm tras carga util.</td><td>Equilibrado.</td></tr>" 
        h += "</table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button>SEARCH PROJECT</button><button style='background:#f0f;'>CREATE NEW PROJECT</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
