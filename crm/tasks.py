from celery import shared_task
from datetime import datetime
import requests
import json

@shared_task
def generate_crm_report():
    # GraphQL query for customers, orders, revenue
    query = """
    query {
        customers { id }
        orders { id totalAmount }
    }
    """

    url = "http://localhost:8000/graphql/"  # Adjust if needed
    response = requests.post(url, json={"query": query})
    data = response.json().get("data", {})

    total_customers = len(data.get("customers", []))
    orders = data.get("orders", [])
    total_orders = len(orders)
    total_revenue = sum([order.get("totalAmount", 0) for order in orders])

    log_message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Report: {total_customers} customers, {total_orders} orders, {total_revenue} revenue\n"

    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(log_message)

    return log_message

