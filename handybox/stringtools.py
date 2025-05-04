def camelToSnake(name):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def toSnake(text):
    import re
    return re.sub(r'\W+', '_', text).strip('_').lower()

def slugify(text):
    import re
    return re.sub(r'\W+', '-', text).strip('-').lower()
