from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('', views.index, name='index'),
    re_path('books', views.BookListView.as_view(), name='books'),
    re_path('book/(<int:pk>\)', views.BookDetailView.as_view(), name='book-detail'),
    re_path('authors/', views.AuthorListView.as_view(), name = 'author'),
    re_path('authors/(<int:pk>\)', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path('mybooks/', views.LoanedBooksListView.as_view(), name='my-borrowed'),

]

