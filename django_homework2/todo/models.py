from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100) # 할 일 제목
    description = models.TextField() #  할 일 상세 내용
    start_date = models.DateTimeField() #  시작 날짝
    end_date = models.DateTimeField() #  마감 날짜
    is_completed = models.BooleanField(default=False)   # 완료 여부
    created_at = models.DateTimeField(auto_now_add=True)    # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)    # 수정 시간

    def __str__(self):
        return self.title # 리스트 에서 제목만 보이게 설정
