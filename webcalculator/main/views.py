from django.shortcuts import render
from rest_framework.views import APIView
from . import operation
from rest_framework.response import Response


class Convert(APIView):
    def get(self, request, number, start_system, end_system):
        try:
            answer = operation.convert(start_system, number, end_system)
            if answer == 'error':
                return Response({'answer': answer, 'message': 'You choose invalid number system'})
            else:
                return Response({'answer': answer, 'message': 'Success'})
        except:
            return Response({'answer': 'error', 'message': 'An unknown error has occurred'})


def main_page(request):
    try:
        number = request.GET.get('number')
        start_system = int(request.GET.get('system1'))
        end_system = int(request.GET.get('system2'))
        if number and start_system and end_system:
            answer = operation.convert(start_system, number, end_system)
            return render(request, 'main/main_page.html', {'answer': answer, 'error': None})
        else:
            return render(request, 'main/main_page.html', {'answer': None, 'error': None})
    except:
        return render(request, 'main/main_page.html', {'answer': None, 'error': None})
