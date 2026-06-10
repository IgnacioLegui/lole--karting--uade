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

# ==============================================================
#   DATOS DEL NEGOCIO (guardados en una lista)
# ==============================================================
# Posiciones: 0 nombre, 1 cuit, 2 direccion, 3 telefono, 4 instagram, 5 horarios
datos_negocio = [
    "LOLE KARTING",
    "30-71234567-9",
    "Av. Cnel. Roca 3850, Lugano, CABA",
    "+54 11 4605-7890",
    "@lolekarting",
    "Lun-Vie 14:00-22:00  /  Sab-Dom 10:00-22:00"
]

# ==============================================================
#   DATOS DE LOS SERVICIOS (listas paralelas)
# ==============================================================
# Cada posicion de las tres listas representa un mismo servicio
nombres_servicios = ["Simulador de manejo", "Pista de karting", "Curso de manejo", "Paquete de cumpleaños"]
precios_servicios = [3500, 6000, 15000, 80000]
detalle_servicios = ["15 min", "10 min / 10 vueltas", "1 hora", "8 hs (pista + simuladores)"]

# ==============================================================
#   SEPARADORES
# ==============================================================
separador = "============================================================"
linea     = "------------------------------------------------------------"

# ==============================================================
#   FUNCIONES DE VALIDACION
# ==============================================================

# Valida que un texto tenga al menos 2 caracteres. Devuelve el texto validado.
def pedir_texto(mensaje):
    texto = input(mensaje).title()
    while len(texto) < 2:
        print("  ERROR: Debe tener al menos 2 caracteres.")
        texto = input(mensaje).title()
    return texto

# Valida que un DNI tenga 7 u 8 digitos. Devuelve el DNI validado.
def pedir_dni(mensaje):
    dni = input(mensaje)
    while len(dni) < 7 or len(dni) > 8:
        print("  ERROR: El DNI debe tener 7 u 8 digitos.")
        dni = input(mensaje)
    return dni

# Valida una respuesta de tipo s/n. Devuelve "s" o "n".
def pedir_si_no(mensaje):
    resp = input(mensaje).lower()
    while resp != "s" and resp != "n":
        print("  ERROR: Ingrese 's' para si o 'n' para no.")
        resp = input(mensaje).lower()
    return resp

# Valida un numero entero dentro de un rango (incluye los limites).
def pedir_numero(mensaje, minimo, maximo):
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        print("  ERROR: Ingrese un numero entre", minimo, "y", maximo, ".")
        numero = int(input(mensaje))
    return numero

# ==============================================================
#   FUNCIONES DE OPERACIONES ARITMETICAS
# ==============================================================

# Calcula el subtotal multiplicando cantidad por precio.
def calcular_subtotal(cantidad, precio):
    return cantidad * precio

# Calcula el total final aplicando descuento y recargo sobre el subtotal.
def calcular_total(subtotal, descuento, recargo):
    return round(subtotal - descuento + recargo, 2)

# Calcula un porcentaje: (parte * 100) / total.
def calcular_porcentaje(parte, total):
    return round((parte * 100) / total, 2)

# Recorre una lista de montos y devuelve la suma de todos.
def sumar_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return round(suma, 2)

# Recorre una lista de montos y devuelve el valor maximo.
def maximo_lista(lista):
    maximo = -9999
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

# Recibe la lista de cantidades y devuelve la lista de subtotales (lista paralela).
def calcular_subtotales(cantidades):
    subtotales = [0, 0, 0, 0]
    for i in range(len(cantidades)):
        subtotales[i] = calcular_subtotal(cantidades[i], precios_servicios[i])
    return subtotales

# ==============================================================
#   FUNCION DE NUMERO DE FACTURA ALEATORIO Y SIN REPETIR
# ==============================================================

# Genera un nro de factura aleatorio que no este ya en la lista de usados.
# Usa busqueda_lineal para verificar si el numero ya fue utilizado.
def generar_factura(facturas_usadas):
    nro = random.randint(1000, 9999)
    while busqueda_lineal(facturas_usadas, nro) != -1:
        nro = random.randint(1000, 9999)
    return nro

