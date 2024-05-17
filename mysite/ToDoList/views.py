from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from .forms import TodoForm
from .models import ToDo

def index(request):
    todo_list = ToDo.objects.order_by('-date')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
    else:
        form = TodoForm()
    context = {"todos":todo_list,
               'form':form
               }
    return render(request,'ToDoList/index.html',context)



def complete(request,pk):
    todo = get_object_or_404(ToDo,pk=pk)
    todo.check_do =True
    todo.save()
    return redirect('ToDoList:index')

def delete_todo(request,pk):
    todo = get_object_or_404(ToDo,pk=pk)
    todo.delete()
    return redirect('ToDoList:index')