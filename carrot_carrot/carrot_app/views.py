from django.shortcuts import render, redirect
from .forms import BoardForm
from .models import Board
from django.utils import timezone
from django.contrib.auth import logout as auth_logout
# Create your views here.
def home(request):
    return render(request, 'home.html')

def main(request):
    if request.user.is_authenticated:
        boards = Board.objects.all().order_by("-registered_date")
        return render(request, 'carrot.html',  {'boards': boards})
    else:
        return redirect('home')

def logout(request):
    auth_logout(request)
    return redirect('login')

def write(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    elif request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user = request.user
            new_board = Board(
                title = form.cleaned_data['title'],
                contents = form.cleaned_data['contents'],
                writer = user,
                price = form.cleaned_data['price'],
                end_date = form.cleaned_data['end_date'],
                start_date = form.cleaned_data['start_date'],
                registered_date = timezone.now()
            )
            new_board.save()
            return redirect('main')
    else:
        form = BoardForm()
    return render(request, 'write.html', {'form' :form})