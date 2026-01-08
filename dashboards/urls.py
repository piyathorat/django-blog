from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories, name="categories"),
    path('categories/add/',views.add_category,name="add_category"),
    path('categories/edit_category/<int:pk>',views.edit_category,name="edit_category"),
     path('categories/delete_category/<int:pk>',views.delete_category,name="delete_category"),
]