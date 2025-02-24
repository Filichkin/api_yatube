from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter


v1_router = SimpleRouter()


urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
]