# ==============================================================
#   FUNCION DE ORDENAMIENTO (METODO BURBUJA)
# ==============================================================

# Ordena la matriz por nro de factura (columna 0) de menor a mayor.
# Ordena en paralelo la lista de DNIs para que cada DNI siga junto a su venta.
def ordenar_matriz(matriz, dnis):
    for i in range(len(matriz)):
        for j in range(len(matriz) - i - 1):
            if matriz[j][0] > matriz[j + 1][0]:
                # Intercambiamos la fila de la matriz
                aux = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = aux
                # Intercambiamos el DNI en la misma posicion (lista paralela)
                aux_dni = dnis[j]
                dnis[j] = dnis[j + 1]
                dnis[j + 1] = aux_dni

# ==============================================================
#   FUNCION QUE MUESTRA EL CATALOGO DE SERVICIOS
# ==============================================================

# Muestra el menu de servicios tomando los precios desde las listas.
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

# ==============================================================
#   FUNCION QUE PIDE Y VALIDA LOS DATOS DEL CLIENTE
# ==============================================================

# Pide los datos del cliente y los devuelve dentro de una lista.
# La lista tiene: [nombre, apellido, dni, nombre_adulto, apellido_adulto, dni_adulto]
# Devuelve None si el menor no cumple la edad minima (se interrumpe la venta).
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
            # CORRECCION: si no llega a la edad minima NO se vuelve a preguntar,
            # se avisa y se interrumpe la venta devolviendo None.
            if edad_menor < 10:
                print("  El menor debe tener al menos 10 años para participar.")
                print("  Se cancela este proceso de venta.")
                return None
            print("-- Datos del adulto acompañante --")
            nombre_adulto   = pedir_texto("Nombre del adulto: ")
            apellido_adulto = pedir_texto("Apellido del adulto: ")
            dni_adulto      = pedir_dni("DNI del adulto (7 u 8 digitos): ")

        # Confirmacion de datos personales
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

# ==============================================================
#   FUNCION QUE PIDE LA SELECCION DE SERVICIOS
# ==============================================================

# Pide los servicios y devuelve una lista con las cantidades de cada uno.
# La posicion coincide con las listas de servicios (0=simulador, 1=karting, etc).
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
                # opcion 1 -> posicion 0, opcion 2 -> posicion 1, etc.
                cantidades[opcion_serv - 1] = cantidades[opcion_serv - 1] + cantidad
                print("    OK - Total", nombres_servicios[opcion_serv - 1], ":", cantidades[opcion_serv - 1])

        # Validar que se haya elegido al menos un servicio
        total_elegido = sumar_lista(cantidades)
        if total_elegido == 0:
            print("  ERROR: Debe seleccionar al menos un servicio.")
        else:
            seleccion_valida = True

    return cantidades

# ==============================================================
#   FUNCIONES DE DESCUENTO, RECARGO Y MEDIO DE PAGO
# ==============================================================

# Calcula el descuento del 20% si hay paquete de cumpleaños y se abona anticipado.
# Recibe las cantidades y los subtotales. Devuelve el monto del descuento.
def procesar_descuento(cantidades, subtotales):
    descuento = 0
    # El paquete de cumpleaños esta en la posicion 3
    if cantidades[3] > 0:
        resp_desc = pedir_si_no("El paquete de cumpleaños se abona con mas de 7 dias de anticipacion? (s/n): ")
        if resp_desc == "s":
            descuento = round(subtotales[3] * 0.20, 2)
            print("  Descuento del 20% aplicado sobre el paquete de cumpleaños.")
    return descuento

# Calcula el recargo del 15% si hubo daños. Recibe el subtotal. Devuelve el recargo.
def procesar_recargo(subtotal):
    recargo = 0
    resp_daño = pedir_si_no("Hubo daños al karting o al equipamiento? (s/n): ")
    if resp_daño == "s":
        recargo = round(subtotal * 0.15, 2)
        print("  Recargo del 15% por daños aplicado.")
    return recargo

