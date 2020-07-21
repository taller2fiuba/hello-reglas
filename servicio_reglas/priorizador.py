from business_rules import run_all

from .video import Video
from .variables_video import VariablesVideo
from .acciones_video import AccionesVideo
from .reglas import REGLAS


class Priorizador:
    def __init__(self):
        self.reglas = REGLAS

    def priorizar(self, videos, autores):
        '''
        Dado un iterable de diccionarios que representan videos,
        devuelve una lista con los diccionarios ordenados por
        importancia.
        '''
        videos_procesados = []
        for video in map(lambda va: Video(va[0], va[1]), zip(videos, autores)):
            run_all(self.reglas,
                    defined_variables=VariablesVideo(video),
                    defined_actions=AccionesVideo(video)
                    )
            videos_procesados.append(video)

        return [(video.importancia, video.datos_video)
                for video in sorted(videos_procesados,
                                    key=lambda e: e.importancia,
                                    reverse=True)]
