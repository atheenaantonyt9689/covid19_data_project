from django.urls import path
from .views import HomePageView,ActiveCasesViews
urlpatterns = [
path('', HomePageView.as_view(), name='case'),
path('top',ActiveCasesViews.as_view(), name='chart'),
]