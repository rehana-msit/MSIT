from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import Question,Book,Sample


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def latest_books(request):
    if request.method=="POST":
        f = Sample(request.POST)
        fn=request.POST.get('fname','')
        ln=request.POST.get('lname','')
        f2 = Sample(fname=fn,lname=ln)
        f2.save()
        return HttpResponse("Success")
    else:
        return HttpResponse("Failure")

def load(request):
    #return HttpResponse("Welcome Django")
    return render(request,'welcome.html')

def sample(request):
    return render(request,'polls/Sample.html')




