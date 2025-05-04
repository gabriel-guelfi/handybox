from datetime import datetime

def nowiso():
    return datetime.utcnow().isoformat()

def todayStr():
    return datetime.utcnow().strftime('%Y-%m-%d')
