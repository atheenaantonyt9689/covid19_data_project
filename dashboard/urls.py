from django.urls import path
from .views import HomePageView
urlpatterns = [
path('', HomePageView.as_view(), name='case'),
#path('chart',ChartView.as_view(), name='chart'),
]