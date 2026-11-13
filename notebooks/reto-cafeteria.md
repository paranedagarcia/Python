A continuación tienes la **solución de referencia completa y comentada en Python** para el caso práctico avanzado de **"Cafetería Central"**. 

El archivo fuente ejecutable ha sido generado y publicado en tu panel de Studio bajo el nombre **`cafeteria_pos_poo.py`**.

---

### **1. Arquitectura y Decisiones de Diseño POO**

1. **Abstracción Formal (`abc.ABC` y `@abstractmethod`):**
   * La clase `Producto` define el contrato que todo artículo vendible debe cumplir (`calcular_precio_final()` y `obtener_detalle()`).
   * Al heredar de `ABC`, Python bloquea la creación directa de instancias genéricas como `Producto("Café", 1000)`, arrojando un error en tiempo de ejecución (`TypeError`).

2. **Encapsulamiento y Validación con `@property`:**
   * Se protegen los atributos críticos (`_precio_base` y `_cantidad`).
   * El uso de `@property` y `@<atributo>.setter` permite que cualquier asignación externa (e.g. `producto.precio_base = -500` o `ItemPedido(prod, cantidad=0)`) sea interceptada y validada, lanzando excepciones descriptivas (`ValueError`).

3. **Herencia y Polimorfismo ("Es-Un" / *Is-A*):**
   * `Bebida` y `Alimento` heredan de `Producto`. Ambas reutilizan la inicialización de atributos mediante `super().__init__(nombre, precio_base)` y extienden sus propios atributos específicos (`tamano`, `tipo_leche`, `calentar`, `es_vegano`).
   * Cada subclase concreta implementa su propia fórmula en `calcular_precio_final()` sin que el resto del sistema deba inspeccionar el tipo de producto.

4. **Composición y Delegación ("Tiene-Un" / *Has-A*):**
   * **Asociación Débil (`ItemPedido`):** Cada línea de detalle mantiene una referencia a un `Producto` y multiplica la cantidad por el precio polimórfico devuelto por este.
   * **Composición Fuerte (`Pedido`):** El `Pedido` crea y gestiona internamente su lista de `ItemPedido`, y delega el porcentaje de descuento en el objeto `Cliente`.
   * **Agregación Histórica (`CajaRegistradora`):** Centraliza la auditoría de ventas iterando sobre los pedidos completados para calcular totales consolidados y métricas del turno.

---

### **2. Código Fuente Completo de Referencia**

