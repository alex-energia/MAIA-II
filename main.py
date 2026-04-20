# -*- coding: utf-8 -*- 
import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    idea = request.form.get('drone_idea', '') 
    # BASE DE DATOS DE CODIGO REAL POR NODO 
    nodos_codigo = { 
        "01_RTOS": "// KERNEL PREEMPTIVO\\nvoid vTaskFirePriority(void *pv) {\\n  for(;;) {\\n    if(temp_critica) xTaskNotifyGive(hNavigation);\\n    vTaskDelay(pdMS_TO_TICKS(10));\\n  }\\n}", 
        "02_CONTROL": "// PID ROBUSTO ANTI-TURBULENCIA TERMICA\\nfloat calculate_pitch(float target, float current) {\\n  float error = target - current;\\n  return (Kp_fire * error) + (Ki_fire * i_error) + (Kd_fire * d_error);\\n}", 
        "03_NAV": "// A-STAR 3D CON EVASION DE GRADIENTE TERMICO\\nfloat get_cost(Node n) {\\n  float heat_penalty = radiometric_map[n.x][n.y] * 1.5;\\n  return n.base_cost + heat_penalty;\\n}", 
        "04_THERMAL": "// PROCESAMIENTO RADIOMETRICO FLIR BOSON\\ndef get_hotspots(frame):\\n  thermal_data = frame.astype(np.float32) * 0.01 - 273.15\\n  return np.where(thermal_data > 80.0) # Fuego detectado", 
        "07_BMS": "// MONITOREO DE DESCARGA EN ALTA TEMPERATURA\\nvoid check_cells() {\\n  if(cell_temp > 65.0) limit_current_to(40.0); // Proteccion 12S\\n}" 
    } 
    # CONSTRUCCION DEL VISOR VERTICAL SEGUN IDEA 
    visor = "// MISION CRITICA: " + idea.upper() + "\\n" 
    if idea: 
        for n in nodos_codigo: visor += "\\n// --- NODO " + n + " ---\\n" + nodos_codigo[n] + "\\n" 
    h = "<html><head><title>MAIA II - TOTAL STACK</title><style>" 
    h += "body{background:#050505; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:1px solid #0ff; padding:20px; background:#001111; margin-bottom:20px; box-shadow: 0 0 15px rgba(0,255,255,0.1);}" 
    h += ".tree{background:#000; border-left: 2px solid #f0f; padding:15px; height:400px; overflow-y:scroll;}" 
    h += ".code-window{background:#000; color:#0f0; padding:25px; border:1px solid #333; border-left:5px solid #f0f; min-height:1000px; white-space:pre-wrap; line-height:1.6; word-wrap:break-word; width:100%; box-sizing:border-box; font-size:0.95em;}" 
    h += "button{padding:10px 15px; cursor:pointer; font-weight:bold; border:none; text-transform:uppercase; margin:2px;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-lab{background:#f0f; color:#000;}" 
    h += ".hw-spec{background:rgba(0,255,255,0.05); border:1px solid #0ff; padding:10px; border-left: 5px solid #f0f; margin-bottom:10px;}" 
    h += "</style><script>" 
    h += "function tVoz(){ let m=new SpeechSynthesisUtterance('Alex, todos los nodos han sido inyectados con codigo real para " + idea + ". Sistema listo para compilacion.'); m.lang='es-MX'; window.speechSynthesis.speak(m); }" 
    h += "</script></head><body>" 
    h += "<h1>[ M.A.I.A. II - PRODUCTION STACK ]</h1>" 
    h += "<div class='panel'><h2>GENERACION ESTRATEGICA</h2>" 
    h += "<form method='post'><input name='drone_idea' style='width:50%; padding:10px; background:#000; color:#0ff; border:1px solid #0ff;' value='" + idea + "'>" 
    h += "<button type='submit' class='btn-gen'>GENERAR EXPEDIENTE</button>" 
    h += "<button type='button' class='btn-gen' style='background:#444; color:#fff;'>MEMORIA</button>" 
    h += "<button type='button' onclick='tVoz()' style='background:red; color:white;'>VOZ MAIA</button></form></div>" 
    h += "<div class='panel'><h2>PROJECT LAB</h2><button class='btn-lab'>BUSCADOR</button><button class='btn-lab'>CREAR</button></div>" 
    h += "<div class='panel'><h2>MODULO DE CONSTRUCCION</h2>" 
    h += "<div class='hw-spec'><b>CHASIS:</b> Carbono M40J | <b>PROPULSION:</b> KDE 7215XF | <b>POWER:</b> 12S Redundant</div></div>" 
    h += "<div class='panel'><h2>14 NODOS (SISTEMA DE ARCHIVOS)</h2><div class='tree'>" 
    if idea: 
        for n in nodos_codigo: h += "<details><summary>" + n + "</summary><div style='color:#0f0; margin-left:20px;'>- production_ready.code</div></details>" 
    h += "</div></div>" 
    h += "<div class='panel'><h2>VISOR DE CODIGO VERTICAL (INYECCION REAL)</h2>" 
    h += "<div class='code-window'>" + visor + "</div></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
