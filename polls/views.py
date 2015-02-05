from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django import forms

from polls.models import Question, Contact


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class ContactForm(forms.Form):
    nom = forms.CharField(label='Nom',max_length=100)
    miss = forms.CharField(label='Missatge',widget=forms.Textarea)
    email = forms.EmailField()



def get_name(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
	    mod = Contact()
            mod.nom = form.cleaned_data['nom']
            mod.msg = form.cleaned_data['miss']
            mod.eml = form.cleaned_data['email']
            mod.save()
            return HttpResponseRedirect('/polls/result/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def result(request):
    return render(request, 'result.html')
