t = int(input())
for i in range(t):
    linha = [int(x) for x in input().split(";")]
    soma = sum(linha)
    print(soma, end="" if i == t-1 else "\n")