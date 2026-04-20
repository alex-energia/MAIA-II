# -*- coding: utf-8 -*-
# main.py - KERNEL MAIA II: RESTAURACIÓN TOTAL DE INTERFAZ
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
except:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {}
    def get_strategic_analysis(x): return {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    db = get_node_library(idea)
    # Forzamos la obtención de las 8 categorías de hardware
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    
    current_code = db.get(target, "// KERNEL ACTIVO") if idea and target else "// AGUARDANDO COMANDO..."

    h = f"""
    <html><head><title>MAIA II - INTERFAZ TOTAL</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:'Segoe UI', monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; gap:10px; padding:12px; background:rgba(0,30,30,0.95); border-bottom:2px solid #0ff; z-index:100; }}
        .input-idea {{ background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1; outline:none; }}
        
        .btn-ui {{ background:none; border:1px solid #0ff; color:#0ff; padding:7px 12px; cursor:pointer; font-weight:bold; font-size:10px; text-transform:uppercase; }}
        .btn-active {{ background:#0ff; color:#000; border:none; padding:8px 15px; font-weight:bold; cursor:pointer; }}
        
        .grid-master {{ display:grid; grid-template-columns: 25% 45% 30%; gap:10px; height:85vh; padding:10px; box-sizing:border-box; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,10,10,0.9); padding:10px; overflow-y:auto; border-radius:4px; display:flex; flex-direction:column; }}
        
        /* HARDWARE 8 CATEGORÍAS */
        .hw-grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:5px; margin-bottom:10px; }}
        .hw-card {{ border:1px solid #0f0; background:rgba(0,255,0,0.05); padding:6px; font-size:9px; text-align:center; color:#0f0; font-weight:bold; }}

        /* CHAT MAIA */
        #chat-container {{ position:fixed; bottom:10px; right:10px; width:280px; background:rgba(0,20,20,0.95); border:2px solid #0ff; border-radius:5px; z-index:1000; }}
        #chat-header {{ background:#0ff; color:#000; padding:8px; font-weight:bold; cursor:pointer; display:flex; justify-content:space-between; }}
        #chat-body {{ height:200px; padding:10px; overflow-y:auto; font-size:10px; display:none; }}
        #chat-input {{ width:100%; background:#000; color:#0ff; border:none; border-top:1px solid #0ff3; padding:8px; box-sizing:border-box; }}

        #proto-container {{ width:100%; height:100%; background:black; }}
        .code-box {{ background:#000; color:#39ff14; padding:10px; font-size:10px; border-left:2px solid #f0f; white-space:pre-wrap; flex-grow:1; overflow-y:auto; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.3em;">MAIA II</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' class='input-idea' placeholder='Misión del Dron...' value='{idea}'>
            <button type='submit' class='btn-active'>DESPLEGAR</button>
        </form>
        <button class='btn-ui' onclick="window.location.href='/'">LIMPIAR</button>
        <button class='btn-ui' onclick="alert('Memoria Sincronizada')">MEMORIA</button>
        <button class='btn-ui' id="voice-btn" onclick="toggleVoice()">VOZ: OFF</button>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#f0f; border-bottom:1px solid #f0f3; margin:0 0 10px 0;">ESTRATEGIA</h4>
            {"".join([f"<div style='margin-bottom:8px;'><b style='color:#0ff; font-size:10px;'>{k}</b><p style='color:#ccc; margin:2px 0;'>{v}</p></div>" for k,v in strat_data.items()])}
        </div>

        <div class="panel" style="padding:0; position:relative;">
            <div id="proto-container"></div>
        </div>

        <div class="panel">
            <h4 style="color:#0ff; margin:0 0 10px 0;">HARDWARE (8 CAPAS)</h4>
            <div class="hw-grid">
                {"".join([f"<div class='hw-card'>{k.upper()}</div>" for k in hw_data.keys()]) if hw_data else "<div class='hw-card' style='grid-column: span 2;'>ESPERANDO DATOS...</div>"}
            </div>
            
            <h4 style="color:#f0f; margin:10px 0 5px 0;">SOFTWARE NODES</h4>
            <div style="max-height:100px; overflow-y:auto; margin-bottom:10px; border-bottom:1px solid #f0f2;">
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:11px;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            <div class="code-box">{current_code}</div>
        </div>
    </div>

    <div id="chat-container">
        <div id="chat-header" onclick="toggleChat()">
            <span>CHAT MAIA II</span><span>▲</span>
        </div>
        <div id="chat-body">
            <div id="chat-log">MAIA: Sistema listo. Esperando órdenes de ingeniería...</div>
        </div>
        <input type="text" id="chat-input" placeholder="Escribe un comando..." onkeydown="if(event.key==='Enter') sendMsg(this)">
    </div>

    <script>
        function toggleChat() {{
            const body = document.getElementById('chat-body');
            body.style.display = body.style.display === 'block' ? 'none' : 'block';
        }}

        function sendMsg(i) {{
            const log = document.getElementById('chat-log');
            log.innerHTML += `<div style="color:#f0f; margin-top:5px;">Alex: ${{i.value}}</div>`;
            setTimeout(() => {{
                log.innerHTML += `<div style="color:#0f0;">MAIA: Procesando módulo ${{i.value}}...</div>`;
                log.scrollTop = log.scrollHeight;
            }}, 500);
            i.value = '';
        }}

        function toggleVoice() {{
            const btn = document.getElementById('voice-btn');
            if(btn.innerText === "VOZ: OFF") {{
                btn.innerText = "VOZ: ON";
                btn.style.background = "#0f0"; btn.style.color = "#000";
                speechSynthesis.speak(new SpeechSynthesisUtterance("Sistemas de voz activos. Hola Alex."));
            }} else {{
                btn.innerText = "VOZ: OFF";
                btn.style.background = "none"; btn.style.color = "#0ff";
                speechSynthesis.cancel();
            }}
        }}

        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);
            const droneGroup = new THREE.Group();
            const body = new THREE.Mesh(new THREE.OctahedronGeometry(0.5, 0), new THREE.MeshStandardMaterial({{color:0x111111, metalness:1}}));
            body.scale.y = 0.4; droneGroup.add(body);
            scene.add(droneGroup); scene.add(new THREE.PointLight(0x00ffff, 2, 100));
            camera.position.set(0, 4, 8); camera.lookAt(0,0,0);
            function animate() {{ requestAnimationFrame(animate); droneGroup.rotation.y += 0.005; renderer.render(scene, camera); }}
            animate();
        }}
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
