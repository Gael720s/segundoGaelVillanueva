class ComponenteControl:
    def __init__(self, nombre, identificador, señalEntrada, estado="Inactivo"):
        self.nombre = nombre
        self.identificador = identificador
        self.señalEntrada = señalEntrada
        self.estado = estado

    def activar(self):
        self.estado = "Activo"

    def desactivar(self):
        self.estado = "Inactivo"

    def mostrarInformacion(self):
        return (f"Componente: {self.nombre}\n"
                f"ID: {self.identificador}\n"
                f"Señal de entrada: {self.señalEntrada}\n"
                f"Estado: {self.estado}")
