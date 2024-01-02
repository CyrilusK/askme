from django.shortcuts import render
from django.core.paginator import Paginator
from .models import get_answers, get_question, get_questions, get_user, question_by_tag
from .models import authorized, TAGS, MEMBERS

def paginate(objects, request, per_page = 10):
    paginator = Paginator(objects, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

def index(request):
    questions = get_questions()
    context = {
        "page_obj": paginate(questions, request),
        "user_data": get_user(authorized.status),
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, 'base.html', context)

def question(request, id):
    question = get_question(id)
    context = {
        "question": question,
        "user_data": get_user(authorized.status),
        "answers": get_answers(id),
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, 'question.html', context)

def register(request):
    return render(request, 'register.html')

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def settings(request, id):
    user = get_user(id)
    context = {
        "user_data": user,
        "user": None,
        "tags": TAGS,
        "best_members": MEMBERS,
    }
    return render(request, 'settings.html', context)


def tag(request):
    context = {
        "page_obj": paginate(question_by_tag(tag), request),
        "tag": tag,
        "tags": TAGS,
        "best_members": MEMBERS,
    }
    return render(request, 'tag.html', context)
