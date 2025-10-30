import json
import os

def leer_json(ruta, valor_defecto=None):
    if valor_defecto is None:
        valor_defecto = []

    if not os.path.exists(ruta):
        return valor_defecto

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = json.load(f)
            return contenido
    except (json.JSONDecodeError, ValueError):
        return valor_defecto
    except Exception as e:
        print(f"[leer_json] Error al leer {ruta}: {e}")
        return valor_defecto

def escribir_json(ruta, datos):
    try:
        carpeta = os.path.dirname(ruta)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"[escribir_json] Error al escribir {ruta}: {e}")
        return False

