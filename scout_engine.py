# -*- coding: utf-8 -*-
import datetime

def get_market_scout(pais_filtro="TODOS"):
    fecha_limite = datetime.date.today() - datetime.timedelta(days=30)
    
    # Base de datos global de activos (Ejemplos verídicos simulación UPME/Brokers)
    activos = [
        {"Nombre": "PCH Río Nare", "Categoria": "Hidroeléctrica", "Estado": "Venta", "Valor": "USD 32M", "Ubicacion": "Colombia", "Fuente": "UPME", "Contacto": "Dr. Roberto Sáenz | +57 315...", "Fecha": datetime.date(2026, 4, 10)},
        {"Nombre": "Parque Solar Atacama", "Categoria": "Solar", "Estado": "Participación", "Valor": "USD 75M", "Ubicacion": "Chile", "Fuente": "Broker Privado", "Contacto": "Elena Müller | +56 2...", "Fecha": datetime.date(2026, 4, 15)},
        {"Nombre": "Offshore Wind North Sea", "Categoria": "Eólica", "Estado": "Licitación", "Valor": "EUR 200M", "Ubicacion": "Alemania", "Fuente": "EU Tenders", "Contacto": "Hans Weber | +49 89...", "Fecha": datetime.date(2026, 4, 12)},
        {"Nombre": "Termoeléctrica Monterrey", "Categoria": "Térmica", "Estado": "Venta Acciones", "Valor": "USD 45M", "Ubicacion": "México", "Fuente": "Banorte Inversión", "Contacto": "Ing. Lucía Méndez | +52 55...", "Fecha": datetime.date(2026, 4, 05)},
        {"Nombre": "Green Hydrogen H2-Dubai", "Categoria": "Hidrógeno", "Estado": "Ronda Inversión", "Valor": "USD 120M", "Ubicacion": "Emiratos Árabes", "Fuente": "DEWA", "Contacto": "Ahmed Al-Farsi | +971 4...", "Fecha": datetime.date(2026, 4, 18)}
    ]

    # Filtrado por vigencia y por país
    resultados = [a for a in activos if a["Fecha"] >= fecha_limite]
    
    if pais_filtro != "TODOS":
        resultados = [a for a in resultados if a["Ubicacion"].upper() == pais_filtro.upper()]
    
    return resultados

def get_countries_list():
    # Lista de países en orden alfabético
    return sorted(["Colombia", "Chile", "México", "España", "Estados Unidos", "China", "Japón", "Emiratos Árabes", "Alemania", "Brasil", "Perú", "Canadá"])