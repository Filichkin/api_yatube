from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from . import views


API_VERSION = 'v1'

v1_router = SimpleRouter()

v1_router.register('posts', views.PostViewSet)
v1_router.register('groups', views.GroupViewSet)
v1_router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path(f'{API_VERSION}/api-token-auth/', obtain_auth_token),
    path(f'{API_VERSION}/', include(v1_router.urls)),
]
