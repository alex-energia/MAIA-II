# -*- coding: utf-8 -*-
# model3d_engine.py - MOTOR DE GEOMETRÍA DINÁMICA MAIA II v2.0

def get_3d_model_data(idea):
    """Genera especificaciones geométricas y de renderizado para Three.js."""
    if not idea: return {}
    
    # Lógica interactiva básica: si es pesado, el chasis es más robusto
    es_pesado = "pesado" in idea.lower() or "carga" in idea.lower()
    es_ataque = "ataque" in idea.lower() or "militar" in idea.lower()
    
    color_chasis = "#222222" # Carbono mate por defecto
    if es_ataque: color_chasis = "#2f353b" # Gris militar
    
    return {
        "CONFIGURACIÓN_GEOMÉTRICA": {
            "Tipo": "Quadcopter en X",
            "Brazos": 4,
            "Hélices": 4,
            "Material_Base": es_pesado and "Carbono Reforzado Kevlar" or "Carbono M40J",
            "Color_Principal": color_chasis
        },
        "ESTADO_OPERATIVO": {
            "Modo": "Vuelo Estacionario (Hover)",
            "RPM_Hélices": es_pesado and 3200 or 4500,
            "Animación_Activa": True,
            "VFX_Estela": es_ataque and "Baja Visibilidad" or "Estela Iónica Azul"
        },
        "DATOS_TECNICOS_RENDER": {
            "Shader": "PBR (Physically Based Rendering)",
            "Textura": "Micro-textura de fibra de carbono",
            "Iluminación": "Táctica de estudio (Tres puntos)"
        }
    }

def get_3d_integrity_hash():
    return "3D-PROTO-DYNAMIC-V2"