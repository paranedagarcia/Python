# -*- coding: utf-8 -*-
"""
MRO & Super Explorer: El Misterio del Diamante
Herramienta interactiva para estudiantes de programación orientada a objetos.
"""

import sys

DIAMOND_ART = """
                 +------------+
                 |    Base    |
                 +------------+
                  /          \\
                 /            \\
          +-------+          +-------+
          |   A   |          |   B   |
          +-------+          +-------+
                 \\            /
                  \\          /
                 +------------+
                 |    Sub     |
                 +------------+
"""

# Implementación real del diamante para demostración dinámica
class Base:
    def __init__(self, tracker=None):
        if tracker is not None:
            tracker.append("Base (Inicio)")
        # Base no llama a super() si sabemos que llega a 'object',
        # pero por diseño cooperativo es buena práctica.
        super().__init__()
        if tracker is not None:
            tracker.append("Base (Fin)")

class A(Base):
    def __init__(self, tracker=None):
        if tracker is not None:
            tracker.append("A (Inicio)")
        super().__init__(tracker)
        if tracker is not None:
            tracker.append("A (Fin)")

class B(Base):
    def __init__(self, tracker=None):
        if tracker is not None:
            tracker.append("B (Inicio)")
        super().__init__(tracker)
        if tracker is not None:
            tracker.append("B (Fin)")

class Sub(A, B):
    def __init__(self, tracker=None):
        if tracker is not None:
            tracker.append("Sub (Inicio)")
        super().__init__(tracker)
        if tracker is not None:
            tracker.append("Sub (Fin)")


def limpiar_pantalla():
    print("\n" * 40)

def mostrar_cabecera():
    print("=" * 70)
    print("      MRO & SUPER() EXPLORER: EL MISTERIO DE LA HERENCIA MÚLTIPLE")
    print("=" * 70)

def mostrar_teoria():
    limpiar_pantalla()
    mostrar_cabecera()
    print("""
¿Qué es el MRO (Method Resolution Order)?
El MRO es el orden que Python sigue para buscar atributos o métodos en una
jerarquía de herencia. Puedes consultar este orden usando 'Clase.__mro__'.

¿Qué hace realmente super()?
Contrario a la creencia popular, super() NO llama necesariamente al padre directo
en el código. En su lugar, super() busca la clase actual en el MRO del objeto
que se instanció, y delega el control a la SIGUIENTE clase en esa lista.

¡Esto permite una inicialización cooperativa impecable!
""")
    input("\nPresiona Enter para ver el diseño del Diamante...")
    
    limpiar_pantalla()
    mostrar_cabecera()
    print("Estructura de clases a analizar:")
    print(DIAMOND_ART)
    print("""
Definición de clases:
  class Base: pass
  class A(Base): pass
  class B(Base): pass
  class Sub(A, B): pass  # ¡Hereda de A y B!
""")
    input("\nPresiona Enter para comenzar el Desafío Interactivo...")

