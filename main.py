import random

guessTaken = 0
MyName = input('Как тебя зовут? ')

number = random.randint(1, 100)
print(f'{MyName}, я загадал число от 1 до 100, попробуй его угадать.')

for guessTaken in range(1, 7):
    guess = int(input('Введи число: '))

    if guess > number:
        print('Мое число меньше. ')
    elif guess < number:
        print('Мое число больше.')
    elif guess == number:
        break

if guess == number:
    guessTaken = guessTaken + 1
    print(f'{MyName}, ты справился за {guessTaken} попыток.')

if guess != number:
    print(f'{MyName}, ты не угадал! Я загадал число {number}')
