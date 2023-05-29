from django import forms
from .models import Board
class BoardForm(forms.Form):
    title = forms.CharField(label = "제목")
    contents = forms.CharField(label = "내용")
    start_date = forms.DateTimeField(label = "시작 시간")
    end_date = forms.DateTimeField(label = "종료 시간")
    price = forms.CharField(label="가격")
    class Meta:
        model = Board
        fields = ('title', 'contents', 'price', 'registered_date', 'start_date', 'end_date', 'writer')