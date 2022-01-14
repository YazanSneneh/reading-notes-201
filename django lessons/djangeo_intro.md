# Django at a glance
- this is django at a glance, for a [tutorial visit thia website](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) and for [detailed documentation tutorial visit this site](https://docs.djangoproject.com/en/4.0/topics/)
- it was designed to make common web development tasks fast and easy.


### Design a model
- it comes with an object-relational mapper in which I describe database layout in Python code.
- The [data-model](https://docs.djangoproject.com/en/4.0/topics/db/models/) syntax offers many rich ways of representing models.
- **Note: when i create a model i dont have to provide an id because it will be handled**
- example:
```python

from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name
        
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

```

#### installing a model
```python
$ python manage.py makemigrations
$ python manage.py migrate
```
- The **makemigrations** command looks at all your available models and creates migrations for whichever tables don’t already exist.
-  **migrate** runs the migrations and creates tables in your database, as well as optionally providing much richer schema control.

#### the database API and how to interact with db
- allow me to interact with database models.
- how to user it?
  1. import my models `from news.models import Article, Reporter`
  2. create object from model : ` report = Reporter(full_name='John Smith')`
  3. to save my object into db i have to call .save() method on my object:   `report.save()`
  4. query the list of objects in that table:  ModelName.objects.all()
  ```python
  Reporter.objects.all()
  <QuerySet [<Reporter: John Smith>]>.  # result
  ``
  5. get object with specific id or value :  ModelName.objects.get(columnName= Value)
 ```python
 Reporter.objects.get(id=1)
 <QuerySet [<Reporter: John Smith>]>.   # result
 ```
 6. starts with a value:
 ```python
 Reporter.objects.get(full_name__startswith='John')
 ```
 7. contains a specefic value: 
```python
 Reporter.objects.get(full_name__startswith='John')
 ```
 
8. delete an object : objectName.delete()

## dynamic admin interface
- when models are defined, Django can automatically create a professional, production ready [administrative interface](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
- admin interface is website that lets authenticated users add, change and delete objects.
- The only step required is to register your model in the admin site.
- example: 
```python
website/news/model.py
from django.db import models

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

website/news/admin.py
from django.contrib import admin

from . import models

admin.site.register(models.Article)    # registering model to admin website

```
- The philosophy here is that the website is edited by a staff, or a client, or maybe just developer – and developer don’t want to have to deal with creating backend interfaces only to manage content.
- One typical **workflow** in creating Django apps is to create models and get the admin sites up and running as fast as possible, so your staff (or clients) can start populating data. Then, develop the way data is presented to the public.

## Design URLs
- A clean, elegant URL scheme is an important detail in a high-quality web application.
- Django encourages beautiful URL design and doesn’t put any cruft in URLs, like .php or .asp.

#### how to create urls
- To design URLs for an app, **create a Python module called a URLconf**.
- It's a table of contents for the app, it contains a **mapping** between **URL patterns** and Python **callback functions**.
- URLconfs serve to decouple URLs from Python code.
- Example of **URLconf** for the Reporter/Article example above:

```python
website/news/urls.py

from django.urls import path

from . import views

urlpatterns = [ 
 path('articles/<int:year>/', views.year_archive),
 path('articles/<int:year>/<int:month>/', views.month_archive),
path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
```
#### explination
- The code above maps **URL paths** to Python **callback functions (“views”)**.
- The path strings use parameter tags to **capture values from the URLs**.
- When a user requests a page, Django runs through each path, in order, and stops at the first one that matches the requested URL. (If none of them matches, Django calls a special-case 404 view.)**This is blazingly.
    - fast, because the paths are compiled into regular expressions at load time**.
- Once one of the URL patterns matches, Django calls the given view, which is a Python function. 
    - Each view gets passed a request object – which contains request metadata – and the values captured in the pattern.
- Example:
```python
# if a user requested the URL “/articles/2005/05/39323/”, Django would call the function:
  news.views.article_detail(request, year=2005, month=5, pk=39323)
```

## Write your views
- Each view is responsible for doing one of two things:
    - Returning an **HttpResponse** object **containing the content for the requested page**, or **raising an exception such as Http404**.
- A view **retrieves** data according to the parameters.
- **loads** a template and **renders the template with the retrieved data**.
- Here’s an example view for year_archive from above:
```python
website/news/view.py
from django.shortcuts import render
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year).  
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
```

## Design your templates
- The code in the **write your views** loads the **news/year_archive.html template**.
- Mechanisim of getting template:
    - Django has a template search path.
    - which allows you to minimize redundancy among templates.
    - In your Django settings.
    - specify a list of directories to check for templates with DIRS.
    - If a template doesn’t exist in the first directory, it checks the second, and so on.
- example of how the code will look if **news/year_archive.html** is found:
```python
{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}
```
- Explination:
    - Variables are surrounded by double-curly braces. **{{ article.headline }}** means “Output the value of the article’s headline attribute.
      - dots aren’t used only for attribute lookup. They also can do dictionary-key lookup, index lookup and function calls.
    - Note **{{ article.pub_date|date:"F j, Y" }}** uses a **Unix-style “pipe”** (the “|” character).
        - This is called a **template filter**, and **it’s a way to filter the value of a variable**.
            - In this case, the date filter formats a Python datetime object in the given format (as found in PHP’s date function).

####Inheritance in Templates
- Django uses the concept of “template inheritance”.
- That’s what the **{% extends "base.html" %} does**.
    - It means “First load the template called ‘base’, which has defined a bunch of blocks.
    - fill the blocks with the following blocks.” 
    - that let's me dramatically cut down on redundancy in templates.
    - each template has to define only what’s unique to that template.
- Here’s what the **“base.html” template**, including the use of static files, might look like:
```python
 website/templates/base.html
{% load static %}
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <img src="{% static 'images/sitelogo.png' %}" alt="Logo">
    {% block content %}{% endblock %}
</body>
</html>
```

 








