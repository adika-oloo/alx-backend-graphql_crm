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
INSTALLED_APPS = [
    # other apps...
    "django_crontab",
]

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]
CRONJOBS = [
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]
