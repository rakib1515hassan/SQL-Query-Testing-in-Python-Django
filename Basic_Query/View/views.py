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
            'ORM_querry': "Student.objects.values('id', 'name', 'city', 'roll')",
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
            'ORM_querry': "Student.objects.values('city').distinct()",
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
            'ORM_querry': f"Student.objects.all()[ {start_point} : {end_point} ]",
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
            'ORM_querry': f"Student.objects.all().order_by({order_attribute})",
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
            'ORM_querry': f"Student.objects.filter(gender = {gen})",
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

    conditio = {}
    condition = {}

    ## ORM Query
    if age and lookups:
        if lookups == 'gt':
            conditio['age__gt'] = age
        elif lookups == 'gte':
            conditio['age__gte'] = age
        elif lookups == 'lt':
            conditio['age__lt'] = age
        elif lookups == 'lte':
            conditio['age__lte'] = age
    else:
        conditio['age__lte'] = age
    
    # students_data = Student.objects.filter(**conditio) ## filter( age__lte = 10 )


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
            'ORM_querry': f"Student.objects.filter({conditio})",
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
    if _operator == '&':
        result = (Q(age__gte =_from) & Q(age__lte =_to))
        # txt = 'এর মধ্যে'
    elif _operator == '|':
        result = (Q(age__gte =_from) | Q(age__lte =_to))
        # txt = 'এর মধ্যে কিংবা এর বাহিরে। বাহিরের গুলোকেও দেখাবে কারন এখানে or ব্যবহার করা হয়েছে।'

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
            'ORM_querry': f"Student.objects.filter(Q(age__gte ={_from}) {_operator} Q(age__lte ={_to}))",
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
            'ORM_querry': f"Student.objects.filter(age__range=({_from}, {_to})",
        }    
    return render(request, 'Result/result_1.html', data)




def ORM_filter_range_date(request):
    _from = '2000-01-01'
    _to   = '2023-12-30'

    ## NOTE For ORM
    # students_data = Student.objects.filter( date_of_birth__range = ( _from, _to ) )

    ## NOTE For SQL
    sql_query = f"SELECT * FROM basic_query_student WHERE date_of_birth BETWEEN '{_from}' AND '{_to}' "
    students_data = Student.objects.raw(sql_query)



    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা শুধু সে সকল Record কে দেখানো হয়েছে যাদের Birth date {_from} থেকে {_to} এর মধ্যে।",
            'ORM_querry': f"Student.objects.filter( date_of_birth__range = ( {_from}, {_to} ))",
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
            'ORM_querry': f"students_data = Student.objects.filter( Q(s_class={_class}) & (~Q(gender={_gender})) ))",
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
            'ORM_querry': f"""students_data = Student.objects.filter(
                                       Q(city ={_city})
                                              &
                            (Q(gender={_gender}) | Q(age__gte = {_age}))
                            )""",
        }    
    return render(request, 'Result/result_1.html', data)





def ORM_filter_in(request):
    _city   = ['Khulna', 'Chittagong']

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
            'ORM_querry': f"Student.objects.filter(city__in={_city})",
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
            'ORM_querry': f"Student.objects.filter(name__iexact = {_name})",
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
            'ORM_querry': f"Student.objects.filter(name__contains = {_name})",
        }    
    return render(request, 'Result/result_1.html', data)




def ORM_filter_icontains(request):
    _name   = 'ki'

    ## NOTE For ORM
    # students_data = Student.objects.filter(name__icontains = _name)

    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE name LIKE %s 
        """
    students_data = Student.objects.raw(sql_query, ['%' + _name + '%'])



    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যার নাম এর মাঝে {_name} এটিকে পাবে, তার সকল Record দেখাবে, তবে এটি case insensitive",
            'ORM_querry': f"Student.objects.filter(name__icontains = {_name})",
        }    
    return render(request, 'Result/result_1.html', data)




"""
SQL এর Constraint Auto Increment গুলো হল NOT NULL, UNIQUE, PRIMARY KEY = NOT NULL + UNIQUE, CHECK, DEFAULT
"""








def ORM_filter_joining_year(request):
    _year = 2022

    if request.method == "POST":
        _year = request.POST.get('year')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter(joiningDate__year = _year) # YYYY 

    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE YEAR(joiningDate) = {_year}
        """

    teacher_data = Student.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের Joing Date {_year}, তাদের Record গুলো দেখানো হয়েছে ।",
            'ORM_querry': f"Teacher.objects.filter(joiningDate__year = {_year}))",
        }    
    return render(request, 'Result/teacher.html', data)







