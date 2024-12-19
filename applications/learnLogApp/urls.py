from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'create-log', views.CreateLog, basename='create_log')


urlpatterns = [
    path('', views.CreateLog.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'patch': 'partial_update'}), name='create_log'),
    # path('', include(router.urls)),
]
