from cronometro import Cronometro
import time

cronometro = Cronometro()

input("Enter para iniciar: ")
cronometro.iniciar()

input("Enter para terminar: ")
cronometro.detener()

print("Tiempo total:", cronometro.tiempo_total())

