from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Question, Tag, Profile
from .models import log_in, log_out, get_user

def paginate(objects, request, per_page = 10):
    paginator = Paginator(objects, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

def index(request):
    questions = Question.objects.get_questions_all()
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    context = {
        "page_obj": paginate(questions, request),
        "user_data": get_user(),
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, 'base.html', context)

def question(request, id):
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    try:
        question = Question.objects.get_by_id(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    answers = question.answers.all()
    context = {
        "question": question,
        "user_data": get_user(),
        "page_obj": paginate(answers, request),
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, 'question.html', context)

def signup(request):
    log_in()
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    context = {
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, "register.html", context)

def ask(request):
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    context = {
        "user_data": get_user(),
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, 'ask.html', context)

def login(request):
    log_in()
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    context = {
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, 'login.html', context)

def settings(request, id):
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    user = get_user()
    if user is None:
        return HttpResponseNotFound()
    context = {
        "user_data": user,
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, 'settings.html', context)

def tag(request, tag):
    try:
        questions = Question.objects.by_tag(tag)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    context = {
        "user_data": get_user(),
        "page_obj": paginate(questions, request),
        "tag": tag,
        "tags": TAGS,
        "members": MEMBERS,
    }
    return render(request, 'tag.html', context)

def logout(request):
    log_out()
    return HttpResponseRedirect('/')

def hot(request):
    questions = Question.objects.hot_questions()
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    context = {"page_obj": paginate(questions, request),
               "user_data": get_user(),
               "tags": TAGS,
               "members": MEMBERS,
               }
    return render(request, "hot.html", context)

def best_users(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

    questions = profile.questions.all()
    TAGS = Tag.objects.all()[:20]
    MEMBERS = Profile.objects.best()
    context = {"page_obj": paginate(questions, request),
               "user_data": get_user(),
               "tags": TAGS,
               "members": MEMBERS,
               }
    return render(request, "base.html", context)