from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        "all_books": Books.objects.all(),
        "all_authors": Authors.objects.all(),
    }
    return render(request, 'index.html', context)


def books_create(request):
    print(request.POST)
    # create a book
    Books.objects.create(
        title=request.POST['title'],
        describe=request.POST['describe']
    )

    return redirect('/')


def books(request, book_id):
    print(request.POST)
    context = {
        "book": Books.objects.get(id=book_id),
        "all_authors": Authors.objects.all(),
    }
    return render(request, 'book.html', context)


def add_author(request):
    author = Author.objects.get(id=request.POST['author_id'])
    book = Books.objects.get(id=request.POST['book_id'])
    book.authors.add(author)
    return redirect(f"/books/{request.POST['book_id']}")


def authors_index(request):
    print(request.POST)
    context = {
        "all_authors": Authors.objects.all(),
        "all_books": Books.objects.all(),
    }
    return render(request, 'author.html', context)


def authors_create(request):
    print(request.POST)
    # create an author
    Authors.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )

    return redirect('/authors')


def authors(request, author_id):
    print(request.POST)
    context = {
        "author": Authors.objects.get(id=author_id),
        "all_books": Books.objects.all(),
    }
    return render(request, 'author.html', context)


def add_book(request):
    author = Authors.objects.get(id=request.POST['author_id'])
    book = Books.objects.get(id=request.POST["book_id"])
    book.authors.add(book)

    return redirect(f"/authors/{request.POST['author_id']}")
