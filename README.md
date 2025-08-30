# alx-backend-graphql_crm

A Django-based CRM system with **GraphQL API**, **scheduled cron jobs**, and **Celery tasks** for automation and reporting.

This project demonstrates:

- GraphQL queries and mutations for CRM operations.
- Cron jobs to automatically restock low-stock products.
- Celery Beat tasks to generate weekly CRM reports.


 Features

1. GraphQL API**
   - Query products, customers, and orders.
   - Mutation to update low-stock products.

2. Cron Jobs (django-crontab)**
   - Runs every 12 hours.
   - Executes `UpdateLowStockProducts` mutation.
   - Logs updates to `/tmp/low_stock_updates_log.txt`.

3. Celery + Celery Beat**
   - Weekly CRM report generation.
   - Summarizes total customers, total orders, and total revenue.
   - Logs reports to `/tmp/crm_report_log.txt`.


Setup Instructions

 1. Clone Repository
```bash
git clone https://github.com/<your-username>/alx-backend-graphql_crm.git
cd alx-backend-graphql_crm
