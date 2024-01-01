from django.shortcuts import render
from django.core.paginator import Paginator

questions = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'Long lorem insum {i}',
    } for i in range(20)
]

def paginate(objects, page, per_page = 10):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)

def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'base.html', {'questions': paginate(questions, page)})

def question(request, question_id):
    item = questions[question_id]
    return render(request, 'question.html', {'questions': item})

def question2(request):
     return render(request, 'question.html')

def register(request):
    return render(request, 'register.html')

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def settings(request):
    return render(request, 'settings.html')

def tag(request):
    return render(request, 'tag.html')