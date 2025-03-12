from django.http import Http404
from django.shortcuts import render
from todo.models import Todo

# 전체 Todo 목록 조회
def todo_list(request):
    todos = Todo.objects.all().values_list('id','title')
    result = [{'id': todo[0], 'title': todo[1]} for todo in todos]

    return render(request, 'todo_list.html',{'data': result})

# 개별 Todo 상세 조회
def todo_info(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        info = {
            'title': todo.title,
            'description': todo.description,
            'start_date': todo.end_date,
            'is_completed': todo.is_completed
        }
        return render(request, 'todo_info.html', {'data':info})
    except Todo.DoesNotExist:
        raise Http404('Todo does not exist')
