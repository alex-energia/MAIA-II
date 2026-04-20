# -*- coding: utf-8 -*-
# hardware_engine.py - STANDAR GLI-V11

def calculate_performance(idea):
    """Calculadora interactiva inmune a errores."""
    if not idea:
        return {"Peso": "0.0kg", "Empuje": "0.0kg", "TWR": "0.0", "Vuelo": "0min"}
    
    # Lógica dinámica básica
    i = idea.lower()
    p = 8.5 if "pesado" in i else 4.8
    e = 82.0 if "pesado" in i else 51.5
    v = 45 if "pesado" in i else 65
    
    return {
        "Peso": f"{p}kg",
        "Empuje": f"{e}kg",
        "TWR": f"{round(e/p, 2)}:1",
        "Vuelo": f"{v}min"
    }

def get_hardware_specs(idea):
    """Las 8 capas críticas de hardware."""
    if not idea: return {}
    return {
        "01 ESTRUCTURA": ["Monocasco Carbono M40J", "Blindaje Grafeno", "Titanio Grado 5"],
        "02 PROPULSIÓN": ["Motores GaN-Core", "Hélices Paso Variable", "ESC Nitruro Galio"],
        "03 ENERGÍA": ["Estado Sólido 450Wh/kg", "BMS Inteligente", "Carga 10C"],
        "04 PERCEPCIÓN": ["Lidar OS2-128", "Térmica FLIR", "Radar 77GHz"],
        "05 AVIÓNICA": ["STM32H7 Dual-Core", "NPU 100 TOPS", "TPM 2.0"],
        "06 COMUNICACIÓN": ["Silvus MIMO Mesh", "Starlink Mini", "Anti-Jamming"],
        "07 NAVEGACIÓN": ["FOG (Fibra Óptica)", "RTK Triple Banda", "Láser Precisión"],
        "08 MISIÓN": ["Payload Dropper", "Foco 60K Lúmenes", "Megafonía 125dB"]
    }

def get_hardware_integrity_hash():
    return "GLI-V11-STRIKE"
