import random

FILENAME = "mutador.py"

# --- BLOQUE DE ADN (El código mutará lo que esté aquí abajo) ---
MOD_VALOR = 255
# --- FIN DEL BLOQUE ---

def evolucionar():
    with open(FILENAME, "r") as f:
        lineas = f.readlines()

    # Buscamos dónde termina el bloque de ADN
    inicio = -1
    fin = -1
    for i, linea in enumerate(lineas):
        if "BLOQUE DE ADN" in linea: inicio = i
# Resultado_Gen: 389 - 35
MOD_VALOR = 389

    # 1. MUTACIÓN: Cambiamos el valor de la variable
    nueva_valor = random.randint(1, 1000)
    lineas[inicio + 1] = f"MOD_VALOR = {nueva_valor}\n"

    # 2. INVENCIÓN: Intentamos añadir una operación matemática aleatoria
    # A veces el bot escribirá cosas que NO funcionan (esto es la selección natural)
    operadores = ['+', '-', '*', '/']
    operacion = f"# Resultado_Gen: {nueva_valor} {random.choice(operadores)} {random.randint(1, 100)}\n"
    lineas.insert(fin, operacion)

    with open(FILENAME, "w") as f:
        f.writelines(lineas)

if __name__ == "__main__":
    evolucionar()
    print("El código ha mutado. Verificando supervivencia...")
    # Intentamos ejecutar la variable mutada para ver si el código sigue 'vivo'
    print(f"Valor actual del ADN: {MOD_VALOR}")
