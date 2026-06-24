from django.urls import path
from .views import CompanyApiView, BinoApiView

urlpatterns = [
    path('companys/', CompanyApiView.as_view()),
    path('companys/<int:pk>/', CompanyApiView.as_view()),

    path('binos/', BinoApiView.as_view()),
    path('binos/<int:pk>/', BinoApiView.as_view()),

]