from django.shortcuts import render
from Basic_Query.models import Student, Teacher, Query_Code
from django.db import connection
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime, date, time

# Combine the conditions using reduce and the selected operator
from functools import reduce

def Query_101(request):

    ## ORM Query
    # students_data = Student.objects.values('id', 'name', 'city', 'roll')

    # Define the variables for columns you want to select dynamically
    selected_columns = ['id', 'name', 'city', 'roll'] # NOTE id (primary key) must be দেয়া লাগবে

    # Construct the SQL query dynamically based on the selected columns
    column_list = ', '.join(selected_columns)

    sql_query = f"""
            SELECT {column_list} 
            FROM basic_query_student
        """

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
            'query': Query_Code.objects.get( query_no = 'Query_101' ),
  
        }    
    return render(request, 'Result/result_2.html', data)








def Query_102(request):

    ## ORM Query
    # students_data = Student.objects.values('city').distinct()

    # Define the variables for columns you want to select dynamically
    selected_columns = ['id','city']            # NOTE id (primary key) must be দেয়া লাগবে
    column_list = ', '.join(selected_columns)
    sql_query = f"""
            SELECT DISTINCT {column_list} 
            FROM basic_query_student
        """

    stu_data = Student.objects.raw(sql_query)

    distinct_cities = set(student.city for student in stu_data)

    data = {
            # 'std_obj': students_data,
            'std_obj_distinct': distinct_cities,
            'SQL_querry': "SELECT DISTINCT city FROM basic_query_student",
            'descripetion': "সম্পূর্ন Table হতে city column দেখাবে। কিন্তু কোন Duplicate value দেখাবে না।",
            'ORM_querry': "Student.objects.values('city').distinct()",
            'query': Query_Code.objects.get( query_no = 'Query_102' ),
        }    
    return render(request, 'Result/result_2.html', data)





def Query_103(request):
    start_point = 0
    end_point = 5
    if request.method == "POST":
        start_point = request.POST.get('start')  # The start point (inclusive)
        end_point   = request.POST.get('end')  # The end point (exclusive)

    ## ORM Query
    # students_data = Student.objects.all()[ start_point : end_point ]  ## [Start : End: Increment]

    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            LIMIT {start_point}, {end_point}
        """
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table হতে কেবল মাত্র {start_point} হতে {end_point} এর আগ পর্যন্ত Data দেখাবে।",
            'ORM_querry': f"Student.objects.all()[ {start_point} : {end_point} ]",
            'query': Query_Code.objects.get( query_no = 'Query_103' ),
        }    
    return render(request, 'Result/result_1.html', data)




def Query_104(request):
    order_attribute = 'roll'

    ## ORM Query
    # students_data = Student.objects.all().order_by(order_attribute)

    # ASC না দিলেও, Ascending order defult থাকে।
    # DESC দিলে Decending order এ sort হবে।
    sql_query = f"""
            SELECT * 
            FROM basic_query_student            
            ORDER BY {order_attribute} ASC 
    
        """                                                                                   
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': "সম্পূর্ন Table কে Roll এর ওপর ভিতি করে Ascending order এ দেখাবে। তবে ASC এর যায়গায় DESC দিলে Decending order এ sort হবে।",
            'ORM_querry': f"Student.objects.all().order_by({order_attribute})",
            'query': Query_Code.objects.get( query_no = 'Query_104' ),
        }    
    return render(request, 'Result/result_1.html', data)





"""
WHERE clause এর সাহায্যে একটি নির্দিষ্ট  শর্ত / condition এর উপর ভিতি করে ডাটা খুজেতে ব্যাবহার কারা হয়।

SELECT column_list
FROM table_name
WHERE condition;

"""




def Query_105(request):
    gen = 'Male'
    if request.method == "POST":
        gen = request.POST.get('gender')

    ## ORM Query
    # students_data = Student.objects.filter(gender = gen)

    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE gender = '{gen}'
        """ 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে কেবল মাত্র gender = {gen} কে আলদাকরে দেখানো হয়েছে।",
            'ORM_querry': f"Student.objects.filter(gender = {gen})",
            'query': Query_Code.objects.get( query_no = 'Query_105' ),
        }    
    return render(request, 'Result/result_1.html', data)
   



