import uuid

def uniqid(prefix=''):
    return f"{f'{prefix}-' if bool(prefix) else ''}{uuid.uuid4().hex[:13]}"
