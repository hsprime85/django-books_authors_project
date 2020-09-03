from django.urls import path
from . import views

urlpatterns = [
    # render routes
    path('', views.index),
    path('books/create', views.books_create),
    path('books/<int:book_id>', views.books),
    path('books/add_author', views.add_author),
    path('authors', views.authors_index),
    path('authors/create', views.authors_create),
    path('authors/<int:author_id>', views.authors),
    path('authors/add_book', views.add_book),

]
