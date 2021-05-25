from django.urls import path
from .views import HomePageView,ActiveCasesViews,DistrictViews,SearchView

urlpatterns = [
path('', HomePageView.as_view(), name='case'),
path('top/active',ActiveCasesViews.as_view(),),
path('state_dashboard',DistrictViews.as_view(),name='state'),
path('search',SearchView.as_view(),name='search'),
]