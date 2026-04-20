# -*- coding: utf-8 -*-
def calculate_performance(idea):
    if not idea: return {"Peso": "---", "Empuje": "---", "TWR": "---", "Vuelo": "---"}
    es_pesado = "pesado" in idea.lower() or "carga" in idea.lower()
    p, e, v = (8.5, 82.0, 45) if es_pesado else (4.8, 51.5, 65)
    return {"Peso": f"{p}kg", "Empuje": f"{e}kg", "TWR": f"{round(e/p, 2)}:1", "Vuelo": f"{v}min"}

def get_hardware_specs(idea):
    if not idea: return {}
    return {
        "ESTRUCTURA": ["Chasis Carbono M40J", "Blindaje Grafeno", "Titanio Grado 5"],
        "PROPULSIÓN": ["Motores GaN-Core", "Hélices Paso Variable", "ESC Nitruro"],
        "ENERGÍA": ["Estado Sólido 450Wh", "BMS Inteligente", "Carga 10C"],
        "PERCEPCIÓN": ["Lidar OS2-128", "Térmica FLIR", "Radar 77GHz"],
        "AVIÓNICA": ["STM32H7 Dual-Core", "NPU 100 TOPS", "TPM 2.0"],
        "COMUNICACIÓN": ["Silvus MIMO Mesh", "Starlink Mini", "Anti-Jamming"],
        "NAVEGACIÓN": ["FOG Fibra Óptica", "RTK Triple Banda", "Láser Precisión"],
        "MISIÓN": ["Payload Dropper", "Foco 60K Lúmenes", "Megafonía 125dB"]
    }

def get_hardware_integrity_hash():
    return "GLI-V11-PROTECTED"