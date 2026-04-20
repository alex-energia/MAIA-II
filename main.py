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
    h = "<html><head><title>MAIA II GLI-60 V-PRO</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px; overflow-x:hidden;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001a1a; margin-bottom:20px; box-shadow: 0 0 50px #0ff;}" 
    h += "details{background:#050505; border:1px solid #444; margin:10px 0; padding:15px; border-radius:4px;}" 
    h += "summary{font-weight:bold; color:#ffff00; cursor:pointer; padding:5px; text-transform:uppercase;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre; font-size:0.9em; height:500px; overflow-y:scroll; overflow-x:auto; line-height:1.6; border-top: 1px solid #333; margin-top:10px; display:block;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:2px solid #0ff; padding:18px; font-size:1.2em;}" 
    h += "button{padding:18px 25px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-mem{background:#444; color:#fff;} .btn-clear{background:#800; color:#fff;}" 
    h += ".folder{margin-left:30px; border-left:2px dotted #f0f; padding-left:20px;}" 
    h += ".hw-card{background:rgba(0,255,255,0.05); border:1px solid #0ff; padding:20px; margin:15px 0; border-left:5px solid #f0f;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:12px; border:1px solid #333; text-align:left;}" 
    h += "th{background:#004d4d; color:#fff;}" 
    h += ".viewer-3d{width:100%; height:350px; background:#000; border:1px solid #333; display:flex; flex-direction:column; align-items:center; justify-content:center;}" 
    h += ".drone-body{width:80px; height:20px; background:#333; position:relative; border:2px solid #0ff; animation: hover 3s infinite ease-in-out;}" 
    h += ".arm{width:60px; height:5px; background:#0ff; position:absolute; top:8px;}" 
    h += "@keyframes hover { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-15px);} }" 
    h += "</style><script>" 
    h += "function tVoz(){ let m=new SpeechSynthesisUtterance('Alex, sistema reconstruido sin errores de sintaxis. Desplegando stack vertical sesenta sesenta.'); m.lang='es-MX'; window.speechSynthesis.speak(m); }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - PRODUCTION STACK 60/60 ]</h1>" 
    h += "<div class='panel'><h2>UNIDAD DE INGENIERIA</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Requerimiento tecnico...' value=''>" 
    h += "<button type='submit' class='btn-gen'>COMPILAR PROYECTO</button>" 
    h += "<button type='button' class='btn-mem'>MEMORIA</button>" 
    h += "<button type='reset' class='btn-clear'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>MODELO ANALITICO 3D</h2><div class='viewer-3d'>" 
        h += "<div class='drone-body'><div class='arm' style='left:-50px;'></div><div class='arm' style='right:-50px;'></div></div>" 
        h += "<p style='margin-top:40px; color:#f0f;'>[ BRAZOS DE CARBONO M40J E INSTRUMENTACION ACTIVA ]</p></div></div>" 
        h += "<div class='panel'><h2>EXPEDIENTE TACTICO: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: PRODUCTION STACK (14 NODOS)</summary><div class='folder'>" 
        h += "<details><summary>?? core/rtos</summary><div class='folder'><div class='code-view'>// task_manager.c\\n#include ^FreeRTOS.h^\\n\\nvoid vFlightControl(void *pvParameters) {\\n    TickType_t xLastWakeTime = xTaskGetTickCount();\\n    const TickType_t xFrequency = pdMS_TO_TICKS(2.5); // 400Hz\\n    for(;;) {\\n        update_attitude_pid();\\n        write_motor_outputs();\\n        vTaskDelayUntil(&xLastWakeTime, xFrequency);\\n    }\\n}</div></div></details>" 
        h += "<details><summary>?? navigation/astar</summary><div class='folder'><div class='code-view'># voxel_planner.py\\nimport numpy as np\\n\\nclass VoxelPathfinder:\\n    def __init__(self, resolution=0.1):\\n        self.resolution = resolution\\n\\n    def compute_cost(self, node_a, node_b):\\n        # Coste euclidiano 3D + penalizacion por proximidad a obstaculos\\n        dist = np.linalg.norm(node_a - node_b)\\n        clearance_penalty = self.get_octomap_clearance(node_b)\\n        return dist + (1.0 / (clearance_penalty + 0.01))</div></div></details>" 
        h += "</div></details>" 
        h += "<details open><summary>[DOM] AGENTE HARDWARE: DOM DETALLADO</summary><div class='folder'>" 
        h += "<div class='hw-card'><h3>?? PROCESAMIENTO Y BUSES</h3>" 
        h += "<b>CPU/GPU:</b> Jetson Orin Nano + FPGA CrossLink-NX para bypass MIPI.<br>" 
        h += "<b>Bus Critico:</b> CAN-FD @ 5Mbps con aislamiento galvanico ISO11898-2.<br>" 
        h += "<b>Almacenamiento:</b> Industrial NVMe (Write endurance 1500 TBW).</div>" 
        h += "<div class='hw-card'><h3>?? DINAMICA DE VUELO</h3>" 
        h += "<b>Relacion TWR:</b> 3.4:1 (Peso: 8.5kg / Empuje: 28.9kg).<br>" 
        h += "<b>Estabilidad:</b> Giroscopios industriales con vibracion amortiguada por Alpha-Gel.</div>" 
        h += "</div></details>" 
        h += "<details open><summary>[ANX] VIABILIDAD, RIESGOS Y MONTAJE</summary><div class='folder'>" 
        h += "<table><tr><th>CATEGORIA</th><th>ESTADO</th><th>DETALLE TECNICO</th></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>60%</td><td>Hardware validado; requiere integracion de software final.</td></tr>" 
        h += "<tr><td><b>RIESGOS</b></td><td>ALTO</td><td>Interferencia EMI en enlace de 2.4GHz en zonas urbanas.</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>PROC</td><td>Ensamblado estructural completado al 40%.</td></tr>" 
        h += "<tr><td><b>FISICA</b></td><td>CALC</td><td>Centro de gravedad (CoG) desplazado 2mm tras carga util.</td></tr>" 
        h += "</table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button>BUSCADOR</button><button style='background:#f0f;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
