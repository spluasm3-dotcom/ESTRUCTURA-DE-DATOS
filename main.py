# Ejercicio 1
class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for n in args:
            if self.validar_nota(n):
                self.notas.append(n)
        return self.notas

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0.0


# Ejercicio 2
class AnalizadorTexto:
    def __init__(self):
        self.conjunto = set()
        self.lista = []

    def agregar_palabra(self, palabra):
        self.conjunto.add(palabra)
        self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.conjunto)

    def agregar_multiples(self, *args):
        for p in args:
            self.agregar_palabra(p)


# Ejercicio 3
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [nom for nom, p in self.articulos.items() if precio_min <= p <= precio_max]


# Ejercicio 4
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for l in listas:
            resultado[tuple(l)] = self.invertir_lista(l)
        return resultado


# Ejercicio 5
class AnalizadorNumeros:
    def __init__(self):
        self.clasificacion = {'pares': [], 'impares': []}

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.clasificacion = {'pares': [], 'impares': []}
        for n in numeros:
            if self.es_par(n):
                self.clasificacion['pares'].append(n)
            else:
                self.clasificacion['impares'].append(n)
        return self.clasificacion

    def cantidad_pares_impares(self):
        return (len(self.clasificacion['pares']), len(self.clasificacion['impares']))


# Ejercicio 6
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas) if self.temperaturas else None

    def maxima(self):
        return max(self.temperaturas) if self.temperaturas else None

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas) if self.temperaturas else 0.0

    def registrar_multiples(self, *temps):
        for t in temps:
            self.registrar_temperatura(t)


# Ejercicio 7
class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        return [nom for nom, ed in self.personas.items() if ed >= edad_minima]

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas) if self.personas else 0.0


# Ejercicio 8
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        return max(self.equipos, key=lambda eq: len(self.equipos[eq]))


# Ejercicio 9
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiouáéíóú"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
            
        conteos = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for char in texto:
            if char.isdigit():
                conteos['digitos'] += 1
            elif char.isalpha():
                if self.solo_vocales(char):
                    conteos['vocales'] += 1
                else:
                    conteos['consonantes'] += 1
        return conteos


# Ejercicio 10
class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [t for t in self.lista_tareas if t[1].lower() == 'alta']

    def eliminar_completada(self, descripcion):
        self.lista_tareas = [t for t in self.lista_tareas if t[0] != descripcion]


# Ejercicio 11
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


# Ejercicio 12
class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()
        for inicio, fin in rangos:
            elementos.update(range(inicio, fin + 1))
        return sorted(list(elementos))


# Ejercicio 13
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        max_len = max(len(lista1), len(lista2))
        for i in range(max_len):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
        resultado = listas[0]
        for l in listas[1:]:
            resultado = self.intercalar(resultado, l)
        return resultado


# Ejercicio 14
class RegistroNotas:
    def __init__(self):
        self.registro = {}

    def registrar(self, estudiante, nota):
        self.registro[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [est for est, nota in self.registro.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        if not self.registro:
            return None
        mejor = max(self.registro.items(), key=lambda x: x[1])
        return mejor


# Ejercicio 15
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = [i for i in range(1, abs(numero) + 1) if numero % i == 0]
        return tuple(divisores)

    def es_perfecto(self, numero):
        if numero <= 0:
            return False
        divisores = self.encontrar_divisores(numero)
        return sum(divisores[:-1]) == numero

    def encontrar_multiples_divisores(self, *numeros):
        return {num: self.encontrar_divisores(num) for num in numeros}


# Ejercicio 16
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            ascii_base = ord('a') if letra.islower() else ord('A')
            return chr((ord(letra) - ascii_base + desplazamiento) % 26 + ascii_base)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = "".join([self.codificar_letra(c, desplazamiento) for c in palabra])
        self.historial[palabra] = codificada
        return codificada


# Ejercicio 17
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {"niño": [], "adolescente": [], "adulto": [], "mayor": []}
        for e in edades:
            cat = self.clasificar_edad(e)
            self.grupos[cat].append(e)
        return {k: v for k, v in self.grupos.items() if v}

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        return sum(edades) / len(edades) if edades else 0.0


# Ejercicio 18
import math

class CalculadorDistancia:
    def __init__(self):
        self.distancias_calculadas = []

    def distancia_euclidiana(self, p1, p2):
        d = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        self.distancias_calculadas.append(d)
        return d

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
        return min(puntos, key=lambda p: self.distancia_euclidiana(referencia, p))


# Ejercicio 19
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [prod for prod, cant in self.stock.items() if cant < minimo]


# Ejercicio 20
class AnalizadorPatrones:
    def __init__(self):
        self.palabras_procesadas = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        self.palabras_procesadas.update(palabras)
        return [p for p in palabras if p.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        self.palabras_procesadas.update(palabras)
        agrupado = {}
        for p in palabras:
            longitud = len(p)
            agrupado.setdefault(longitud, []).append(p)
        return agrupado

    def palabras_unicas(self):
        return self.palabras_procesadas