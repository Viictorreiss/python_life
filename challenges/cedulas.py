num = int(input())

print(f'{num//100} nota(s) de R$ 100',)
num = num%100
print(f'{num//50} nota(s) de R$ 50')
num = num%50
print(f'{num//20} nota(s) de R$ 20')
num = num%20
print(f'{num//10} nota(s) de R$ 10')
num = num%10
print(f'{num//5} nota(s) de R$ 5')
num = num%5
print(f'{num//2} nota(s) de R$ 2')
num = num%2
print(f'{num//1} nota(s) de R$ 1', end="")