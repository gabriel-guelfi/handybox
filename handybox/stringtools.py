def toCamelCase(s):
    parts = s.replace('-', ' ').replace('_', ' ').split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

def camelToSnake(name):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def toSnake(text):
    import re
    return re.sub(r'\W+', '_', text).strip('_').lower()

def slugify(text):
    import re
    return re.sub(r'\W+', '-', text).strip('-').lower()
