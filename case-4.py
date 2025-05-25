import random

def guessthenumber():
    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 10  # Ограничиваем количество попыток

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. У тебя есть 10 попыток, чтобы его угадать!")

    for attempt in range(attempts):
        try:
            guess = int(input(f"Попытка {attempt + 1}: Введи твое предположение: "))

            if guess < 1 or guess > 100:
                print("Пожалуйста, введи число от 1 до 100.")
                continue

            if guess < secret_number:
                print("Слишком маленькое число!")
            elif guess > secret_number:
                print("Слишком большое число!")
            else:
                print(f"Поздравляю! Ты угадал число {secret_number} за {attempt + 1} попыток!")
                break
        except ValueError:
            print("Ошибка: Пожалуйста, введи корректное целое число.")

    else:
        print(f"Увы, ты не угадал число. Оно было {secret_number}.")

if name == "main":
    guessthenumber()