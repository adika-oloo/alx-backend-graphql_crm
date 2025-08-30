INSTALLED_APPS = [
    # Django defaults...
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "graphene_django",
    "django_crontab",   # ✅ Required for cron jobs
    # Your apps
    "crm",
]
CRONJOBS = [
    # Runs every minute for testing
    ('* * * * *', 'crm.cron.order_reminder', '>> /tmp/order_reminder.log 2>&1'),
]
