# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template_string, request
from software_engine import get_node_library
from hardware_engine import get_hardware_specs  # <--- IMPORTACIÓN DEL HARDWARE

app = Flask(__name__)

# --- PROTECCIÓN DE SOFTWARE: ESTADO GLOBAL ---
# Este bloque asegura que el software esté cargado y sellado
SOFTWARE_INTEGRITY_KEY = "GLI-ALPHA-LOCKED"

@app.route('/', methods=['GET', 'POST'])
def home():
    idea = request.form.get('drone_idea', '')
    target = request.form.get('target_node', '')
    
    # Cargar Hardware y Software por separado
    hw = get_hardware_specs()
    db = get_node_library(idea)
    
    # ... (resto de la lógica del visor) ...

    # SECCIÓN DEL MÓDULO DE CONSTRUCCIÓN ACTUALIZADA
    h_hw = f"""
    <div class='panel'>
        <h3>MODULO DE CONSTRUCCIÓN (HARDWARE EXTRAÍDO)</h3>
        <div class='hw-spec'>
            <span><b>ESTRUCTURA:</b> {hw['FRAME']['model']}</span>
            <span><b>MOTORES:</b> {hw['PROPULSION']['motors']}</span>
            <span><b>RADIO:</b> {hw['COMMS']['radio']}</span>
            <span><b>ENERGÍA:</b> {hw['ENERGY_SYSTEM']['battery']}</span>
        </div>
    </div>
    """
    # (El resto del HTML sigue igual, solo inyectamos h_hw donde corresponde)
