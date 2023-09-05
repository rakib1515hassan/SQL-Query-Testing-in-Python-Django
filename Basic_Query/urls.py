from django.urls import path
from Basic_Query.View import create, views

urlpatterns = [
    ## create.py
    path('', create.home, name='home'),
    path('query1/', create.Query_1, name='Query_1'),
    path('Result/', create.Result, name='Result'),

    path('add-student/', create.add_student, name='add_student'),



    ## views.py
    path('orm-values/', views.ORM_values, name='ORM_values'),
    path('orm-values-distinct/', views.ORM_values_distinct, name='ORM_values_distinct'),
    path('orm-limit/', views.ORM_limit, name='ORM_limit'),
    path('orm-order_by/', views.ORM_order_by, name='ORM_order_by'),
]

