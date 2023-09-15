from django.shortcuts import render
from Basic_Query.models import Student, Teacher, Query_Code
from django.db import connection
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime, date, time

# Combine the conditions using reduce and the selected operator
from functools import reduce



# Create your views here.
def Query_2(request):
    return render(request, 'Query\query_2.html')




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
    _second = 30 
    if request.method == "POST":
        _second = request.POST.get('second')

    ## NOTE For ORM
    # teacher_data = Teacher.objects.filter( joiningDate__second__lt = _second ) # 1 minute = 60 seconds

    ## NOTE For SQL
    ## এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    sql_query = f"""
            SELECT * 
            FROM basic_query_teacher 
            WHERE SECOND(joiningDate) <= {_second}
        """

    ## SQLite3
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE strftime('%S', joiningDate) <= '{_second}';
    #     """
    
    teacher_data = Teacher.objects.raw(sql_query)

    print("------------------")
    # print(" OBJ:", teacher_data)
    # print(" OBJ:", minutes)
    print("------------------")

    data = {
            'teacher_obj': teacher_data,
            'SQL_querry': teacher_data.query,
            'descripetion': f"সম্পূর্ন Table থেকে যারা প্রতি মিনিটে {_second} এর আগে Join করেছে তাদের Record গুলো দেখাবে। এটি ভালো কাজ করে যখন আমরা টাইম টি auto now add করি তখন। ## NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।",
            'ORM_querry': f"Teacher.objects.filter( joiningDate__second__lt = {_second} )",
            'query': Query_Code.objects.get( query_no = 'Query_126' ),
        }    
    return render(request, 'Result/teacher.html', data)
    # return HttpResponse()
