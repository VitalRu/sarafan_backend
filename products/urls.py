from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductMixinView.as_view()),
    path('<int:pk>/', views.ProductMixinView.as_view())
]
