import time

class Cronometro:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tiempo = 0
        
    def iniciar(self):
        self.inicio = time.time()

    def detener(self):
        if self.inicio is not None:
            self.fin = time.time()
            self.tiempo = self.fin - self.inicio
            self.inicio = None

    def tiempo_total(self):
        return self.tiempo