# Muestra los medios de pago, pide la opcion y devuelve el texto del medio elegido.
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

# ==============================================================
#   FUNCION QUE MUESTRA LA FACTURA
# ==============================================================

# Muestra la factura completa de una venta.
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

# ==============================================================
#   FUNCION QUE PROCESA UNA VENTA COMPLETA
# ==============================================================

# Muestra el titulo/encabezado de un proceso de venta.
def mostrar_titulo_venta(numero, total_ventas):
    print(separador)
    print("    LOLE KARTING  -  PROCESO DE VENTA", numero, "DE", total_ventas)
    print(separador)

# Procesa una venta de principio a fin.
# Recibe el numero de venta, el total de ventas y la lista de facturas ya usadas.
# Devuelve una lista con dos cosas:
#   - la fila para la matriz 3x4: [nro_factura, nombre, apellido, total]
#   - el dni del cliente (para guardarlo en la lista paralela de DNIs)
# Devuelve None si la venta se cancela (menor sin la edad minima).
def procesar_venta(numero, total_ventas, facturas_usadas):
    mostrar_titulo_venta(numero, total_ventas)

    # PASO 1: Datos del cliente
    cliente = pedir_datos_cliente()
    if cliente == None:
        return None

    # PASO 2: Catalogo y seleccion de servicios
    mostrar_catalogo()
    cantidades = pedir_servicios()

    # PASO 3: Calculos (subtotales, descuento, recargo y total)
    subtotales = calcular_subtotales(cantidades)
    subtotal   = sumar_lista(subtotales)
    descuento  = procesar_descuento(cantidades, subtotales)
    recargo    = procesar_recargo(subtotal)
    medio_pago = elegir_medio_pago()
    total      = calcular_total(subtotal, descuento, recargo)

    # PASO 4: Numero de factura aleatorio y sin repetir
    nro_factura = generar_factura(facturas_usadas)
    facturas_usadas.append(nro_factura)

    # PASO 5: Mostrar factura
    mostrar_factura(nro_factura, cliente, cantidades, subtotales, subtotal, descuento, recargo, total, medio_pago)

    # La fila de la matriz tiene 4 columnas (matriz 3x4 con 3 ventas):
    #   0 factura, 1 nombre, 2 apellido, 3 total
    fila = [nro_factura, cliente[0], cliente[1], total]
    # El DNI se guarda aparte, en una lista paralela a la matriz.
    dni = cliente[2]
    return [fila, dni]

# ==============================================================
#   FUNCION QUE MUESTRA LA MATRIZ DE VENTAS
# ==============================================================

# Muestra la matriz 3x4 ya ordenada (factura, nombre, apellido, total).
def mostrar_matriz(matriz):
    print(separador)
    print("        MATRIZ DE VENTAS 3x4 (ordenada por factura)")
    print(separador)
    print("  FACTURA  |  NOMBRE      |  APELLIDO    |  TOTAL")
    print(linea)
    for i in range(len(matriz)):
        print("  FC-", matriz[i][0], " | ", matriz[i][1], " | ", matriz[i][2], " | $", matriz[i][3])
    print(separador)

# ==============================================================
#   FUNCION QUE MUESTRA LAS ESTADISTICAS
# ==============================================================

# Calcula y muestra el resumen de las ventas (total, promedio, maximo y porcentajes).
def mostrar_estadisticas(matriz):
    # Armamos una lista solo con los totales (columna 3) para las estadisticas
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

# ==============================================================
#   BUSQUEDA LINEAL
# ==============================================================

# Recorre una lista posicion por posicion buscando el dato.
# Si algun elemento coincide, devuelve su posicion.
# Si no lo encuentra, devuelve -1.
# Funciona con cualquier tipo de dato (strings, enteros, etc.).
def busqueda_lineal(lista, dato):
    posicion = -1
    for i in range(len(lista)):
        if lista[i] == dato:
            posicion = i
    return posicion

