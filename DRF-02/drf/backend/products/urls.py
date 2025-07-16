# drf/backend/products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Mixin
    # path('', views.product_mixin_view),
    # path('<int:pk>/', views.product_mixin_view),
    
    # List Create
    path('', views.product_list_create_view),
    path('<int:pk>', views.product_list_create_view),
    
    # Update
    path('', views.product_update_view),
    path('<int:pk>/update/', views.product_update_view),
    
    # Delete
    path('', views.product_delete_view),
    path('<int:pk>/delete/', views.product_delete_view),
    
    # Detail
    path("", views.product_detail_view),
    path('<int:pk>', views.product_detail_view),
        
    # path('', views.product_create_view),
    # path('', views.product_alt_view),
    # path("<int:pk>/", views.product_alt_view),
    # path("<int:pk>/", views.ProductDetailAPIView.as_view()),
]
