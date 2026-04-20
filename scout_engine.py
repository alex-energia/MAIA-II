# -*- coding: utf-8 -*-
import datetime

def get_market_scout(pais_filtro="TODOS"):
    fecha_limite = datetime.date.today() - datetime.timedelta(days=30)
    
    # Base de datos de activos (Simulación de rastreo verídico)
    activos = [
        {"Nombre": "PCH Río Nare", "Categoria": "Hidroeléctrica", "Estado": "Venta EPC", "Valor": "USD 32M", "Ubicacion": "Colombia", "Fuente": "UPME", "Contacto": "Dr. Roberto Sáenz | +57 315 XXX | r.saenz@hidronare.co", "Fecha": datetime.date(2026, 4, 10)},
        {"Nombre": "Solar Atacama", "Categoria": "Solar", "Estado": "Participación", "Valor": "USD 75M", "Ubicacion": "Chile", "Fuente": "Broker Privado", "Contacto": "Elena Müller | +56 2 XXX | e.muller@chile.cl", "Fecha": datetime.date(2026, 4, 15)},
        {"Nombre": "Eólica Offshore", "Categoria": "Eólica", "Estado": "Licitación", "Valor": "EUR 200M", "Ubicacion": "Alemania", "Fuente": "EU Tenders", "Contacto": "Hans Weber | +49 89 XXX | h.weber@energy.de", "Fecha": datetime.date(2026, 4, 12)}
    ]

    resultados = [a for a in activos if a["Fecha"] >= fecha_limite]
    if pais_filtro != "TODOS":
        resultados = [a for a in resultados if a["Ubicacion"].upper() == pais_filtro.upper()]
    return resultados

def get_countries_list():
    return sorted(["Colombia", "Chile", "México", "España", "Estados Unidos", "China", "Japón", "Emiratos Árabes", "Alemania"])
