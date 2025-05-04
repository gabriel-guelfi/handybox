def camelToSnake(name):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def slugify(text):
    import re
    return re.sub(r'\W+', '-', text).strip('-').lower()
