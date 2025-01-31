from django.urls import path


from . import views


urlpatterns = [
    path('<int:pk>/',views.pdv),
    path('', views.plcv),
    path('<int:pk>/update/',views.puv),
    path('<int:pk>/delete/',views.pdev),
]