def ORM_filter_joining_from_to(request):
    _from = 2010
    _to   = 2022

    if request.method == "POST":
        _from = request.POST.get('year-from')
        _to   = request.POST.get('year-to')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter(joiningDate__year__range = (_from, _to)) # YYYY 


    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE YEAR(joiningDate) BETWEEN {_from} AND {_to}
        """
    
    teacher_data = Student.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের Joing date {_from} থেকে {_to}, তাদের Record গুলোকে দেখাবে।",
            'ORM_querry': f"Teacher.objects.filter(joiningDate__year__range = ({_from}, {_to}))",
        }    
    return render(request, 'Result/teacher.html', data)






def ORM_filter_joining__month__gte(request):
    _month = 6

    if request.method == "POST":
        if int(request.POST.get('month')) >= 12 or int(request.POST.get('month')) <= 0:
            _month = 1
        else:
            _month = request.POST.get('month')


    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( joiningDate__month__gte = _month ) # MM


    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE MONTH(joiningDate) >= {_month}
        """

    teacher_data = Student.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের Joing Month {_month} এর সমান কিংবা বেশি ছিল তাদের Record গুলো দেখানো হয়েছে।",
            'ORM_querry': f"Teacher.objects.filter( joiningDate__month__gte = {_month} )",
        }    
    return render(request, 'Result/teacher.html', data)





def ORM_filter_joining__year_month_day(request):
    _year = 2010
    _month = 1
    _from = 1
    _to   = 31

    if request.method == "POST":
        _year  = request.POST.get('year')
        _month = request.POST.get('month')

        if int(request.POST.get('day-from')) > 31 or int(request.POST.get('day-to')) <= 0:
            _month = 1
            _to    = 31
        else:
            _from  = request.POST.get('day-from')
            _to    = request.POST.get('day-to')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter(
    #         Q(joiningDate__year=_year) & Q(joiningDate__month=_month) & Q(joiningDate__day__range=(_from, _to))
    #     )


    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE   YEAR(joiningDate) = {_year}
                             AND 
                    MONTH(joiningDate) = {_month}
                             AND
                    DAY(joiningDate) BETWEEN {_from} AND {_to}

        """
    teacher_data = Student.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে সে সকল Record গুলো দেখাবে যাদের Year = {_year} এবং Monty = {_month} এবং Day {_from} থেকে {_to}।",
            'ORM_querry': f"""
                        Teacher.objects.filter(
                            Q(joiningDate__year={_year}) & Q(joiningDate__month={_month}) & Q(joiningDate__day__range=({_from}, {_to}))
                        )
                    """,
        }    
    return render(request, 'Result/teacher.html', data)
   




def ORM_filter_joining_date_week(request):
    _week = 13    ## 1 week = 12 * 4 = 48 কিংবা তার ও বেশি week 
    if request.method == "POST":
        if int(request.POST.get('week')) <=0 and int(request.POST.get('week')) <= 49:
            _week = 1
        else:
            _week = request.POST.get('week')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( joiningDate__week__lte = _week )  

    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE WEEK(joiningDate) <= {_week}

        """
    teacher_data = Student.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"""
                            সম্পূর্ন Table থেকে যাদের Joining Date week = {_week} এর কম তাদেরকে দেখাবে।
                            NOTE: 1 Year = 12 * 4 = 48 কিংবা তার ও বেশি Week হতে পারে। যেমন 13 weeks = 13/4 = 3 months (March)
                            এর 1st week এর আগে যাদের Joint Date তাদের Record গুলো দেখাবে। 
                        """,
            'ORM_querry': f"Teacher.objects.filter( joiningDate__week__lte = {_week} ) ",
        }    
    return render(request, 'Result/teacher.html', data)






def ORM_filter_joining(request):
    _year = 2022

    if request.method == "POST":
        _year = request.POST.get('year')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter(joiningDate__year = _year) # YYYY 


    ## NOTE For SQL

    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE YEAR(joiningDate) = {_year}
        """

    teacher_data = Student.objects.raw(sql_query)

    ## NOTE Print
    # Iterate through the RawQuerySet and print each student's name
    # print("------------------")
    # for student in students_data:
    #     print("Student Name:", student.name)
    # print("------------------")

    print("------------------")
    print("Teacher Name:", teacher_data)
    print("------------------")

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যার নাম এর মাঝে",
            'ORM_querry': f"Teacher.objects.filter(joiningDate__year = {_year}))",
        }    
    return render(request, 'Result/teacher.html', data)
    # return HttpResponse()