# Book Distribution System 📚

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![Django](https://img.shields.io/badge/django-4.2-brightgreen)](https://djangoproject.com)

A Django-based system for managing books with advanced search capabilities and user access control.

## 🎯 Project Overview
**Business Need:** Transition from error-prone spreadsheet tracking to an automated web solution for managing 50,000+ technical books across 15+ categories including Data Science, Python, and Business Analytics.

**Key Solutions:**
- Real-time expense tracking per category
- Secure CRUD operations for inventory management
- Automated reporting and data import/export
- Role-based access control for managers

  
## Features

- **Book Management**
  - Create/Edit books with detailed metadata
  - Categorization system with Category model
  - Track distribution expenses
  - Search across titles, authors, and subtitles
  - Paginated book listings

- **User Management**
  - Manager user group with special privileges
  - Authentication system integration
  - Role-based access control

- **Advanced Features**
  - Production-ready configuration
  - Unit test coverage for core functionality

## Models

### Book
- `title` - Book title (CharField)
- `subtitle` - Subtitle (CharField)
- `authors` - Author(s) (CharField)
- `publisher` - Publishing company (CharField)
- `published_date` - Publication date (DateField)
- `category` - Category relationship (ForeignKey)
- `distribution_expense` - Distribution cost (DecimalField)

### Category
- `name` - Category name (CharField)
-`description` - Category description (CharField) is can be null

## Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/Hcode7/Expense-Tracker-App.git
