import datetime
import requests

def log_crm_heartbeat():
    """
    Logs a heartbeat every 5 minutes to /tmp/crm_heartbeat_log.txt
    and optionally queries the GraphQL hello endpoint.
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive"

    try:
        # Optional GraphQL hello query
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            hello_msg = data.get("data", {}).get("hello", "No hello response")
            message += f" | GraphQL says: {hello_msg}"
        else:
            message += " | GraphQL unreachable"
    except Exception as e:
        message += f" | GraphQL error: {e}"

    # Append to log file
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(message + "\n")

    print(message)
