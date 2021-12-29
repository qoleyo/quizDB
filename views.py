from django.shortcuts import render, HttpResponse
from random import randint, choice, shuffle
import datetime


def main_page(request):
    myList = [1, 2, 3, 4, 5, 6]
    myRandom = randint(0,10)
    return HttpResponse(f"<h1 style='color: red;' >{myList}: {myRandom}</h1>")

def week10_page(request):
    Book.objects.all().delete()
    Author.objects.all().delete()

    book_1 = Book(book_title="Book 1",
                   book_genre="Psychology",
                   book_publish_date=datetime.datetime.now())

    book_1.save()

    book_2 = Book(book_title="Book 2",
                       book_genre="Cognitive Psychology",
                       book_publish_date=datetime.datetime.now())
    book_2.save()

    author_1 = Author(author_first_name="Author 1 F",
                        author_last_name="Author 1 L")

    author_1.save()

    book_1.authors.add(author_1)
    book_2.authors.add(author_1)
    #book_1.author_set.add(author_1)
    #book_2.author_set.add(author_1)

    #author_1.books.add(book_1)
    #author_1.books.add(book_2)

    return HttpResponse("This is Week 10")

def quiz_page(request):

    my_list = [1, 2, 3]
    shuffle(my_list)

    choice(my_list)
    my_list[randint(0, len(my_list)- 1)]
    all_questions = Question.objects.filter(quiz_id=8)

    for question in all_questions:
        question.shuffled_answers = [question.question_correct_answer,
                                     question.question_incorrect_answer_1,
                                     question.question_incorrect_answer_2,
                                     question.question_incorrect_answer_3]
        shuffle(question.shuffled_answers)


   # print(all_questions[0].question_text)
   # print(all_questions[0].question_correct_answer)
   # print(all_questions[0].question_incorrect_answer_1)
   # print(all_questions[0].question_incorrect_answer_2)
   # print(all_questions[0].question_incorrect_answer_3)
   # print(all_questions[0].quiz_id)
   # print(all_questions[0].id)
   # print(all_questions[0].quiz.quiz_title)

    return render(request=request,
                  template_name="main/quiz.html",
                  context={"all_questions": all_questions})
    #Access the database (using ORM) and get the data that you need
    #Get the html page that you've created earlier
    #  Render the data (pulled from db) into the html page
    #      put the data inside the html page in some specific format
    #      return the html page
    ##return HttpResponse("This is the quiz page")

from main.models import*

def login_page(request):

    # every time i refresh the page, this function will be called
    # whenever this function is called, I'm going to insert something into a table
    #my_rand_duration = randint(20, 30)
   # my_rand_is_open = choice([True, False])

   # new_quiz = Quiz(duration_in_minutes=my_rand_duration, is_open=my_rand_is_open)

    #new_quiz.save()

    #all_quizzes = Quiz.objects.all()

    open_quizzes = Quiz.objects.filter(is_open=True).order_by('-quiz_order')

    returned_result = Quiz.objects.filter(is_open=True,
                                          quiz_title='Quiz01')[0]

    randFirst = randint(0,100)
    randSecond = randint(0,100)
    result_of_addition = randFirst + randSecond

    my_message = f"{randFirst} + {randSecond} is equal to {result_of_addition}"

    return render(request=request,
            template_name="main/login.html",
            context={"rand_first": randFirst,
                      "rand_second": randSecond,
                      "result_of_addition": result_of_addition,
                      "open_quizzes": open_quizzes,
                      "returned_result": returned_result})
