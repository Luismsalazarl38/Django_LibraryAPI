from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import AdminView, ClientView, LoginView, LogoutView, RootView


router = routers.DefaultRouter()
router.register(r'admins', AdminView, basename='admins')
router.register(r'clients', ClientView, basename='clients')
router.register(r'roots', RootView, basename='root')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Documentación de mi API')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
