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
```bash
pygmentize -L
pygmentize -S default -f html -a .codehilite > static/assets/css/codehilite.css
```

### Contributors
- Burak BÜYÜKYÜKSEL *(buyukyukselburak@gmail.com)*