def Query_106(request):
    age = '10'
    lookups = 'gt'
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

    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE age {condition} {age}
        """ 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা age {condition} {age} condition টি কে মানে, সে সকল Data গুলোকে এখানে দেখানো হয়েছে।",
            'ORM_querry': f"Student.objects.filter({conditio})",
            'query': Query_Code.objects.get( query_no = 'Query_106' ),
        }    
    return render(request, 'Result/result_1.html', data)






def Query_107(request):
    _from = '10'
    _to   = '14'
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

    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE age >= {_from} {operator} age <= {_to}
        """ 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা শুধু সে সকল Record কে দেখানো হয়েছে যাদের Age {_from} থেকে {_to} {txt}।",
            'ORM_querry': f"Student.objects.filter(Q(age__gte ={_from}) {_operator} Q(age__lte ={_to}))",
            'query': Query_Code.objects.get( query_no = 'Query_107' ),
        }    
    return render(request, 'Result/result_1.html', data)






def Query_108(request):
    _from = '15'
    _to   = '20'

    if request.method == "POST":
        _from = request.POST.get('from')
        _to   = request.POST.get('to')  

    ## NOTE For ORM
    # students_data = Student.objects.filter(age__range=(_from, _to))

    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE age BETWEEN {_from} AND {_to}
        """ 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা শুধু সে সকল Record কে দেখানো হয়েছে যাদের Age {_from} থেকে {_to} এর মধ্যে।",
            'ORM_querry': f"Student.objects.filter(age__range=({_from}, {_to})",
            'query': Query_Code.objects.get( query_no = 'Query_108' ),
        }    
    return render(request, 'Result/result_1.html', data)




def Query_109(request):
    _from = '2000-01-01'
    _to   = '2023-12-30'

    ## NOTE For ORM
    # students_data = Student.objects.filter( date_of_birth__range = ( _from, _to ) )

    ## NOTE For SQL
    sql_query = f"""
                    SELECT * 
                    FROM basic_query_student 
                    WHERE date_of_birth BETWEEN '{_from}' AND '{_to}'
                """
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা শুধু সে সকল Record কে দেখানো হয়েছে যাদের Birth date {_from} থেকে {_to} এর মধ্যে।",
            'ORM_querry': f"Student.objects.filter( date_of_birth__range = ( {_from}, {_to} ))",
            'query': Query_Code.objects.get( query_no = 'Query_109' ),
        }    
    return render(request, 'Result/result_1.html', data)





def Query_110(request):
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
    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE s_class = '{_class}' AND NOT gender = '{_gender}'
        """ 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে জাদের Class = {_class} এবং যাদের Gender = {_gender} না সে সকল Record গুলো দেখানো হয়েছে।",
            'ORM_querry': f"students_data = Student.objects.filter( Q(s_class={_class}) & (~Q(gender={_gender})) ))",
            'query': Query_Code.objects.get( query_no = 'Query_110' ),
        }    
    return render(request, 'Result/result_1.html', data)



"""
SQL এর Logical Operator গুলো হল AND, OR, IN, NOT and LIKE

SELECT column_list
FROM table_name
WHERE condition;

"""





def Query_111(request):
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
    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE city = '{_city}'
                        AND
                    ( (gender = '{_gender}') OR (age >= {_age}) )
        """ 
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
            'query': Query_Code.objects.get( query_no = 'Query_111' ),
        }    
    return render(request, 'Result/result_1.html', data)





def Query_112(request):
    _city   = ['Khulna', 'Chittagong']

    ## NOTE For ORM
    # ORM Query using the 'in' lookup
    # students_data = Student.objects.filter(city__in=_city)

    ## NOTE For SQL
    # Enclose each city name in single quotes
    city_list = [f"'{city}'" for city in _city]  # return = ["'Dhaka'", "'Noakhali'", "'Chandpur'"]
    column_list = ', '.join(city_list)           # return = 'Dhaka', 'Noakhali', 'Chandpur'

    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE city IN ({column_list})
        """ 
    students_data = Student.objects.raw(sql_query)

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের City {_city}, সে সকল Record গুলোকে দেখাবে।",
            'ORM_querry': f"Student.objects.filter(city__in={_city})",
            'query': Query_Code.objects.get( query_no = 'Query_112' ),
        }    
    return render(request, 'Result/result_1.html', data)





def Query_113(request):
    _name   = 'rijon'

    ## NOTE For ORM
    # students_data = Student.objects.filter(name__iexact = _name)

    ## NOTE For SQL
    sql_query = """
            SELECT * 
            FROM basic_query_student 
            WHERE name LIKE %s
        """
    students_data = Student.objects.raw(sql_query, [_name + '%'])
    

    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যার নাম {_name}, তার সকল Record দেখাবে, তবে এটি case insensitive এই SQL Query ব্যেবহার করে start with ও বের কারা যায়।",
            'ORM_querry': f"Student.objects.filter(name__iexact = {_name})",
            'query': Query_Code.objects.get( query_no = 'Query_113' ),
        }    
    return render(request, 'Result/result_1.html', data)




