from django.urls import include, path
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('ingredient/', IngredientListCreateAPIView.as_view(), name='ingredient-list'),
    path('ingredient/<int:pk>/', IngredientDetailAPIView.as_view(), name='ingredient-detail'),
    path('storage/', StorageListCreateAPIView.as_view(), name='storage-list'),
    path('storage/<int:pk>/', StorageDetailAPIView.as_view(), name='storage-detail'),
    path('partner/', PartnerListCreateAPIView.as_view(), name='partner-list'),
    path('partner/<int:pk>/', PartnerDetailAPIView.as_view(), name='partner-detail'),
    path('acceptance/', AcceptanceListCreateAPIView.as_view(), name='acceptance-list'),
    path('acceptance/<int:pk>/', AcceptanceDetailAPIView.as_view(), name='acceptance-detail')
]

urlpatterns += router.urls