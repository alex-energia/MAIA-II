# -*- coding: utf-8 -*-
def calculate_performance(idea):
    if not idea: return {"Peso": "---", "Empuje": "---", "TWR": "---", "Vuelo": "---"}
    es_pesado = "pesado" in idea.lower() or "carga" in idea.lower()
    p, e, v = (12.8, 115.0, 42) if es_pesado else (3.4, 48.2, 58)
    return {"Peso": f"{p}kg", "Empuje": f"{e}kg", "TWR": f"{round(e/p, 2)}:1", "Vuelo": f"{v}min"}

def get_hardware_specs(idea):
    if not idea: return {}
    # ESTRUCTURA DE 8 CAPAS PROTEGIDA
    return {
        "ESTRUCTURA": ["Chasis Carbono M40J", "Blindaje Grafeno", "Titanio G5"],
        "PROPULSIÓN": ["Motores GaN-Core 5200KV", "Hélices Paso Variable", "ESC 120A"],
        "ENERGÍA": ["Estado Sólido 500Wh", "BMS Dual Inteligente", "Carga 10C"],
        "PERCEPCIÓN": ["Lidar OS2-128", "Térmica FLIR Boson", "Radar 77GHz"],
        "AVIÓNICA": ["STM32H7 Dual-Core", "NPU 100 TOPS", "TPM 2.0 Secure"],
        "COMUNICACIÓN": ["Silvus MIMO Mesh", "Starlink Mini", "Anti-Jamming"],
        "NAVEGACIÓN": ["FOG Fibra Óptica", "RTK Triple Banda", "Láser Precisión"],
        "MISIÓN": ["Payload Dropper", "Foco 60K Lúmenes", "Cámara 8K 120fps"]
    }

def get_hardware_integrity_hash():
    return "GLI-V12-FULL-8-LAYER-PROTECTED"