def Query_114(request):
    _name   = 'Ra'

    ## NOTE For ORM
    # students_data = Student.objects.filter(name__contains = _name)

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
            'ORM_querry': f"Student.objects.filter(name__contains = {_name})",
            'query': Query_Code.objects.get( query_no = 'Query_114' ),
        }    
    return render(request, 'Result/result_1.html', data)




def Query_115(request):
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
            'query': Query_Code.objects.get( query_no = 'Query_115' ),
        }    
    return render(request, 'Result/result_1.html', data)




"""
SQL এর Constraint Auto Increment গুলো হল NOT NULL, UNIQUE, PRIMARY KEY = NOT NULL + UNIQUE, CHECK, DEFAULT
"""








def Query_116(request):
    _year = 2022

    if request.method == "POST":
        _year = request.POST.get('year')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter(joiningDate__year = _year) # YYYY 

    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE YEAR(joiningDate) = {_year}
        """

    # # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE CAST(strftime('%Y', joiningDate) AS INTEGER) = {_year}
    #     """
    
    teacher_data = Teacher.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের Joing Date {_year}, তাদের Record গুলো দেখানো হয়েছে । ",
            'ORM_querry': f"Teacher.objects.filter(joiningDate__year = {_year}))",
            'query': Query_Code.objects.get( query_no = 'Query_116' ),
        }    
    return render(request, 'Result/teacher.html', data)







def Query_117(request):
    _from = 2010
    _to   = 2022

    if request.method == "POST":
        _from = request.POST.get('year-from')
        _to   = request.POST.get('year-to')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter(joiningDate__year__range = (_from, _to)) # YYYY 


    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE YEAR(joiningDate) BETWEEN {_from} AND {_to}
        """
    
    # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE strftime('%Y', joiningDate) BETWEEN '{_from}' AND '{_to}'
    #     """
    
    teacher_data = Teacher.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের Joing date {_from} থেকে {_to}, তাদের Record গুলোকে দেখাবে।",
            'ORM_querry': f"Teacher.objects.filter(joiningDate__year__range = ({_from}, {_to}))",
            'query': Query_Code.objects.get( query_no = 'Query_117' ),
        }    
    return render(request, 'Result/teacher.html', data)






def Query_118(request):
    _month = 6

    if request.method == "POST":
        if int(request.POST.get('month')) >= 12 or int(request.POST.get('month')) <= 0:
            _month = 1
        else:
            _month = request.POST.get('month')


    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( joiningDate__month__gte = _month ) # MM


    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE MONTH(joiningDate) >= {_month}
        """
    
    # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE strftime('%m', joiningDate) >= '{_month}'
    #     """
    
    teacher_data = Teacher.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যাদের Joing Month {_month} এর সমান কিংবা বেশি ছিল তাদের Record গুলো দেখানো হয়েছে।",
            'ORM_querry': f"Teacher.objects.filter( joiningDate__month__gte = {_month} )",
            'query': Query_Code.objects.get( query_no = 'Query_118' ),
        }    
    return render(request, 'Result/teacher.html', data)





def Query_119(request):
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
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE   YEAR(joiningDate) = {_year}
                             AND 
                    MONTH(joiningDate) = {_month}
                             AND
                    DAY(joiningDate) BETWEEN {_from} AND {_to}
        """
    
    # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE 
    #             strftime('%Y', joiningDate) = '{_year}' AND
    #             strftime('%m', joiningDate) = '{_month}' AND
    #             strftime('%d', joiningDate) BETWEEN '{_from}' AND '{_to}';
    #     """
    teacher_data = Teacher.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে সে সকল Record গুলো দেখাবে যাদের Year = {_year} এবং Monty = {_month} এবং Day {_from} থেকে {_to}।",
            'ORM_querry': f"""
                        Teacher.objects.filter(
                            Q(joiningDate__year={_year}) & Q(joiningDate__month={_month}) & Q(joiningDate__day__range=({_from}, {_to}))
                        )
                    """,
            'query': Query_Code.objects.get( query_no = 'Query_119' ),
        }    
    return render(request, 'Result/teacher.html', data)
   




