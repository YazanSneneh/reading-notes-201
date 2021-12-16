# Django at a glance
- 
- it was designed to make common web development tasks fast and easy.


### Design a model
- it comes with an object-relational mapper in which I describe database layout in Python code.
- The (data-model)[https://docs.djangoproject.com/en/4.0/topics/db/models/] syntax offers many rich ways of representing models.
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
from django.db import models

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
```

