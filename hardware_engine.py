# -*- coding: utf-8 -*-
def calculate_performance(idea):
    if not idea: return {"Peso": "---", "Empuje": "---", "TWR": "---", "Vuelo": "---"}
    es_pesado = "pesado" in idea.lower() or "carga" in idea.lower()
    p, e, v = (12.4, 110.0, 40) if es_pesado else (3.2, 45.8, 55)
    return {"Peso Total": f"{p}kg", "Empuje Máx": f"{e}kg", "Ratio TWR": f"{round(e/p, 2)}:1", "Autonomía": f"{v}min"}

def get_hardware_specs(idea):
    if not idea: return {}
    return {
        "ESTRUCTURA": ["Chasis Tubular M40J", "Nodos de Titanio", "Carcasa Kevlar"],
        "PROPULSIÓN": ["Motores GaN 4800KV", "Hélices Carbono 12\"", "ESC 120A"],
        "ENERGÍA": ["Lipo Solid-State", "BMS Dual Redundante", "Puerto Carga Rápida"],
        "SISTEMAS": ["Lidar OS1", "IMU Redundante", "GPS RTK Triple"]
    }
