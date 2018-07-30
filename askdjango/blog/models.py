from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요. 최대 100자 내외',
                             choices=(
                                 ('제목1', '제목1 레이블'),
                                 ('제목2', '제목2 레이블'),
                                 ('제목3', '제목3 레이블'),
                             ))  # 길이 제한이 있는 문자열
    content = models.TextField()  # 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
