
s = 0
contador = int(input("Numero de sumas: "))
while contador > 0:
    numero = int(input("Numero a sumar: "))
    s = s + numero
    contador -= 1 #* esto es igual a decir contador = contador + 1
    print(f"Resultado: {s}")
    print(f"Iteraciones restantes: {contador}")   
