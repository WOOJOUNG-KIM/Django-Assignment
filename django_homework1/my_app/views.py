from django.shortcuts import render
from django.http import Http404

# 가짜 데이터(fake_db) 사용 (임시 데이터)
user_db = {
    1: {'이름': '김우정', '나이': 28, '이메일': 'woojoong@email.com','취미':'운동','거주지':'제주특별자치도 제주시 연동'},
    2: {"이름": "박민수", "나이": 30, "이메일": "minsu@example.com"},
    3: {"이름": "이하나", "나이": 28, "이메일": "hana@example.com"},
}

# 유저 리스트 페이지
def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in user_db.items()]
    return render(request, 'user_list.html',{'data': names})

# 유저 상세 정보 페이지
def user_info(request, user_id):
    if user_id not in user_db:
        raise Http404('유저가 없습니다.')
    info = user_db[user_id]
    return render(request, 'user_info.html', {'data': info})
