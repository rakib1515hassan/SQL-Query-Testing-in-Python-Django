# Install MySQLclient under the virtual environment

    > pip install mysqlclient


# DATABASES

    DATABASES = {
        "default": {
            "ENGINE":  "django.db.backends.postgresql",
            "NAME":    "mydatabase",
            "USER":    "mydatabaseuser",
            "PASSWORD":"mypassword",
            "HOST":    "127.0.0.1",
            "PORT":    "3306",
        }
    }  


# ENGINE

    'django.db.backends.postgresql'
    'django.db.backends.mysql'
    'django.db.backends.sqlite3'
    'django.db.backends.oracle'


# HOST

    "HOST": "/var/run/mysql"


## Create Database in MySQL

1. Go to CMD

        > mysql -u root

    if password then

             > mysql -u root -p
    password:> your_password



2. See the Database:

        > show databases;

3. Exit into Mysql:

        > exit

4. Show Table:

        > use mysql
        > show tables;     এতে আমরা সব Tabel দেখতে পারবো।

5. কোন Table এর ভেতরে দেখতে চাইলে 

        > select user from user;

6. User create করতে,

        > CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
        > CREATE USER rakib@localhost IDENTIFIED BY '123456ra';

    Let's break down the components of this command:

    i) username: নতুন ইউজারের জন্য প্রয়োজনীয় ইউজারনেম দিন।

    ii) hostname: ইউজারটির সংযোগ করতে পারবে সেই হোস্টের নাম বা IP ঠিকানা নির্ধারণ করুন। '%' ব্যবহার করে যেকোনো হোস্ট থেকে সংযোগ অনুমোদন দিতে পারেন। আপনি সংযোগ সীমিত করতে চাইলে 'localhost' ব্যবহার করতে পারেন।

    iii) password: নতুন ইউজারের পাসওয়ার্ড নির্ধারণ করুন। আপনি এই জায়গায় 'পাসওয়ার্ড' সংজ্ঞা ব্যবহার করে যে পাসওয়ার্ড সেট করতে চান তা দিতে হবে।

    Example:- 
        
        > CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypassword';
        > CREATE USER rakib@localhost IDENTIFIED BY '123456ra';

    ইউজারটি তৈরি করার পরে, আপনার ইউজারের ডেটাবেস এবং টেবিলের সাথে কাজ করতে তাদের সাথে সম্পর্ক করার জন্য নির্দিষ্ট সুবিধা দেওয়ার জন্য সম্ভাব্য সুবিধা দেওয়া হতে পারে। উদাহরণস্বরূপ, 'myuser' ইউজারে সমস্ত সুবিধা দেওয়া হল একটি নির্দিষ্ট ডেটাবেসে:

    Example:- 
    
        > GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'%';

    iv) mydatabase: নামটি যে ডেটাবেসে সুবিধা দেওয়া হবে তা সংজ্ঞানে দিতে নিশ্চিত হন। আপনি যদি প্রয়োজন হলে বিশেষ সুবিধা যেমন SELECT, INSERT, UPDATE, বা DELETE সিস্টেমগুলি স্বতন্ত্রভাবে প্রদান করতে পারেন।

    সুবিধা প্রদানের পরে, পরিবর্তন যেন প্রভাবিত হয়ে এসে নিশ্চিত করার জন্য আপনাকে সুবিধা ফ্লাশ করতে হবে:

        > FLUSH PRIVILEGES;

    দয়া করে মনোনিবেশন করুন যে MySQL ডেটাবেসে ইউজারের অ্যাকাউন্ট এবং সুবিধা নির্ধারণ এবং তাদের সুরক্ষা এবং সুরক্ষা সংরক্ষণের জন্য সাবধান এবং নিরাপদভাবে পরিচালনা করতে হবে। আপনার প্রকল্পের প্রয়োজনীয় সুবিধা নির্ধারণ করার জন্য আপনি প্রতিটি ব্যবহারকারীর ব্যবহারে বৈচিত্র্যপূর্ণ এবং প্রয়োজনীয় সুবিধা ব্যবহার করতে হবে।





## Create Database:

    > CREATE DATABASE database_name;
    > CREATE DATABASE testdb;

shwo database

    > show databases;

এখন permission grant করতে হবে, জাতে এই Database এর access শুধু rakib user এ পায়।

    > GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'%';
    > GRANT ALL PRIVILEGES ON testsqldb.* TO rakib@localhost;


now go to setting and set,

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "testsql",
            "USER": "rakib",
            "PASSWORD": "123456ra",
            "HOST": "127.0.0.1",
            "PORT": "3306",
        }
    }

then run makemigrations and migrate,
To see the created table,

    > use testsql;
    > show tables;





WARNINGS:
?: (mysql.W002) MariaDB Strict Mode is not set for database connection 'default'
        HINT: MariaDB's Strict Mode fixes many data integrity problems in MariaDB, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/4.2/ref/databases/#mysql-sql-mode


Repare Xampp mysql: https://www.youtube.com/watch?v=84IOtc05TuA&ab_channel=BoostMyTool




# When to Use Raw SQL in Django
We should only use raw SQL in Django as a last resort, when it’s necessary to achieve a specific goal or to optimize the performance of a query. Here are a few scenarios where you might consider using raw SQL in Django:

    i) When you need to execute a complex query that involves multiple table joins and aggregations: The Django ORM is powerful, but it may not be able to handle complex queries that involve multiple table joins and aggregations. In these cases, you might need to use raw SQL to get the results you need.
    
    ii) When you need to perform a bulk update or delete operation on a large number of records: The Django ORM provides a convenient way to update or delete individual records, but it can be inefficient when you need to perform a bulk operation on a large number of records. Using raw SQL can be a faster and more efficient way to perform these types of operations.

    iii) When you need to optimize the performance of a query: In some cases, you may find that using raw SQL can improve the performance of a query. For example, if you have a complex query that is slow when executed using the Django ORM, you might be able to optimize the performance by writing the query as raw SQL.


    from django.db.models import RawSQL

# Example:- Here’s an example of how you might use raw SQL queries with the Django ORM:

# Find users with a username that starts with 'john'
users = User.objects.raw(
    'SELECT * FROM users WHERE username LIKE %s', ['john%']
)

## Update the age of all the users in the queryset
users.update(age=30)

## Find the user with the highest age
max_age_user = users.latest('age')

## Delete all the users in the queryset
users.delete()


# Example:- Here’s an example of how you might map a raw SQL query to a Django model:

from django.db.models import RawSQL

## Map the results of a raw SQL query to the User model
users = User.objects.raw(
    'SELECT * FROM users WHERE username LIKE %s', ['john%'],
    model=User,
    columns=['id', 'username', 'age']
)

## Access the attributes of the mapped model objects
for user in users:
    print(f'{user.username} is {user.age} years old')


# # Example:- Here’s an example of how you might use raw SQL for an aggregate function in Django:

from django.db.models import RawSQL

# Count the number of users in the database
num_users = User.objects.raw(
    'SELECT COUNT(*) FROM users',
).scalar()

# Calculate the total age of all the users
total_age = User.objects.raw(
    'SELECT SUM(age) FROM users',
).scalar()

# Calculate the average age of all the users
avg_age = User.objects.raw(
    'SELECT AVG(age) FROM users',
).scalar()