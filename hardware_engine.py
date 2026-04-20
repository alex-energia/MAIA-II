# -*- coding: utf-8 -*-
# hardware_engine.py - MOTOR DINÁMICO DE INGENIERÍA GLI-V10

def calculate_performance(idea):
    """Calculadora interactiva: Ajusta la física según la idea."""
    if not idea:
        return {"Peso": "---", "Empuje": "---", "TWR": "---", "Vuelo": "---", "Carga": "---"}
    
    # Lógica interactiva básica
    idea_str = idea.lower()
    base_peso = 5.0
    base_empuje = 50.0
    base_vuelo = 60
    
    if "pesado" in idea_str or "carga" in idea_str:
        base_peso += 3.5
        base_empuje += 40.0
        base_vuelo -= 20
    elif "ligero" in idea_str or "carrera" in idea_str:
        base_peso -= 2.0
        base_empuje -= 10.0
        base_vuelo -= 10
    
    twr = base_empuje / base_peso
    
    return {
        "Peso": f"{base_peso:.1f} kg",
        "Empuje": f"{base_empuje:.1f} kg",
        "TWR": f"{twr:.2f}:1",
        "Vuelo": f"{base_vuelo} min",
        "Carga": f"{(base_empuje - base_peso * 2):.1f} kg"
    }

def get_hardware_specs(idea):
    """Genera materiales específicos según el propósito."""
    if not idea: return {}
    
    # Base de datos de materiales brutal
    specs = {
        "01_ESTRUCTURA": ["Monocasco Carbono M40J", "Blindaje Grafeno", "Titanio Grado 5"],
        "02_PROPULSIÓN": ["Motores GaN-Core 750KV", "Hélices Paso Variable", "ESC Nitruro Galio"],
        "03_ENERGÍA": ["Estado Sólido 450Wh/kg", "BMS Balanceo Activo", "Carga 10C"],
        "04_PERCEPCIÓN": ["Lidar Ouster OS2-128", "Térmica FLIR Boson", "Radar 77GHz"],
        "05_AVIÓNICA": ["STM32H7 Triple Núcleo", "NPU 100 TOPS", "TPM 2.0 Encriptado"],
        "06_COMUNICACIONES": ["Silvus MIMO Mesh", "Starlink Mini", "Módulo Anti-Jamming"],
        "07_NAVEGACIÓN": ["FOG (Giro Fibra Óptica)", "RTK Triple Banda", "Láser Centimétrico"],
        "08_MISIÓN": ["Payload Dropper Mag", "Foco 60K Lúmenes", "Megafonía 125dB"]
    }
    return specs

def get_hardware_integrity_hash():
    return "GLI-V10-DYNAMIC-ACTIVE"