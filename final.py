# Sistema de cifrado César modificado (+N)
# Hecho por: Santiago Ospina Bran

LETRAS = 26
CODIGO_A = ord("A")


def es_letra_valida(caracter):
    """Devuelve True solo si el carácter es una letra de la A a la Z (sin Ñ ni tildes)."""
    return caracter.isalpha() and "A" <= caracter <= "Z"


def desplazar_letra(caracter, pasos):
    """Mueve una letra 'pasos' posiciones de forma circular."""
    posicion = ord(caracter) - CODIGO_A
    nueva_posicion = (posicion + pasos) % LETRAS
    return chr(CODIGO_A + nueva_posicion)


def encriptar(mensaje, n):
    """Cifra el mensaje avanzando cada letra N posiciones."""
    texto_cifrado = ""
    for caracter in mensaje.upper():
        if es_letra_valida(caracter):
            texto_cifrado += desplazar_letra(caracter, n % LETRAS)
        else:
            texto_cifrado += caracter  # espacios, números y signos no cambian
    return texto_cifrado


def desencriptar(mensaje, n):
    """Recupera el mensaje original retrocediendo cada letra N posiciones."""
    texto_original = ""
    for caracter in mensaje.upper():
        if es_letra_valida(caracter):
            texto_original += desplazar_letra(caracter, -(n % LETRAS))
        else:
            texto_original += caracter
    return texto_original


def pedir_n():
    """Pide N hasta que el usuario ingrese un entero mayor o igual a 0."""
    while True:
        try:
            n = int(input("Ingrese el desplazamiento N: ").strip())
            if n >= 0:
                return n
            print("N no puede ser negativo. Intente de nuevo.")
        except ValueError:
            print("Valor inválido: N debe ser un número entero.")


def pedir_confirmacion(pregunta):
    """Pide una respuesta S o N y devuelve True si es S."""
    respuesta = input(pregunta).strip().upper()
    while respuesta not in ("S", "N"):
        print("Responda únicamente S o N.")
        respuesta = input(pregunta).strip().upper()
    return respuesta == "S"


def opcion_encriptar(registros):
    texto = input("Ingrese el mensaje: ").strip()
    n = pedir_n()
    resultado = encriptar(texto, n)

    print("Mensaje original:", texto.upper())
    print("Mensaje encriptado:", resultado)

    if pedir_confirmacion("¿Desea guardar el mensaje? (S/N): "):
        registros.append({"original": texto.upper(), "cifrado": resultado, "n": n})
        print("Mensaje guardado correctamente.")
    else:
        print("El mensaje no fue guardado.")


def opcion_desencriptar():
    texto = input("Ingrese el mensaje encriptado: ").strip()
    n = pedir_n()
    print("Mensaje desencriptado:", desencriptar(texto, n))


def opcion_imprimir(registros):
    if len(registros) == 0:
        print("No hay mensajes guardados.")
        return
    print("MENSAJES GUARDADOS")
    numero = 1
    for registro in registros:
        print(f"{numero}. Original: {registro['original']}")
        print(f"   Encriptado: {registro['cifrado']}")
        print(f"   Desplazamiento: {registro['n']}")
        numero += 1


def imprimir_menu():
    linea = "=" * 32
    print()
    print("SISTEMA DE CIFRADO CÉSAR MODIFICADO")
    print(linea)
    print("1. Encriptar mensaje (Opción de Guardar mensaje (S/N))")
    print("2. Desencriptar mensaje")
    print("3. Imprimir mensajes guardados")
    print("4. Salir")
    print(linea)


def main():
    registros = []
    activo = True

    while activo:
        imprimir_menu()
        eleccion = input("Seleccione una opción: ").strip()

        if eleccion == "1":
            opcion_encriptar(registros)
        elif eleccion == "2":
            opcion_desencriptar()
        elif eleccion == "3":
            opcion_imprimir(registros)
        elif eleccion == "4":
            print("Gracias por utilizar el sistema.")
            activo = False
        else:
            print("Opción inexistente. Elija un número del 1 al 4.")


if __name__ == "__main__":
    main()