def ejecutar_desafio():
    puntuacion = 0
    total_preguntas = 4
    
    # PREGUNTA 1
    limpiar_pantalla()
    mostrar_cabecera()
    print("PREGUNTA 1/4:")
    print("Teniendo en cuenta la clase 'Sub(A, B)', ¿cuál es el MRO exacto de 'Sub'?")
    print(DIAMOND_ART)
    print("A) Sub -> A -> Base -> B -> Base -> object")
    print("B) Sub -> A -> B -> Base -> object")
    print("C) Sub -> B -> A -> Base -> object")
    print("D) Sub -> A -> B -> object")
    
    ans = ""
    while ans not in ['A', 'B', 'C', 'D']:
        ans = input("\nTu respuesta (A, B, C, D): ").strip().upper()
        
    if ans == 'B':
        print("\n¡CORRECTO! 🌟")
        print("Python utiliza el Algoritmo C3 de Linealización. El MRO es:")
        print(" -> ".join([c.__name__ for c in Sub.__mro__]))
        puntuacion += 1
    else:
        print("\nIncorrecto. ❌")
        print("La respuesta correcta es la B.")
        print("El MRO calcula las ramas y unifica los ancestros comunes al final:")
        print(" -> ".join([c.__name__ for c in Sub.__mro__]))
    input("\nPresiona Enter para ir a la Pregunta 2...")

    # PREGUNTA 2
    limpiar_pantalla()
    mostrar_cabecera()
    print("PREGUNTA 2/4:")
    print("Si creamos un objeto 'obj = Sub()' y se ejecuta su constructor,")
    print("el método 'Sub.__init__' llama a 'super().__init__()'.")
    print("¿Qué clase se ejecutará inmediatamente después?")
    print("\nMRO de referencia: Sub -> A -> B -> Base -> object")
    print("A) Base")
    print("B) B")
    print("C) A")
    
    ans = ""
    while ans not in ['A', 'B', 'C']:
        ans = input("\nTu respuesta (A, B, C): ").strip().upper()
        
    if ans == 'C':
        print("\n¡CORRECTO! 🌟")
        print("Como 'A' es el siguiente en el MRO después de 'Sub', se ejecuta A.__init__.")
        puntuacion += 1
    else:
        print("\nIncorrecto. ❌")
        print("La respuesta correcta es la C ('A').")
        print("Al llamar a super() desde Sub, Python mira el MRO y salta al siguiente elemento, que es A.")
    input("\nPresiona Enter para ir a la Pregunta 3...")

    # PREGUNTA 3 (LA TRICKY)
    limpiar_pantalla()
    mostrar_cabecera()
    print("PREGUNTA 3/4 (El verdadero misterio):")
    print("Cuando estamos dentro de 'A.__init__' y se ejecuta su 'super().__init__()',")
    print("¿adónde saltará el flujo de control a continuación?")
    print("\nMRO de referencia: Sub -> A -> B -> Base -> object")
    print("A) Base (Porque Base es el padre directo de A)")
    print("B) B (Porque B es el siguiente en el MRO de la instancia 'Sub')")
    print("C) Termina la ejecución")
    
    ans = ""
    while ans not in ['A', 'B', 'C']:
        ans = input("\nTu respuesta (A, B, C): ").strip().upper()
        
    if ans == 'B':
        print("\n¡CORRECTO! 🎉 ¡Eres un maestro de la POO!")
        print("¡Esta es la magia de super()! Aunque el padre directo de A es Base,")
        print("como el objeto original es de clase 'Sub', super() mira el MRO de 'Sub'.")
        print("El elemento que sigue a 'A' en el MRO es 'B', por lo que delegamos a 'B'!")
        puntuacion += 1
    else:
        print("\nIncorrecto. ❌ (¡Pero no te preocupes, es el error más común!)")
        print("La respuesta correcta es la B ('B').")
        print("Si 'A' llamara directamente a 'Base', la clase 'B' nunca se inicializaría,")
        print("dejando el objeto incompleto. super() soluciona esto obligando a recorrer el MRO completo.")
    input("\nPresiona Enter para ir a la última Pregunta...")

    # PREGUNTA 4
    limpiar_pantalla()
    mostrar_cabecera()
    print("PREGUNTA 4/4:")
    print("¿Por qué es fundamental que 'Base' también llame a 'super().__init__()' en su constructor")
    print("si es el ancestro de todos en el diagrama?")
    print("A) Porque es obligatorio por sintaxis en Python.")
    print("B) Para que el flujo cooperativo continúe y llegue a la clase base de Python ('object').")
    print("C) No es necesario, se puede omitir sin problemas.")
    
    ans = ""
    while ans not in ['A', 'B', 'C']:
        ans = input("\nTu respuesta (A, B, C): ").strip().upper()
        
    if ans == 'B':
        print("\n¡CORRECTO! 🌟")
        print("Exacto. En jerarquías complejas, delegar hasta 'object' asegura que todos los métodos")
        print("en la cadena tengan la oportunidad de ejecutarse de forma ordenada.")
        puntuacion += 1
    else:
        print("\nIncorrecto. ❌")
        print("La respuesta correcta es la B.")
    
    input("\nPresiona Enter para ver la simulación en tiempo real...")
    
    # SIMULACIÓN DINÁMICA
    limpiar_pantalla()
    mostrar_cabecera()
    print("EJECUCIÓN DEL FLUJO EN TIEMPO REAL:")
    print("-" * 50)
    tracker = []
    # Instanciamos la clase real
    sub_obj = Sub(tracker)
    
    print("\nOrden de entrada y salida de constructores:")
    for i, paso in enumerate(tracker, 1):
        print(f"  Paso {i:02d}: {paso}")
        
    print("-" * 50)
    print("\n¡Resultado del Desafío!")
    print(f"Tu puntuación final: {puntuacion}/{total_preguntas}")
    if puntuacion == total_preguntas:
        print("🏆 ¡Excelente! Has dominado el Diamante de la herencia múltiple.")
    elif puntuacion >= 2:
        print("👍 ¡Buen trabajo! Tienes bases sólidas, sigue practicando.")
    else:
        print("📖 Te recomendamos repasar el orden del MRO y volver a intentarlo.")

def menu():
    while True:
        limpiar_pantalla()
        mostrar_cabecera()
        print("1. Guía Teórica de MRO y Super")
        print("2. Iniciar Desafío de Preguntas (El Diamante)")
        print("3. Ver MRO de la clase 'Sub'")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ").strip()
        if opcion == '1':
            mostrar_teoria()
        elif opcion == '2':
            ejecutar_desafio()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == '3':
            limpiar_pantalla()
            mostrar_cabecera()
            print("MRO de la clase 'Sub':\n")
            for i, clase in enumerate(Sub.__mro__, 1):
                print(f"  {i}. {clase}")
            print("\nEstructura jerárquica de resolución:")
            print(" -> ".join([c.__name__ for c in Sub.__mro__]))
            input("\nPresiona Enter para volver al menú...")
        elif opcion == '4':
            print("\n¡Gracias por aprender con MRO Explorer! Hasta pronto.\n")
            break

if __name__ == "__main__":
    menu()