```python
"""
SISTEMA MODULAR DE PUNTO DE VENTA Y GESTIÓN DE PEDIDOS - "CAFETERÍA CENTRAL"
Solución de Referencia Oficial para Docentes y Estudiantes.
Paradigma: Programación Orientada a Objetos (POO) en Python.
Pilares aplicados: Abstracción (ABC), Herencia, Polimorfismo, Encapsulamiento (@property) y Composición.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any

# =====================================================================
# MÓDULO A: ABSTRACCIÓN Y ENCAPSULAMIENTO
# =====================================================================

class Producto(ABC):
    """
    Clase Base Abstracta que define la interfaz y atributos comunes
    para cualquier artículo comercializable de la cafetería.
    
    Aplica:
    - Abstracción: No permite instanciarse directamente (requiere ABC).
    - Encapsulamiento: Protege _precio_base con getter y setter validado.
    """

    def __init__(self, nombre: str, precio_base: float):
        self._nombre = nombre
        # Usamos el setter para garantizar la validación desde la inicialización
        self.precio_base = precio_base

    @property
    def nombre(self) -> str:
        """Getter para el nombre del producto."""
        return self._nombre

    @property
    def precio_base(self) -> float:
        """Getter para el precio base del producto."""
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor: float) -> None:
        """
        Setter con validación de integridad de datos.
        Evita precios negativos o nulos.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError("El precio base debe ser un valor numérico.")
        if valor <= 0:
            raise ValueError(f"El precio base debe ser mayor a 0. Valor recibido: {valor}")
        self._precio_base = float(valor)

    @abstractmethod
    def calcular_precio_final(self) -> float:
        """
        Método polimórfico abstracto. Cada subclase concreta debe implementar
        sus propias reglas de cálculo (recargos, tamaños, impuestos, etc.).
        """
        pass

    @abstractmethod
    def obtener_detalle(self) -> str:
        """
        Retorna la descripción detallada del producto para la emisión del ticket.
        """
        pass

    def __str__(self) -> str:
        """Representación textual formal del producto."""
        return f"{self._nombre} (Base: ${self._precio_base:,.0f})"

# =====================================================================
# MÓDULO B: ESPECIALIZACIÓN Y HERENCIA
# =====================================================================

class Bebida(Producto):
    """
    Especialización de Producto para bebidas preparadas (cafés, infusiones, etc.).
    
    Aplica:
    - Herencia: Hereda nombre y precio base desde Producto.
    - Polimorfismo: Implementa sus propias reglas de tamaño y tipo de leche.
    """

    RECARGOS_TAMANO = {
        "Pequeño": 0.0,
        "Mediano": 0.15,   # +15%
        "Grande": 0.30     # +30%
    }
    RECARGO_LECHE_VEGETAL = 500.0  # Costo fijo por leche vegetal

    def __init__(self, nombre: str, precio_base: float, tamano: str = "Mediano", tipo_leche: str = "Entera"):
        super().__init__(nombre, precio_base)
        
        # Normalizar tamaño permitiendo mayúsculas/minúsculas
        tamano_encontrado = None
        for k in self.RECARGOS_TAMANO:
            if k.lower() == tamano.strip().lower():
                tamano_encontrado = k
                break
        
        if not tamano_encontrado:
            raise ValueError(f"Tamaño inválido: '{tamano}'. Opciones válidas: {list(self.RECARGOS_TAMANO.keys())}")
        
        self._tamano = tamano_encontrado
        self._tipo_leche = tipo_leche

    @property
    def tamano(self) -> str:
        return self._tamano

    @property
    def tipo_leche(self) -> str:
        return self._tipo_leche

    def calcular_precio_final(self) -> float:
        """
        Aplica recargo proporcional según tamaño y recargo fijo si usa leche vegetal.
        """
        porcentaje_tamano = self.RECARGOS_TAMANO[self._tamano]
        precio_con_tamano = self._precio_base * (1 + porcentaje_tamano)
        
        costo_adicional = 0.0
        leche_lower = self._tipo_leche.lower()
        if "vegetal" in leche_lower or "soya" in leche_lower or "almendra" in leche_lower or "avena" in leche_lower:
            costo_adicional += self.RECARGO_LECHE_VEGETAL
            
        return round(precio_con_tamano + costo_adicional, 2)

    def obtener_detalle(self) -> str:
        return f"Bebida: {self._nombre} ({self._tamano} | Leche: {self._tipo_leche})"

class Alimento(Producto):
    """
    Especialización de Producto para repostería, pastelería y alimentos salados.
    
    Aplica:
    - Herencia: Especializa Producto.
    - Polimorfismo: Aplica recargo por calentado en horno e impuesto local de elaboración.
    """

    COSTO_CALENTADO = 200.0
    IMPUESTO_ELABORACION = 0.05  # +5%

    def __init__(self, nombre: str, precio_base: float, calentar: bool = False, es_vegano: bool = False):
        super().__init__(nombre, precio_base)
        self._calentar = bool(calentar)
        self._es_vegano = bool(es_vegano)

    @property
    def calentar(self) -> bool:
        return self._calentar

    @property
    def es_vegano(self) -> bool:
        return self._es_vegano

    def calcular_precio_final(self) -> float:
        """
        Aplica el 5% de impuesto de elaboración y añade $200 si requiere calentado en horno.
        """
        precio_con_impuesto = self._precio_base * (1 + self.IMPUESTO_ELABORACION)
        costo_servicio = self.COSTO_CALENTADO if self._calentar else 0.0
        return round(precio_con_impuesto + costo_servicio, 2)

    def obtener_detalle(self) -> str:
        opc_caliente = "Horno: Sí" if self._calentar else "Horno: No"
        opc_vegano = " [Vegano]" if self._es_vegano else ""
        return f"Alimento: {self._nombre}{opc_vegano} ({opc_caliente})"

# =====================================================================
# MÓDULO C: COMPOSICIÓN Y DELEGACIÓN
# =====================================================================

class Cliente:
    """
    Representa a la persona que realiza la compra.
    Contiene la lógica de descuentos asociados a su nivel o categoría.
    """

    DESCUENTOS = {
        "Regular": 0.0,
        "Frecuente": 0.10,  # 10% de descuento
        "VIP": 0.20         # 20% de descuento
    }

    def __init__(self, nombre: str, rut: str, tipo_cliente: str = "Regular"):
        self._nombre = nombre
        self._rut = rut
        
        # Mapeo insensible a mayúsculas/minúsculas
        tipo_encontrado = None
        for k in self.DESCUENTOS:
            if k.lower() == tipo_cliente.strip().lower():
                tipo_encontrado = k
                break
                
        if not tipo_encontrado:
            raise ValueError(f"Tipo de cliente inválido: '{tipo_cliente}'. Opciones válidas: {list(self.DESCUENTOS.keys())}")
            
        self._tipo_cliente = tipo_encontrado

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def rut(self) -> str:
        return self._rut

    @property
    def tipo_cliente(self) -> str:
        return self._tipo_cliente

    def obtener_porcentaje_descuento(self) -> float:
        """Retorna la tasa porcentual de descuento según la categoría."""
        return self.DESCUENTOS[self._tipo_cliente]

    def __str__(self) -> str:
        return f"{self._nombre} (RUT: {self._rut}) [{self._tipo_cliente}]"

class ItemPedido:
    """
    Línea de detalle individual dentro de un pedido.
    
    Aplica:
    - Composición Débil / Asociación: Contiene una referencia a un Producto.
    - Encapsulamiento: Valida que la cantidad sea un entero >= 1.
    """

    def __init__(self, producto: Producto, cantidad: int = 1):
        if not isinstance(producto, Producto):
            raise TypeError("El item debe contener una instancia derivada de Producto.")
        
        self._producto = producto
        self.cantidad = cantidad

    @property
    def producto(self) -> Producto:
        return self._producto

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 1:
            raise ValueError(f"La cantidad debe ser un entero mayor o igual a 1. Valor recibido: {valor}")
        self._cantidad = valor

    def calcular_subtotal(self) -> float:
        """
        Delega el cálculo unitario al polimorfismo de la clase Producto
        y multiplica por la cantidad.
        """
        return round(self._producto.calcular_precio_final() * self._cantidad, 2)

class Pedido:
    """
    Entidad compuesta central que agrupa al cliente y las líneas de detalle.
    
    Aplica:
    - Composición Fuerte: Gestiona la lista interna de ItemPedido.
    - Delegación: Delega los subtotales a cada item y el descuento al cliente.
    """

    def __init__(self, id_pedido: int, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("El pedido debe asociarse a una instancia válida de Cliente.")
        
        self._id_pedido = id_pedido
        self._cliente = cliente
        self._items: List[ItemPedido] = []
        self._fecha_hora = datetime.now()

    @property
    def id_pedido(self) -> int:
        return self._id_pedido

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def items(self) -> List[ItemPedido]:
        # Devolvemos una copia superficial para proteger la encapsulación interna
        return list(self._items)

    @property
    def fecha_hora(self) -> datetime:
        return self._fecha_hora

    def agregar_item(self, producto: Producto, cantidad: int = 1) -> None:
        """Crea internamente el ItemPedido y lo anexa a la colección."""
        nuevo_item = ItemPedido(producto, cantidad)
        self._items.append(nuevo_item)

    def calcular_subtotal(self) -> float:
        """Calcula el total bruto antes de descuentos."""
        return round(sum(item.calcular_subtotal() for item in self._items), 2)

    def calcular_descuento(self) -> float:
        """Aplica la tasa de descuento del cliente sobre el subtotal."""
        porcentaje = self._cliente.obtener_porcentaje_descuento()
        return round(self.calcular_subtotal() * porcentaje, 2)

    def calcular_total(self) -> float:
        """Monto neto definitivo a cobrar."""
        return round(self.calcular_subtotal() - self.calcular_descuento(), 2)

    def emitir_boleta(self) -> str:
        """
        Genera la representación gráfica formal de la boleta de venta.
        """
        porcentaje_desc = int(self._cliente.obtener_porcentaje_descuento() * 100)
        lineas = [
            "=" * 72,
            "                   CAFETERÍA CENTRAL - BOLETA DE VENTA",
            "=" * 72,
            f"Pedido N°   : {self._id_pedido}",
            f"Cliente     : {self._cliente.nombre} [{self._cliente.tipo_cliente}]",
            f"RUT         : {self._cliente.rut}",
            f"Fecha / Hora: {self._fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}",
            "-" * 72,
            f"{'CANT.':<6} {'DESCRIPCIÓN':<42} {'UNITARIO':<10} {'TOTAL':<10}",
            "-" * 72,
        ]

        for item in self._items:
            unitario = item.producto.calcular_precio_final()
            subtotal_linea = item.calcular_subtotal()
            desc = item.producto.obtener_detalle()
            desc_formateada = (desc[:39] + '...') if len(desc) > 42 else desc
            lineas.append(f"{item.cantidad:<6} {desc_formateada:<42} ${unitario:>8,.0f} ${subtotal_linea:>8,.0f}")

        lineas.extend([
            "-" * 72,
            f"{'SUBTOTAL BRUTO':<50} : ${self.calcular_subtotal():>14,.0f}",
            f"{f'DESCUENTO ({self._cliente.tipo_cliente} {porcentaje_desc}%)':<50} : -${self.calcular_descuento():>13,.0f}",
            "=" * 72,
            f"{'TOTAL A PAGAR':<50} : ${self.calcular_total():>14,.0f}",
            "=" * 72,
        ])
        return "\n".join(lineas)

# =====================================================================
# MÓDULO D: GESTIÓN GLOBAL DE TURNO Y CAJA
# =====================================================================

class CajaRegistradora:
    """
    Administra la colección de pedidos completados en el turno de trabajo.
    Permite el cierre de caja y la auditoría estadística de ventas.
    """

    def __init__(self, id_caja: str, cajero: str):
        self._id_caja = id_caja
        self._cajero = cajero
        self._pedidos: List[Pedido] = []

    @property
    def id_caja(self) -> str:
        return self._id_caja

    @property
    def cajero(self) -> str:
        return self._cajero

    def registrar_pedido(self, pedido: Pedido) -> None:
        """Registra un pedido finalizado en la memoria del turno."""
        if not isinstance(pedido, Pedido):
            raise TypeError("Solo se pueden registrar instancias de Pedido.")
        if len(pedido.items) == 0:
            raise ValueError("No se puede registrar un pedido sin items de compra.")
        self._pedidos.append(pedido)

    def generar_cierre_caja(self) -> Dict[str, Any]:
        """
        Calcula las métricas consolidadas del turno.
        """
        total_pedidos = len(self._pedidos)
        if total_pedidos == 0:
            return {
                "id_caja": self._id_caja,
                "cajero": self._cajero,
                "total_pedidos": 0,
                "recaudacion_bruta": 0.0,
                "descuentos_totales": 0.0,
                "recaudacion_neta": 0.0,
                "ticket_promedio": 0.0,
                "pedido_maximo": None
            }

        recaudacion_bruta = sum(p.calcular_subtotal() for p in self._pedidos)
        descuentos_totales = sum(p.calcular_descuento() for p in self._pedidos)
        recaudacion_neta = sum(p.calcular_total() for p in self._pedidos)
        ticket_promedio = recaudacion_neta / total_pedidos
        pedido_maximo = max(self._pedidos, key=lambda p: p.calcular_total())

        return {
            "id_caja": self._id_caja,
            "cajero": self._cajero,
            "total_pedidos": total_pedidos,
            "recaudacion_bruta": round(recaudacion_bruta, 2),
            "descuentos_totales": round(descuentos_totales, 2),
            "recaudacion_neta": round(recaudacion_neta, 2),
            "ticket_promedio": round(ticket_promedio, 2),
            "pedido_maximo": pedido_maximo
        }

    def emitir_informe_cierre(self) -> str:
        """Retorna el informe formateado de cierre de caja."""
        cierre = self.generar_cierre_caja()
        max_pedido_str = "N/A"
        if cierre["pedido_maximo"]:
            p = cierre["pedido_maximo"]
            max_pedido_str = f"Pedido #{p.id_pedido} (${p.calcular_total():,.0f} - {p.cliente.nombre})"

        lineas = [
            "#" * 72,
            "             INFORME CONSOLIDADO DE CIERRE DE CAJA",
            "#" * 72,
            f"Terminal de Caja         : {cierre['id_caja']}",
            f"Cajero Responsable       : {cierre['cajero']}",
            f"Fecha de Emisión         : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "-" * 72,
            f"Cantidad de Pedidos      : {cierre['total_pedidos']}",
            f"Venta Bruta Acumulada    : ${cierre['recaudacion_bruta']:>14,.0f}",
            f"Descuentos Otorgados     : -${cierre['descuentos_totales']:>13,.0f}",
            f"Recaudación Neta en Caja : ${cierre['recaudacion_neta']:>14,.0f}",
            f"Ticket Promedio de Venta : ${cierre['ticket_promedio']:>14,.0f}",
            f"Venta Más Alta del Turno : {max_pedido_str}",
            "#" * 72,
        ]
        return "\n".join(lineas)

# =====================================================================
# BLOQUE PRINCIPAL: SIMULACIÓN Y VALIDACIÓN DEL CASO PRÁCTICO
# =====================================================================

if __name__ == "__main__":
    print("\nIniciando simulación del Sistema POS en 'Cafetería Central'...\n")

    # 1. Verificación de Abstracción: No se puede instanciar la clase abstracta
    try:
        prod_invalido = Producto("Genérico", 1000)
    except TypeError as e:
        print(f"[OK] Abstracción verificada: Producto no puede instanciarse directamente.")
        print(f"     Mensaje de excepción: {e}\n")

    # 2. Inicialización de la Caja Registradora
    caja = CajaRegistradora(id_caja="CAJA-01", cajero="Roberto Fuentes")

    # 3. Creación de Catálogo de Productos
    cafe_latte = Bebida(nombre="Café Latte", precio_base=2500, tamano="Grande", tipo_leche="Vegetal")
    expresso = Bebida(nombre="Expresso Doble", precio_base=1800, tamano="Pequeño", tipo_leche="Entera")
    muffin = Alimento(nombre="Muffin de Arándanos", precio_base=2500, calentar=True, es_vegano=True)
    croissant = Alimento(nombre="Croissant Jamón Queso", precio_base=3200, calentar=True, es_vegano=False)

    # 4. Caso 1: Pedido con Cliente VIP (20% Descuento)
    cliente_vip = Cliente(nombre="Andrea Morales", rut="16.789.123-4", tipo_cliente="VIP")
    pedido_1 = Pedido(id_pedido=101, cliente=cliente_vip)
    pedido_1.agregar_item(cafe_latte, cantidad=2)
    pedido_1.agregar_item(muffin, cantidad=1)

    print(pedido_1.emitir_boleta())
    caja.registrar_pedido(pedido_1)
    print("\n")

    # 5. Caso 2: Pedido con Cliente Frecuente (10% Descuento)
    cliente_frecuente = Cliente(nombre="Carlos Mendoza", rut="18.456.789-K", tipo_cliente="Frecuente")
    pedido_2 = Pedido(id_pedido=102, cliente=cliente_frecuente)
    pedido_2.agregar_item(croissant, cantidad=2)
    pedido_2.agregar_item(expresso, cantidad=1)

    print(pedido_2.emitir_boleta())
    caja.registrar_pedido(pedido_2)
    print("\n")

    # 6. Caso 3: Pedido con Cliente Regular (Sin descuento)
    cliente_regular = Cliente(nombre="Lucía Silva", rut="21.111.222-3", tipo_cliente="Regular")
    pedido_3 = Pedido(id_pedido=103, cliente=cliente_regular)
    pedido_3.agregar_item(expresso, cantidad=1)

    print(pedido_3.emitir_boleta())
    caja.registrar_pedido(pedido_3)
    print("\n")

    # 7. Verificación de Encapsulamiento y Validaciones
    try:
        muffin.precio_base = -500  # Intento de precio negativo
    except ValueError as err:
        print(f"[OK] Encapsulamiento verificado: Validación de precio base exitosa.")
        print(f"     Excepción capturada: {err}\n")

    try:
        ItemPedido(expresso, cantidad=0)  # Intento de cantidad 0
    except ValueError as err:
        print(f"[OK] Encapsulamiento verificado: Validación de cantidad en ItemPedido exitosa.")
        print(f"     Excepción capturada: {err}\n")

    # 8. Emisión del Cierre Consolidado de Turno
    print(caja.emitir_informe_cierre())
    print("\n[+] Simulación finalizada exitosamente.")
```

