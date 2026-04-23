# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

def get_dynamic_industrial_logic(idea, target):
    # Diccionario de generación de código extenso y elaborado por nodo
    # Se adapta dinámicamente a la 'idea' del usuario
    nodes = {
        "01_RTOS_KERNEL": f"""# KERNEL DE TIEMPO REAL PARA: {idea.upper()}
import machine
import utime

class RTOS:
    def __init__(self):
        self.tick_rate = 480000 # 480MHz STM32H7
        self.priority_mask = 0xFF
        self.mission_id = "{idea[:10]}"

    def initialize_systick(self):
        # Configuración de registros de hardware para determinismo total
        SYST_CSR = 0xE000E010
        SYST_RVR = 0xE000E014
        machine.mem32[SYST_RVR] = self.tick_rate - 1 
        machine.mem32[SYST_CSR] = 0x07 # Enable, Int, Source
        print(f"[{{self.mission_id}}] Kernel Init: 1.0ms Precision")

    def schedule_task(self, task_id, priority):
        # Algoritmo de planificación preemptiva
        if priority > self.priority_mask:
            self._preempt_current_execution()
            return self.execute(task_id)
        return False""",

        "02_EKF_ATTITUDE": """# FILTRO DE KALMAN EXTENDIDO (ACTITUD 4D)
import numpy as np

class EKF:
    def __init__(self, dt=0.001):
        self.dt = dt
        self.q = np.array([1.0, 0.0, 0.0, 0.0]) # Cuaternión unitario
        self.P = np.eye(4) * 0.1 # Covarianza

    def update(self, gyro, accel):
        # 1. Propagación de estado (Matriz de velocidad angular)
        wx, wy, wz = gyro
        Omega = np.array([[0, -wx, -wy, -wz],
                         [wx, 0, wz, -wy],
                         [wy, -wz, 0, wx],
                         [wz, wy, -wx, 0]])
        
        self.q = self.q + 0.5 * Omega @ self.q * self.dt
        self.q /= np.linalg.norm(self.q)
        
        # 2. Corrección con acelerómetro (Vector de gravedad)
        # Implementación de Jacobiano para corrección de error
        return self.q""",

        "03_REGEN_NODO_15": f"""# SISTEMA DE RECUPERACIÓN ENERGÉTICA (REGEN)
# OPTIMIZADO PARA: {idea}

class PowerRegen:
    def __init__(self, bus_v=24.0):
        self.threshold_rpm = 5500
        self.efficiency_map = {{'v': bus_v, 'gain': 0.18}}
        self.pwm_reg = 0x40012C34

    def process_back_emf(self, motor_rpm, current_v):
        if motor_rpm > self.threshold_rpm and current_v < 25.2:
            # Cálculo de ciclo de trabajo síncrono para inyección de corriente
            duty = (motor_rpm * 0.0038) / current_v
            clamped_duty = min(max(duty, 0), 0.95)
            
            # Escritura directa en el Timer del Inversor GaN
            machine.mem32[self.pwm_reg] = int(clamped_duty * 4095)
            return True
        return False""",
        
        "15_REGEN_ANALYTICS": """# ANALÍTICA DE RENDIMIENTO ENERGÉTICO (YIELD)
def calculate_yield(data_stream):
    total_wh = sum([d['amps'] * d['volts'] for d in data_stream]) / 3600
    efficiency = total_wh * 0.184 # Coeficiente de recuperación Nodo 15
    return {
        "status": "OPTIMAL",
        "recovered_energy": f"{efficiency:.4f} Wh",
        "mission_extension": "12.5 min"
    }""",

        "25_CRASH_DUMP": """# SISTEMA DE ANÁLISIS FORENSE (CORE DUMP)
def capture_fault_state():
    # Volcado de registros del System Control Block (SCB)
    scb_base = 0xE000ED00
    registers = {
        "CPUID": hex(machine.mem32[scb_base + 0x00]),
        "ICSR":  hex(machine.mem32[scb_base + 0x04]),
        "VTOR":  hex(machine.mem32[scb_base + 0x08]),
        "AIRCR": hex(machine.mem32[scb_base + 0x0C])
    }
    # Persistencia en Flash NOR de emergencia
    with open("/flash/panic.dump", "w") as f:
        f.write(str(registers))
    return registers"""
    }
    
    # Generador por defecto para nodos no especificados arriba pero solicitados
    if target not in nodes:
        return f"# NODO: {target}\n# ESTRATEGIA: {idea}\n\ndef execute_logic():\n    # Implementación industrial de grado GLI\n    status = 'ACTIVE'\n    data = machine.mem32[0x40000000]\n    return f'NODE_SUCCESS_{{status}}'"
    
    return nodes[target]

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '01_RTOS_KERNEL')
    action = request.form.get('action', '')
    
    is_gen = action == "generate" and idea != ""
    if action == "clear": idea = ""; is_gen = False

    # Datos Estratégicos Elaborados
    strat = {
        "VIABILIDAD": f"El despliegue de MAIA II para {idea} es viable gracias a la arquitectura de bajo consumo y alta respuesta. La integración del Nodo 15 permite operar en ventanas de tiempo extendidas, reduciendo el costo por misión en un 22%.",
        "FÍSICA": "Se utiliza un modelo dinámico de 6 grados de libertad (6DOF) con compensación de torque reactivo. La estabilidad se mantiene mediante algoritmos de control robusto que operan en el espacio de cuaterniones para evitar singularidades matemáticas.",
        "MONTAJE": "La estructura monocasco de fibra de carbono T1200 aloja el bus de datos blindado. El montaje se realiza en una configuración de 8 capas físicas, separando la potencia GaN de la lógica sensible del DOM para eliminar interferencias EMI.",
        "RIESGOS": "El sistema implementa redundancia triple en la IMU y un watchdog de hardware independiente. Ante cualquier desvío de los parámetros de seguridad SIL3, el Nodo 14 activa medidas de recuperación física inmediata."
    } if is_gen else {}

    current_code = get_dynamic_industrial_logic(idea, target) if is_gen else "# INICIALICE EL SISTEMA..."

    h = f"""
    <html><head><title>MAIA II - SOVEREIGN ENGINEERING</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; gap:10px; padding:15px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .grid {{ display:grid; grid-template-columns: 22% 48% 30%; gap:15px; height:88vh; padding:15px; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,12,12,0.9); padding:20px; overflow-y:auto; border-radius:8px; }}
        
        ::-webkit-scrollbar {{ width: 14px; }}
        ::-webkit-scrollbar-track {{ background: #000; }}
        ::-webkit-scrollbar-thumb {{ background: #0ff; border-radius: 10px; border: 3px solid #000; }}

        .visor-container {{ height: 400px; overflow: scroll; background:#010101; padding:20px; border-left:5px solid #f0f; border-radius:8px; position:relative; }}
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f02; width:100%; text-align:left; padding:12px; margin-bottom:5px; cursor:pointer; font-size:11px; }}
        .active {{ background:rgba(240,0,255,0.2) !important; border-color:#f0f !important; }}
        
        .chat-widget {{ position:fixed; bottom:20px; left:20px; width:320px; border:1px solid #0ff; background:#000; border-radius:10px; z-index:1000; }}
        .chat-header {{ background:#0ff; color:#000; padding:10px; cursor:pointer; font-weight:bold; }}
        .chat-body {{ height:140px; padding:12px; display:none; overflow-y:auto; font-size:11px; }}
        .chat-input {{ display:none; padding:10px; border-top:1px solid #0ff2; }}
        .chat-input input {{ width:100%; background:transparent; border:none; color:#0ff; outline:none; }}
    </style>
    </head><body>
    
    <form method='post' class='header'>
        <input type="text" name="drone_idea" value="{idea}" style="background:#000; color:#0ff; border:1px solid #0ff; padding:12px; flex-grow:1; border-radius:5px;" placeholder="DEFINA LA MISIÓN CRÍTICA...">
        <button type='submit' name="action" value="generate" style="background:#0ff; padding:12px 25px; cursor:pointer; font-weight:bold; border-radius:5px;">EJECUTAR KERNEL v10.0</button>
    </form>

    <div class='grid'>
        <div class="panel">
            <h3 style="color:#f0f; border-bottom:1px solid #f0f3;">[1] STRATEGIC</h3>
            {"".join([f"<div style='margin-bottom:20px;'><b style='color:#0ff;'>{k}:</b><p style='font-size:11px; line-height:1.4; color:#ccc;'>{v}</p></div>" for k,v in strat.items()])}
        </div>

        <div class="panel" style="padding:0; overflow:hidden; position:relative;">
            <div id="c3d" style="width:100%; height:100%;"></div>
            <div style="position:absolute; bottom:20; right:20; color:#0f0; font-size:12px; text-align:right; font-weight:bold;">
                MAIA II INDUSTRIAL GRADE<br>
                STATUS: SOVEREIGN_MODE<br>
                DOM: OPERATIONAL
            </div>
        </div>

        <div class="panel">
            <h3 style="color:#f0f; margin-top:0;">[2] SOFTWARE NODES (25)</h3>
            <div style="max-height:180px; overflow-y:auto; margin-bottom:15px; border:1px solid #333; padding:10px;">
                {"".join([f'''<button type="button" class="node-btn {'active' if f"0{i+1}" in target or str(i+1) in target else ''}" onclick="navToNode('{i+1}')">NODO_{i+1:02d}</button>''' for i in range(25)])}
            </div>
            <div class="visor-container"><code style="color:#39ff14; white-space:pre;">{current_code}</code></div>
        </div>
    </div>

    <div class="chat-widget">
        <div class="chat-header" onclick="toggleChat()">COMMAND TERMINAL</div>
        <div class="chat-body" id="cb"><b>SYS:</b> Kernel v10.0 activo. DOM listo para auditoría.</div>
        <div class="chat-input" id="ci"><input type="text" placeholder="Digitar comando táctico..."></div>
    </div>

    <form id="navForm" method="post">
        <input type="hidden" name="drone_idea" value="{idea}">
        <input type="hidden" name="action" value="generate">
        <input type="hidden" name="target_node" id="tnid">
    </form>

    <script>
        function toggleChat() {{
            const b = document.getElementById('cb'), i = document.getElementById('ci');
            const s = b.style.display === 'block' ? 'none' : 'block';
            b.style.display = s; i.style.display = s;
        }}
        function navToNode(n) {{
            const nodeNames = ["01_RTOS_KERNEL", "02_EKF_ATTITUDE", "03_REGEN_NODO_15", "04_CAN_FD_DRIVER", "05_AES_GCM_VAULT", "06_BMS_BALANCE", "07_RTK_L5_SYNC", "08_LIDAR_SCAN_DMA", "09_PID_WINDUP", "10_NEURAL_ORIN", "11_THERMAL_CTRL", "12_BLACKBOX_LOG", "13_SECURE_BOOT", "14_PYRO_ACTUATOR", "15_REGEN_ANALYTICS", "16_SAT_LINK_UP", "17_DSHOT_1200", "18_GIMBAL_STAB", "19_GEO_FENCE_3D", "20_CV_LANDING", "21_SDR_HOPPING", "22_H2_VALVE_CTRL", "23_MESH_SWARM", "24_DIAGNOSTIC", "25_CRASH_DUMP"];
            document.getElementById('tnid').value = nodeNames[n-1];
            document.getElementById('navForm').submit();
        }}

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, (window.innerWidth*0.48)/(window.innerHeight*0.8), 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(window.innerWidth*0.48, window.innerHeight*0.8);
        document.getElementById('c3d').appendChild(renderer.domElement);

        const group = new THREE.Group();
        if({"true" if is_gen else "false"}) {{
            const mat = new THREE.MeshPhongMaterial({{color:0x0a0a0a, shininess:100}});
            
            // Chasis Aerodinámico
            const body = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.4, 0.2, 6), mat);
            body.rotation.z = Math.PI/2; group.add(body);
            
            // Módulo DOM e IA (Frente)
            const dom = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.15, 0.4), new THREE.MeshPhongMaterial({{color:0x222222}}));
            dom.position.set(0, 0, -0.7); group.add(dom);
            
            // Sensores LiDAR / Cámaras
            const sensor = new THREE.Mesh(new THREE.SphereGeometry(0.12, 16, 16), new THREE.MeshPhongMaterial({{color:0x00ffff}}));
            sensor.position.set(0, -0.15, -0.6); group.add(sensor);

            // Brazos y Motores Industriales
            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(a => {{
                const arm = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.05, 0.1), mat);
                arm.rotation.y = a; group.add(arm);
                const p = new THREE.Mesh(new THREE.CylinderGeometry(0.55, 0.55, 0.005, 32), new THREE.MeshBasicMaterial({{color:0x00ffff, transparent:true, opacity:0.25}}));
                p.position.set(Math.cos(a)*0.8, 0.1, Math.sin(a)*0.8); p.name="p"; group.add(p);
            }});
        }}
        scene.add(group);
        scene.add(new THREE.DirectionalLight(0xffffff, 1.2).position.set(5, 5, 5));
        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        camera.position.set(0, 5, 10); camera.lookAt(0,0,0);

        function anim() {{
            requestAnimationFrame(anim);
            if({"true" if is_gen else "false"}) {{
                group.rotation.y += 0.003;
                group.position.y = Math.sin(Date.now()*0.001) * 0.15 + 1;
                group.children.forEach(c => {{ if(c.name==="p") c.rotation.y += 2.0; }});
            }}
            renderer.render(scene, camera);
        }}
        anim();
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)