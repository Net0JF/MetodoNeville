def neville_interpolation(x, y, target):
    n = len(x)
    Q = [[0] * n for _ in range(n)]

    for i in range(n):
        Q[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i][j] = ((target - x[i - j]) * Q[i][j - 1] - (target - x[i]) * Q[i - 1][j - 1]) / (x[i] - x[i - j])

    return Q[n - 1][n - 1]

if __name__ == "__main__":
    # Solicita los valores de x e y al usuario
    n = int(input("Ingresa el número de puntos de datos: "))
    x = []
    y = []
    for i in range(n):
        x_val = float(input(f"Ingrese el valor de x{i}: "))
        y_val = float(input(f"Ingrese el valor de y{i}: "))
        x.append(x_val)
        y.append(y_val)

    target_value = float(input("Ingrese el valor de x para la interpolación: "))

    # Calcula el polinomio interpolante
    interpolated_value = neville_interpolation(x, y, target_value)

    print(f"El valor interpolado en x = {target_value} es: {interpolated_value:.4f}")
