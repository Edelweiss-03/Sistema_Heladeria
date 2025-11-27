# ============================================
# SISTEMA DE GESTIÓN DE PEDIDOS DE HELADERÍA
# ============================================

from crear_pedido import guardar_pedido, mostrar_gustos, mostrar_tamaños_y_precios
from archivo_json import leer_json
from mostrar_pedidos_guardados import mostrar_base_datos


def main():
    precios = leer_json("data/precios.json")
    gustos_disponibles = leer_json("data/gustos.json")
    pedidos = []

    while True:
        print("====== MENÚ PRINCIPAL ======")
        print("1️⃣ Registrar un nuevo pedido")
        print("2️⃣ Mostrar resumen de pedidos")
        print("3️⃣ Salir")
        opcion = input("> ").strip()

        if opcion == "1":
            guardar_pedido(pedidos, gustos_disponibles, precios)
        elif opcion == "2":
            mostrar_base_datos()
        elif opcion == "3":
            print("👋 ¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()


