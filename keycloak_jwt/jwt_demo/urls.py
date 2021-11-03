from django.urls import path
from .views import MyApiView

app_name = "jwt_demo"

urlpatterns = [
    path(
        "",
        MyApiView.as_view(),
        name="my_api",
    ),
]
