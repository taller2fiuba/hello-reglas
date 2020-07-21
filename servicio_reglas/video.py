import datetime

from .usuario import Usuario

class Video:
    def __init__(self, video, usuario):
        self.datos_video = video
        self.autor = Usuario(usuario)
        self.cantidad_reacciones = video.get('cantidad-reacciones', 0)
        self.cantidad_comentarios = video.get('cantidad-comentarios', 0)
        self.ubicacion = video.get('ubicacion', '')
        now = datetime.datetime.now().timestamp()
        self.fecha_publicacion = int(now - video.get('fecha', now))
        self.importancia = 0
