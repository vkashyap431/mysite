from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={
		'latest_question_list':latest_question_list,
	}
	return render(request,'polls/index.html',context)
	#output=', '.join([q.question_test for q in latest_question_list] )
	#return HttpResponse(output)
def details(request,question_id):
	return HttpResponse("you are loking at question %s. " % question_id)
def results(request,question_id):
	response="you are looking at the results of question %s"
	return HttpResponse(response % question_id)
def vote(request, question_id):
	return HttpResponse("you are voting on question %s. " % question_id)
def dummy1(request):
	pass
