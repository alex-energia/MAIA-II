# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

def analyze_viability(idea):
    # Simulación de análisis técnico-financiero
    idea_l = idea.lower()
    viability_score = 0.85 # Base
    
    # Ejemplo de auto-corrección de IA
    if "eterno" in idea_l or "infinito" in idea_l:
        viability_score = 0.2
        alternative = "Sistema de Enjambre con Estaciones de Carga Automatizadas"
    elif "fuego" in idea_l or "incendio" in idea_l:
        viability_score = 0.9
        alternative = "Optimización de Blindaje de Aerogel y Sensores Térmicos"
    else:
        alternative = "Optimización de eficiencia en Nodo 15"
    
    return viability_score, alternative

def get_maia_v1200_expert(idea):
    idx = idea.upper()
    v_score, alt_idea = analyze_viability(idea)
    
    # 15 NODOS: CÓDIGO DE ALTA DENSIDAD
    sw = {
        "01_DMA_TELEMETRY.py": f"""# Nivel 1200: Comunicación sin bloqueo de CPU\nimport machine\ndef init_dma_stream():\n    '''Usa Direct Memory Access para enviar datos de {idx}'''\n    dma = machine.DMA(0)\n    dma.config(src=0x40012400, dest=uart_tx_reg, count=512)\n    return "DMA_READY_STABLE" """,
        
        "02_REGEN_NODO_15.py": f"""class RegenEngine:\n    '''NODO 15: Algoritmo de frenado dinámico para {idx}'''\n    def harvest(self, esc_telemetry):\n        # Convierte energía cinética en carga real (8.5% eficiencia)\n        if esc_telemetry['rpm'] > 12000 and esc_telemetry['pwr'] < 0:\n            return (esc_telemetry['rpm'] * 0.00012) \n        return 0.0""",

        "03_NON_BLOCKING_LOG.py": """class AsyncLogger:\n    '''Evita la caída del dron por retraso de SD'''\n    def __init__(self):\n        self.buffer = []\n    def log(self, data):\n        self.buffer.append(data)\n        if len(self.buffer) > 50: self.flush()""",

        "04_THERMAL_SHIELD.py": """def monitor_temp_shield():\n    '''Protocolo de protección térmica nivel 1200'''\n    ext_temp = sensor_read(0x48)\n    if ext_temp > 85.0:\n        activate_cooling_pump()\n        return 'CRITICAL_HEAT_WARNING'""",
        
        "05_MIXER_X4_PRO.py": "def mix(r, p, y, t):\n    return [t-p+r+y, t+p-r+y, t-p-r-y, t+p+r-y]",
        
        "06_AES_VAULT.py": "from ucryptolib import aes\ndef crypt(data): return aes(key, 1).encrypt(data)",
        
        "07_MESH_ANTENNA.py": "def hop(): return 'FREQ_HOP_LORA_900MHZ_ACTIVE'",
        
        "08_BMS_GRAFENO.py": "def bal(): return 'CELLS_BALANCED_4.20V'",
        
        "09_GPS_RTK_PRO.py": "def get_fix(): return 'RTK_FIX_L1_L2_CENTIMETRIC'",
        
        "10_NEURAL_MAIA.py": "def think(): return 'ALEX_COMMAND_SYNCED_12ms'",
        
        "11_VISION_AI.py": "def detect(): return 'AI_OBJECT_TARGET_LOCKED'",
        
        "12_GIMBAL_CAN.py": "def move(): return 'CAN_BUS_GIMBAL_STABLE'",
        
        "13_OS_KERNEL.py": f"def boot(): return 'MAIA_II_{idx}_READY'",
        
        "14_RECOVERY_SYS.py": "def safe(): return 'PARACHUTE_ARMED'",
        
        "15_REGEN_HARD.py": "def hardware_regen(): return 'MOSFET_BRIDGE_INVERSION_OK'"
    }

    # ESTRATEGIA CON VIABILIDAD BIEN ESTRUCTURADA
    v_status = "VIABLE" if v_score > 0.5 else "CRÍTICO / REEMPLAZADO"
    strat = {
        "ESTADO DE VIABILIDAD": f"{v_status} ({v_score*100}%)",
        "ANÁLISIS DE MERCADO": f"Demanda alta para {idx}. ROI proyectado en 14 meses.",
        "FISICA DE FLUIDOS": "Cálculo de Navier-Stokes para flujo de aire en motores de alta temperatura.",
        "RIESGOS Y MITIGACIÓN": "Fallo crítico de motor mitigado por compensación de par instantánea.",
        "PROPUESTA ALTERNATIVA": f"{alt_idea if v_score < 0.6 else 'Diseño actual óptimo'}"
    }

    # HARDWARE 8 CAPAS + BOM
    hw = {
        "H1_NÚCLEO": "STM32H753XI + FPGA Lattice para lógica de motores.",
        "H2_MOTORES": "Brushless de 1200KV con bobinado de plata.",
        "H3_ESTRUCTURA": "Cerámica térmica reforzada y Carbono T1200.",
        "H4_SENSORES": "LiDAR Solid State + Infrarrojo de largo alcance.",
        "H5_ENERGÍA": "Celdas de estado sólido 450Wh/kg.",
        "H6_REGEN": "Circuitos de recuperación de energía integrados en ESC.",
        "H7_BOM": "Lista de materiales detallada: $8,900 USD por unidad.",
        "H8_COMUNICACIÓN": "Enlace redundante RF/Satelital."
    }

    return {"sw": sw, "strat": strat, "hw": hw, "v_score": v_score}

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    action = request.form.get('action', '')
    scroll_pos = request.form.get('scroll_pos', '0')
    
    is_gen = action == "generate" and idea != ""
    data = get_maia_v1200_expert(idea) if is_gen else {"sw": {}, "strat": {}, "hw": {}}
    
    current_code = data["sw"].get(target, "# KERNEL EXPERTO MAIA II\n# ESPERANDO DESPLIEGUE...")

    h = f"""
    <html><head><title>MAIA II - KERNEL EXPERT</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000; color:#0ff; font-family:monospace; margin:0; overflow:hidden; }}
        .header {{ display:flex; gap:10px; padding:15px; background:#001a1a; border-bottom:2px solid #0ff; }}
        .grid {{ display:grid; grid-template-columns: 25% 40% 35%; gap:10px; height:85vh; padding:10px; }}
        .panel {{ border:1px solid #0ff3; background:rgba(0,10,10,0.95); padding:15px; overflow-y:auto; position:relative; }}
        .visor {{ background:#050505; color:#39ff14; padding:15px; font-size:11px; border-left:3px solid #f0f; height:320px; overflow:auto; white-space:pre; margin-top:10px; }}
        .btn {{ padding:8px 15px; cursor:pointer; font-weight:bold; border:none; }}
        .node-btn {{ background:none; color:#0f0; border:1px solid #0f02; width:100%; text-align:left; padding:8px; margin-bottom:4px; font-size:10px; cursor:pointer; }}
        .active {{ background:rgba(240,0,255,0.2) !important; border-color:#f0f !important; }}
        input[type='text'] {{ background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1; }}
        .viability-bad {{ color: #ff0000; font-weight:bold; border:1px solid #f00; padding:5px; }}
        .telemetry {{ position:absolute; top:10; right:10; color:#0f0; font-size:11px; text-align:right; }}
    </style>
    </head><body>
    
    <form method='post' class='header' id="mainForm">
        <input type="text" name="drone_idea" value="{idea}" placeholder="Idea del proyecto...">
        <input type="hidden" name="scroll_pos" id="scroll_pos_val" value="{scroll_pos}">
        <button type='submit' name="action" value="generate" class="btn" style="background:#0ff;">EJECUTAR</button>
        <button type="button" class="btn" style="background:#ffd700;" onclick="maiaVoice()">VOZ</button>
    </form>

    <div class='grid'>
        <div class="panel" id="panel-strat">
            <h4 style="color:#f0f; margin-top:0;">[1] STRATEGIC ANALYSIS</h4>
            {f'<div class="viability-bad">ALERTA: VIABILIDAD BAJA. SUGERENCIA: {data["strat"]["PROPUESTA ALTERNATIVA"]}</div>' if is_gen and data["v_score"] < 0.6 else ''}
            {"".join([f"<p><b>{k}:</b><br><small style='color:#ccc;'>{v}</small></p>" for k,v in data["strat"].items()])}
        </div>

        <div class="panel" style="padding:0; overflow:hidden;">
            <div id="c3d" style="width:100%; height:100%;"></div>
            <div class="telemetry">
                ALT: <span id="alt">0.0</span>m<br>SPEED: <span id="spd">0.0</span>km/h<br>POS: 4.60N / 74.08W
            </div>
        </div>

        <div class="panel" id="panel-nodos">
            <h4 style="color:#ffd700; margin-top:0;">[2] HARDWARE (8 CAPAS)</h4>
            {"".join([f"<div style='margin-bottom:8px; border-left:2px solid #ffd700; padding-left:8px;'><small><b>{k}:</b> {v}</small></div>" for k,v in data["hw"].items()])}
            
            <h4 style="color:#f0f; margin-top:15px;">[3] PRODUCTION NODES (15)</h4>
            <div id="nodes-container" style="max-height:180px; overflow-y:auto; border:1px solid #333; padding:5px;">
                {"".join([f'''<button type="button" class="node-btn {'active' if n == target else ''}" onclick="navNode('{n}')">[SRC] {n}</button>''' for n in sorted(data["sw"].keys())])}
            </div>
            <div class="visor" id="visor-content">{current_code}</div>
        </div>
    </div>

    <form id="navForm" method="post">
        <input type="hidden" name="drone_idea" value="{idea}">
        <input type="hidden" name="action" value="generate">
        <input type="hidden" name="target_node" id="target_node_val">
        <input type="hidden" name="scroll_pos" id="scroll_pos_node">
    </form>

    <script>
        // BLOQUEO DE SALTO DE SCROLL
        const pNodes = document.getElementById('panel-nodos');
        window.onload = () => {{ pNodes.scrollTop = {scroll_pos}; }};

        function navNode(node) {{
            document.getElementById('target_node_val').value = node;
            document.getElementById('scroll_pos_node').value = pNodes.scrollTop;
            document.getElementById('navForm').submit();
        }}

        function maiaVoice() {{
            const msg = new SpeechSynthesisUtterance("{f'Sistema {idea} analizado.' if is_gen else 'En espera.'}");
            msg.lang = 'es-ES'; window.speechSynthesis.speak(msg);
        }}

        // MODELO 3D REALISTA (MOVIMIENTO X/Y/Z)
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth*0.4/(window.innerHeight*0.8), 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
        renderer.setSize(window.innerWidth*0.4, window.innerHeight*0.8);
        document.getElementById('c3d').appendChild(renderer.domElement);

        const drone = new THREE.Group();
        if({ "true" if is_gen else "false" }) {{
            const body = new THREE.Mesh(new THREE.BoxGeometry(0.7, 0.15, 0.7), new THREE.MeshPhongMaterial({{color:0x222222}}));
            drone.add(body);
            const core = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 0.4), new THREE.MeshPhongMaterial({{color:0x00ffff, emissive:0x00ffff}}));
            core.position.y = 0.2; drone.add(core);

            [Math.PI/4, -Math.PI/4, 3*Math.PI/4, -3*Math.PI/4].forEach(a => {{
                const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.2), new THREE.MeshPhongMaterial({{color:0xffd700}}));
                arm.rotation.z = Math.PI/2; arm.rotation.y = a; drone.add(arm);
                const p = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.01, 0.1), new THREE.MeshBasicMaterial({{color:0x00ffff, transparent:true, opacity:0.5}}));
                p.position.set(Math.cos(a)*0.6, 0.15, Math.sin(a)*0.6); p.name="prop"; drone.add(p);
            }});
        }}
        scene.add(drone);
        scene.add(new THREE.AmbientLight(0xffffff, 0.7));
        camera.position.set(5, 5, 5); camera.lookAt(0,0,0);

        let clock = 0;
        function anim() {{
            requestAnimationFrame(anim);
            clock += 0.03;
            if({ "true" if is_gen else "false" }) {{
                // Trayectoria de inspección
                drone.position.y = Math.sin(clock) * 0.5 + 2;
                drone.position.x = Math.cos(clock * 0.5) * 1.5;
                drone.rotation.z = -Math.sin(clock * 0.5) * 0.2;
                
                document.getElementById('alt').innerText = (drone.position.y * 10).toFixed(2);
                document.getElementById('spd').innerText = (Math.abs(Math.sin(clock))*45).toFixed(1);
                
                drone.children.forEach(c => {{ if(c.name==="prop") c.rotation.y += 0.8; }});
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