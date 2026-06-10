# ==============================================================
#   INTRODUCCION A LA ALGORITMIA
#   TRABAJO PRACTICO GRUPAL Y OBLIGATORIO  -  PARTE 2
#   Docente: Lic. Christian G. SCHENDEL
#
#   Nro. de Grupo: 6
#   Integrantes:
#       - Leguizamon Jose
#       - Volpe Santiago
#       - Martino Tiago
#       - Martinez Victor
#       - Molinari Matias
#
#   LOLE KARTING  -  Sistema de Ventas
# ==============================================================

import random

def pedir_texto(mensaje):
    texto = input(mensaje).title()
    while len(texto) < 2:
        print("  ERROR: Debe tener al menos 2 caracteres.")
        texto = input(mensaje).title()
    return texto

def pedir_dni(mensaje):
    dni = input(mensaje)
    while len(dni) < 7 or len(dni) > 8:
        print("  ERROR: El DNI debe tener 7 u 8 digitos.")
        dni = input(mensaje)
    return dni

def pedir_si_no(mensaje):
    resp = input(mensaje).lower()
    while resp != "s" and resp != "n":
        print("  ERROR: Ingrese 's' para si o 'n' para no.")
        resp = input(mensaje).lower()
    return resp

def pedir_numero(mensaje, minimo, maximo):
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        print("  ERROR: Ingrese un numero entre", minimo, "y", maximo, ".")
        numero = int(input(mensaje))
    return numero


def calcular_subtotal(cantidad, precio):
    return cantidad * precio

def calcular_total(subtotal, descuento, recargo):
    return round(subtotal - descuento + recargo, 2)

def calcular_porcentaje(parte, total):
    return round((parte * 100) / total, 2)

def sumar_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return round(suma, 2)

def maximo_lista(lista):
    maximo = -9999
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

def calcular_subtotales(cantidades):
    subtotales = [0, 0, 0, 0]
    for i in range(len(cantidades)):
        subtotales[i] = calcular_subtotal(cantidades[i], precios_servicios[i])
    return subtotales


def generar_factura(facturas_usadas):
    nro = random.randint(1000, 9999)
    while busqueda_lineal(facturas_usadas, nro) != -1:
        nro = random.randint(1000, 9999)
    return nro


def ordenar_matriz(matriz, dnis):
    for i in range(len(matriz)):
        for j in range(len(matriz) - i - 1):
            if matriz[j][0] > matriz[j + 1][0]:
                aux = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = aux
                aux_dni = dnis[j]
                dnis[j] = dnis[j + 1]
                dnis[j + 1] = aux_dni


def mostrar_catalogo():
    print(separador)
    print("        SERVICIOS DISPONIBLES  -  LOLE KARTING")
    print(separador)
    for i in range(len(nombres_servicios)):
        print(" ", i + 1, ".", nombres_servicios[i], "  $", precios_servicios[i], " |", detalle_servicios[i])
    print("  DESCUENTOS:")
    print("    20% en paquete de cumpleaños abonando con mas de 7 dias de anticipacion")
    print("  RECARGOS:")
    print("    15% por daños al karting o al equipamiento")
    print("  MEDIOS DE PAGO:")
    print("    Efectivo | Tarjeta credito/debito | Billetera virtual (MP/Uala)")
    print(separador)
    print("  Ingrese 0 para finalizar la seleccion.")
    print(separador)


def pedir_datos_cliente():
    datos_ok = "n"
    while datos_ok == "n":
        print("--- DATOS DEL CLIENTE ---")
        nombre   = pedir_texto("Nombre del cliente: ")
        apellido = pedir_texto("Apellido del cliente: ")
        dni      = pedir_dni("DNI del cliente (7 u 8 digitos): ")
        es_mayor = pedir_si_no("El cliente es mayor de 18 años? (s/n): ")

        nombre_adulto   = "-"
        apellido_adulto = "-"
        dni_adulto      = "-"

        if es_mayor == "n":
            print("-- Verificacion de edad del menor --")
            edad_menor = int(input("Edad del menor: "))
            if edad_menor < 10:
                print("  El menor debe tener al menos 10 años para participar.")
                print("  Se cancela este proceso de venta.")
                return None
            print("-- Datos del adulto acompañante --")
            nombre_adulto   = pedir_texto("Nombre del adulto: ")
            apellido_adulto = pedir_texto("Apellido del adulto: ")
            dni_adulto      = pedir_dni("DNI del adulto (7 u 8 digitos): ")

        print("-- Confirme los datos ingresados --")
        print("  Cliente :", nombre, apellido)
        print("  DNI     :", dni)
        if es_mayor == "n":
            print("  Adulto  :", nombre_adulto, apellido_adulto)
            print("  DNI ad. :", dni_adulto)
        datos_ok = pedir_si_no("Son correctos los datos? (s/n): ")
        if datos_ok == "n":
            print("  Volvamos a cargar los datos...")

    return [nombre, apellido, dni, nombre_adulto, apellido_adulto, dni_adulto]


