import os 
from flask import Flask, render_template_string, request 
import random 
app = Flask(__name__) 
logs = [] 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    global logs 
    if request.method == 'POST': 
        u_m = request.form.get('msg') 
        logs.append((u_m, "MAIA_II_CORE: Iniciando secuencia de ingenieria...")) 
    h = "<html><body style='background:#000; color:#0ff; font-family:monospace; padding:30px;'>" 
    h += "<h1 style='color:#fff; text-align:center; border-bottom:2px solid #0ff;'> [ M.A.I.A. II - NEXO DE INGENIERIA ]</h1>" 
    h += "<div style='display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-top:30px;'>" 
    h += "<div style='border:2px solid #0ff; padding:20px; background:#001515;'>" 
    h += "<h2 style='color:yellow;'>DRONE CONSTRUCTOR</h2>" 
    h += "<p>Estado: Esperando planos de chasis...</p>" 
    h += "<pre style='font-size:10px; color:#555;'>  __  \\n /  \\ \\n( [] )\\n \\__/ </pre>" 
    h += "<ul style='font-size:12px;'><li>Calculo de empuje</li><li>Configuracion ESC</li><li>Planos de fibra de carbono</li></ul></div>" 
    h += "<div style='border:2px solid #f0f; padding:20px; background:#150015;'>" 
    h += "<h2 style='color:white;'>PROJECT LAB</h2>" 
    h += "<p>Estado: Multiagente en espera de metas...</p>" 
    h += "<pre style='font-size:10px; color:#555;'> [===]\\n  | |\\n [===] </pre>" 
    h += "<ul style='font-size:12px;'><li>Diagramas de Gantt</li><li>Analisis de inversion</li><li>Escalabilidad</li></ul></div></div>" 
    h += "<div style='margin-top:30px; border:1px solid #333; padding:20px; background:#080808;'>" 
    h += "<h3>CONSOLA DE MAIA II</h3>" 
    h += "<div style='height:120px; overflow-y:scroll; border-bottom:1px solid #333;'>{% for u, r in history %}<p style='color:#aaa;'><b>U:</b> {{u}}<br><span style='color:#0ff;'><b>M:</b> {{r}}</span></p>{% endfor %}</div>" 
    h += "<form method='post' style='display:flex; gap:10px; margin-top:10px;'><input name='msg' style='flex-grow:1; background:#000; color:#0ff; border:1px solid #0ff; padding:10px;' placeholder='Comando de sistema...'><button style='background:#0ff; color:#000; border:none; padding:10px 20px; font-weight:bold; cursor:pointer;'>ENVIAR</button></form></div></body></html>" 
    return render_template_string(h, history=logs) 
if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 10000)) 
    app.run(host="0.0.0.0", port=port) 
