
from django.urls import path
from . import views
#from .views import india, australia, japan, country
from .views import HomeView, ChartData



# urlpatterns = [
#     path('', country.as_view(), name='country'),
#     path('india/', india.as_view(), name='india-view'),
#     path('australia/', australia.as_view(), name='australia-view'),
#     path('japan/', japan.as_view(), name='japan-view'),
# ]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('india/', ChartData.as_view(), name='api-view'),
    path('aus/', ChartData.as_view(), name='aus-view'),

]
