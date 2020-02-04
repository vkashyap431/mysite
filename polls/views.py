from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.shortcuts import get_object_or_404

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={
		'latest_question_list':latest_question_list,
	}
	return render(request,'polls/index.html',context)
	#output=', '.join([q.question_test for q in latest_question_list] )
	#return HttpResponse(output)
def detail(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/details.html',{'question':question})
def result(request,question_id):
	response="you are looking at the results of question %s"
	return HttpResponse(response % question_id)
def vote(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, choice.DoesNotExist):
		return render(request,'polls/details.html',{'question':question,'error_message':"You didn't select choice."})
	else:
		selected_choice.vote+=1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:result',args=(question_id,)))


