# -*- coding: utf-8 -*-
import datetime

def get_market_scout():
    fecha_limite = datetime.date.today() - datetime.timedelta(days=30)
    # Simulación de base de datos curada de UPME, Brokers y Bancos de Inversión
    activos = [
        {
            "Nombre": "PCH Río Nare - Fase III",
            "Descripcion": "Central Hidroeléctrica de Pasada. 19.8MW. Licencia ambiental vigente.",
            "Estado": "Venta de Proyecto en Construcción (EPC)",
            "Valor": "USD 32,000,000",
            "Ubicacion": "Antioquia, Colombia",
            "Fuente": "UPME / Agencia Nacional de Minería",
            "Contacto": "Dr. Roberto Sáenz (CEO) | +57 315 888 XX XX | r.saenz@hidronare.com.co | Cra 43A #1-50, Medellín",
            "Fecha": datetime.date(2026, 4, 10)
        },
        {
            "Nombre": "Planta Fotovoltaica 'Sol de Atacama'",
            "Descripcion": "Parque solar operativo de 150MW. Incluye sistemas de almacenamiento BESS.",
            "Estado": "Venta de Participación (49% Equity)",
            "Valor": "USD 75,000,000",
            "Ubicacion": "Desierto de Atacama, Chile",
            "Fuente": "Investment Bank (Confidencial)",
            "Contacto": "Elena Müller (M&A Director) | +56 2 2334 XXXX | e.muller@latinenergy.ch | Av. Apoquindo 3000, Santiago",
            "Fecha": datetime.date(2026, 4, 15)
        }
    ]
    return [a for a in activos if a["Fecha"] >= fecha_limite]
