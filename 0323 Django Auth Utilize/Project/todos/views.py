from django.shortcuts import render, redirect
from .form import TodoForms
from .models import Todo

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    print('index 함수 도착')
    form = TodoForms()
    todo_list = Todo.objects.all() # 모든 데이터 조회
    context = {
        'form': form,
        'todo_list': todo_list,
    }
    
    return render(request, 'todos/index.html', context)


def create(request):
    print('#'*30)
    print('create 함수 도착')
    print(f'request : {request}')
    print(request.method) # POST
    print(type(request.method)) # str
    print(request.POST)
    print('#'*30)

    if request.method == 'POST': # Todo 작성 요청
        # task = request.POST.get('task')
        form = TodoForms(request.POST)
        if form.is_valid(): # 유효성 검사 -> cleaned_data(dict) => clean_field
            form.save()
        
        return redirect('todos:index')
        

@login_required
def update(request, pk):
    print('update')
    print(pk)
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForms(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:index')



    else:
        form = TodoForms(instance=todo)

    context = {
        'form':form,
        'todo':todo,
    }
    return render(request, 'todos/update.html', context)


def delete(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        todo.delete()

    else:
        pass
    return redirect('todos:index')


def done(request, pk):
    # Auth가 있다면?
    todo = Todo.objects.get(pk=pk)
    todo.isCompleted = True
    todo.save()
    return redirect('todos:index')
