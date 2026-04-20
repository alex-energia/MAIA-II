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
    h = "<html><head><title>MAIA II GLI-60 ULTIMATE</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px; overflow-x:hidden;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001a1a; margin-bottom:20px; box-shadow: 0 0 50px #0ff;}" 
    h += "details{background:#050505; border:1px solid #444; margin:10px 0; padding:15px; border-radius:4px;}" 
    h += "summary{font-weight:bold; color:#ffff00; cursor:pointer; padding:5px; text-transform:uppercase; font-size:1.1em;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre; font-size:0.9em; height:500px; overflow-y:scroll; overflow-x:auto; line-height:1.6; border-top: 1px solid #333; margin-top:10px; display:block;}" 
    h += "input{width:50%; background:#000; color:#0ff; border:2px solid #0ff; padding:18px; font-size:1.2em;}" 
    h += "button{padding:18px 25px; font-weight:bold; cursor:pointer; margin:5px; border:none; text-transform:uppercase; transition:0.3s;}" 
    h += ".btn-mem{background:#444; color:#fff;} .btn-clear{background:#800; color:#fff;} .btn-gen{background:#0ff; color:#000;}" 
    h += ".folder{margin-left:30px; border-left:2px dotted #f0f; padding-left:20px;}" 
    h += ".hw-card{background:rgba(0,255,255,0.05); border:1px solid #0ff; padding:20px; margin:15px 0; border-left:5px solid #f0f;}" 
    h += ".viewer-3d{width:100%; height:400px; background:#000; border:1px solid #333; display:flex; align-items:center; justify-content:center; position:relative;}" 
    h += ".drone-sim{width:100px; height:100px; border:2px solid #0ff; position:relative; animation: fly 4s infinite ease-in-out;}" 
    h += "@keyframes fly { 0%,100%{transform:translateY(0) rotate(0);} 50%{transform:translateY(-20px) rotate(5deg);} }" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:10px; border:1px solid #222; text-align:left;}" 
    h += "</style><script>" 
    h += "function tVoz(){ let m=new SpeechSynthesisUtterance('Alex, sistema cargado al sesenta por ciento real. Desplegando modulos de fisica, riesgo y montaje.'); m.lang='es-MX'; window.speechSynthesis.speak(m); }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO ESTRATEGICO TOTAL 60/60 ]</h1>" 
    h += "<div class='panel'><h2>TERMINAL DE COMANDO</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Requerimiento de mision...' value=''>" 
    h += "<button type='submit' class='btn-gen'>GENERAR STACK COMPLETO</button>" 
    h += "<button type='button' class='btn-mem'>MEMORIA PROYECTO</button>" 
    h += "<button type='reset' class='btn-clear'>LIMPIAR TERMINAL</button>" 
    h += "<button type='button' id='btnVoz' style='background:red; color:#fff;' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>VISUALIZACION 3D PRE-MONTAJE</h2><div class='viewer-3d'>" 
        h += "<div style='color:#0ff; text-align:center;'>[ SIMULACION BRAZOS Y HELICES ACTIVAS ]<br><div class='drone-sim' style='margin:20px auto; border-radius:50%; border-top:5px solid #f0f;'></div>" 
        h += "ESTRUCTURA: MONOCASCO M40J | PROPULSION: KDE 7215XF</div></div></div>" 
        h += "<div class='panel'><h2>EXPEDIENTE: " + idea + "</h2>" 
        h += "<details open><summary>[DIR] AGENTE SOFTWARE: PRODUCTION STACK (VERTICAL)</summary><div class='folder'>" 
        h += "<details><summary>?? telemetry/mavlink</summary><div class='folder'><div class='code-view'># fast_mavlink_parser.py\\nimport struct\\n\\nclass MAVLinkParser:\\n    def __init__(self):\\n        self.HEADER = 0xFD # MAVLink 2.0\\n\\n    def parse_frame(self, buffer):\\n        # Sincronizacion de frame y validacion de CRC-16 X.25\\n        if buffer[0] != self.HEADER: return None\\n        payload_len = buffer[1]\\n        msg_id = struct.unpack('<I', buffer[7:10] + b'\\\\x00')[0]\\n        payload = buffer[10:10+payload_len]\\n        checksum = struct.unpack('<H', buffer[10+payload_len:12+payload_len])[0]\\n        \\n        if self.verify_crc(buffer[:10+payload_len], checksum):\\n            return {'id': msg_id, 'data': payload}\\n        return None</div></div></details>" 
        h += "<details><summary>?? power/bms</summary><div class='folder'><div class='code-view'>// can_bms_driver.cpp\\n#include ^mcp2515.h^\\n\\nvoid BMS_Update() {\\n    CAN_Frame msg;\\n    if (CAN_Read(&msg)) {\\n        if (msg.id == BMS_CELL_VOLTAGE_ID) {\\n            float v_cell[12];\\n            for(int i=0; i<12; i++) {\\n                v_cell[i] = ((msg.data[i*2] << 8) | msg.data[i*2+1]) * 0.001f;\\n                if(v_cell[i] < 3.2f) Critical_Shutdown();\\n            }\\n        }\\n    }\\n}</div></div></details>" 
        h += "</div></details>" 
        h += "<details open><summary>[DOM] AGENTE HARDWARE: ARQUITECTURA FISICA</summary><div class='folder'>" 
        h += "<div class='hw-card'><h3>?? ANALISIS DE FISICA DE VUELO</h3>" 
        h += "<b>Empuje Maximo:</b> 52.4 kg (Relacion TWR 3.2:1)<br>" 
        h += "<b>Momento de Inercia:</b> Calculado para ejes X/Y en 0.45 kg*m^2.<br>" 
        h += "<b>Carga Alar:</b> 14.2 kg/m^2 (Optimo para estabilidad en vigilancia urbana).</div>" 
        h += "<div class='hw-card'><h3>??? PROTOCOLO DE MONTAJE</h3>" 
        h += "1. Torque de tornilleria Titanio Grado 5 a 2.5Nm con Loctite 243.<br>" 
        h += "2. Alineacion de IMUs en bloque de amortiguacion Alpha-Gel.<br>" 
        h += "3. Calibracion de ESCs KDE con protocolo DSHOT600.</div>" 
        h += "</div></details>" 
        h += "<details open><summary>[ANX] ANALISIS ESTRATEGICO (VIABILIDAD Y RIESGOS)</summary><div class='folder'>" 
        h += "<table><tr><th>CATEGORIA</th><th>NIVEL</th><th>DETALLE TêCNICO</th></tr>" 
        h += "<tr><td><b>VIABILIDAD</b></td><td>ALTA</td><td>Costo unitario estimado $14,500 USD vs $45k competencia.</td></tr>" 
        h += "<tr><td><b>RIESGO RFI</b></td><td>MEDIO</td><td>Blindaje EMI necesario en bus de camara GMSL2.</td></tr>" 
        h += "<tr><td><b>MONTAJE</b></td><td>COMPLEJO</td><td>Requiere horno de curado para el chasis de carbono.</td></tr>" 
        h += "</table></div></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button>BUSCADOR</button><button style='background:#f0f;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
