"""
Sistema de Caja y Control de Ventas - "Cafetería Central"
Paradigma de programación: Programación Estructurada / Procedimental
Descripción: Terminal de punto de venta (POS) para el registro
de ventas diarias, cálculo de descuentos, desglose de IVA y cierre de caja.
"""

# ==============================================================================
# A. PARÁMETROS FIJOS (CONSTANTES)
# ==============================================================================
IMPUESTO_IVA = 0.19             # 19% de IVA (incluido en los precios finales)
MONTO_MINIMO_DESCUENTO = 15000  # Monto mínimo en pesos para aplicar descuento
PORCENTAJE_DESCUENTO = 0.10     # 10% de descuento sobre el total bruto


def ejecutar_sistema_caja():
    """
    Función principal que controla el flujo de atención de clientes
    y genera el reporte estadístico al cierre del turno.
    """
    # ==========================================================================
    # DECLARACIÓN DE VARIABLES (Contadores, Acumuladores y Banderas)
    # ==========================================================================
    total_clientes_atendidos = 0       # Contador (int) de ventas válidas
    monto_total_recaudado = 0.0        # Acumulador (float) de ingresos finales
    total_descuentos_otorgados = 0.0   # Acumulador (float) de descuentos dados
    continuar_turno = True             # Bandera booleana (bool) de control

    print("=" * 55)
    print("   BIENVENIDO AL SISTEMA POS - CAFETERÍA CENTRAL")
    print("=" * 55)

    # ==========================================================================
    # B. REGISTRO ITERATIVO DE CLIENTES
    # ==========================================================================
    while continuar_turno:
        print("\n--- NUEVO REGISTRO DE VENTA ---")

        # 1. Solicitar el nombre del cliente (str)
        nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
        if nombre_cliente == "":
            nombre_cliente = "Cliente General"

        # 2. Solicitar el monto total bruto de su consumo con manejo de errores
        try:
            monto_bruto = float(input("Ingrese el monto total bruto del consumo ($): "))
        except ValueError:
            print("[ERROR] Debe ingresar un valor numérico válido. Venta cancelada.")
            # Preguntar si desea continuar antes de reiniciar el ciclo
            respuesta = input("\n¿Desea registrar otra venta? (s/n): ").strip()
            continuar_turno = (respuesta == "s" or respuesta == "S")
            continue

        # 3. Validación básica: el monto debe ser estrictamente mayor a cero
        if monto_bruto <= 0:
            print("[ADVERTENCIA] El monto ingresado debe ser mayor a $0. No se procesará la venta.")
        else:
            # 4. Cálculo de Descuento según regla de negocio
            if monto_bruto >= MONTO_MINIMO_DESCUENTO:
                descuento_aplicado = monto_bruto * PORCENTAJE_DESCUENTO
                tiene_descuento = True
            else:
                descuento_aplicado = 0.0
                tiene_descuento = False

            # 5. Cálculo del Total a Pagar y desglose de IVA (19% incluido)
            total_a_pagar = monto_bruto - descuento_aplicado
            monto_neto = total_a_pagar / (1 + IMPUESTO_IVA)
            monto_iva = total_a_pagar - monto_neto

            # Actualización de contadores y acumuladores de caja
            total_clientes_atendidos += 1
            monto_total_recaudado += total_a_pagar
            total_descuentos_otorgados += descuento_aplicado

            # 6. Emisión de Boleta en Pantalla
            print("\n" + "*" * 45)
            print("         BOLETA - CAFETERÍA CENTRAL")
            print("*" * 45)
            print(f"Cliente            : {nombre_cliente}")
            print(f"Subtotal consumido : ${round(monto_bruto):,}")

            if tiene_descuento:
                porcentaje_texto = int(PORCENTAJE_DESCUENTO * 100)
                print(f"Descuento ({porcentaje_texto}%)    : -${round(descuento_aplicado):,}")
            else:
                print("Descuento aplicado : $0")

            print("-" * 45)
            print(f"Valor Neto         : ${round(monto_neto):,}")
            print(f"IVA (19% incluido) : ${round(monto_iva):,}")
            print(f"TOTAL A PAGAR      : ${round(total_a_pagar):,}")
            print("*" * 45)

        # 7. Control del Ciclo mediante confirmación del operador
        respuesta = input("\n¿Desea registrar otra venta? (s/n): ").strip()
        if respuesta == "s" or respuesta == "S":
            continuar_turno = True
        else:
            continuar_turno = False

    # ==========================================================================
    # C. RESUMEN ESTADÍSTICO AL CIERRE DE CAJA
    # ==========================================================================
    # Evitar división por cero si no se registraron ventas válidas en el turno
    if total_clientes_atendidos > 0:
        promedio_gasto = monto_total_recaudado / total_clientes_atendidos
    else:
        promedio_gasto = 0.0

    print("\n" + "=" * 55)
    print("       RESUMEN ESTADÍSTICO - CIERRE DE CAJA")
    print("=" * 55)
    print(f"1. Total de clientes atendidos   : {total_clientes_atendidos}")
    print(f"2. Monto total recaudado         : ${round(monto_total_recaudado):,}")
    print(f"3. Total descuentos otorgados    : ${round(total_descuentos_otorgados):,}")
    print(f"4. Promedio de gasto por cliente : ${round(promedio_gasto):,}")
    print("=" * 55)
    print("Turno finalizado. ¡Buen descanso!")


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_sistema_caja()