from clases.herencia2.controlador import Controlador
from clases.herencia2.modulo_salida import ModuloSalida



def main():
    # Objeto Controlador
    controlador = Controlador("Controlador PID", "C001", "4-20 mA", "PID")
    controlador.activar()
    print(controlador.mostrarInformacion())
    print(controlador.procesarSeñal())

    print()

    # Objeto Módulo de salida
    modulo = ModuloSalida("Módulo de salida", "C002", "24V", "Digital")
    modulo.activar()
    print(modulo.mostrarInformacion())
    print(modulo.enviarSeñal())

if __name__ == "__main__":
    main()
