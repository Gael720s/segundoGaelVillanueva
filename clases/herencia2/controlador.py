from clases.herencia1.componente_control import ComponenteControl

class Controlador(ComponenteControl):
    def __init__(self, nombre, identificador, señalEntrada, tipoControl, estado="Inactivo"):
        super().__init__(nombre, identificador, señalEntrada, estado)
        self.tipoControl = tipoControl

    def procesarSeñal(self):
        return f"El controlador está procesando la señal con control {self.tipoControl}"

    def mostrarInformacion(self):
        base_info = super().mostrarInformacion()
        return f"{base_info}\nTipo de control: {self.tipoControl}"
