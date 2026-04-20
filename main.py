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
    h = "<html><head><title>MAIA II - TACTICAL RESTORE</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001a1a; margin-bottom:20px; box-shadow: 0 0 40px rgba(0,255,255,0.2);}" 
    h += "details{background:#050505; border:1px solid #444; margin:10px 0; padding:15px; border-radius:4px;}" 
    h += "summary{font-weight:bold; color:#ffff00; cursor:pointer; text-transform:uppercase; font-size:1.1em;}" 
    h += ".code-view{background:#000; color:#0f0; padding:15px; border-left:4px solid #f0f; white-space:pre; font-size:0.85em; height:450px; overflow-y:scroll; overflow-x:auto; line-height:1.5; border-top: 1px solid #333; margin-top:10px; display:block;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em;}" 
    h += "button{padding:15px 25px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-mem{background:#444; color:#fff;} .btn-clear{background:#800; color:#fff;}" 
    h += ".hw-grid{display:grid; grid-template-columns: 1fr 1fr; gap:20px;}" 
    h += ".hw-spec{background:rgba(0,255,255,0.05); border:1px solid #0ff; padding:15px; border-left: 5px solid #f0f;}" 
    h += "table{width:100%; border-collapse:collapse; margin-top:10px;} td, th{padding:10px; border:1px solid #222; text-align:left;}" 
    h += ".viewer-3d{width:100%; height:400px; background:#000; border:2px solid #333; display:flex; flex-direction:column; align-items:center; justify-content:center; position:relative;}" 
    h += ".drone-core{width:100px; height:20px; background:#222; border:2px solid #0ff; position:relative; animation: hover 4s infinite ease-in-out;}" 
    h += ".arm{width:80px; height:4px; background:#0ff; position:absolute; top:8px;}" 
    h += "@keyframes hover { 0%,100%{transform:translateY(0) rotate(0);} 50%{transform:translateY(-30px) rotate(3deg);} }" 
    h += "</style><script>" 
    h += "function tVoz(){ let m=new SpeechSynthesisUtterance('Alex, restauracion completa. Eliminando ruido y volviendo a la verticalidad tecnica de sesenta por ciento.'); m.lang='es-MX'; window.speechSynthesis.speak(m); }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - PRODUCTION STACK 60/60 ]</h1>" 
    h += "<div class='panel'><h2>UNIDAD DE INGENIERIA</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Mision Tactica...' value=''>" 
    h += "<button type='submit' class='btn-gen'>COMPILAR EXPEDIENTE</button>" 
    h += "<button type='button' class='btn-mem'>MEMORIA PROYECTO</button>" 
    h += "<button type='reset' class='btn-clear'>LIMPIAR TERMINAL</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>MODELO ANALITICO 3D (ASSEMBLY)</h2><div class='viewer-3d'>" 
        h += "<div class='drone-core'><div class='arm' style='left:-80px;'></div><div class='arm' style='right:-80px;'></div></div>" 
        h += "<p style='margin-top:50px; color:#f0f;'>[ CONFIGURACION HEXA-QUAD | CHASIS CARBONO M40J ]</p></div></div>" 
        h += "<div class='panel'><h2>EXPEDIENTE TACTICO: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: 14 NODOS (PRODUCTION)</summary><div style='padding-left:20px; border-left:1px dotted #f0f;'>" 
        h += "<details><summary>?? control/attitude_mahony.py</summary><div class='code-view'>import numpy as np\\n\\nclass MahonyFilter:\\n    def __init__(self, Kp=2.0, Ki=0.005, dt=0.0025):\\n        self.q = np.array([1.0, 0.0, 0.0, 0.0])\\n        self.integral_error = np.zeros(3)\\n        self.dt = dt\\n\\n    def update(self, gyro, acc):\\n        a_norm = np.linalg.norm(acc)\\n        if a_norm < 0.01: return\\n        acc /= a_norm\\n        v = np.array([2*(self.q[1]*self.q[3] - self.q[0]*self.q[2]),\\n                      2*(self.q[0]*self.q[1] + self.q[2]*self.q[3]),\\n                      self.q[0]**2 - self.q[1]**2 - self.q[2]**2 + self.q[3]**2])\\n        error = np.cross(acc, v)\\n        self.integral_error += error * Ki * self.dt\\n        gyro_corr = gyro + Kp * error + self.integral_error\\n        dq = 0.5 * self.q_mult(self.q, gyro_corr) * self.dt\\n        self.q = (self.q + dq) / np.linalg.norm(self.q + dq)</div></details>" 
        h += "<details><summary>?? navigation/astar_3d.cpp</summary><div class='code-view'>#include ^vector^\\n#include ^cmath^\\n\\nfloat get_dynamic_cost(Node n, float fire_intensity) {\\n    // Penalizacion exponencial por gradiente termico\\n    return n.base_cost * exp(fire_intensity / 50.0);\\n}</div></details>" 
        h += "<details><summary>?? power/bms_can.cpp</summary><div class='code-view'>// CAN-FD Smart Battery Telemetry\\nvoid process_bms_frame(CAN_Frame f) {\\n    if(f.id == 0x100) {\\n        float voltage = ((f.data[0] << 8) | f.data[1]) * 0.01f;\\n        if(voltage < 40.0f) enter_failsafe();\\n    }\\n}</div></details>" 
        h += "</div></details>" 
        h += "<details open><summary>[DOM] AGENTE HARDWARE: ARQUITECTURA TACTICA</summary><div class='hw-grid'>" 
        h += "<div class='hw-spec'><h3>? POTENCIA</h3><b>Bus:</b> 12S Solid-State.<br><b>PDB:</b> Cobre 4oz Galvanico.<br><b>ESC:</b> KDE CAN-FD 120A.</div>" 
        h += "<div class='hw-spec'><h3>?? COMPUTO</h3><b>SoM:</b> Jetson Orin Nano.<br><b>FPGA:</b> Lattice CrossLink-NX.<br><b>SSD:</b> NVMe Industrial 1TB.</div>" 
        h += "<div class='hw-spec'><h3>?? SENSORES</h3><b>Lidar:</b> Ouster OS1-64 V2.<br><b>IR:</b> FLIR Boson Radiometrica.<br><b>GNSS:</b> u-blox ZED-F9P.</div>" 
        h += "<div class='hw-spec'><h3>?? CHASIS</h3><b>Material:</b> Carbono M40J.<br><b>Reflexion:</b> Kapton / Oro.<br><b>Motores:</b> KDE 7215XF IP67.</div>" 
        h += "</div></details>" 
        h += "<details open><summary>[ANX] ANALISIS DE VIABILIDAD Y FISICA</summary><div class='folder'>" 
        h += "<table><tr><th>CATEGORIA</th><th>ESTADO</th><th>DETALLE TECNICO</th></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>60%</td><td>TWR 3.4:1 validado para carga de 3kg.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>CRITICO</td><td>Vibracion de alta frecuencia en IMU.</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>PROC</td><td>Estructura monocasco al 45% de curado.</td></tr>" 
        h += "<tr><td><b>FISICA</b></td><td>CALC</td><td>CoG centrado con margen de 2mm.</td></tr>" 
        h += "</table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button>SEARCH PROJECT</button><button style='background:#f0f;'>CREATE NEW PROJECT</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
