from django.urls import path
from . import views

urlpatterns = [
    # urls of categories
    path('categories/', views.categories_view, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/<int:id>/edit/', views.update_category, name='update_category'),
    path('categories/<int:id>/delete/', views.delete_category, name='delete_category'),

    # urls of books
    path('', views.books_view, name='books'),
    path('books/categories/', views.add_book, name='add_book'),
    path('books/<int:id>/edit/', views.update_book, name='update_book'),
    path('books/<int:id>/delete/', views.delete_book, name='delete_book'),

    # import data
    path('import-data/', views.import_data, name='import'),

    # report of books
    path('report/', views.report_book, name='report')

]