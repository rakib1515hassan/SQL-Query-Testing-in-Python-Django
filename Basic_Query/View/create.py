from django.shortcuts import render
from django.db import connection
from datetime import datetime
import uuid
from Basic_Query.models import Student, Teacher
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def Query_1(request):
    return render(request, 'Query\query_1.html')


def Result(request):
    return render(request, 'Result/result.html')


def add_student(request):
    # if request.method == "POST" and 'add_std' in request.POST :
    if request.method == "POST":
        name = request.POST.get('s_name')
        gender = request.POST.get('s_gender')
        s_class = request.POST.get('s_class')
        roll = request.POST.get('s_roll')
        age = request.POST.get('s_age')
        city = request.POST.get('s_city')
        birth = request.POST.get('s_birth')

        if not Student.objects.filter( roll = roll).exists():

            # Generate a UUID for the id field without hyphens
            student_id = str(uuid.uuid4()).replace("-", "")

            # Parse the date_of_birth string to a datetime object
            date_of_birth = datetime.strptime(birth, '%Y-%m-%d').date()

            # Define the SQL query for inserting data into the Student table
            sql_query = """
                INSERT INTO basic_query_student (id, name, gender, s_class, roll, date_of_birth, age, city)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Execute the SQL query with the data
            with connection.cursor() as cursor:
                cursor.execute(sql_query, (student_id, name, gender, s_class, roll, date_of_birth, age, city))

            """ NOTE Data save by ORM
            student = Student(
                name=name,
                gender=gender,
                s_class=s_class,
                roll=roll,
                age=age,
                city=city,
                date_of_birth=date_of_birth
            )
            student.save()
            """
            response_data = {'message': 'Student added successfully', 'success': True}
        else:
            response_data = {'message': 'Employee ID already exists', 'success': False}
            
        return JsonResponse(response_data)
   
    return render(request, 'Data_Insurt/add_student.html')



def all_student(request):

    # Execute a raw SQL query to select all rows from the Student table
    students_data = Student.objects.raw("SELECT * FROM basic_query_student")  # Replace 'yourapp_student' with your actual table name

    """ NOTE It return a tupal, that's why don't use it.
    sql_query = "SELECT * FROM basic_query_student"  # Replace 'yourapp_student' with your actual table name

    # Execute the SQL query
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        students_data = cursor.fetchall()  # Fetch all rows from the result

    print result = (('a79401fe674b4c52893792f78b9170b8', 'Md Hassan', 'ix', 221, datetime.date(1995, 10, 20), 15, 'Kamrangirchar', 'Male'), ('a961385151a945f48dffeaf93127674e', 'Rakib', 'x', 162, datetime.date(1998, 10, 20), 16, 'Lalbagh', 'Male'))

    """
    

    # ## Iterate through the RawQuerySet and print each student's name
    # for student in students_data:
    #     print("------------------")
    #     print("Student Name:", student.name)
    #     print("------------------")


    data = {
        'std_obj': students_data,
        'total': Student.objects.all().count()
    }

    return render(request, 'Data_Insurt/all_students.html', data)





def add_teacher(request):
    # if request.method == "POST" and 'add_teacher' in request.POST :
    if request.method == "POST":
        name       = request.POST.get('t_name')
        emplyee_id = request.POST.get('t_emplyee_id')
        city       = request.POST.get('t_city')
        salary     = request.POST.get('t_salary')
        join       = request.POST.get('t_join')

        if Teacher.objects.filter( emplyee_id = emplyee_id).exists():
            response_data = {'message': 'Employee ID already exists', 'success': False}

        else:
            # Generate a UUID for the id field without hyphens
            id = str(uuid.uuid4()).replace("-", "")

            # Parse the date_of_birth string to a datetime object
            join = datetime.strptime(join, "%Y-%m-%dT%H:%M")

            # Define the SQL query for inserting data into the Student table
            sql_query = """
                INSERT INTO basic_query_teacher (id, name, emplyee_id, city, salary, joiningDate )
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            # Execute the SQL query with the data
            with connection.cursor() as cursor:
                cursor.execute(sql_query, (id, name, emplyee_id, city, salary, join))

            response_data = {'message': 'Teacher added successfully', 'success': True}
        return JsonResponse(response_data)

    return render(request, 'Data_Insurt/add_teacher.html')







def all_teacher(request):

    ## NOTE For ORM
    # teacher_data = Teacher.objects.all()


    ## NOTE For SQL
    teacher_data = Teacher.objects.raw("SELECT * FROM basic_query_teacher")


    data = {
        'teacher_obj': teacher_data,
        'total': Teacher.objects.all().count()
    }

    return render(request, 'Data_Insurt/all_teacher.html', data)