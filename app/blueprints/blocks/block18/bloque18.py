from core.formatter import cprint as print, cinput as input
from abc import ABC, abstractmethod

# ==========================================
# EJERCICIO 1: Clases Abstractas
# ==========================================
class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2

def run_exercise_18_1():
    print("=== Ejercicio 1: Clase Abstracta ===")
    triangulo = Triangulo(base=10.0, altura=5.0)
    print(f"Figura: Triángulo")
    print(f"Base: {triangulo.base} | Altura: {triangulo.altura}")
    print(f"Área calculada: {triangulo.area()}")


# ==========================================
# EJERCICIO 2: Properties y Encapsulamiento
# ==========================================
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio  # Pasa automáticamente por el setter al instanciar

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ValueError("El precio no puede ser un valor negativo.")
        self._precio = valor

def run_exercise_18_2():
    print("=== Ejercicio 2: @property y Validación ===")
    try:
        prod = Producto("Controlador MPPT", 150.0)
        print(f"Producto creado con éxito: {prod.nombre} a ${prod.precio}")
        
        print("\nIntentando asignar un precio negativo (-20)...")
        prod.precio = -20.0
    except ValueError as e:
        print(f"[ERROR CAPTURADO] {e}")


# ==========================================
# EJERCICIO 3: Herencia y Polimorfismo
# ==========================================
class Animal(ABC):
    @abstractmethod
    def sonido(self) -> str:
        pass

class Perro(Animal):
    def sonido(self) -> str:
        return "Guau, guau!"

class Gato(Animal):
    def sonido(self) -> str:
        return "Miau, miau!"

class Vaca(Animal):
    def sonido(self) -> str:
        return "Muuu, muuu!"

def run_exercise_18_3():
    print("=== Ejercicio 3: Polimorfismo ===")
    # Lista polimórfica: Diferentes objetos tratados por su clase padre
    granja: list[Animal] = [Perro(), Gato(), Vaca()]
    
    for animal in granja:
        # animal.__class__.__name__ extrae el nombre de la clase hija
        print(f"El animal {animal.__class__.__name__} hace: {animal.sonido()}")


# ==========================================
# DICCIONARIO DE OPCIONES DEL MENÚ
# ==========================================
options_bloque_18 = {
    "1": ("Ejercicio 1: Clase Abstracta (Triángulo)", run_exercise_18_1),
    "2": ("Ejercicio 2: Encapsulamiento (@property)", run_exercise_18_2),
    "3": ("Ejercicio 3: Jerarquía y Polimorfismo", run_exercise_18_3),

}