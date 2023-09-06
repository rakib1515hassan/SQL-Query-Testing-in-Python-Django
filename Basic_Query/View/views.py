from django.shortcuts import render
from Basic_Query.models import Student, Teacher
from django.db import connection
from django.http import HttpResponse
from django.db.models import Q

# Combine the conditions using reduce and the selected operator
from functools import reduce

def ORM_values(request):

    ## ORM Query
    # students_data = Student.objects.values('id', 'name', 'city', 'roll')


    # Define the variables for columns you want to select dynamically
    selected_columns = ['id', 'name', 'city', 'roll'] # NOTE id (primary key) must be দেয়া লাগবে

    # Construct the SQL query dynamically based on the selected columns
    column_list = ', '.join(selected_columns)

    sql_query = f"SELECT {column_list} FROM basic_query_student" 

    students_data = Student.objects.raw(sql_query)


    """NOTE This return tuple
    # Define the variables for columns you want to select
    selected_columns = ['id', 'name', 'city']

    # Construct the SQL query dynamically based on the selected columns
    column_list = ', '.join(selected_columns)
    sql_query = f"SELECT {column_list} FROM basic_query_student"  # Replace 'yourapp_student' with your actual table name

    # Execute the SQL query
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        students_data = cursor.fetchall()  # Fetch all rows from the result
    """

    ## NOTE Print
    # Iterate through the RawQuerySet and print each student's name
    # print("------------------")
    # for student in students_data:
    #     print("Student Name:", student.name)
    # print("------------------")

    # print("------------------")
    # print("Student Name:", students_data)
    # print("------------------")

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': "সম্পূর্ন Table হতে name, roll and city column দেখাবে।",
        }    
    return render(request, 'Result/result_2.html', data)








def ORM_values_distinct(request):

    ## ORM Query
    # students_data = Student.objects.values('city').distinct()

    # Define the variables for columns you want to select dynamically
    selected_columns = ['id','city']            # NOTE id (primary key) must be দেয়া লাগবে
    column_list = ', '.join(selected_columns)
    sql_query = f"SELECT DISTINCT {column_list} FROM basic_query_student"

    stu_data = Student.objects.raw(sql_query)
    distinct_cities = set(student.city for student in stu_data)

    data = {
            # 'std_obj': students_data,
            'std_obj_distinct': distinct_cities,
            'SQL_querry': "SELECT DISTINCT city FROM basic_query_student",
            'descripetion': "সম্পূর্ন Table হতে city column দেখাবে। কিন্তু কোন Duplicate value দেখাবে না।",
        }    
    return render(request, 'Result/result_2.html', data)





def ORM_limit(request):
    start_point = ''
    end_point = ''
    if request.method == "POST":
        start_point = request.POST.get('start')  # The start point (inclusive)
        end_point   = request.POST.get('end')  # The end point (exclusive)

    ## ORM Query
    # students_data = Student.objects.all()[ start_point : end_point ]  ## [Start : End: Increment]

    sql_query = f"SELECT * FROM basic_query_student LIMIT {start_point}, {end_point}"
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table হতে কেবল মাত্র {start_point} হতে {end_point} এর আগ পর্যন্ত Data দেখাবে।",
        }    
    return render(request, 'Result/result_1.html', data)




def ORM_order_by(request):
    order_attribute = 'roll'

    ## ORM Query
    # students_data = Student.objects.all().order_by(order_attribute)

    sql_query = f"SELECT * FROM basic_query_student ORDER BY {order_attribute} ASC"   # ASC না দিলেও, Ascending order defult থাকে।
                                                                                      # DESC দিলে Decending order এ sort হবে।
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': "সম্পূর্ন Table কে Roll এর ওপর ভিতি করে Ascending order এ দেখাবে। তবে ASC এর যায়গায় DESC দিলে Decending order এ sort হবে।",
        }    
    return render(request, 'Result/result_1.html', data)





"""
WHERE clause এর সাহায্যে একটি নির্দিষ্ট  শর্ত / condition এর উপর ভিতি করে ডাটা খুজেতে ব্যাবহার কারা হয়।

SELECT column_list
FROM table_name
WHERE condition;

"""