---

### **3. Salida de la Ejecución de Prueba en Consola**

```text
Iniciando simulación del Sistema POS en 'Cafetería Central'...

[OK] Abstracción verificada: Producto no puede instanciarse directamente.
     Mensaje de excepción: Can't instantiate abstract class Producto without an implementation for abstract methods 'calcular_precio_final', 'obtener_detalle'

========================================================================
                   CAFETERÍA CENTRAL - BOLETA DE VENTA
========================================================================
Pedido N°   : 101
Cliente     : Andrea Morales [VIP]
RUT         : 16.789.123-4
Fecha / Hora: 2026-11-12 20:30:31
------------------------------------------------------------------------
CANT.  DESCRIPCIÓN                                UNITARIO   TOTAL     
------------------------------------------------------------------------
2      Bebida: Café Latte (Grande | Leche: Veg... $   3,750 $   7,500
1      Alimento: Muffin de Arándanos [Vegano] ... $   2,825 $   2,825
------------------------------------------------------------------------
SUBTOTAL BRUTO                                     : $        10,325
DESCUENTO (VIP 20%)                                : -$        2,065
========================================================================
TOTAL A PAGAR                                      : $         8,260
========================================================================

========================================================================
                   CAFETERÍA CENTRAL - BOLETA DE VENTA
========================================================================
Pedido N°   : 102
Cliente     : Carlos Mendoza [Frecuente]
RUT         : 18.456.789-K
Fecha / Hora: 2026-11-12 20:30:31
------------------------------------------------------------------------
CANT.  DESCRIPCIÓN                                UNITARIO   TOTAL     
------------------------------------------------------------------------
2      Alimento: Croissant Jamón Queso (Horno:... $   3,560 $   7,120
1      Bebida: Expresso Doble (Pequeño | Leche... $   1,800 $   1,800
------------------------------------------------------------------------
SUBTOTAL BRUTO                                     : $         8,920
DESCUENTO (Frecuente 10%)                          : -$          892
========================================================================
TOTAL A PAGAR                                      : $         8,028
========================================================================

========================================================================
                   CAFETERÍA CENTRAL - BOLETA DE VENTA
========================================================================
Pedido N°   : 103
Cliente     : Lucía Silva [Regular]
RUT         : 21.111.222-3
Fecha / Hora: 2026-11-12 20:30:31
------------------------------------------------------------------------
CANT.  DESCRIPCIÓN                                UNITARIO   TOTAL     
------------------------------------------------------------------------
1      Bebida: Expresso Doble (Pequeño | Leche... $   1,800 $   1,800
------------------------------------------------------------------------
SUBTOTAL BRUTO                                     : $         1,800
DESCUENTO (Regular 0%)                             : -$            0
========================================================================
TOTAL A PAGAR                                      : $         1,800
========================================================================

[OK] Encapsulamiento verificado: Validación de precio base exitosa.
     Excepción capturada: El precio base debe ser mayor a 0. Valor recibido: -500

[OK] Encapsulamiento verificado: Validación de cantidad en ItemPedido exitosa.
     Excepción capturada: La cantidad debe ser un entero mayor o igual a 1. Valor recibido: 0

########################################################################
             INFORME CONSOLIDADO DE CIERRE DE CAJA
########################################################################
Terminal de Caja         : CAJA-01
Cajero Responsable       : Roberto Fuentes
Fecha de Emisión         : 2026-11-12 20:30:31
------------------------------------------------------------------------
Cantidad de Pedidos      : 3
Venta Bruta Acumulada    : $        21,045
Descuentos Otorgados     : -$        2,957
Recaudación Neta en Caja : $        18,088
Ticket Promedio de Venta : $         6,029
Venta Más Alta del Turno : Pedido #101 ($8,260 - Andrea Morales)
########################################################################

[+] Simulación finalizada exitosamente.
```

---

🧪 Podríamos añadir una suite de pruebas automatizadas con `unittest` o `pytest` para evaluar las entregas de los estudiantes de forma desatendida.