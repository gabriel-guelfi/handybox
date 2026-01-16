# handybox

*A lightweight toolbox of handy Python helper functions*

[![PyPI version](https://badge.fury.io/py/handybox.svg)](https://pypi.org/project/handybox/)

## 📦 Installation
Install using pip:

```bash
pip install handybox
```

## 📘 Description
**handybox** is a compact Python utility library that offers a curated set of useful helper functions for everyday development. It avoids bloat, has no dependencies, and is built for clarity and speed.

## 🔧 Features

### 🔤 String Utilities
- `camelToSnake(str)` — Converts CamelCase strings to snake_case.
- `slugify(str)` — Converts a string into a URL-friendly slug.
- `removeAccents(str)` —  Removes accents from characters in a string.

```python
from handybox import camelToSnake, slugify

camelToSnake("MyVariableName")   # "my_variable_name"
slugify("Hello, World!")           # "hello-world"
removeAccents("Café")              # "Cafe"
```

### 📅 Date Utilities
- `nowiso()` — Returns the current datetime in ISO format.
- `todayStr()` — Returns today’s date as a string (YYYY-MM-DD).

```python
from handybox import nowiso, todayStr

nowiso()     # "2025-05-01T17:45:00.123456"
todayStr()   # "2025-05-01"
```

### 🧰 Miscelaneous Utilities
- `uniqid(prefix="")` — Generates a unique ID string, similar to PHP’s `uniqid()`.

```python
from handybox import uniqid

uniqid()             # "f5e3a9c0b1d2"
uniqid("user")      # "user-f5e3a9c0b1d2"
```

## 🚀 Why handybox?
- ✅ Lightweight and dependency-free  
- ✅ Easy to install and use  
- ✅ Common utilities in one place  
- ✅ Minimal API surface  
- ✅ Built for real-world usage  

## 📄 License
MIT License  
© 2025 Gabriel Valentoni Guelfi

## 👤 Author
**Gabriel Valentoni Guelfi**  
📧 [gabriel.valguelfi@gmail.com](mailto:gabriel.valguelfi@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/gabriel-valentoni-guelfi/)