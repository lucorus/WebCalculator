from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.views import APIView
from . import operation
from .serializers import SuccessSerializer


class Convert(APIView):
    def get(self, request, number, start_system, end_system):
        return Response(operation.convert(start_system, number, end_system))


def main_page(request):
    try:
        number = int(request.GET.get('number'))
        start_system = int(request.GET.get('system1'))
        end_system = int(request.GET.get('system2'))
        if number:
            print(operation.convert(start_system, number, end_system))
            return render(request, 'main/main_page.html', {'answer': operation.convert(start_system, number, end_system)})
        else:
            return render(request, 'main/main_page.html', {'answer': '-'})
    except:
        return render(request, 'main/main_page.html', {'answer': '-'})
