from django.urls import path
from .views import main_page, add_product_view, order_view

urlpatterns = [
    path('', main_page, name='home'),
    path('add_product/', add_product_view, name='add'),
    path('order/<int:id>/', order_view, name='order')
]