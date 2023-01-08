from django.db import models
# from django.contrib.admin.models import CHANGE, LogEntry
from ckeditor.fields import RichTextField

class GatewayProtect(models.Model):
    is_protected = models.BooleanField(default=True)
    
class Content(models.Model):
    pass

# Create your models here.
class Preamble(models.Model):
    title = models.CharField(max_length=300,blank=True)
    # essential = models.BooleanField(default=False,blank=True)
    # The following attributes ends with '1' not 'l'
    # essentia1 = models.BooleanField(default=False,blank=True)     
    is_published = models.BooleanField(default=True)
    author = models.CharField(max_length=30,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    #body = models.RichTextField(config_name='awesome_ckeditor')
   
    # posting_date = models.DateField(auto_now=False, auto_now_add=False, **options), https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.DateField

    def __str__(self):
        return f'{self.title}'
    
class Induction(models.Model):
    title = models.CharField(max_length=300,blank=True)
    #_essential = models.BooleanField(default=False,blank=True)
    # The following attributes ends with '1' not 'l'
    essentia1 = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=30,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    
    def __str__(self):
        if self.essentia1 == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essentia1 == False:
            return f'{self.title}'

class ScriptSuggestion(models.Model):
    # id = models.IntegerField(blank=False, null=False)
    title = models.CharField(max_length=300,blank=True)
    # essential = models.BooleanField(default=False,blank=True)
    # The following attributes ends with '1' not 'l'
    essentia1 = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    geeks_field = RichTextField(config_name='default',max_length=300000,blank=True)
    # changed = LogEntry.objects.filter(action_flag=CHANGE,blank=False, null=False)
    
    def __str__(self):
        if self.essentia1 == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essentia1 == False:
            return f'{self.title}'

class Research(models.Model):
    title = models.CharField(max_length=300,blank=True)
    # essential = models.BooleanField(default=False,blank=True)
    # The following attributes ends with '1' not 'l'
    essentia1 = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    geeks_field = RichTextField(config_name='default',max_length=300000,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    
    def __str__(self):
        if self.essentia1 == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essentia1 == False:
            return f'{self.title}'

class StockScript(models.Model):
    title = models.CharField(max_length=300,blank=True)
    # essential = models.BooleanField(default=False,blank=True)
    # The following attributes ends with '1' not 'l'
    essentia1 = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    
    def __str__(self):
        if self.essentia1 == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essentia1 == False:
            return f'{self.title}'