def Query_120(request):
    _week = 13    ## 1 week = 12 * 4 = 48 কিংবা তার ও বেশি week 
    if request.method == "POST":
        if int(request.POST.get('week')) <=0 or int(request.POST.get('week')) > 49:
            _week = 13
        else:
            _week = request.POST.get('week')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( joiningDate__week__lte = _week )  

    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE WEEK(joiningDate) <= {_week}
        """

    # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE strftime('%W', joiningDate) <= '{_week}';
    #     """
    
    teacher_data = Teacher.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"""
                            সম্পূর্ন Table থেকে যাদের Joining Date week = {_week} এর কম তাদেরকে দেখাবে।
                            NOTE: 1 Year = 12 * 4 = 48 কিংবা তার ও বেশি Week হতে পারে। Example:- 13 weeks = 13/4 = 3 months (March)
                            এর 1st week এর আগে যাদের Joint Date তাদের Record গুলো দেখাবে। 
                        """,
            'ORM_querry': f"Teacher.objects.filter( joiningDate__week__lte = {_week} ) ",
            'query': Query_Code.objects.get( query_no = 'Query_120' ),
        }    
    return render(request, 'Result/teacher.html', data)





def Query_121(request):
    _day = 1    ## Sunday=1, Monday=2, Tuesday=3, Wednesday=4, Thursday=5, Friday=6, Saturday=7
    if request.method == "POST":
        if int(request.POST.get('day')) <=0 or int(request.POST.get('day')) > 7:
            _day = 1
        else:
            _day = request.POST.get('day')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( joiningDate__week_day = _day )  

    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE DAYOFWEEK(joiningDate) = {_day}
        """

    # # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE strftime('%w', joiningDate) = '{_day}'
    #     """
    
    teacher_data = Teacher.objects.raw(sql_query)
    
    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"""
                            সম্পূর্ন Table থেকে যাদের Joining এর week days = {_day}, তাদেরকে দেখাবে।
                            NOTE: Sunday=1, Monday=2, Tuesday=3, Wednesday=4, Thursday=5, Friday=6, Saturday=7 
                        """,
            'ORM_querry': f"Teacher.objects.filter( joiningDate__week__lte = {_day} ) ",
            'query': Query_Code.objects.get( query_no = 'Query_121' ),
        }    
    return render(request, 'Result/teacher.html', data)






def Query_122(request):
    ## NOTE এটি DateField and DateTimeField উভয় এর সাথে work করে।
    ## 1 Year = 4 Quarter. So,
        # 1st Quarter = (January, February, March), 
        # 2nd Quarter = (April, May, Jun),
        # 3rd Quarter = (Jyly, Augest, Septamber), 
        # 4th Quarer = (October, November, December))

    _quarter = 1   
    if request.method == "POST":
        if int(request.POST.get('quarter')) <=0 or int(request.POST.get('quarter')) > 4:
            _quarter = 1
        else:
            _quarter = request.POST.get('quarter')

    ## NOTE For ORM
    # students_data = Student.objects.filter( date_of_birth__quarter = _quarter )  

    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_student 
            WHERE QUARTER(date_of_birth) = {_quarter}
        """
    
    # # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_student 
    #         WHERE strftime('%m', date_of_birth) BETWEEN '{int(_quarter) * 3 - 2}' AND '{int(_quarter) * 3}'
    #     """

    students_data = Student.objects.raw(sql_query)
    
    data = {
            'std_obj': students_data,
            'SQL_querry': students_data.query,
            'descripetion': f"""
                            সম্পূর্ন Table থেকে যাদের Date of Birth {_quarter} Quarter এর মধ্যে, তাদের Record গুলো দেখাবে।
                            NOTE: এটি DateField and DateTimeField উভয় এর সাথে work করে।
                            ## 1 Year = 4 Quarter. So,
                                # 1st Quarter = (January, February, March), 
                                # 2nd Quarter = (April, May, Jun),
                                # 3rd Quarter = (Jyly, Augest, Septamber), 
                                # 4th Quarer = (October, November, December))
                        """,
            'ORM_querry': f"Student.objects.filter( date_of_birth__quarter = {_quarter} ) ",
            'query': Query_Code.objects.get( query_no = 'Query_122' ),
        }    
    return render(request, 'Result/result_1.html', data)