def ORM_filter(request):
    gen = ''
    if request.method == "POST":
        gen = request.POST.get('gender')

    ## ORM Query
    # students_data = Student.objects.filter(gender = gen)


    sql_query = f"SELECT * FROM basic_query_student WHERE gender = '{gen}' " 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে কেবল মাত্র gender = {gen} কে আলদাকরে দেখানো হয়েছে।",
        }    
    return render(request, 'Result/result_1.html', data)
    # return HttpResponse()



def ORM_filter_gt_lt(request):
    age = '10'
    lookups = ''
    if request.method == "POST":
        age = request.POST.get('age')
        if request.POST.get('lookups'):
            lookups = request.POST.get('lookups')

    condition = {}

    ## ORM Query
    # if age and lookups:
    #     if lookups == 'gt':
    #         condition['age__gt'] = age
    #     elif lookups == 'gte':
    #         condition['age__gte'] = age
    #     elif lookups == 'lt':
    #         condition['age__lt'] = age
    #     elif lookups == 'lte':
    #         condition['age__lte'] = age
    # else:
    #     condition['age__lte'] = age
    
    # students_data = Student.objects.filter(**condition) ## filter( age__lte = 10 )


    ## SQL Query
    if age and lookups:
        if lookups == 'gt':
            condition = ">"
        elif lookups == 'gte':
            condition = '>='
        elif lookups == 'lt':
            condition = '<'
        elif lookups == 'lte':
            condition = '<='
    else:
        condition = '>'

    sql_query = f"SELECT * FROM basic_query_student WHERE age {condition} {age} " 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা age {condition} {age} condition টি কে মানে, সে সকল Data গুলোকে এখানে দেখানো হয়েছে।",
        }    
    return render(request, 'Result/result_1.html', data)






def ORM_filter_and_or(request):
    _from = ''
    _to   = ''
    _operator = '&'

    if request.method == "POST":
        _from = request.POST.get('from')
        _to   = request.POST.get('to') 
        if request.POST.get('operator'):
            _operator = request.POST.get('operator') 

    result = ''

    ## NOTE For ORM
    # if _operator == '&':
    #     result = (Q(age__gte =_from) & Q(age__lte =_to))
    #     txt = 'এর মধ্যে'
    # elif _operator == '|':
    #     result = (Q(age__gte =_from) | Q(age__lte =_to))
    #     txt = 'এর মধ্যে কিংবা এর বাহিরে। বাহিরের গুলোকেও দেখাবে কারন এখানে or ব্যবহার করা হয়েছে।'

    # students_data = Student.objects.filter(result)

    ## NOTE For SQL
    if _operator == '&':
        operator = 'AND'
        txt = 'এর মধ্যে'
    elif _operator == '|':
        operator = 'OR'
        txt = 'এর মধ্যে কিংবা এর বাহিরে। বাহিরের গুলোকেও দেখাবে কারন এখানে or ব্যবহার করা হয়েছে।'

    sql_query = f"SELECT * FROM basic_query_student WHERE age >= {_from} {operator} age <= {_to}" 

    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা শুধু সে সকল Record কে দেখানো হয়েছে যাদের Age {_from} থেকে {_to} {txt}।",
        }    
    return render(request, 'Result/result_1.html', data)






def ORM_filter_between(request):
    _from = ''
    _to   = ''

    if request.method == "POST":
        _from = request.POST.get('from')
        _to   = request.POST.get('to')  

    ## NOTE For ORM
    # students_data = Student.objects.filter(age__range=(_from, _to))

    ## NOTE For SQL
    sql_query = f"SELECT * FROM basic_query_student WHERE age BETWEEN {_from} AND {_to}" 

    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা শুধু সে সকল Record কে দেখানো হয়েছে যাদের Age {_from} থেকে {_to} এর মধ্যে।",
        }    
    return render(request, 'Result/result_1.html', data)





def ORM_filter_not(request):
    _class  = 'x'
    _gender = 'Male'

    if request.method == "POST":
        if request.POST.get('class'):
            _class = request.POST.get('class')
        if request.POST.get('gender'):
            _gender   = request.POST.get('gender')


    ## NOTE For ORM
    # students_data = Student.objects.filter(
    #     Q(s_class=_class) & (~Q(gender=_gender))
    #     )

    ## NOTE For SQL
    sql_query = f"SELECT * FROM basic_query_student WHERE s_class = '{_class}' AND NOT gender = '{_gender}' " 

    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে জাদের Class = {_class} এবং যাদের Gender = {_gender} না সে সকল Record গুলো দেখানো হয়েছে।",
        }    
    return render(request, 'Result/result_1.html', data)



