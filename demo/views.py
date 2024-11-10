from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

  return render(request,'hello.html',{'name1':'ramuuuuuuuukkkuuu'})
def add(request):
  first=int(request.POST['input1'])
  second=int(request.POST['input2'])
  result=first+second
  return render(request,'result.html',{'result':result})
