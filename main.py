# -*- coding: utf-8 -*- 
import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    idea = request.form.get('drone_idea', 'VIGILANCIA URBANA') 
    # Logica de inyeccion de misiones en los nodos 
    mission_code = "// MISION: " + idea.upper() + "\\n" 
    if "vigilancia" in idea.lower(): 
        mission_code += "import cv2\\n# Algoritmo de deteccion de flujo peatonal activo\\ndef detect_targets(frame):\\n    return model.inference(frame, threshold=0.75)" 
    elif "incendio" in idea.lower(): 
        mission_code += "# Filtro Termico Radiometrico activado\\ndef thermal_mask(raw_ir):\\n    return (raw_ir > 350.0) # Umbral de ignicion" 
    else: 
        mission_code += "# Modo Reconocimiento General activo\\ndef mission_loop():\\n    pass" 
    h = "<html><head><title>MAIA II - GENERATOR</title><style>" 
    h += "body{background:#050505; color:#0ff; font-family:monospace; padding:20px;}" 
    h = "<html><head><style>" 
    h += "body{background:#050505; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:1px solid #0ff; padding:20px; background:#001111; margin-bottom:20px;}" 
    h += ".tree{background:#000; border-left: 2px solid #f0f; padding:15px; height:300px; overflow-y:scroll;}" 
    h += ".code-window{background:#000; color:#0f0; padding:25px; border:1px solid #333; border-left:5px solid #f0f; min-height:600px; white-space:pre-wrap; line-height:1.6;}" 
    h += "button{padding:10px 15px; cursor:pointer; font-weight:bold; border:none; text-transform:uppercase; margin:2px;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-lab{background:#f0f; color:#000;}" 
    h += "</style><script>" 
    h += "function tVoz(){ let m=new SpeechSynthesisUtterance('Alex, procesando la mision " + idea + ". Nodos actualizados con codigo de produccion.'); m.lang='es-MX'; window.speechSynthesis.speak(m); }" 
    h += "</script></head><body>" 
    h += "<h1>[ M.A.I.A. II - CENTRAL TACTICA ]</h1>" 
    h += "<div class='panel'><h2>GENERACION ESTRATEGICA</h2>" 
    h += "<form method='post'><input name='drone_idea' style='width:50%; padding:10px; background:#000; color:#0ff; border:1px solid #0ff;' value='" + idea + "'>" 
    h += "<button type='submit' class='btn-gen'>GENERAR EXPEDIENTE</button>" 
    h += "<button type='button' onclick='tVoz()' style='background:red; color:white;'>VOZ MAIA</button></form></div>" 
    h += "<div class='panel'><h2>MODULO DE CONSTRUCCION</h2>" 
    h += "<b>ESPECIFICACION:</b> Carbono M40J | KDE 7215XF | 12S Redundant.</div>" 
    h += "<div class='panel'><h2>14 NODOS (SISTEMA DE ARCHIVOS)</h2><div class='tree'>" 
    h += "<details open><summary>04_PERCEPTION</summary><div style='color:#0f0; margin-left:20px;'>- logic_main.py (INJECTED)</div></details>" 
    h += "<details><summary>01_CORE_RTOS</summary>...</details></div></div>" 
    h += "<div class='panel'><h2>VISOR DE CODIGO VERTICAL (DINAMICO)</h2>" 
    h += "<div class='code-window'>" + mission_code + "\\n\\n// ARCHIVO: control/mahony_filter.py (ESTRUCTURA DE VUELO BASE)\\nclass MahonyIMU:\\n    def __init__(self, freq=400):\\n        self.q = np.array([1, 0, 0, 0])\\n        self.dt = 1.0/freq\\n\\n    def update(self, gyro, acc):\\n        # Logica avanzada de fusion sensorial para " + idea + "\\n        pass</div></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
