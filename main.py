# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

try:
    from software_engine import get_node_library
    from hardware_engine import get_hardware_specs
    from strategic_engine import get_strategic_analysis
except:
    def get_node_library(x): return {}
    def get_hardware_specs(x): return {"Error": "No se cargó el motor de HW"}
    def get_strategic_analysis(x): return {}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    db = get_node_library(idea)
    hw_data = get_hardware_specs(idea)
    strat_data = get_strategic_analysis(idea)
    current_code = db.get(target, "// KERNEL MAIA II") if idea and target else "// AGUARDANDO COMANDO..."

    h = f"""
    <html><head><title>MAIA II - V17 FINAL</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ background:#000202; color:#0ff; font-family:monospace; margin:0; overflow:hidden; font-size:12px; }}
        .header {{ display:flex; align-items:center; gap:10px; padding:12px; background:rgba(0,30,30,0.95); border-bottom:2px solid #0ff; }}
        .btn-ui {{ background:none; border:1px solid #0ff; color:#0ff; padding:7px 12px; cursor:pointer; font-weight:bold; font-size:10px; }}
        
        /* BOTÓN VOZ ESPECIAL */
        #voice-btn {{ background:#ff0000; color:#fff; border:none; transition: 0.3s; }}
        
        .grid-master {{ display:grid; grid-template-columns: 25% 40% 35%; gap:10px; height:85vh; padding:10px; box-sizing:border-box; }}
        .panel {{ border:1px solid #0ff2; background:rgba(0,10,10,0.9); padding:10px; overflow-y:auto; border-radius:4px; }}
        
        /* EXPLICACIÓN HARDWARE */
        .hw-list {{ display:flex; flex-direction:column; gap:8px; }}
        .hw-item {{ border-left:2px solid #0f0; background:rgba(0,255,0,0.05); padding:8px; }}
        .hw-title {{ color:#0f0; font-weight:bold; font-size:11px; text-transform:uppercase; }}
        .hw-desc {{ color:#ccc; font-size:10px; margin-top:3px; }}

        #proto-container {{ width:100%; height:100%; min-height:400px; background:#000; }}
        .code-box {{ background:#000; color:#39ff14; padding:10px; font-size:10px; border:1px solid #f0f3; white-space:pre-wrap; overflow-y:auto; }}

        #chat-container {{ position:fixed; bottom:10px; right:10px; width:250px; border:2px solid #0ff; background:#001a1a; z-index:1000; }}
        #chat-header {{ background:#0ff; color:#000; padding:5px; font-weight:bold; cursor:pointer; }}
    </style>
    </head><body>
    
    <div class='header'>
        <b style="font-size:1.3em; color:#0ff;">MAIA II</b>
        <form method='post' style="display:flex; flex-grow:1; gap:10px; margin:0;">
            <input name='drone_idea' style="background:#000; color:#0ff; border:1px solid #0ff; padding:8px; flex-grow:1;" placeholder='Misión...' value='{idea}'>
            <button type='submit' style="background:#0ff; border:none; padding:8px 15px; font-weight:bold;">GENERAR</button>
        </form>
        <button class='btn-ui' onclick="window.location.href='/'">LIMPIAR</button>
        <button class='btn-ui' onclick="alert('Memoria Sincronizada')">MEMORIA</button>
        <button class='btn-ui' id="voice-btn" onclick="activateMaiaVoice()">VOZ MAIA II: OFF</button>
    </div>

    <div class='grid-master'>
        <div class="panel">
            <h4 style="color:#f0f; border-bottom:1px solid #f0f2;">INTELIGENCIA ESTRATÉGICA</h4>
            {"".join([f"<div style='margin-bottom:10px;'><b style='color:#0ff;'>{k}</b><p style='color:#ccc; font-size:10px;'>{v}</p></div>" for k,v in strat_data.items()])}
        </div>

        <div class="panel" style="padding:0; overflow:hidden;">
            <div id="proto-container"></div>
        </div>

        <div class="panel">
            <h4 style="color:#0ff; margin-top:0;">HARDWARE: 8 CATEGORÍAS TÉCNICAS</h4>
            <div class="hw-list">
                {"".join([f"<div class='hw-item'><div class='hw-title'>{k}</div><div class='hw-desc'>{v}</div></div>" for k,v in hw_data.items()]) if idea else "<p>Aguardando misión para detallar componentes...</p>"}
            </div>
            
            <h4 style="color:#f0f; margin-top:15px;">NODOS DE SOFTWARE</h4>
            <div style="max-height:80px; overflow-y:auto; border-bottom:1px solid #f0f2; margin-bottom:5px;">
                {"".join([f"<form method='post' style='margin:0;'><input type='hidden' name='drone_idea' value='{idea}'><input type='hidden' name='target_node' value='{n}'><button type='submit' style='background:none; color:#0f0; border:none; cursor:pointer; font-size:10px;'>▶ {n}</button></form>" for n in sorted(db.keys())])}
            </div>
            <div class="code-box">{current_code}</div>
        </div>
    </div>

    <div id="chat-container">
        <div id="chat-header" onclick="document.getElementById('chat-b').style.display='block'">CHAT MAIA II ▲</div>
        <div id="chat-b" style="display:none; height:150px; padding:10px; overflow-y:auto; font-size:10px; color:#0f0;">
            MAIA: Protocolo de chat listo...
        </div>
    </div>

    <script>
        // LÓGICA DE VOZ: ROJO -> VERDE + SALUDO
        function activateMaiaVoice() {{
            const btn = document.getElementById('voice-btn');
            btn.style.background = "#00ff00";
            btn.style.color = "#000";
            btn.innerText = "VOZ MAIA II: ON";
            
            const msg = new SpeechSynthesisUtterance("Sistemas de voz activos. Hola Alex, estoy lista para configurar tu dron.");
            msg.lang = 'es-ES';
            window.speechSynthesis.speak(msg);
        }}

        // RENDER DEL DRON (ASEGURADO)
        const container = document.getElementById('proto-container');
        if ('{idea}' !== '' && container) {{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth/container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{antialias:true, alpha:true}});
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            const droneGroup = new THREE.Group();
            // Cuerpo
            const body = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.2, 0.8), new THREE.MeshStandardMaterial({{color:0x222222}}));
            droneGroup.add(body);
            
            // Hélices
            [1,-1].forEach(x => [1,-1].forEach(z => {{
                const p = new THREE.Mesh(new THREE.TorusGeometry(0.3, 0.02, 16, 100), new THREE.MeshBasicMaterial({{color:0x00ff00, transparent:true, opacity:0.5}}));
                p.position.set(x*0.7, 0.1, z*0.7); p.rotation.x = Math.PI/2;
                droneGroup.add(p);
            }}));

            scene.add(droneGroup);
            scene.add(new THREE.PointLight(0x00ffff, 2, 100));
            scene.add(new THREE.AmbientLight(0xffffff, 0.5));
            camera.position.set(2, 3, 5); camera.lookAt(0,0,0);

            function animate() {{
                requestAnimationFrame(animate);
                droneGroup.rotation.y += 0.01;
                renderer.render(scene, camera);
            }}
            animate();
        }}
    </script>
    </body></html>
    """
    return render_template_string(h)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)