# CRM Celery & Scheduled Tasks Setup

This guide explains how to set up and run Celery with Django for scheduled CRM reporting tasks.

---

## Prerequisites

- Python **3.8+**
- Django project already set up
- Redis installed and running (used as the Celery broker)
- Pip and virtualenv available

---

## 1. Install Dependencies

Make sure you have all dependencies installed:

```bash
pip install -r requirements.txt
requirements.txt
Django>=3.2
celery>=5.2
django-celery-beat>=2.5
requests

Install and Start Redis
sudo apt-get update
sudo apt-get install redis-server
sudo systemctl enable redis-server
sudo systemctl start redis-server

Apply Database Migrations
## python manage.py migrate

Configure Celery
from .celery import app as celery_app

__all__ = ('celery_app',)


