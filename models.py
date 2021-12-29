from django.db import models


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_genre = models.CharField(max_length=200)
    book_publish_date = models.DateField()

class Author(models.Model):
    author_first_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book,
                                   related_name="authors")

class Quiz(models.Model):
    duration_in_minutes = models.IntegerField()
    quiz_title = models.CharField(max_length=100, default="Quiz01")
    quiz_order = models.IntegerField(default=10)
    is_open = models.BooleanField(default=True)

#question_text, correct_answer, points, ans_1, ans_2, ans_3

class Question(models.Model):
    question_text = models.TextField()
    question_points = models.IntegerField()
    question_correct_answer = models.CharField(max_length=300)
    question_incorrect_answer_1 = models.CharField(max_length=300)
    question_incorrect_answer_2 = models.CharField(max_length=300)
    question_incorrect_answer_3 = models.CharField(max_length=300)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)



#student info (student table)
#
#   phone num 1 (phone table)
#   phone num 2 (phone table_


#One question belongs to one quiz
#One quiz has many questions
#
#One email belongs to one student
#One student has many emails
#
#One trail review belong to one trail
#One trail has many trail reviews

class Student(models.Model):
    first_name = models.CharField(max_length=50) #first name varChar(50)
    last_name = models.CharField(max_length=50) #last name varChar(50)
    age = models.IntegerField(default=30)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_num = models.CharField(max_length=20)
    is_undergrad = models.BooleanField()
    course_credit_hours = models.IntegerField()
    course_description = models.TextField()
    course_prereq = models.CharField(max_length=200)


    """CREATE TABLE"""
    """ALTER TABLE student ADD COLUMN age INT DEFAULT 30;"""

    """
        ORM methods 
            INSERTS INTO
            SEARCH (SELECT * FROM...) 
            """