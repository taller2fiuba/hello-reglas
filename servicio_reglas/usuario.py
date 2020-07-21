
class Usuario:
    def __init__(self, usuario):
        self.videos_por_dia = usuario.get('videos-por-dia', 0)
        self.cantidad_contactos = usuario.get('cantidad-contactos', 0)
