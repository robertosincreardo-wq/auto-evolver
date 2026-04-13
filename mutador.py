import random
import os

# 1. El programa lee su propio código
with open("mutador.py", "r") as f:
    lineas = f.readlines()

# 2. SELECCIÓN NATURAL: Elige una línea al azar para "mutar"
# Solo mutamos líneas que tengan valores numéricos o strings simples
idx = random.randint(0, len(lineas) - 1)
if "MOD_" in lineas[idx]:
    # Creamos un cambio aleatorio en una variable de control
    nueva_valor = random.randint(1, 1000)
    lineas[idx] = f"MOD_VALOR = {nueva_valor} # Mutación automática\n"

# 3. El programa se escribe a sí mismo con el cambio
with open("mutador.py", "w") as f:
    f.writelines(lineas)

print("Mutación completada con éxito.")
