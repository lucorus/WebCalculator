from django.shortcuts import render
from rest_framework.views import APIView
from . import operation
from rest_framework.response import Response


# API, переводящее число в end_system счисления
class Convert(APIView):
    def get(self, request, number, start_system, end_system):
        try:
            answer = operation.convertation(start_system, number, end_system)
            if answer == 'error':
                return Response({'answer': answer, 'message': 'You choose invalid number system'})
            else:
                return Response({'answer': answer, 'message': 'Success'})
        except:
            return Response({'answer': 'error', 'message': 'An unknown error has occurred'})


# API, вычисляющее результат операции и возвращающее ответ в end_system системе
class Calculate(APIView):
    def get(self, request, first_number, first_number_start_system: int, second_number, second_number_start_system: int, oper: str, end_system: int=None):
        print(first_number, first_number_start_system, second_number, second_number_start_system, oper)
        try:
            answer = operation.calculate(first_number, first_number_start_system, second_number, second_number_start_system, oper)
            if answer == 'unknown operation':
                return Response({'answer': 'error', 'message': 'Unknown operation'})
            else:
                # если конечная система счисления не 10 или если она не указана, то переводим число в нужную систему
                if end_system != None and end_system != 10:
                    answer = operation.convertation(10, answer, end_system)

                if answer == 'error':
                    return Response({'answer': 'error', 'message': 'An unknown error has occurred'})

                return Response({'answer': answer, 'message': 'Success'})
        except:
            return Response({'answer': 'error', 'message': 'An unknown error has occurred'})


# переводит число в нужную систему счисления system2
def translate(request):
    try:
        number = request.GET.get('number')
        start_system = int(request.GET.get('system1'))
        end_system = int(request.GET.get('system2'))
        if number and start_system and end_system:
            answer = operation.convertation(start_system, number, end_system)
            return render(request, 'main/main_page.html', {'answer': answer, 'error': None})
        else:
            return render(request, 'main/main_page.html', {'answer': None, 'error': None})
    except:
        return render(request, 'main/main_page.html', {'answer': None, 'error': None})


# вычисляет результат операции между 2 числами и возвращает ответ в end_system
def calculator(request):
    try:
        first_number = request.GET.get('number1')
        first_number_start_system = int(request.GET.get('system1'))
        second_number = request.GET.get('number2')
        second_number_start_system = int(request.GET.get('system2'))
        oper = request.GET.get('operation')
        end_system = int(request.GET.get('end_system'))
        # проверяем наличие переменных
        if first_number and first_number_start_system and second_number and second_number_start_system and oper and end_system:
            answer = operation.calculate(first_number, first_number_start_system, second_number, second_number_start_system, oper)
            # если нужно вернуть ответ не в 10 системе, то переводим в end_system
            if end_system != 10:
                answer = operation.convertation(10, answer, end_system)

            if answer == 'error':
                return render(request, 'main/calculator.html', {'answer': 'error', 'error': None})

            return render(request, 'main/calculator.html', {'answer': answer, 'error': None})
        else:
            return render(request, 'main/calculator.html', {'answer': None, 'error': None})
    except:
        return render(request, 'main/calculator.html', {'answer': None, 'error': None})