"""
SQL এর Logical Operator গুলো হল AND, OR, IN, NOT and LIKE

SELECT column_list
FROM table_name
WHERE condition;

"""





def ORM_filter_and_or_2(request):
    _city   = 'Dhaka'
    _gender = 'Female'
    _age    = 12

    ## NOTE For ORM
    # students_data = Student.objects.filter(
    #                 Q(city =_city)
    #                        &
    #     (Q(gender=_gender) | Q(age__gte = _age))
    # )

    ## NOTE For SQL
    sql_query = f"SELECT * FROM basic_query_student WHERE city = '{_city}' AND ( (gender = '{_gender}') OR (age >= {_age}) ) " 

    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের City = {_city} এবং Gender = {_gender} অথবা Age {_age} এর বেশি তাদের Record গুলো দেখাবে।",
        }    
    return render(request, 'Result/result_1.html', data)





def ORM_filter_in(request):
    _city   = ['Noakhali', 'Chandpur']

    ## NOTE For ORM
    # ORM Query using the 'in' lookup
    # students_data = Student.objects.filter(city__in=_city)

    ## NOTE For SQL
    # Enclose each city name in single quotes
    city_list = [f"'{city}'" for city in _city]  # return = ["'Dhaka'", "'Noakhali'", "'Chandpur'"]
    column_list = ', '.join(city_list)           # return = 'Dhaka', 'Noakhali', 'Chandpur'

    sql_query = f"SELECT * FROM basic_query_student WHERE city IN ({column_list}) " 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের City {_city}, সে সকল Record গুলোকে দেখাবে।",
        }    
    return render(request, 'Result/result_1.html', data)





def ORM_filter_iexact(request):
    _name   = 'rijon'

    ## NOTE For ORM
    # students_data = Student.objects.filter(name__iexact = _name)

    ## NOTE For SQL
    sql_query = 'SELECT * FROM basic_query_student WHERE name LIKE %s'
    students_data = Student.objects.raw(sql_query, [_name + '%'])
    

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যার নাম {_name}, তার সকল Record দেখাবে, তবে এটি case insensitive এই SQL Query ব্যেবহার করে start with ও বের কারা যায়।",
        }    
    return render(request, 'Result/result_1.html', data)




def ORM_filter_contains(request):
    _name   = 'Ra'

    ## NOTE For ORM
    # students_data = Student.objects.filter(name__contains = _name)

    ## NOTE For SQL
    sql_query = f"SELECT * FROM basic_query_student WHERE name LIKE %s "
    students_data = Student.objects.raw(sql_query, ['%' + _name + '%'])



    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যার নাম এর মাঝে {_name} এটিকে পাবে, তার সকল Record দেখাবে, তবে এটি case insensitive",
        }    
    return render(request, 'Result/result_1.html', data)




def ORM_filter_icontains(request):
    _name   = 'ki'

    ## NOTE For ORM
    # students_data = Student.objects.filter(name__icontains = _name)

    ## NOTE For SQL
    sql_query = f"SELECT * FROM basic_query_student WHERE name LIKE %s "
    students_data = Student.objects.raw(sql_query, ['%' + _name + '%'])



    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যার নাম এর মাঝে {_name} এটিকে পাবে, তার সকল Record দেখাবে, তবে এটি case insensitive",
        }    
    return render(request, 'Result/result_1.html', data)




"""
SQL এর Constraint Auto Increment গুলো হল NOT NULL, UNIQUE, PRIMARY KEY = NOT NULL + UNIQUE, CHECK, DEFAULT
"""






def ORM_(request):

    ## NOTE For ORM
    students_data = students_data = Student.objects.filter() ## filter( age__lte = 10 )


    ## NOTE For SQL
    # sql_query = f"SELECT {column_list} FROM basic_query_student" 

    # students_data = Student.objects.raw(sql_query)




    ## NOTE Print
    # Iterate through the RawQuerySet and print each student's name
    # print("------------------")
    # for student in students_data:
    #     print("Student Name:", student.name)
    # print("------------------")

    print("------------------")
    print("Student Name:", students_data)
    print("------------------")

    # return render(request, 'abc.html')
    return HttpResponse()