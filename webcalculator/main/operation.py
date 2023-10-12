# делим число на отдельные элементы массива
def divide_number(number) -> list:
    letter_to_number = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    arr = []
    for item in str(number):
        if item in 'ABCDEF':
           arr.append(letter_to_number[item])
        else:
            arr.append(int(item))

    return arr


# если есть числа больше 10, то заменяем их на буквы
def translate_to_letters(number):
    letter_to_number = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for item in range(len(number)):
        if number[item] > 9:
            number[item] = letter_to_number[number[item]]
    return number


# конвертирует number из start_system в 10
def convert_to_10(start_system: int, number) -> int:
    number = divide_number(number)[::-1]
    answer = 0
    i = 0
    while len(number) > i:
        answer += number[i] * (start_system**i)
        i += 1

    return answer


# переводит число из 10 в систему system
def convert_to_x(system: int, number):
    answer = []
    number = int(number)
    while number >= system:
        answer.append(number % system)
        number = number // system

    answer.append(number)
    answer = translate_to_letters(answer[::-1])
    return answer


# берёт число и систему счисления и проверяет число на валидность
def is_valid(number, system) -> bool:
    letter_to_number = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for item in number:
        if item in '1234567890':
            if int(item) >= system:
                return False
        # если число записывается в виде буквы, то проверяем есть ли оно в этой системе счисления
        elif item in letter_to_number.keys():
            if letter_to_number[item] >= system:
                return False
        # если числа (буквы) нет в словаре, то возвращаем error
        elif item not in letter_to_number.keys():
            return False
    return True


# переводит число в end_system систему
def convertation(start_system: int, number, end_system: int):
    try:
        number = str(number).upper()

        if start_system != end_system:
            if start_system != 10:
                # переводим число в 10 систему
                number = convert_to_10(start_system, number)

            return ''.join(list(map(str, convert_to_x(end_system, number))))

        else:
            return number
    except:
        return 'error'


# подготовка чисел к операции + проведение её (возвращает результат в 10 системе)
def calculate(number1, system1: int, number2, system2: int, operation: str):
    if operation != '+' and operation != '/' and operation != '*' and operation != '-' and operation != '**':
        return 'unknown operation'

    if system1 != 10:
        number1 = convert_to_10(system1, number1)
    if system2 != 10:
        number2 = convert_to_10(system2, number2)

    if operation == '/' and number2 == 0:
        return 'error'
    answer = eval(f'{number1} {operation} {number2}')
    if type(answer) == float:
        answer = round(answer, 2)
    return answer