def pedir_servicios():
    seleccion_valida = False
    cantidades = [0, 0, 0, 0]

    while seleccion_valida == False:
        cantidades = [0, 0, 0, 0]
        opcion_serv = -1
        while opcion_serv != 0:
            opcion_serv = pedir_numero("  Seleccione servicio (1-4) o 0 para terminar: ", 0, 4)
            if opcion_serv != 0:
                cantidad = pedir_numero("    Cuantas sesiones/unidades? ", 1, 999)
                cantidades[opcion_serv - 1] = cantidades[opcion_serv - 1] + cantidad
                print("    OK - Total", nombres_servicios[opcion_serv - 1], ":", cantidades[opcion_serv - 1])

        total_elegido = sumar_lista(cantidades)
        if total_elegido == 0:
            print("  ERROR: Debe seleccionar al menos un servicio.")
        else:
            seleccion_valida = True

    return cantidades


def procesar_descuento(cantidades, subtotales):
    descuento = 0
    if cantidades[3] > 0:
        resp_desc = pedir_si_no("El paquete de cumpleaños se abona con mas de 7 dias de anticipacion? (s/n): ")
        if resp_desc == "s":
            descuento = round(subtotales[3] * 0.20, 2)
            print("  Descuento del 20% aplicado sobre el paquete de cumpleaños.")
    return descuento

def procesar_recargo(subtotal):
    recargo = 0
    resp_daño = pedir_si_no("Hubo daños al karting o al equipamiento? (s/n): ")
    if resp_daño == "s":
        recargo = round(subtotal * 0.15, 2)
        print("  Recargo del 15% por daños aplicado.")
    return recargo

def elegir_medio_pago():
    print("MEDIOS DE PAGO:")
    print("  1. Efectivo")
    print("  2. Tarjeta de credito / debito")
    print("  3. Billetera virtual (Mercado Pago / Uala)")
    opcion_pago = pedir_numero("Seleccione medio de pago (1-3): ", 1, 3)
    if opcion_pago == 1:
        medio_pago = "Efectivo"
    elif opcion_pago == 2:
        medio_pago = "Tarjeta de credito / debito"
    else:
        medio_pago = "Billetera virtual (Mercado Pago / Uala)"
    return medio_pago


def mostrar_factura(nro_factura, cliente, cantidades, subtotales, subtotal, descuento, recargo, total, medio_pago):
    print(separador)
    print("                    F A C T U R A")
    print(separador)
    print("  Nro. de Factura : FC-", nro_factura)
    print("  *** DATOS DEL NEGOCIO ***")
    print("  Nombre    :", datos_negocio[0])
    print("  CUIT      :", datos_negocio[1])
    print("  Direccion :", datos_negocio[2])
    print("  Telefono  :", datos_negocio[3])
    print("  Instagram :", datos_negocio[4])
    print("  Horarios  :", datos_negocio[5])
    print("  *** DATOS DEL CLIENTE ***")
    print("  Nombre    :", cliente[0], cliente[1])
    print("  DNI       :", cliente[2])
    if cliente[3] != "-":
        print("  Adulto    :", cliente[3], cliente[4])
        print("  DNI adult.:", cliente[5])
    print("  *** DETALLE DE SERVICIOS ***")
    for i in range(len(cantidades)):
        if cantidades[i] > 0:
            print("  ", nombres_servicios[i], ":", cantidades[i], "x $", precios_servicios[i], "= $", subtotales[i])
    print(linea)
    print("  Subtotal             : $", subtotal)
    if descuento > 0:
        print("  Descuento 20% cumple : -$", descuento)
    if recargo > 0:
        print("  Recargo 15% daños    : +$", recargo)
    print(linea)
    print("  TOTAL A PAGAR        : $", total)
    print("  Medio de pago        :", medio_pago)
    print(separador)


def mostrar_titulo_venta(numero, total_ventas):
    print(separador)
    print("    LOLE KARTING  -  PROCESO DE VENTA", numero, "DE", total_ventas)
    print(separador)

def procesar_venta(numero, total_ventas, facturas_usadas):
    mostrar_titulo_venta(numero, total_ventas)

    cliente = pedir_datos_cliente()
    if cliente == None:
        return None

    mostrar_catalogo()
    cantidades = pedir_servicios()

    subtotales = calcular_subtotales(cantidades)
    subtotal   = sumar_lista(subtotales)
    descuento  = procesar_descuento(cantidades, subtotales)
    recargo    = procesar_recargo(subtotal)
    medio_pago = elegir_medio_pago()
    total      = calcular_total(subtotal, descuento, recargo)

    nro_factura = generar_factura(facturas_usadas)
    facturas_usadas.append(nro_factura)

    mostrar_factura(nro_factura, cliente, cantidades, subtotales, subtotal, descuento, recargo, total, medio_pago)

    fila = [nro_factura, cliente[0], cliente[1], total]
    dni = cliente[2]
    return [fila, dni]


