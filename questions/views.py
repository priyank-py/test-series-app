from django.shortcuts import render, get_object_or_404
from .models import QuestionPaper


def home(request):
    return render(request, 'questions/index.html')

def about(request):
    return render(request, 'questions/about.html')

def contact_us(request):
    return render(request, 'questions/contact_us.html')

def question_paper(request, pk):
    question = get_object_or_404(QuestionPaper, id=pk)

    context = {
        'question': question,
    }
    return render(request, 'questions/question_paper.html', context)
