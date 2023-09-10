from django.urls import path
from Basic_Query.View import create, views

urlpatterns = [
    ## create.py
    path('', create.home, name='home'),
    path('query1/', create.Query_1, name='Query_1'),
    path('Result/', create.Result, name='Result'),

    path('add-student/', create.add_student, name='add_student'),
    path('all-student/', create.all_student, name='all_student'),
    path('add-teacher/', create.add_teacher, name='add_teacher'),
    path('all-teacher/', create.all_teacher, name='all_teacher'),





    ## views.py
    path('orm-values/', views.ORM_values, name='ORM_values'),
    path('orm-values-distinct/', views.ORM_values_distinct, name='ORM_values_distinct'),
    path('orm-limit/', views.ORM_limit, name='ORM_limit'),
    path('orm-order_by/', views.ORM_order_by, name='ORM_order_by'),
    path('orm-filter/', views.ORM_filter, name='ORM_filter'),
    path('orm-filter-gt-ls/', views.ORM_filter_gt_lt, name='ORM_filter_gt_lt'),
    path('orm-filter-and-or/', views.ORM_filter_and_or, name='ORM_filter_and_or'),
    path('orm-filter-between/', views.ORM_filter_between, name='ORM_filter_between'),
    path('orm-filter-range-date/', views.ORM_filter_range_date, name='ORM_filter_range_date'),
    path('orm-filter-not/', views.ORM_filter_not, name='ORM_filter_not'),
    path('orm-filter-and-or_2/', views.ORM_filter_and_or_2, name='ORM_filter_and_or_2'),
    path('orm-filter-in/', views.ORM_filter_in, name='ORM_filter_in'),
    path('orm-filter-iexact/', views.ORM_filter_iexact, name='ORM_filter_iexact'),
    path('orm-filter-contains/', views.ORM_filter_contains, name='ORM_filter_contains'),
    path('orm-filter-icontains/', views.ORM_filter_icontains, name='ORM_filter_icontains'),
    path('orm-filter-joining_year/', views.ORM_filter_joining_year, name='ORM_filter_joining_year'),
    path('orm-filter-joining_year-from-to/', views.ORM_filter_joining_from_to, name='ORM_filter_joining_from_to'),
    path('orm-filter-joining_month/', views.ORM_filter_joining__month__gte, name='ORM_filter_joining__month__gte'),
    path('orm-filter-joining_year_month_day/', views.ORM_filter_joining__year_month_day, name='ORM_filter_joining__year_month_day'),
    path('orm-filter-joining_week/', views.ORM_filter_joining_date_week, name='ORM_filter_joining_date_week'),
]


