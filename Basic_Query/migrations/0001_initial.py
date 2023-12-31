# Generated by Django 4.2.5 on 2023-09-14 13:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query_Code',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('query_no', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('SQL_query', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ORM_query', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('s_class', models.CharField(choices=[('vi', 'vi'), ('vii', 'vii'), ('viii', 'viii'), ('ix', 'ix'), ('x', 'x')], max_length=50)),
                ('roll', models.IntegerField(null=True)),
                ('date_of_birth', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('emplyee_id', models.CharField(max_length=50, unique=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('salary', models.IntegerField()),
                ('joiningDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('marks', models.IntegerField(blank=True, null=True)),
                ('result', models.DecimalField(decimal_places=2, max_digits=4)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Basic_Query.student')),
            ],
        ),
    ]
