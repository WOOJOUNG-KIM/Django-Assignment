from django.urls import path
from . import views # 같은 폴더에 있는 views.py 파일에서 함수 가져오기

urlpatterns = [
    path('', views.user_list, name='user_list'), # /users/ → user_list() 함수 실행
    path('<int:user_id>/', views.user_info, name='user_info'), # /users/1/ → user_info() 함수 실행
]