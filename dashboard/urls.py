from django.urls import path
from .views import ActiveCasesViews,DistrictViews,SearchView,DateFilterView #,HomePageView,

urlpatterns = [
path('',DateFilterView.as_view(),name=''),
#('filter', HomePageView.as_view(), name='case'),
path('top/active',ActiveCasesViews.as_view(),),
path('state_dashboard',DistrictViews.as_view(),name='state'),
path('search',SearchView.as_view(),name='search'),

]