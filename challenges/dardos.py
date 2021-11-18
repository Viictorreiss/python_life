coordenadas = input().split()
x = int(coordenadas[0])
y = int(coordenadas[1])

if x == 0 and y == 0:
    print("NO ALVO!", end="")
elif x > 0 and y > 0:
    print("R1", end="")
elif x > 0 and y < 0:
    print("R4", end="")
elif x < 0 and y < 0:
    print("R3", end="")
else:
    print("R2", end="")