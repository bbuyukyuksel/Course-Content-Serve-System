# Django based Course Content Serve System

### Description

- This project aims to serve your own local course content as like Udacity, Coursera websites.
- You can track whether you have watched your course contents.
___
### Installation
- Requirement Packages
  - Django
  - Markdown

- Usage
  - python ```manage.py``` makemigrations
  - python ```manage.py``` migrate
  - python ```manage.py``` createsuperuser

### Features
- Can serve local video content.
- Can serve local markdown (.md or .markdown) file as HTML.

### Code Hilite CSS Generate

for [reference](https://www.devdungeon.com/content/convert-markdown-html-python)

```bash
python -m pip install markdown
python -m pip install pygments
```

```python
import markdown

md_text = """
​```python hl_lines="1 3"
# some Python code
hi = 'Hello'
print(hi)
​```
"""
html = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])
print(html)
```

```bash
pygmentize -L
pygmentize -S default -f html -a .codehilite > static/assets/css/codehilite.css
```

```html
<link rel="stylesheet" href="/static/css/codehilite.css"/>
```



### Contributors

- Burak BÜYÜKYÜKSEL *(buyukyukselburak@gmail.com)*
