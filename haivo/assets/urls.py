from django.urls import path
from . import views

urlpatterns = [
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/lend/<int:asset_id>/', views.lend_asset, name='lend'),
    path('assets/return/<int:asset_id>/', views.return_asset, name='return_asset'),
]