# ==============================================================
#   FUNCION BUSCADOR DE CLIENTES
# ==============================================================

# Pide un dato por teclado y busca una venta por nombre, apellido o DNI.
# Arma listas separadas en minusculas y aplica busqueda_lineal sobre cada una.
# Repite hasta que el dato coincida con alguna venta.
def buscar_venta(matriz, dnis):
    print("  BUSCADOR DE VENTAS")
    print("  Ingrese un nombre, apellido o DNI para buscar una venta.")

    # Armamos listas en minusculas para que la busqueda no distinga mayusculas
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

        # Aplicamos busqueda lineal sobre cada lista por separado
        pos = busqueda_lineal(nombres, dato)
        if pos == -1:
            pos = busqueda_lineal(apellidos, dato)
        if pos == -1:
            pos = busqueda_lineal(dnis_lower, dato)

        # Si busqueda_lineal devolvio -1 en las tres listas, no se encontro
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

# ==============================================================
#   FUNCION DE DESPEDIDA
# ==============================================================

# Muestra el mensaje final de despedida del negocio.
def mostrar_despedida():
    print(separador)
    print("  Gracias por elegirnos! Seguinos en", datos_negocio[4])
    print("  ", datos_negocio[0], "-", datos_negocio[2])
    print(separador)

# ==============================================================
#   FUNCION DE CIERRE (matriz + estadisticas + buscador)
# ==============================================================

# Cierra el programa: si hubo ventas las ordena, muestra la matriz,
# las estadisticas, el buscador y la despedida.
# Recibe la matriz 3x4 y la lista paralela de DNIs.
def mostrar_cierre(matriz, dnis):
    if len(matriz) == 0:
        print(separador)
        print("  No se concreto ninguna venta.")
        print(separador)
    else:
        ordenar_matriz(matriz, dnis)   # burbuja por nro de factura (matriz + dnis en paralelo)
        mostrar_matriz(matriz)
        mostrar_estadisticas(matriz)
        buscar_venta(matriz, dnis)
        mostrar_despedida()

# ==============================================================
#   FUNCION QUE PROCESA TODAS LAS VENTAS
# ==============================================================

# Procesa todas las ventas. Devuelve una lista con dos cosas:
#   - la matriz 3x4 con las ventas concretadas
#   - la lista paralela de DNIs
def procesar_todas_las_ventas(cantidad_ventas):
    matriz_ventas   = []   # cada fila: [factura, nombre, apellido, total]
    dnis_ventas     = []   # lista paralela: el dni de cada venta
    facturas_usadas = []   # para controlar que no se repitan los nros

    nro_venta = 0
    while nro_venta < cantidad_ventas:
        resultado = procesar_venta(nro_venta + 1, cantidad_ventas, facturas_usadas)

        # Si la venta no se cancelo, guardamos la fila y el dni en paralelo
        if resultado != None:
            matriz_ventas.append(resultado[0])   # la fila 3x4
            dnis_ventas.append(resultado[1])      # el dni
        else:
            print("  Pasamos a la siguiente venta.")

        nro_venta = nro_venta + 1
        if nro_venta < cantidad_ventas:
            input("  Presione ENTER para continuar...")

    return [matriz_ventas, dnis_ventas]

# ==============================================================
#   PROGRAMA PRINCIPAL
# ==============================================================

# Cantidad de ventas a procesar (cambiando este numero el programa
# sigue funcionando: con 3, con 100, etc.)
CANTIDAD_VENTAS = 3

# 1) Procesamos todas las ventas y obtenemos la matriz 3x4 y la lista de DNIs
resultado_ventas = procesar_todas_las_ventas(CANTIDAD_VENTAS)
matriz_ventas = resultado_ventas[0]
dnis_ventas   = resultado_ventas[1]

# 2) Mostramos el cierre (matriz ordenada, estadisticas, buscador y despedida)
mostrar_cierre(matriz_ventas, dnis_ventas)