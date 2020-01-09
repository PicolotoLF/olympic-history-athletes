from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'athletes', views.AthleteList)
router.register(r'attributes', views.AttributesList)

urlpatterns = [
    path('', include(router.urls)),
]