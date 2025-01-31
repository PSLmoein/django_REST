from django.urls import path


from . import views


urlpatterns = [
    path('<int:pk>/',views.pmv),
    path('', views.pmv),
    path('<int:pk>/update',views.puv),
    path('<int:pk>/delete',views.pdev),
]
