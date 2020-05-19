letras = list((chr(ord('a') + x)) for x in range(10))

# Cantidad de girasoles en los 100 cuadros
ESQUEMA = [
    #   1  2  3  4  5  6  7  8  9  10
    2, 3, 2, 2, 1, 3, 3, 3, 2, 2,  # A
    3, 2, 3, 2, 3, 3, 3, 2, 3, 2,  # B
    1, 2, 2, 3, 3, 1, 3, 2, 2, 3,  # C
    4, 2, 3, 2, 2, 4, 1, 2, 3, 2,  # D
    2, 3, 3, 3, 3, 2, 2, 1, 2, 3,  # E
    3, 3, 1, 3, 3, 2, 2, 2, 3, 2,  # F
    3, 4, 4, 3, 3, 1, 3, 3, 2, 2,  # G
    2, 3, 2, 2, 2, 4, 2, 3, 2, 3,  # H
    3, 3, 2, 3, 2, 1, 4, 1, 2, 3,  # I
    1, 0, 0, 2, 1, 0, 1, 0, 1, 1  # J
]
TOTAL = sum(ESQUEMA)
PROMEDIO = TOTAL / len(ESQUEMA)


# Se genera la matriz que contiene los valores respectivos según el cuadro
def generar_matriz():
    """Utilizo Set, porque es una estructura que almacena
    de forma aleatorio los valores que son alamacenados en ella"""
    cuadro = set()
    x = 0

    for letra in letras:
        for numero in range(1, len(letras) + 1):
            cuadro.add((letra.upper(), numero, ESQUEMA[x]))
            x = x + 1
    return list(cuadro)  # Lo convierto en lista, por manejabilidad


def sum_col(matriz):  # Suma los valores de una columna en matriz
    total = 0
    col = 2  # En la columna 3 se almacena el valor, se inicia el conteo desde cero
    for fil in range(len(matriz)):
        total += matriz[fil][col]
    return total


NUMERO_MUESTRAS = 10
MUESTREO = generar_matriz()[0:NUMERO_MUESTRAS]
suma_muestreo = sum_col(MUESTREO)
promedio_muestreo = suma_muestreo / len(MUESTREO)
total_muestreo = promedio_muestreo * 100

# Mostrar resultados
print(f"""
           -- INFORMACIÓN REAL --
Total de número de girasoles:                    {TOTAL}
Promedio de número de girasoles en cada cuadro:  {PROMEDIO}

           -- INFORMACIÓN DE MUESTREO ALEATORIO --

Segmento del Campo      Número de girasoles""")
for iteracion, muestra in enumerate(MUESTREO, 1):
    print(f"""{muestra[:2]}                  {muestra[-1]}""")

print(f"""
Total de girasoles en muestreo:                  {suma_muestreo}
Promedio (total dividido por 10):                {promedio_muestreo}
Total del número de plantas del área:            {total_muestreo}""")
