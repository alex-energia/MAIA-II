# -*- coding: utf-8 -*- 
import os 
from flask import Flask, render_template_string, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def home(): 
    idea = request.form.get('drone_idea', 'DRON GENERICO') 
    nodo_solicitado = request.form.get('target_node', '01_CORE_RTOS') 
    # MOTOR DE GENERACION REAL PARA LOS 14 NODOS 
    db = { 
        "01_CORE_RTOS": f"// KERNEL PARA: {idea}\\nvoid vApplicationIdleHook(void) {{ \\n  // Low power mode para {idea}\\n  HAL_PWR_EnterSLEEPMode(PWR_MAINREGULATOR_ON, PWR_SLEEPENTRY_WFI);\\n}}", 
        "02_CONTROL_ATTITUDE": f"// CONTROL DE VUELO ESTRATEGICO\\nvoid stabilize() {{ \\n  float bias = calc_vibration_offset('{idea}');\\n  apply_foc_correction(bias);\\n}}", 
        "03_NAVIGATION_ASTAR": f"// NAVEGACION AUTONOMA\\n// Pathfinding optimizado para {idea}\\nint[][] grid = create_dynamic_occupancy_grid();", 
        "04_PERCEPTION_THERMAL": f"// ANALISIS TERMICO\\ndef process_ir():\\n  raw = sensor.get_radiometric_data()\\n  return analyze_signature(raw, '{idea}')", 
        "05_PERCEPTION_LIDAR": "// SEGMENTACION POINTCLOUD\\nvoid filter_cloud() { ground_filter.setInputCloud(raw_cloud); }", 
        "06_TELEMETRY_MAVLINK": "// ENCRIPTACION AES-256 MAVLINK\\nvoid secure_send() { mavlink_msg_heartbeat_pack(ID, AES_ENCRYPT(status)); }", 
        "07_POWER_BMS": "// GESTION ENERGIA 12S\\nvoid balance_cells() { if(v_cell < 3.2) emergency_land(); }", 
        "08_COMM_SILVUS": "// MESH NETWORK TACTICA\\nvoid silvus_init() { radio.set_frequency(4400); // MHz }", 
        "09_DIAGNOSTICS_HEALTH": "// FAILSAFE LOGIC\\nvoid check_health() { if(esc_temp > 95) throttle_cut(); }", 
        "10_SIMULATION_SITL": "// PHYSICS OVERRIDE\\ndef apply_wind_drag():\\n  return drag_coefficient * air_density * velocity**2", 
        "11_MISSION_PLANNER": "// GEOFENCING ESTRATEGICO\\nbool is_inside_mission_area(double lat, double lon) { return poly.contains(lat, lon); }", 
        "12_HARDWARE_HAL": "// PINOUT DEFINITION\\n#define MOT_1 GPIO_PIN_0 // PWM TIM1", 
        "13_AI_INFERENCE": f"// TENSORRT DEPLOYMENT\\ndef infer():\\n  engine = load_engine('{idea}_model.plan')\\n  return engine.execute(input_data)", 
        "14_FILESYSTEM_LOGS": "// BLACKBOX 400Hz\\nvoid log_data() { sd_write(imu_data, timestamp); }" 
    } 
    current_code = db.get(nodo_solicitado, "// Selecciona un nodo del arbol") 
    h = "<html><head><title>MAIA II - EXPERT MODE</title><style>" 
    h += "body{background:#0a0a0a; color:#0ff; font-family:monospace; padding:10px; margin:0;}" 
    h += ".panel{border:1px solid #0ff; padding:15px; background:#001111; margin-bottom:10px;}" 
    h += ".flex{display:flex; gap:15px;} .col-tree{width:30%;} .col-code{width:70%;}" 
    h += ".tree{background:#000; border:1px solid #333; height:600px; overflow-y:auto; padding:10px;}" 
    h += ".code-window{background:#000; color:#0f0; padding:20px; border-left:4px solid #f0f; height:600px; overflow-y:scroll; white-space:pre-wrap; word-wrap:break-word;}" 
    h += "summary{color:#ffff00; cursor:pointer; font-weight:bold; padding:5px; border-bottom:1px solid #222;}" 
    h += "button{padding:8px 15px; cursor:pointer; border:none; margin:2px; font-weight:bold;}" 
    h += ".btn-gen{background:#0ff; color:#000;} .btn-node{background:none; color:#0f0; border:none; text-align:left; width:100%; cursor:pointer;}" 
    h += ".btn-node:hover{background:#003333;}" 
    h += ".hw-tag{display:inline-block; background:rgba(0,255,255,0.1); padding:5px; border:1px solid #0ff; margin-right:5px; font-size:0.8em;}" 
    h += "</style></head><body>" 
    h += "<h1>[ M.A.I.A. II - SISTEMA INTEGRAL DE INGENIERIA ]</h1>" 
    h += "<div class='panel'><h2>GENERADOR DE DRONES (CUALQUIER MISION)</h2>" 
    h += "<form method='post'><input name='drone_idea' value='" + idea + "' style='width:50%; background:#000; color:#0ff; border:1px solid #0ff; padding:10px;'>" 
    h += "<button type='submit' class='btn-gen'>GENERAR EXPEDIENTE</button>" 
    h += "<button type='button' style='background:red; color:white;' onclick=\\\"window.speechSynthesis.speak(new SpeechSynthesisUtterance('Alex, todos los nodos actualizados para la mision " + idea + ".'))\\\">VOZ MAIA</button></div>" 
    h += "<div class='panel'><h2>MODULO DE CONSTRUCCION</h2>" 
    h += "<span class='hw-tag'>CHASIS: Carbono M40J</span><span class='hw-tag'>ESC: CAN-FD</span><span class='hw-tag'>BMS: 12S Redundant</span></div>" 
    h += "<div class='flex'><div class='col-tree'><div class='panel'><h3>ARBOL DE 14 NODOS</h3><div class='tree'>" 
    for n in db.keys(): 
        h += f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button class='btn-node'>?? {n}</button></form>" 
    h += "</div></div><div class='panel'><h3>PROJECT LAB</h3><button style='background:#f0f;'>BUSCADOR</button><button style='background:#f0f;'>NUEVO</button></div></div>" 
    h += "<div class='col-code'><div class='panel'><h3>VISOR VERTICAL: " + nodo_solicitado + "</h3>" 
    h += "<div class='code-window'>" + current_code + "</div></div></div></div>" 
    h += "</form></body></html>" 
    return render_template_string(h) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 