def Query_123(request):
    ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।
    _time = "10:20"  # Time you want to filter before (10:20 AM)
    if request.method == "POST":
        _time = request.POST.get('time')

    ## NOTE For ORM
    ## input time string কে Split করে integer করে hours and minutes এ converted করে দিবে map function use করে।
    hours, minutes = map(int, _time.split(':'))
    # input_time = time(hours, minutes)
    # teacher_data = Teacher.objects.filter( joiningDate__time__lt = input_time )  # 13:00pm means, 1:00 pm এর পর যারা যারা 

    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE TIME(joiningDate) < '{_time}'

        """
    teacher_data = Teacher.objects.raw(sql_query)

    hr = ''
    periods = ''
    if hours >=12:
        hr = hours - 12
        periods = "P.M"
    else:
        hr = hours
        periods = "A.M"

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা {hr}:{minutes} {periods} এর আগে Join করেছে তাদের Record গুলো দেখাবে। ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।",
            'ORM_querry': f"Teacher.objects.filter( joiningDate__time__lt = time({_time}) )",
            'query': Query_Code.objects.get( query_no = 'Query_123' ),
        }    
    return render(request, 'Result/teacher.html', data)





def Query_124(request):
    ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে কাজ করে।
    _time = "10:00" 
    if request.method == "POST":
        _time = request.POST.get('hour')

    ## input time string কে Split করে integer করে hours and minutes এ converted করে দিবে map function use করে।
    hours, minutes = map(int, _time.split(':'))

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( joiningDate__hour__lt = hours ) # 1 day = 24 hour

    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE HOUR(joiningDate) < '{hours}'
        """

    # # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE strftime('%H', joiningDate) < '{hours}'
    #     """

    teacher_data = Teacher.objects.raw(sql_query)

    hr = ''
    periods = ''
    if hours >=12:
        hr = hours - 12
        periods = "P.M"
    else:
        hr = hours
        periods = "A.M"
    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা {hr} {periods} এর আগে Join করেছে তাদের Record গুলো দেখাবে। ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে কাজ করে।",
            'ORM_querry': f"Teacher.objects.filter( joiningDate__hour__lt = {hours} )",
            'query': Query_Code.objects.get( query_no = 'Query_124' ),
        }    
    return render(request, 'Result/teacher.html', data)





def Query_125(request):
    ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে কাজ করে।
    _time = "09:30" 
    if request.method == "POST":
        _time = request.POST.get('minute')

    ## input time string কে Split করে integer করে hours and minutes এ converted করে দিবে map function use করে।
    hours, minutes = map(int, _time.split(':'))

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( Q(joiningDate__hour = 9) & Q(joiningDate__minute__lt = minutes) ) # 1 hour = 60 minutes

    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE ( HOUR(joiningDate) = 9 ) AND ( MINUTE(joiningDate) <= {minutes} )
        """

    # # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE strftime('%H', joiningDate) = '09' AND strftime('%M', joiningDate) <= '{minutes}';
    #     """
    teacher_data = Teacher.objects.raw(sql_query)

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা 9:{minutes} A.M এর আগে Join করেছে তাদের Record গুলো দেখাবে। ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে। এখানে যদি আমরা Hour = 9 fix করে না দিতাম তবে প্রতি ঘণ্টায় {minutes} মিনিট এর আগে যারা join করেছে তাদের দেখাতো।",
            'ORM_querry': f"Teacher.objects.filter( joiningDate__minute__lt = {minutes} )",
            'query': Query_Code.objects.get( query_no = 'Query_125' ),
        }    
    return render(request, 'Result/teacher.html', data)





def Query_126(request):
    ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে কাজ করে।
    _time = "09:30" 
    if request.method == "POST":
        _time = request.POST.get('minute')

    ## input time string কে Split করে integer করে hours and minutes এ converted করে দিবে map function use করে।
    hours, minutes = map(int, _time.split(':'))

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( Q(joiningDate__hour = 9) & Q(joiningDate__minute__lt = minutes) ) # 1 hour = 60 minutes

    ## NOTE For SQL
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE ( HOUR(joiningDate) = 9 ) AND ( MINUTE(joiningDate) >= {minutes} )
        """
    teacher_data = Teacher.objects.raw(sql_query)

    print("------------------")
    # print(" OBJ:", teacher_data)
    print(" OBJ:", minutes)
    print("------------------")

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা {hours} এর আগে Join করেছে তাদের Record গুলো দেখাবে। ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।",
            'ORM_querry': f"Teacher.objects.filter( joiningDate__minute__lt = {minutes} )",

            # 'query': Query_Code.objects.get( query_no = 'Query_125' ),
        }    
    return render(request, 'Result/teacher.html', data)
    # return HttpResponse()







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
    # return render(request, 'Result/result_1.html', data)
    # return HttpResponse()