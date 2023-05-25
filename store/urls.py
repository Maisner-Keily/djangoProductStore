from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('buyDelivery', view=views.buyDelivery, name='buyDelivery'),
    path('surfaces', view=views.surface, name='surface'),
    path('product/<int:id>', view=views.product, name='product'),
    path('createComment', view=views.add_comment, name='createComment'),
]
