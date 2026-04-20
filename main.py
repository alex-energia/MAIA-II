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
    h = "<html><head><title>MAIA II - FULL ENGINEERING</title><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001a1a; margin-bottom:20px;}" 
    h += "details{background:#050505; border:1px solid #444; margin:10px 0; padding:15px;}" 
    h += ".code-view{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; white-space:pre; font-size:0.85em; height:400px; overflow-y:scroll; border-top: 1px solid #333; display:block;}" 
    h += ".hw-map{background:#002222; border:1px dashed #0ff; padding:15px; color:#fff; font-size:0.9em;}" 
    h += "table{width:100%; border-collapse:collapse;} td, th{padding:8px; border:1px solid #222;}" 
    h += "</style></head><body>" 
    h += "<h1> [ M.A.I.A. II - SISTEMA DE INGENIERIA 60/60 ]</h1>" 
    h += "<form method='post' class='panel'><input name='drone_idea' style='width:60%; padding:10px;' placeholder='Mision...'><button type='submit' style='padding:10px 20px;'>DESPLEGAR NODOS</button></form>" 
    if res: 
        h += "<div class='panel'><h2>ESTRUCTURA DE CONSTRUCCION: " + idea + "</h2>" 
        h += "<details open><summary>?? NODO 04: COMMS / MAVLINK_V2.PY</summary><div class='code-view'># MAVLink 2.0 Packet Encoder\\ndef create_heartbeat():\\n    # [STX, LEN, INC_FLAGS, CMP_FLAGS, SEQ, SYSID, COMPID, MSGID(3), PAYLOAD, CK]\\n    packet = bytearray([0xFD, 0x09, 0x00, 0x00, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00])\\n    # Tipo de dron: MAV_TYPE_QUADROTOR (2) | Autopiloto: MAV_AUTOPILOT_GENERIC (0)\\n    payload = struct.pack('<IBBBB', 0, 2, 0, 0, 3)\\n    return finalize_packet(packet + payload)</div></details>" 
        h += "<details><summary>?? NODO 07: POWER / BMS_MANAGER.CPP</summary><div class='code-view'>// SMBus/I2C Smart Battery Interface\\nvoid Read_Battery_Status() {\\n    uint16_t voltage = i2c_read_word(BMS_ADDR, 0x09); // Voltage en mV\\n    int16_t current = i2c_read_word(BMS_ADDR, 0x0A);  // Current en mA\\n    if (voltage < 42000) trigger_failsafe_land();     // Umbral 3.5V/celda (12S)\\n}</div></details>" 
        h += "<div class='panel'><h2>MAPEO DE HARDWARE (PINOUT TACTICO)</h2><div class='hw-map'>" 
        h += "<b>JETSON ORIN PINS:</b><br>" 
        h += "[PIN 31] -> CAN_HI (Bus de Motores)<br>[PIN 33] -> CAN_LO<br>" 
        h += "[MIPI CSI-2] -> FLIR BOSON GMSL2 Bridge<br>" 
        h += "[UART 1] -> GPS u-blox (57600 baud)<br>" 
        h += "</div></div>" 
        h += "</div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=10000) 
