import datetime

from servicio_reglas.priorizador import Priorizador

videos = [
    {"cantidad-reacciones": 500, "cantidad-comentarios": 273, "ubicacion": "casa", 
     "fecha": datetime.datetime.now().timestamp()},
    {"cantidad-reacciones": 100, "cantidad-comentarios": 2,
     "fecha": datetime.datetime.now().timestamp() - 30*3600*24},
    {"cantidad-reacciones": 2, "cantidad-comentarios": 2, "ubicacion": "la costa", 
     "fecha": datetime.datetime.now().timestamp() - 15*3600*24},
    {"cantidad-reacciones": 10, "cantidad-comentarios": 2, "ubicacion": "lugano", 
     "fecha": datetime.datetime.now().timestamp() - 10*3600*24},
]

autores = [
    {"videos-por-dia": 1, "cantidad-contactos": 40},
    {"videos-por-dia": 0.01, "cantidad-contactos": 300},
    {"videos-por-dia": 1.5, "cantidad-contactos": 40000},
    {"videos-por-dia": 0.04, "cantidad-contactos": 1}
]

s = Priorizador()
priorizados = s.priorizar(videos, autores)