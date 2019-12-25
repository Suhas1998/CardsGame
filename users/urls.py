from django.urls import path
from . import views as user_views
from .views import SignUpView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', user_views.profile , name='profile'),
    path('portfolio', TemplateView.as_view(template_name='portfolio.html'), name = 'portfolio')
]
