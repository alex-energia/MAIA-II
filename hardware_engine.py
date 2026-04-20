# -*- coding: utf-8 -*-
# hardware_engine.py - ARQUITECTURA GLI-V11 (FULL INJECTION)

def get_hardware_specs(idea):
    """Genera las 8 categorías críticas de hardware GLI."""
    if not idea: return {}
    
    return {
        "01_NÚCLEO_ESTRUCTURAL": [
            "Chasis Monocasco Carbono M40J", 
            "Blindaje Grafeno EMI", 
            "Titanio Grado 5"
        ],
        "02_PROPULSIÓN_Y_DINÁMICA": [
            "Motores GaN-Core 750KV", 
            "Hélices Paso Variable", 
            "ESC Nitruro de Galio"
        ],
        "03_ENERGÍA_ESTADO_SÓLIDO": [
            "Celdas 450Wh/kg", 
            "BMS Balanceo Activo", 
            "Carga Rápida 10C"
        ],
        "04_PERCEPCIÓN_Y_VISIÓN": [
            "Lidar Ouster OS2-128", 
            "Térmica FLIR Boson", 
            "Radar 77GHz"
        ],
        "05_AVIÓNICA_Y_BÚNKER_IA": [
            "STM32H7 Triple Núcleo", 
            "NPU 100 TOPS", 
            "TPM 2.0 Encriptado"
        ],
        "06_COMUNICACIONES_MESH": [
            "Silvus MIMO SC4200", 
            "Starlink Mini", 
            "Anti-Jamming FHSS"
        ],
        "07_NAVEGACIÓN_INERCIAL": [
            "FOG (Giro Fibra Óptica)", 
            "RTK Triple Banda", 
            "Láser Centimétrico"
        ],
        "08_SISTEMAS_DE_MISIÓN": [
            "Payload Dropper Mag", 
            "Foco 60K Lúmenes", 
            "Megafonía 125dB"
        ]
    }

def calculate_performance(idea):
    """Calculadora dinámica interactiva."""
    if not idea:
        return {"PESO": "---", "EMPUJE": "---", "TWR": "---", "VUELO": "---", "CARGA": "---"}
    
    # Lógica de cálculo basada en la intención
    es_pesado = "pesado" in idea.lower() or "carga" in idea.lower()
    peso = 8.5 if es_pesado else 4.8
    empuje = 85.0 if es_pesado else 52.0
    vuelo = 45 if es_pesado else 65
    
    return {
        "PESO": f"{peso}kg",
        "EMPUJE": f"{empuje}kg",
        "TWR": f"{round(empuje/peso, 2)}:1",
        "VUELO": f"{vuelo}min",
        "CARGA": f"{round(empuje-(peso*1.5), 1)}kg"
    }

def get_hardware_integrity_hash():
    return "GLI-V11-8-LAYER-STRIKE"
