# Generated by Django 4.2.4 on 2023-09-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_Query', '0002_alter_teacher_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='emplyee_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
