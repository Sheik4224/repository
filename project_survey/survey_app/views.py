from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question,Answer

def func(request):
        if request.method=='POST':
            question_id=request.POST.get('question_id')
            title=request.POST.get('title')
            question=request.POST.get('question')
            result=Question(question_id=question_id,title=title,question=question)
            result.save()
            return render (request,'message.html')
        return render (request,'home.html')   

def func1(request,question_id):
        if request.method=='POST':
            use=Question.objects.get(question_id=question_id)
            new_answer=request.POST.get("answer")
            result=Answer(surveyid=use,answer=new_answer)
            result.save()
            return render(request,'message.html')
        return render(request,'answer.html')

def func2(request):
    if request.method=='GET':
        show_all=Question.objects.all()
        return render(request,'get_ques.html',{'show_question':show_all})
def get_answer(request):
     if request.method=='GET':
        use=Answer.objects.all()
        return render(request,'get_ans.html',{'show_answer':use})
     
def func3(request,surveyid):
    survey=Answer.objects.get(surveyid=surveyid)
    if request.method== "POST":
        new_answer=request.POST.get("answer")
        survey.answer=new_answer
        survey.save()
        return render(request,'message.html')
    return render(request,'update.html')

def delete(request, surveyid_id):
        answer = Answer.objects.get(surveyid_id=surveyid_id)
        answer.delete()
        return render (request,'message.html')

def del_ques(request,question_id):
     question=Question.objects.get(question_id=question_id)
     question.delete()
     return render (request,'message.html') 