def mostrar_base_datos():
    print("\n📖 RESUMEN DE PEDIDOS GUARDADOS")
    print("----------------------------------")

    try:
        with open("pedidos.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            if contenido:
                print(contenido)
            else:
                print("No hay pedidos registrados todavía.")
    except FileNotFoundError:
        print("El archivo 'pedidos.txt' no existe aún. No hay pedidos guardados.")

    print("----------------------------------\n")
