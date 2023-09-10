from django.db import models
import uuid


# Create your models here.
class Student(models.Model):
    id            = models.UUIDField( primary_key = True, unique=True, default = uuid.uuid4, editable=False )
                            
    name          = models.CharField( max_length=50 )
    s_class       = models.CharField( max_length=50, choices=(
        ('vi','vi'),
        ('vii','vii'),
        ('viii','viii'),
        ('ix','ix'),
        ('x','x'),
        ))
    
    roll          = models.IntegerField( null=True )
    date_of_birth = models.DateField()
    age           = models.PositiveIntegerField()
    city          = models.CharField(max_length=50, null=True, blank=True)
    gender        = models.CharField(max_length=20, choices=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
        ))

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    id         = models.UUIDField( primary_key = True, unique=True, default = uuid.uuid4, editable=False )

    name       = models.CharField(max_length=50, null=True, blank=True)
    emplyee_id = models.CharField(max_length=50, unique=True, null=False)
    city       = models.CharField(max_length=50, null=True, blank=True)
    salary     = models.IntegerField()
    joiningDate = models.DateTimeField()

    def __str__(self):
        return self.name
    


class ExamResult(models.Model):
    id         = models.UUIDField( primary_key = True, unique=True, default = uuid.uuid4, editable=False )
    student    = models.OneToOneField( Student, on_delete = models.CASCADE )

    marks      = models.IntegerField(null=True, blank=True)
    result     = models.DecimalField( 
        max_digits = 4,    # Specifies the maximum number of digits (including both sides of the decimal point)
        decimal_places = 2 # Specifies the number of decimal places
        )
    
    def __str__(self):
        return f"NAME: {self.student.name}, RESULT = {self.result}"


# class Subject(models.Model):
#     id      = models.UUIDField( primary_key = True, unique=True, default = uuid.uuid4, editable=False )
#     name = models.CharField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return self.name
    

# class Select_Subject(models.Model):
#     id      = models.UUIDField( primary_key = True, unique=True, default = uuid.uuid4, editable=False )
#     subject = models.ForeignKey( Subject, on_delete=models.CASCADE )
#     student = models.ManyToManyField(Student)
#     teacher = models.ManyToManyField(Teacher)

#     def __str__(self):
#         return self.name