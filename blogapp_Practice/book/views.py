from django.shortcuts import render, redirect
from .models import Tutorial
from .forms import BookForm

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def book_desc(request):
    return render(request, 'tutorial_list.html') 
def list1(request):
    return render(request, 'list1.html') 
def list2(request):
    return render(request, 'list2.html') 
def list3(request):
    return render(request, 'list3.html') 
def about(request):
    return render(request, 'about.html') 
def contact(request):
    return render(request, 'contact.html') 

def book_list(request):
    books = Tutorial.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = Tutorial.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html')

def book_update(request, pk):
    book = Tutorial.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': book})

def book_delete(request, pk):
    book = Tutorial.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')
