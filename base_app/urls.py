from django.urls import path
from .views import HomeView, UnterschreibnView

app_name = 'base_app'

urlpatterns = [

    path('', HomeView.as_view(), name='home_page'),
    path('unterschreiben/', UnterschreibnView.as_view(), name='unterschreiben_page'),

]
