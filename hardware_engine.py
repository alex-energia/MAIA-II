# -*- coding: utf-8 -*-
def calculate_performance(idea):
    if not idea: return {"Peso": "---", "Empuje": "---", "TWR": "---", "Vuelo": "---"}
    return {"Peso": "3.4kg", "Empuje": "48.2kg", "TWR": "14.1:1", "Vuelo": "58min"}

def get_hardware_specs(idea):
    if not idea: return {}
    return {
        "ESTRUCTURA": ["Chasis Carbono M40J", "Blindaje Grafeno", "Titanio G5"],
        "PROPULSIÓN": ["Motores GaN-Core 5200KV", "Hélices Carbono", "ESC 120A"],
        "ENERGÍA": ["Estado Sólido 500Wh", "BMS Dual", "Carga 10C"],
        "PERCEPCIÓN": ["Lidar OS2-128", "Térmica FLIR", "Radar 77GHz"],
        "AVIÓNICA": ["STM32H7 Dual-Core", "NPU 100 TOPS", "TPM 2.0"],
        "COMUNICACIÓN": ["Silvus MIMO Mesh", "Starlink Mini", "ECC Encrypted"],
        "NAVEGACIÓN": ["FOG Fibra Óptica", "RTK Triple", "Láser Precisión"],
        "MISIÓN": ["Payload Dropper", "Foco 60K Lúmenes", "Cámara 8K"]
    }
