def task_1_variant_5():
    negatives = []
    zeros = []
    positives = []

    print("Введите целые числа (нажмите Enter, чтобы завершить):")

    while True:
        user_input = input("> ")
        # Если строка пустая - выходим из цикла
        if user_input == "":
            break

        try:
            num = int(user_input)
            if num < 0:
                negatives.append(num)
            elif num == 0:
                zeros.append(num)
            else:
                positives.append(num)
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

    print("\nРезультат:")
    # Выводим каждое число с новой строки
    for n in negatives + zeros + positives:
        print(n)


task_1_variant_5()