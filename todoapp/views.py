from django.shortcuts import render, redirect

from todoapp.forms import TodoForm
from todoapp.models import Todo


# Create your views here.
def mainpage(request):
    form = TodoForm()
    todos = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainpage')

    return render(request,'mainpage.html',{'form':form,'todos':todos})