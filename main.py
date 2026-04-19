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
    h = "<html><head><style>" 
    h += "body{background:#000; color:#0ff; font-family:monospace; padding:20px;}" 
    h += ".panel{border:2px solid #0ff; padding:20px; background:#001515; margin-bottom:20px; box-shadow: 0 0 20px #0ff;}" 
    h += "details{background:#050505; border:1px solid #333; margin:15px 0; padding:15px; border-radius:5px;}" 
    h += "summary{font-weight:bold; color:yellow; font-size:1.2em; cursor:pointer;}" 
    h += ".code-block{background:#080808; color:#0f0; padding:25px; border-left:5px solid #0f0; white-space:pre-wrap; font-size:0.9em; margin:15px 0; line-height:1.6; border-radius:0 10px 10px 0;}" 
    h += "input{width:65%; background:#000; color:#0ff; border:2px solid #0ff; padding:15px; font-size:1.1em; border-radius:5px;}" 
    h += "button{padding:15px 25px; font-weight:bold; cursor:pointer; margin:5px; border:none; border-radius:5px; text-transform:uppercase;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-voz{background:red; color:#fff;}" 
    h += "table{width:100%; border-collapse:collapse; margin-top:15px;} td, th{padding:12px; border:1px solid #1a1a1a; text-align:left;}" 
    h += "th{background:#002222; color:yellow; border:1px solid #0ff;}" 
    h += ".drone-3d{color:#fff; font-size:14px; line-height:1.2; background:#111; padding:20px; border:1px dashed #0ff; text-align:center;}" 
    h += "</style><script>" 
    h += "let h=false; function tVoz(){ let b=document.getElementById('btnVoz'); " 
    h += "if(!h){ b.style.background='green'; h=true; " 
    h += "let m=new SpeechSynthesisUtterance('Hola Alex, soy Maia. Nexo de ingenieria activo. Procesando arquitectura de sistemas.'); " 
    h += "m.lang='es-MX'; m.onend=()=>{ b.style.background='red'; h=false; }; window.speechSynthesis.speak(m); " 
    h += "} else { window.speechSynthesis.cancel(); b.style.background='red'; h=false; } }" 
    h += "</script></head><body>" 
    h += "<h1> [ M.A.I.A. II - NEXO DE INGENIERIA AVANZADA ]</h1>" 
    h += "<div class='panel'><h2>MODULO: DRONE CONSTRUCTOR</h2>" 
    h += "<form method='post'><input name='drone_idea' placeholder='Ingrese requerimiento tecnico...' value=''>" 
    h += "<button type='submit' class='btn-gen'>GENERAR SISTEMA</button>" 
    h += "<button type='reset' style='background:#555; color:#fff;'>LIMPIAR</button>" 
    h += "<button type='button' id='btnVoz' class='btn-voz' onclick='tVoz()'>VOZ MAIA</button></form></div>" 
    if res: 
        h += "<div class='panel'><h2>PROYECTO: " + idea + "</h2>" 
        h += "<details open><summary>[+] AGENTE 3D: ARQUITECTURA FISICA</summary><div class='drone-3d'>" 
        h += "      [M1]  _______  [M2]      <br>        \\ | BRAZO | /        <br>         \\|_______|/         <br>    <---[ CORE_BODY ]--->    <br>         /|_______|\\         <br>        / | BRAZO | \\        <br>      [M4]  -------  [M3]      <br><br>ESTRUCTURA: MONOCASCO REFORZADO - FIBRA 4K</div></details>" 
        h += "<details><summary>[+] AGENTE SOFTWARE: KERNEL Y NAVEGACION</summary>" 
        h += "<div class='code-block'>// flight_stabilization.cpp\n#include ^Redundant_IMU.h^\nvoid calculateAttitude() {\n    Quaternion q = fusion_filter.update(accel, gyro, mag);\n    Vector3 error = target_orientation - q.toEuler();\n    motor_out = pid_controller.compute(error, dt);\n    limit_current_draw(motor_out);\n}</div>" 
        h += "<div class='code-block'># autonomous_logic.py\nclass PathPlanner:\n    def get_safe_path(self, lidar_cloud):\n        voxels = self.generate_octree(lidar_cloud)\n        return self.a_star_search(self.current_pos, self.goal, voxels)</div></details>" 
        h += "<details><summary>[+] AGENTE HARDWARE: DOM PROFESIONAL (BOM)</summary>" 
        h += "<table><tr><th>SUBSISTEMA</th><th>COMPONENTE EXPLICITO</th><th>FUNCION</th></tr>" 
        h += "<tr><td>AVIONICA</td><td>Cube Orange+ (Triple IMU)</td><td>Control de Vuelo Redundante</td></tr>" 
        h += "<tr><td>COMUNICACION</td><td>Herelink Blue v1.1</td><td>Enlace encriptado 20km HD</td></tr>" 
        h += "<tr><td>ENERGIA</td><td>BMS Smart 12S 60A</td><td>Gestion de Celdas de Estado Solido</td></tr></table></details>" 
        h += "<details><summary>[+] AGENTE EXPERTO: MATRIZ DE ANALISIS</summary>" 
        h += "<table><tr><td><b>FISICA DINAMICA</b></td><td>Analisis CFD completado. Coeficiente de arrastre optimizado para 15m/s.</td></tr>" 
        h += "<tr><td><b>MITIGACION RIESGOS</b></td><td>Paracaidas de emergencia con despliegue pirotecnico integrado.</td></tr>" 
        h += "<tr><td><b>SISTEMA DE MISION</b></td><td>Estabilizacion GIMBAL 3-Ejes con compensacion de vibracion activa.</td></tr></table></details></div>" 
    h += "<div class='panel' style='border-color:#f0f;'><h2>PROJECT LAB</h2>" 
    h += "<button style='background:transparent; border:1px solid #f0f; color:#f0f;'>BUSCADOR PROYECTOS</button>" 
    h += "<button style='background:#f0f; color:#fff;'>CREAR NUEVO PROYECTO</button></div>" 
    h += "</body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
