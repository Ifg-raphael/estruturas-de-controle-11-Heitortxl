# Sua solução aqui
a = int(input())
b = int(input())
c = int(input())


if a >= b + c or b >= a + c or c >= a + b:
    print("Não forma triângulo")

elif a != b and a != c and b != c:
    print("Escaleno")

elif a == b and a == c:
    print("Equilátero")

else:
    print("Isósceles")

