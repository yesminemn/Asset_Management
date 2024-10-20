from django.urls import path
from . import views

urlpatterns = [
    path('assets/select-employee/', views.select_employee, name='select_employee'),
    path('assets/select-asset/<int:employee_id>/', views.choose_asset, name='choose_asset'),
    path('assets/return/<int:asset_id>/', views.return_asset, name='return_asset'),
]