def mostrar_matriz(matriz):
    print(separador)
    print("        MATRIZ DE VENTAS 3x4 (ordenada por factura)")
    print(separador)
    print("  FACTURA  |  NOMBRE      |  APELLIDO    |  TOTAL")
    print(linea)
    for i in range(len(matriz)):
        print("  FC-", matriz[i][0], " | ", matriz[i][1], " | ", matriz[i][2], " | $", matriz[i][3])
    print(separador)


def mostrar_estadisticas(matriz):
    totales = []
    for i in range(len(matriz)):
        totales.append(matriz[i][3])

    total_recaudado = sumar_lista(totales)
    promedio_ventas = round(total_recaudado / len(totales), 2)
    maximo_venta    = maximo_lista(totales)

    print(separador)
    print("      RESUMEN Y ESTADISTICAS DE LAS VENTAS")
    print("                 LOLE KARTING")
    print(separador)
    for i in range(len(matriz)):
        porc = calcular_porcentaje(matriz[i][3], total_recaudado)
        print("  Venta", i + 1, " (FC-", matriz[i][0], ") : $", matriz[i][3], "->", porc, "% del total")
    print(linea)
    print("  Total recaudado    : $", total_recaudado)
    print("  Promedio por venta : $", promedio_ventas)
    print("  Maximo recaudado   : $", maximo_venta)
    print(separador)


def busqueda_lineal(lista, dato):
    posicion = -1
    for i in range(len(lista)):
        if lista[i] == dato:
            posicion = i
    return posicion


def buscar_venta(matriz, dnis):
    print("  BUSCADOR DE VENTAS")
    print("  Ingrese un nombre, apellido o DNI para buscar una venta.")

    nombres   = []
    apellidos = []
    dnis_lower = []
    for i in range(len(matriz)):
        nombres.append(matriz[i][1].lower())
        apellidos.append(matriz[i][2].lower())
        dnis_lower.append(dnis[i].lower())

    encontrado = False
    while encontrado == False:
        dato = input("  Dato a buscar: ").lower()

        pos = busqueda_lineal(nombres, dato)
        if pos == -1:
            pos = busqueda_lineal(apellidos, dato)
        if pos == -1:
            pos = busqueda_lineal(dnis_lower, dato)

        if pos == -1:
            print("  No encontrado. Intente de nuevo.")
        else:
            print(linea)
            print("  VENTA ENCONTRADA")
            print("  Factura :", "FC-", matriz[pos][0])
            print("  Cliente :", matriz[pos][1], matriz[pos][2])
            print("  DNI     :", dnis[pos])
            print("  Total   : $", matriz[pos][3])
            print(linea)
            encontrado = True


def mostrar_despedida():
    print(separador)
    print("  Gracias por elegirnos! Seguinos en", datos_negocio[4])
    print("  ", datos_negocio[0], "-", datos_negocio[2])
    print(separador)


def mostrar_cierre(matriz, dnis):
    if len(matriz) == 0:
        print(separador)
        print("  No se concreto ninguna venta.")
        print(separador)
    else:
        ordenar_matriz(matriz, dnis)
        mostrar_matriz(matriz)
        mostrar_estadisticas(matriz)
        buscar_venta(matriz, dnis)
        mostrar_despedida()


def procesar_todas_las_ventas(cantidad_ventas):
    matriz_ventas   = []
    dnis_ventas     = []
    facturas_usadas = []

    nro_venta = 0
    while nro_venta < cantidad_ventas:
        resultado = procesar_venta(nro_venta + 1, cantidad_ventas, facturas_usadas)

        if resultado != None:
            matriz_ventas.append(resultado[0])
            dnis_ventas.append(resultado[1])
        else:
            print("  Pasamos a la siguiente venta.")

        nro_venta = nro_venta + 1
        if nro_venta < cantidad_ventas:
            input("  Presione ENTER para continuar...")

    return [matriz_ventas, dnis_ventas]

datos_negocio = [
    "LOLE KARTING",
    "30-71234567-9",
    "Av. Cnel. Roca 3850, Lugano, CABA",
    "+54 11 4605-7890",
    "@lolekarting",
    "Lun-Vie 14:00-22:00  /  Sab-Dom 10:00-22:00"
]

nombres_servicios = ["Simulador de manejo", "Pista de karting", "Curso de manejo", "Paquete de cumpleaños"]
precios_servicios = [3500, 6000, 15000, 80000]
detalle_servicios = ["15 min", "10 min / 10 vueltas", "1 hora", "8 hs (pista + simuladores)"]

separador = "============================================================"
linea     = "------------------------------------------------------------"

CANTIDAD_VENTAS = 3

resultado_ventas = procesar_todas_las_ventas(CANTIDAD_VENTAS)
matriz_ventas = resultado_ventas[0]
dnis_ventas   = resultado_ventas[1]

mostrar_cierre(matriz_ventas, dnis_ventas)
