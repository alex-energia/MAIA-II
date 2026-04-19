import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
logs = [] 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    global logs 
    if request.method == 'POST': 
        u_m = request.form.get('msg') or request.form.get('drone_idea') 
        if u_m: logs.append((u_m, "MAIA_II_CORE: Procesando requerimiento tecnico...")) 
    h = "<html><body style='background:#000; color:#0ff; font-family:monospace; padding:30px;'>" 
    h += "<h1 style='color:#fff; text-align:center; border-bottom:2px solid #0ff;'> [ M.A.I.A. II - LABORATORIO DE INGENIERIA ]</h1>" 
    h += "<div style='display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-top:30px;'>" 
    h += "<div style='border:2px solid #0ff; padding:20px; background:#001515;'>" 
    h += "<h2 style='color:yellow;'>DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Escribe tu idea (Aereo o Maritimo)...' style='width:100%; background:#000; color:#0ff; border:1px solid #0ff; padding:10px; margin-bottom:10px;'>" 
    h += "<div style='display:grid; grid-template-columns:1fr 1fr; gap:5px;'>" 
    h += "<button type='submit' style='background:#0ff; border:none; padding:8px; font-weight:bold; cursor:pointer;'>GENERAR</button>" 
    h += "<button type='button' style='background:#555; color:white; border:none; padding:8px; cursor:pointer;'>MEMORIA</button>" 
    h += "<button type='reset' style='background:#a00; color:white; border:none; padding:8px; cursor:pointer;'>LIMPIAR</button>" 
    h += "<button type='button' style='background:#0a0; color:white; border:none; padding:8px; cursor:pointer;'>VOZ MAIA</button></div></form></div>" 
    h += "<div style='border:2px solid #f0f; padding:20px; background:#150015;'>" 
    h += "<h2 style='color:white;'>PROJECT LAB</h2>" 
    h += "<p>Gestion de proyectos complejos</p>" 
    h += "<div style='display:flex; flex-direction:column; gap:10px;'>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f; padding:10px; cursor:pointer;'>BUSCADOR DE PROYECTOS</button>" 
    h += "<button style='background:#f0f; border:none; color:white; padding:10px; font-weight:bold; cursor:pointer;'>CREAR NUEVO PROYECTO</button></div></div></div>" 
    h += "<div style='margin-top:30px; border:1px solid #333; padding:20px; background:#080808;'>" 
    h += "<h3>CONSOLA DE MAIA II</h3>" 
    h += "<div style='height:120px; overflow-y:scroll; border-bottom:1px solid #333;'>{% for u, r in history %}<p style='color:#aaa;'><b>U:</b> {{u}}<br><span style='color:#0ff;'><b>M:</b> {{r}}</span></p>{% endfor %}</div></div></body></html>" 
    return render_template_string(h, history=logs) 
if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 10000)) 
    app.run(host="0.0.0.0", port=port) 
