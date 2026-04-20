# -*- coding: utf-8 -*-
def get_hardware_specs(idea):
    if not idea: return {}
    return {
        "Estructura": "Chasis de polímero reforzado con fibra de carbono y titanio grado 5.",
        "Propulsión": "Motores brushless de 2400KV con hélices de paso variable.",
        "Energía": "Células de hidrógeno sólido con autonomía de 120 minutos.",
        "Sensores": "LiDAR de 360°, cámara térmica Flir y sensor ultrasónico.",
        "Navegación": "Módulo GPS diferencial RTK con precisión de 1cm.",
        "Comunicaciones": "Enlace satelital Starlink ecriptado con salto de frecuencia.",
        "Procesamiento": "Unidad de cómputo neuronal integrada para IA en el borde.",
        "Blindaje": "Recubrimiento electromagnético contra pulsos (EMP) y lluvia ácida."
    }
