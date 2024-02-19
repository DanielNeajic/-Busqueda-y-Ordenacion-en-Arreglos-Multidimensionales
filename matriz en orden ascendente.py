def ordenar_fila(matriz, numero_fila):
    matriz[numero_fila] = sorted(matriz[numero_fila])

# Ejemplo de uso
mi_matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

numero_fila_a_ordenar = 1
print("Matriz original:")
for fila in mi_matriz:
    print(fila)

ordenar_fila(mi_matriz, numero_fila_a_ordenar)

print(f"\nMatriz con la fila {numero_fila_a_ordenar} ordenada:")
for fila in mi_matriz:
    print(fila)