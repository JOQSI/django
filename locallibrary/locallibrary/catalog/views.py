from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
from django.views.generic import ListView
from .models import Author


from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_visits': num_visits},  # num_visits appended
    )



class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorDetailView(generic.DetailView):
    model = Author

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    template_name = 'catalog/author_list.html'
    context_object_name = 'author_list'



class LoanedBooksListView(PermissionRequiredMixin, ListView):
    """
    Generic class-based view listing all books on loan with their borrowers.
    """
    model = BookInstance
    template_name = 'catalog/loaned_books_list.html'  # Укажите путь к вашему шаблону
    context_object_name = 'loaned_books'
    permission_required = 'yourapp.can_mark_returned'  # Укажите правильное разрешение

    def get_queryset(self):
        return BookInstance.objects.filter(borrower__isnull=False).select_related('book', 'borrower')