from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class MyApiView(APIView):

    def get(self, request):
        return HttpResponse({'status': 'ok'})
