from django.shortcuts import render


TODO_LIST = [
    {'id': 1, 'title': '첫 번째 할 일'},
    {'id': 2, 'title': '두 번째 할 일'},
    {'id': 3, 'title': '세 번째 할 일'},
]

def todo_list(request):
    context = {'data': TODO_LIST}
    return render(request, 'todo_list.html', context)

def todo_info(request, todo_id):
    todo_item = next((item for item in TODO_LIST if item['id'] == todo_id), None)
    context = {'todo':todo_item}
    return render(request, 'todo_list.html', context)
