import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    res = None 
    idea = "" 
    if request.method == 'POST': 
        idea = request.form.get('drone_idea', '') 
        res = "active" 
    h = "<html><head><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px;}" 
    h += "details{background:#050505; border:1px solid #333; margin:10px 0; padding:10px; cursor:pointer;}" 
    h += "summary{font-weight:bold; color:yellow; font-size:1.2em;}" 
    h += ".code-view{background:#111; color:#0f0; padding:10px; border-left:3px solid #0f0; white-space:pre; font-size:0.9em;}" 
    h += "input{width:60%; background:#000; color:#0ff; border:1px solid #0ff; padding:10px;}" 
    h += "button{background:#0ff; border:none; padding:10px 20px; font-weight:bold; cursor:pointer; margin:2px;}" 
    h += "</style></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO MULTIAGENTE ]</h1>" 
    h += "<div class='panel'><h2>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Idea de dron (Aereo/Maritimo)...'>" 
    h += "<button type='submit'>GENERAR</button>" 
    h += "<button type='button'>MEMORIA</button>" 
    h += "<button type='button' style='background:#a00; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' style='background:#0a0; color:#fff;'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>PROYECTO: " + idea + "</h2>" 
        h += "<details><summary>[+] AGENTE IA: SOFTWARE</summary><div class='code-view'>// Kernel Flight Control\\nvoid loop() {\\n  stabilize_gyro();\\n  process_ai_vision();\\n}</div></details>" 
        h += "<details><summary>[+] AGENTE HARDWARE: FISICO</summary><ul><li>ESC: 60A 4-in-1</li><li>Motores: 2207 2400KV</li><li>FC: F722 Flight Controller</li></ul></details>" 
        h += "<details><summary>[+] AGENTE 3D: MODELADO</summary><ul><li>Frame: Carbon Fiber X-Layout</li><li>Propellers: 5 inch Tri-blade</li></ul></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: VIABILIDAD Y RIESGOS</summary><ul><li>Viabilidad: Alta</li><li>Riesgo: Interferencia GPS en zonas densas</li><li>Fisica: Ratio Empuje-Peso 3:1</li></ul></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR PROYECTOS</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
