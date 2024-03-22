print("Добро пожаловать в мою викторину!")

playing = input("Хочешь поиграть? ")

if playing.lower() != "да":
    quit()

print("Хорошо! Погнали :)")
score = 0

answer = input("Что такое гитара? ")
if answer.lower() == "музыкальный инструмент":
    print('Правильно!')
    score += 1
else:
    print("Неверно!")

answer = input("Как по англиски будет крокодил? ")
if answer.lower() == "crocodile":
    print('Правильно!')
    score += 1
else:
    print("Неверно!")

answer = input("Сколько будет 9*9+65/5? ")
if answer.lower() == "94":
    print('Правильно!')
    score += 1
else:
    print("Неверно!")

answer = input("Что пьёт корова? ")
if answer.lower() == "воду":
    print('Правильно!')
    score += 1
else:
    print("Неверно!")

answer = input("Как называют гриб, который находится под берёзой? ")
if answer.lower() == "подберёзовик":
    print('Правильно!')
    score += 1
else:
    print("Неверно")

answer = input("Кто такой енот? ")
if answer.lower() == "животное":
    print('Правильно!')
    score += 1
else:
    print("Неверно")

print("У вас " + str(score) + " правильных вопроса!")
print("Пройдено на " + str((score / 6) * 100) + "%.")