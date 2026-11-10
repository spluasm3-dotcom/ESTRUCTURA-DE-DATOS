from pasajero import Pasajero

class MiPila:
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La pila está llena.")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número.")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):
            marca = " <- TOPE" if i == self.cantidad - 1 else (" <- FONDO" if i == 0 else "")
            print(f"  [{i}] {self.datos[i]}{marca}")

    def desapilar(self):
        if self.cantidad == 0:
            return None
        pasajero = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return pasajero

    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        if self.buscar(numero) == -1:
            return False
        auxiliar = MiPila(self.capacidad)
        eliminado = False
        while self.cantidad > 0:
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                eliminado = True
                break
            auxiliar.apilar(pasajero)
        while auxiliar.cantidad > 0:
            self.apilar(auxiliar.desapilar())
        return eliminado

    def copiar(self):
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0

