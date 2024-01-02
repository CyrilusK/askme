from django.db import models
from random import choice, randint
from faker import Faker


# Create your models here.
class User:
    def __init__(self, id, avatar, name):
        self.id = id
        self.avatar = avatar
        self.name = name

class Question:
    def __init__(self, id, author, title, text, num_likes, num_answers, tags):
        self.id = id
        self.author = author
        self.title = title
        self.text = text
        self.num_likes = num_likes
        self.num_answers = num_answers
        self.tags = tags

class Answer:
    def __init__(self, id, author, question, text, correct, num_likes):
        self.id = id
        self.author = author
        self.question = question
        self.text = text
        self.correct = correct
        self.num_likes = num_likes

class authorized:
    status = True

def logout():
    authorized.status = False

def login():
    authorized.status = True

randomData = Faker()

NUM_USERS = 6
NUM_QUESTIONS = 50
NUM_ANSWERS = 30
PICTURES = ["img/user1.jpeg", "img/user2.jpeg", "img/user3.png", "img/user4.png", "img/user5.jpeg",
            "img/user6.jpeg", "img/user7.jpeg"]
TAGS = [randomData.word() for _ in range(7)]
MEMBERS = [randomData.name() for _ in range(7)]
USERS = [User(i, choice(PICTURES), randomData.name()) for i in range(NUM_USERS)]
QUESTIONS = [Question(i, choice(USERS), f'Question{i}', randomData.text(), randint(-100, 100),
                      0, [choice(TAGS) for _ in range(randint(1,6))])
             for i in range(NUM_QUESTIONS)]
ANSWERS = [Answer(i, choice(USERS), choice(QUESTIONS), randomData.text(), choice([True, False]),
                  randint(-50, 100)) for i in range(NUM_ANSWERS)]

def get_questions():
    return QUESTIONS

def get_question(id):
    for question in QUESTIONS:
        if question.id == id:
            return question

def get_answers(question_id):
    res = []
    for answer in ANSWERS:
        if answer.question.id == question_id:
            res.append(answer)
            print(res)
    return res

for i in range(NUM_QUESTIONS):
    QUESTIONS[i].num_answers = len(get_answers(QUESTIONS[i].id))

def get_user(status):
    if status is False:
        return None
    elif status is True:
        return USERS[randint(0, NUM_USERS - 1)]
    status = int(status)
    if status < 0 or status >= len(USERS):
        return None
    return USERS[int(status)]

def question_by_tag(tag):
    res = []
    for question in QUESTIONS:
        if tag == question.tags:
            res.append(question)
    return res