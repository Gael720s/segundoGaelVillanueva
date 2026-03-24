from clases.herencia1.componente_control import ComponenteControl

class ModuloSalida(ComponenteControl):
    def __init__(self, nombre, identificador, señalEntrada, tipoSalida, estado="Inactivo"):
        super().__init__(nombre, identificador, señalEntrada, estado)
        self.tipoSalida = tipoSalida

    def enviarSeñal(self):
        return f"El módulo está enviando una señal de tipo {self.tipoSalida}"

    def mostrarInformacion(self):
        base_info = super().mostrarInformacion()
        return f"{base_info}\nTipo de salida: {self.tipoSalida}"
