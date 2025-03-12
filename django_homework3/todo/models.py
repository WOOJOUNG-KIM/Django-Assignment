from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100) # 할 일 제목
    complete = models.BooleanField(default=False) # 완료 여부

    def __str__(self):
        return self.title