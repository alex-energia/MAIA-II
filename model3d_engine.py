# -*- coding: utf-8 -*-
def get_3d_model_data(idea):
    if not idea: return {}
    return {
        "DISEÑO": "MAIA-II Stealth Recon",
        "MATERIALES": {
            "Chasis": "Polímero Reforzado con Carbono (CFRP)",
            "Hélices": "Policarbonato de Alta Resistencia con Bordes de Ataque",
            "Óptica": "Lentes de Germanio para Térmica"
        },
        "ANIMACIÓN": {
            "Frecuencia_Vibración": 0.005,
            "Velocidad_Rotación": 0.5,
            "Inclinación_Ataque": 15
        }
    }
