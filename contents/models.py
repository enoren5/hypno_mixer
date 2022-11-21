from django.db import models

class Content(models.Model):
    pass

# Create your models here.
class Preamble(models.Model):
    title = models.CharField(max_length=300,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    #body = models.RichTextField(config_name='awesome_ckeditor')
    author = models.CharField(max_length=30,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    # posting_date = models.DateField(auto_now=False, auto_now_add=False, **options), https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.DateField

    def __str__(self):
        return f'{self.title}'
    
class Induction(models.Model):
    title = models.CharField(max_length=300,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    author = models.CharField(max_length=30,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    
    def __str__(self):
        return f'{self.title}'

class ScriptSuggestion(models.Model):
    title = models.CharField(max_length=300,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return f'{self.title}'

class Research(models.Model):
    title = models.CharField(max_length=300,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return f'{self.title}'

class StockScript(models.Model):
    title = models.CharField(max_length=300,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return f'{self.title}'