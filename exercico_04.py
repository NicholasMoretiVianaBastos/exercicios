def somar_numeros(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

numeros_aleatorios = [15, 26, 33, 49, 56]
resultado = somar_numeros(numeros_aleatorios)
media = resultado / 5

print(f"Sua media é {media}")
