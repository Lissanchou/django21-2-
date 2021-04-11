from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursus,Student, Call_of_roll
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView
from .forms import StudentForm
from django.urls import reverse

# Create your views here.
# def index(request):
  # return HttpResponse("Racine de lycee")

def detail(request,cursus_id):
 resp = 'result for cursus {}'.format(cursus_id)
 return HttpResponse(resp)

def index(request):
  result_list = Cursus.objects.order_by('name')
  #result_list = Cursus.objects.all()
  #

  template = loader.get_template('lycee/index.html')

  context = {
    'liste' : result_list,
  }
  #return HttpResponse(template.render(context,request))

  return render(request,'lycee/index.html',context)

def detail_student(request,student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {
    'liste' : result_list,
  }
  return render(request,'lycee/student/detail_student.html',context)

def detail_cursus(request,cursus_id):
  #result_list = Cursus.objects.all()
  result_list = Student.objects.filter(cursus=cursus_id).order_by('last_name')
  context = {
    'liste' : result_list,
  }
  return render(request,'lycee/detail_cursus.html',context)

def indexcalllist(request):
  #result_list = Cursus.objects.all()
  result_list = Call_of_roll.objects.order_by('date')

  context = {
    'liste' : result_list,
  }
  #return HttpResponse(template.render(context,request))
  return render(request,'lycee/call_of_roll.html',context)

def cursus_call_of_roll(request, cursus_id):
  #result_list = Cursus.objects.all()
  result_list = Call_of_roll.objects.filter(cursus=cursus_id).order_by('-date')

  context = {
    'liste' : result_list,
  }
  #return HttpResponse(template.render(context,request))
  return render(request,'lycee/call_of_roll.html',context)



class StudentCreateView(CreateView):
  #model
  model = Student

  #formulaire
  form_class = StudentForm

  #Template
  template_name = 'lycee/student/create.html'

  def get_success_url(self):
    return reverse('detail_student',args=(self.object.pk,))

class StudentUpdateView(UpdateView):
  #modele
  model = Student
  #formulaire
  #template
  template_name = 'lycee/student/edit.html'

  fields = ['first_name','birth_date','last_name','phone','email','comments','cursus']

  def get_success_url(self):
    return reverse('detail_student',args=(self.object.pk,))