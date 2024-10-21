# Asset Management System

Django-based web application for managing asset lending and returns. 
User can select employees, assign assets, and keep track of asset availability. 
If an asset is unavailable, the system checks if the asset is borrowed by the current employee and allows them to return it, or else informs them that the asset is unavailable.

## Features

- Manage employees and assets.
- Lend and return assets based on availability.

## Prerequisites

- Python 3.8+
- Django 4.1+

## Getting Started

```bash
git clone https://github.com/yesminemn/Asset_Management
cd haivo

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py add_test_data
python manage.py runserver

