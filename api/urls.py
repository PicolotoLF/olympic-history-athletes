from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'athletes', views.AthleteView)
router.register(r'attributes', views.AttributesView)
router.register(r'games', views.GamesView)
router.register(r'team', views.TeamView)
router.register(r'season', views.SeasonView)
router.register(r'city', views.CityView)
router.register(r'sport', views.SportView)
router.register(r'event', views.EventView)
router.register(r'medals', views.MedalView)

urlpatterns = [
    path('', include(router.urls)),
    path('athletes_search/', views.AthleteFilter.as_view()),
]