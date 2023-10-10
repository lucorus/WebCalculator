# делим число на отдельные элементы массива
def divide_number(number) -> list:
    arr = []
    for item in str(number):
        if item in 'ABCDEF':
            match item:
                case 'A':
                    arr.append(10)
                case 'B':
                    arr.append(11)
                case 'C':
                    arr.append(12)
                case 'D':
                    arr.append(13)
                case 'E':
                    arr.append(14)
                case 'F':
                    arr.append(15)
        else:
            arr.append(int(item))

    return arr


# конвертирует number из start_system в 10
def convert_to_10(start_system: int, number) -> int:
    number = divide_number(number)[::-1]
    answer = 0
    i = 0
    while len(number) > i:
        answer += number[i] * (start_system**i)
        i += 1

    return answer


# разворачиваем строку (если ревёрсить через срез, то 0 спереди пропадают)
def revers(number):
    answer = ''
    for item in range(len(number)-1, -1, -1):
        answer += number[item]
    return answer


# переводит число из 10 в систему system
def convert_to_x(system: int, number):
    answer = ''

    while number >= system:
        answer += str(number % system)
        number = number // system

    answer = (answer + str(number))
    # переворачиваем число
    return revers(answer)


# легко конвертирует число в какую-либо систему
def convert(start_system: int, number, end_system: int):
    if start_system != end_system:
        if start_system != 10:
            number = convert_to_10(start_system, number)

        return convert_to_x(end_system, number)
    else:
        return number


# подготовка чисел к операции, проведение её (возвращает результат в 10 системе)
def preparation_for_surgery(number1: int, system1: int, number2: int, system2: int, operation: str):
    if system1 != 10:
        number1 = convert_to_10(system1, number1)
    if system2 != 10:
        number2 = convert_to_10(system2, number2)

    if operation == '/' and number2 == 0:
        return 0
    answer = eval(f'{number1} {operation} {number2}')
    if type(answer) == float:
        answer = round(answer, 2)
    return answer

