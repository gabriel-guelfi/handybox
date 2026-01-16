import unicodedata

def toCamelCase(s):
    parts = s.replace('-', ' ').replace('_', ' ').split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

def camelToSnake(name):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def toSnake(text):
    import re
    return re.sub(r'\W+', '_', text).strip('_').lower()

def remove_accents(text):
        return ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )

def slugify(text):
    import re
    return re.sub(r'\W+', '-', text).strip('-').lower()
