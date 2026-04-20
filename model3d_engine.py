# -*- coding: utf-8 -*-
def get_3d_model_data(idea):
    if not idea: return {}
    return {
        "CONFIGURACIÓN_GEOMÉTRICA": {
            "Tipo": "Quadcopter en X",
            "Brazos": 4,
            "Hélices": 4,
            "Material_Base": "Carbono M40J",
            "Color_Principal": "#222222"
        },
        "ESTADO_OPERATIVO": {
            "Modo": "Vuelo Estacionario",
            "RPM_Hélices": 4500
        },
        "DATOS_TECNICOS_RENDER": {
            "Shader": "PBR"
        }
    }

def get_3d_integrity_hash():
    return "3D-PROTO-V2-FIXED"
