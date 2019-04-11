from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MenuView, SectionView

urlpatterns = [
    path('', MenuView.as_view(), name="all"),
    path('add/', MenuView.as_view(), name="add"),
    path('<int:pk>/', SectionView.as_view(), name="single"),
    path('<int:pk>/edit/', SectionView.as_view(), name="edit"),
    path('<int:pk>/delete/', SectionView.as_view(), name="delete"),
]
