from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
from oidc_auth.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView


class MyApiView(APIView):

    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        user = request.user
        if type(user) == User:
            return JsonResponse({'status': 'ok'})
        else :
            return JsonResponse({'status' : 'authentication failed'}, status=401)