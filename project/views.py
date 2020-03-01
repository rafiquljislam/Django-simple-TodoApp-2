from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    form = TodosForm
    todos = Todos.objects.all()

    context={
        'form':form,
        'todos':todos
    }
    return render(request,'project/home.html',context)

def add(request):
    text = request.POST['content']
    a=Todos(text=text)
    a.save()
    return redirect('home')
def deleta(request,num):
    text = Todos.objects.filter(id=num).delete()
    return redirect('home')
def update(request,num):
    text = Todos.objects.get(id=num)
    form = TodosForm(instance=text)

    if request.method=="POST":
        form = TodosForm(request.POST,instance=text)
        if form.is_valid():
            form.save()
            return redirect('home')

    content = {
        'form':form,
    }
    return render(request,'project/update.html',content)
