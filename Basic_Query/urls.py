from django.urls import path
from Basic_Query.View import create, views

urlpatterns = [
    ## create.py
    path('', create.home, name='home'),
    path('query1/', create.Query_1, name='Query_1'),
    path('Result/', create.Result, name='Result'),

    path('add-student/', create.add_student, name='add_student'),
    path('all-student/', create.all_student, name='all_student'),



    ## views.py
    path('orm-values/', views.ORM_values, name='ORM_values'),
    path('orm-values-distinct/', views.ORM_values_distinct, name='ORM_values_distinct'),
    path('orm-limit/', views.ORM_limit, name='ORM_limit'),
    path('orm-order_by/', views.ORM_order_by, name='ORM_order_by'),
    path('orm-filter/', views.ORM_filter, name='ORM_filter'),
    path('orm-filter-gt-ls/', views.ORM_filter_gt_lt, name='ORM_filter_gt_lt'),
    path('orm-filter-and-or/', views.ORM_filter_and_or, name='ORM_filter_and_or'),
    path('orm-filter-between/', views.ORM_filter_between, name='ORM_filter_between'),
    path('orm-filter-not/', views.ORM_filter_not, name='ORM_filter_not'),
    path('orm-filter-and-or_2/', views.ORM_filter_and_or_2, name='ORM_filter_and_or_2'),
    path('orm-filter-in/', views.ORM_filter_in, name='ORM_filter_in'),
    path('orm-filter-iexact/', views.ORM_filter_iexact, name='ORM_filter_iexact'),
    path('orm-filter-contains/', views.ORM_filter_contains, name='ORM_filter_contains'),
    path('orm-filter-icontains/', views.ORM_filter_icontains, name='ORM_filter_icontains'),
]


