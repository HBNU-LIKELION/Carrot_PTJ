from django.db import models
from User.models import User


class Board(models.Model):
    state = models.CharField(max_length=10, default = "구인중", verbose_name="상태")
    title = models.CharField(max_length=64, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    price = models.CharField(max_length=20,  verbose_name="가격")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name = "등록 시간")
    start_date = models.DateTimeField(verbose_name = "시작 시간")
    end_date = models.DateTimeField(verbose_name = "종료 시간")
    writer = models.ForeignKey(User, verbose_name = "작성자", on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "community_board"
        verbose_name = "게시물"
        verbose_name_plural = "게시물"