print("Bem vindo ao jogo do meu PC!")

playing = input("Você tem ctz que quer jogar ?? ")

if playing.lower() != "sim":
    quit()

print("Okay! Vamos jogar...")
score = 0

answer = input("Qual meu nome ? ")
if answer.lower() == "resp":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Qual meu nome ? ")
if answer.lower() == "resp":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Qual meu nome ? ")
if answer.lower() == "resp":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Qual meu nome ? ")
if answer.lower() == "resp":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Você fez " + str(score) + " questões corretas!")
print("Você fez " + str((score / 4) * 100) + "%.")