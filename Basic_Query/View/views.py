from django.shortcuts import render
from Basic_Query.models import Student, Teacher
from django.db import connection
from django.http import HttpResponse

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








def ORM_(request):

    ## ORM Query
    students_data = Student.objects.values('city').distinct()


    # Define the variables for columns you want to select dynamically
    # selected_columns = ['id', 'name', 'city', 'roll'] # NOTE id (primary key) must be দেয়া লাগবে

    # # Construct the SQL query dynamically based on the selected columns
    # column_list = ', '.join(selected_columns)

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