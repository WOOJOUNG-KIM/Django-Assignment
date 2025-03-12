from django.urls import path
from todo.views import todo_list, todo_info

urlpatterns = [
    path('', todo_list, name='todo_list'), # 전체 목록 페이지
    path('<int:todo_id>/', todo_info, name='todo_info') # 개별 상세 페이지
]