from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from . import views

v1_router = SimpleRouter()
v1_router.register(r'posts', views.PostViewSet)
v1_router.register(r'groups', views.GroupViewSet)
v1_router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]
