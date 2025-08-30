from datetime import datetime

def log_crm_heartbeat():
    """Logs a heartbeat timestamp to /tmp/crm_heartbeat_log.txt"""
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"CRM heartbeat at {datetime.now()}\n")


