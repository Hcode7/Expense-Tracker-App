from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Book
from .forms import CategoryForm, BookForm, ImportFile
import csv
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64

# Create your views here.

# CRUD operation of Categories

def categories_view(request):
    page_num = request.GET.get('page')
    search = request.GET.get('search')
    if search:
        categories = Category.objects.filter(name=search)
    else:
        categories = Category.objects.all()
    user_manager = request.user.groups.filter(name='Manager').exists()
    paginator = Paginator(categories, 4)
    page_obj = Paginator.get_page(paginator, page_num)
    context = {
        'categories' : categories,
        'page_obj' : page_obj,
        'user_manager' : user_manager
    }
    return render(request, 'pages/category_list.html', context)

@login_required
def add_category(request):
    if not request.user.is_staff and not request.user.groups.filter(name='Manager').exists():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('books')
    
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'pages/add_record.html', {'form' : form, 'categories' : categories})

@login_required
def update_category(request, id):
    if not request.user.is_staff and not request.user.groups.filter(name='Manager').exists():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('books')
    
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm(instance=category)
    return render(request, 'pages/update_category.html', {'form' : form})

@login_required
def delete_category(request, id):
    if not request.user.is_staff and not request.user.groups.filter(name='Manager').exists():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('books')
    
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('books')

# CRUD operation of Books

def books_view(request):
    search = request.GET.get('search')
    page_number = request.GET.get('page')
    user_manager = request.user.groups.filter(name='Manager').exists()
    if search:
        books = Book.objects.filter(title__icontains=search, authors__icontains=search, subtitle__icontains=search)
    else:
        books = Book.objects.all().order_by('-published_date')[:10]
    
    paginator = Paginator(books, 4)
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'books' : books,
        'page_obj' : page_obj,
        'user_manager' : user_manager,
    }
    return render(request, 'pages/book_list.html', context)

@login_required
def add_book(request):
    if not request.user.is_staff and not request.user.groups.filter(name='Manager').exists():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('books')
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'pages/add_book.html', {'form' : form})

@login_required
def update_book(request, id):
    if not request.user.is_staff and not request.user.groups.filter(name='Manager').exists():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('books')
    
    book = get_object_or_404(Book, id=id)
    book = request.GET.get('book')
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
    else:
        form = BookForm(instance=book)
    return render(request, 'pages/update_book.html', {'form' : form})

@login_required
def delete_book(request, id):
    if not request.user.is_staff and not request.user.groups.filter(name='Manager').exists():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('books')
    
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books')

@login_required
def import_data(request):
    if not request.user.is_staff:
        messages.error(request, "You don't have permission to access this page.")
        return redirect('books')
    
    if request.method == 'POST':
        form = ImportFile(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            decode_file = file.read().decode('utf-8')
            reader = csv.DictReader(decode_file.splitlines())
            next(reader)

            for row in reader:
                category_row = row['category']
                category, created = Category.objects.get_or_create(name=category_row)
                Book.objects.create(
                    book_id=row['id'],
                    title=row['title'],
                    subtitle=row['subtitle'],
                    authors=row['authors'],
                    publisher=row['publisher'],
                    published_date=row['published_date'],
                    category=category,
                    distribution_expense=row['distribution_expense']
                )
    else:
        form = ImportFile()
    return render(request, 'pages/import_data.html', {'form' : form})


def report_book(request):
    
    data = (
        Book.objects.values('category__name').annotate(total_expenses=Sum('distribution_expense'))
    )

    categories = [item['category__name'] for item in data]
    expenses = [item['total_expenses'] for item in data]

    plt.figure(figsize=(16, 5))
    plt.bar(categories, expenses, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Expense')
    plt.title('Book Distribution Expenses by Category')
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_data = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'pages/report_chart.html', {'chart_data': chart_data})
