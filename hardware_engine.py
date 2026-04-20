# -*- coding: utf-8 -*-
# hardware_engine.py - MOTOR DE DINÁMICA FÍSICA GLI

def get_hardware_specs(idea):
    """Genera lista de materiales bruta basada en la complejidad de la idea."""
    if not idea:
        return None

    # Lógica de selección de materiales industrial
    return {
        "ESTRUCTURA": {
            "Cuerpo": "Chasis Monocasco de Carbono M40J con blindaje EMI",
            "Tren de Aterrizaje": "Fibra de carbono retráctil neumática",
            "Protección": "Clasificación IP67 contra polvo y agua"
        },
        "PROPULSIÓN": {
            "Motores": "KDE Direct 700KV (Serie Industrial High-Torque)",
            "Hélices": "22x7.4 Carbono Triple-Pala equilibradas dinámicamente",
            "ESC": "KDE-UAS125UVC con telemetría CAN-Bus 2.0"
        },
        "ENERGÍA": {
            "Baterías": "Pack de Estado Sólido 12S 22,000mAh (400Wh/kg)",
            "BMS": "Sistema de gestión activa MAIA con balanceo de 2A",
            "Conectores": "AS150 Anti-spark de alta corriente"
        },
        "SENSÓRICA Y CÁMARAS": {
            "Cámara Principal": "Gimbal 3-ejes con Sensor 4K 60fps + Térmico Radiométrico",
            "Lidar": "Ouster OS1 (128 canales) para mapeo centimétrico",
            "Evitación": "Sensores ultrasónicos y cámaras estéreo en 360°"
        },
        "MANDO Y COMUNICACIONES": {
            "Control Remoto": "Estación de tierra rugerizada con enlace Silvus MIMO",
            "Enlace": "Frecuencia S/C Band con salto automático (Anti-Jamming)",
            "Pantalla": "Panel táctil de 2000 nits legible bajo luz solar"
        }
    }

def calculate_performance(idea):
    """Simulación de rendimiento para el Módulo de Construcción."""
    if not idea: return {}
    # Valores base simulados para un sistema GLI
    peso_estimado = 6.5 # kg
    empuje_max = 32.0 # kg
    ratio_twr = empuje_max / peso_estimado
    autonomia = 45 # minutos
    
    return {
        "Peso Total": f"{peso_estimado} kg",
        "Empuje Máximo": f"{empuje_max} kg",
        "Ratio Empuje/Peso": f"{ratio_twr:.2f}:1",
        "Autonomía Est.": f"{autonomia} min"
    }