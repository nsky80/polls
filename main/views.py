from django.shortcuts import render, HttpResponse, Http404, get_object_or_404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, template_name='main/index.html', context={"latest_question_list": latest_question_list})

def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'main/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)