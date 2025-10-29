from archivo_json import leer_json


def pedir_nombre_cliente():
    while True:
        nombre = input("Ingrese el nombre del cliente: ").strip()
        if nombre:
            return nombre.capitalize()
        else:
            print("❌ El nombre no puede estar vacío. Intente nuevamente.")

def mostrar_tamaños_y_precios():
    ruta_precios = "data/precios.json"
    precios = leer_json(ruta_precios)

    if not precios:
        print("⚠️ No se encontraron precios. Verifique el archivo data/precios.json.")
        return {}

    print("\n🍦 Tamaños disponibles:")
    print("----------------------")
    for tamaño, precio in precios.items():
        print(f"{tamaño.capitalize():<10} → ${precio}")
    print("----------------------\n")

    return precios

def pedir_tamaño(precios):
    print("\nIngrese el tamaño que desea (chico / mediano / grande):")
    while True:
        tamaño = input("> ").strip().lower()
        if tamaño in precios:
            print(f"✅ Tamaño elegido: {tamaño.capitalize()}")
            return tamaño
        else:
            print("❌ Tamaño no reconocido. Intente nuevamente.")


def mostrar_gustos():
    ruta_gustos = "data/gustos.json"
    gustos = leer_json(ruta_gustos)

    if not gustos:
        print("⚠️ No se encontraron gustos. Verifique el archivo data/gustos.json.")
        return {}

    print("\n🍦 Gustos disponibles:")
    print("----------------------")
    for gusto, disponible in gustos.items():
        estado = "Disponible" if disponible else "No disponible"
        print(f"{gusto.capitalize():<20} → {estado}")
    print("----------------------\n")

    return gustos

def pedir_gusto(gustos, tamaño):
    validos = 0
    gustos_elegidos = []

    if tamaño == 'chico' or tamaño == 'mediano':
        limite = 3
    else:
        limite = 4

    while validos < limite:
        print(f"\nIngrese el gusto que desea (máximo {limite} gustos):")
        print("(chocolate, dulce de leche, frutilla, menta granizada, limón, vainilla)")
        gusto = input("> ").strip().lower()

        if gusto in gustos:
            if gusto not in gustos_elegidos:
                gustos_elegidos.append(gusto)
                validos += 1
                print(f"✅ Gusto elegido: {gusto.capitalize()}")
            else:
                print("⚠️ Ya elegiste ese gusto, probá con otro.")
        else:
            print("❌ Gusto no reconocido. Intente nuevamente.")

    return gustos_elegidos


def calcular_total(tamaño):
    if tamaño == 'chico':
        return 1200
    elif tamaño == 'mediano':
        return 1800
    elif tamaño == 'grande':
        return 2300
    else:
        return 0


def guardar_pedido(pedidos, gustos_disponibles,precios):
    cliente = pedir_nombre_cliente()
    tamaño = pedir_tamaño(precios)
    gustos_elegidos = pedir_gusto(gustos_disponibles, tamaño)
    total = calcular_total(tamaño)

    pedido = {
        "cliente": cliente,
        "tamaño": tamaño,
        "gustos": gustos_elegidos,
        "total": total
    }

    pedidos.append(pedido)


    with open("pedidos.txt", "a", encoding="utf-8") as archivo:
        linea = f"Cliente: {cliente} | Tamaño: {tamaño.capitalize()} | Gustos: {', '.join(gustos_elegidos)} | Total: ${total}\n"
        archivo.write(linea)

    print("\n🧾 Pedido guardado correctamente.")
    print(f"👤 Cliente: {cliente}")
    print(f"🍦 Tamaño: {tamaño.capitalize()}")
    print(f"🥄 Gustos: {', '.join(gustos_elegidos)}")
    print(f"💰 Total a pagar: ${total}\n")







    
