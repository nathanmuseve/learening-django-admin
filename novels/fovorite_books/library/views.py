from django.shortcuts import render,get_list_or_404
from .models import Book

# Create your views here.
# def main(request): #main/index page
#   return(request,'main.html')

def book_list(request):
  books = Book.objects.all()
  context = {
    'books': books,
  }
  return render(request, 'book_list.html', context)


def book_detail(request):
  books = Book.objects.all()
  context = {
    'books': books,
  }
  return render(request, 'book_detail.html', context)

def book_detail_pk(request, pk):
  book = get_list_or_404(Book, pk=pk)
  return render(request, 'book_detail.html', {'book' : book})