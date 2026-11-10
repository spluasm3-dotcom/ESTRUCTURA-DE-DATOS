from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero.")

def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)

def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A")
    ]

def mostrar_menu(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")

def menu_pila():
    while True:
        mostrar_menu("MENÚ 1 - PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()
        if op == "1":
            if pila.apilar(leer_pasajero()): print("  Pasajero apilado.")
        elif op == "2": pila.listar()
        elif op == "3":
            p = pila.desapilar()
            if p is None: print("  La pila está vacía.")
            else:
                print(f"  Salió: {p}")
                print("  Nuevo tope: " + (pila.ver_tope().nombre if pila.ver_tope() else "(pila vacía)"))
        elif op == "4":
            p = pila.ver_tope()
            print(f"  Tope: {p}" if p else "  La pila está vacía.")
        elif op == "5":
            n = leer_entero("  Número de pasajero: "); pos = pila.buscar(n)
            print(f"  Encontrado en [{pos}]: {pila.datos[pos]}" if pos != -1 else "  No existe ese pasajero.")
        elif op == "6":
            n = leer_entero("  Número: "); d = input("  Nuevo destino: ").strip(); a = input("  Nuevo asiento: ").strip().upper()
            print("  Modificado correctamente." if pila.modificar(n, d, a) else "  No existe ese pasajero.")
        elif op == "7":
            n = leer_entero("  Número a eliminar: ")
            print("  Pasajero eliminado." if pila.eliminar_por_numero(n) else "  No existe ese pasajero.")
        elif op == "8":
            copia = pila.copiar(); print("  Copia de la pila:"); copia.listar()
        elif op == "9":
            print(f"  Longitud: {pila.longitud()}")
            print("  La pila está vacía." if pila.esta_vacia() else "  La pila no está vacía.")
        elif op == "C":
            total = 0
            for p in datos_prueba():
                if pila.apilar(p): total += 1
            print(f"  Se agregaron {total} pasajeros nuevos. Total: {pila.longitud()}.")
        elif op == "0": break
        else: print("  Opción no válida.")

def menu_cola():
    while True:
        mostrar_menu("MENÚ 2 - COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()
        if op == "1":
            if cola.encolar(leer_pasajero()): print("  Pasajero encolado.")
        elif op == "2": cola.listar()
        elif op == "3":
            p = cola.desencolar()
            if p is None: print("  La cola está vacía.")
            else:
                print(f"  Salió: {p}")
                print("  Nuevo frente: " + (cola.ver_frente().nombre if cola.ver_frente() else "(cola vacía)"))
        elif op == "4":
            p = cola.ver_frente()
            print(f"  Frente: {p}" if p else "  La cola está vacía.")
        elif op == "5":
            n = leer_entero("  Número de pasajero: "); pos = cola.buscar(n)
            print(f"  Encontrado en [{pos}]: {cola.datos[pos]}" if pos != -1 else "  No existe ese pasajero.")
        elif op == "6":
            n = leer_entero("  Número: "); d = input("  Nuevo destino: ").strip(); a = input("  Nuevo asiento: ").strip().upper()
            print("  Modificado correctamente." if cola.modificar(n, d, a) else "  No existe ese pasajero.")
        elif op == "7":
            n = leer_entero("  Número a eliminar: ")
            print("  Pasajero eliminado." if cola.eliminar_por_numero(n) else "  No existe ese pasajero.")
        elif op == "8":
            copia = cola.copiar(); print("  Copia de la cola:"); copia.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()}")
            print("  La cola está vacía." if cola.esta_vacia() else "  La cola no está vacía.")
        elif op == "C":
            total = 0
            for p in datos_prueba():
                if cola.encolar(p): total += 1
            print(f"  Se agregaron {total} pasajeros nuevos. Total: {cola.longitud()}.")
        elif op == "0": break
        else: print("  Opción no válida.")

def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS - PASAJEROS =====")
        print("1. Menú 1 - Pila")
        print("2. Menú 2 - Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1": menu_pila()
        elif op == "2": menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else: print("Opción no válida.")

if __name__ == "__main__":
    main()

