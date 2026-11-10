from pasajero import Pasajero

class MiCola:
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La cola está llena.")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número.")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):
            marca = " <- FRENTE" if i == 0 else (" <- FINAL" if i == self.cantidad - 1 else "")
            print(f"  [{i}] {self.datos[i]}{marca}")

    def desencolar(self):
        if self.cantidad == 0:
            return None
        pasajero = self.datos[0]
        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.cantidad -= 1
        self.datos[self.cantidad] = None
        return pasajero

    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
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
        cantidad_inicial = self.cantidad
        eliminado = False
        for i in range(cantidad_inicial):
            pasajero = self.desencolar()
            if pasajero.numero == numero:
                eliminado = True
            else:
                self.encolar(pasajero)
        return eliminado

    def copiar(self):
        nueva = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0