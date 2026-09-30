from django.conf import settings
from django.db import models
#from ckeditor.fields import RichTextField

class UserExcludable(models.Model):
    # Users listed here can neither see nor open the article
    excluded_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='+')

    class Meta:
        abstract = True

class GatewayProtect(models.Model):
    is_protected = models.BooleanField(default=True)
    
class Content(models.Model):
    pass

# Create your models here.
class Preamble(UserExcludable):
    title = models.CharField(max_length=300,blank=True)
    # essential = models.BooleanField(default=False,blank=True)     
    is_published = models.BooleanField(default=True)
    author = models.CharField(max_length=30,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    #body = models.RichTextField(config_name='awesome_ckeditor')
   
    # posting_date = models.DateField(auto_now=False, auto_now_add=False, **options), https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.DateField
    class Meta:
        verbose_name        = "Preamble"
        verbose_name_plural = "Preambles"
    
    def __str__(self):
        return f'{self.title}'
    
class Induction(UserExcludable):
    title = models.CharField(max_length=300,blank=True)
    is_published = models.BooleanField(default=True)
    essential = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=30,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)

    class Meta:
        verbose_name        = "Induction"
        verbose_name_plural = "Inductions"

    def __str__(self):
        if self.essential == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essential == False:
            return f'{self.title}'

class ScriptSuggestion(UserExcludable):
    # id = models.IntegerField(blank=False, null=False)
    title = models.CharField(max_length=300,blank=True)
    is_published = models.BooleanField(default=True)
    essential = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    # geeks_field = RichTextField(config_name='default',max_length=300000,blank=True)
    # changed = LogEntry.objects.filter(action_flag=CHANGE,blank=False, null=False)
    
    class Meta:
        verbose_name        = "Scripting (Custom)"
        verbose_name_plural = "Scripting (Custom)"
   
    def __str__(self):
        if self.essential == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essential == False:
            return f'{self.title}'

class Research(UserExcludable):
    title = models.CharField(max_length=300,blank=True)
    is_published = models.BooleanField(default=True)
    essential = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    # geeks_field = RichTextField(config_name='default',max_length=300000,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    
    class Meta:
        verbose_name        = "Research"
        verbose_name_plural = "Research"

    def __str__(self):
        if self.essential == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essential == False:
            return f'{self.title}'

class StockScript(UserExcludable):
    title = models.CharField(max_length=300,blank=True)
    is_published = models.BooleanField(default=True)
    essential = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)

    class Meta:
        verbose_name        = "Scripting (Stock)"
        verbose_name_plural = "Scripting (Stock)"

    def __str__(self):
        if self.essential == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essential == False:
            return f'{self.title}'

class NYTimes(UserExcludable):
    title = models.CharField(max_length=300,blank=True)
    is_published = models.BooleanField(default=True)
    essential = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    
    class Meta:
        verbose_name        = "NY Times"
        verbose_name_plural = "NY Times"    
    
    def __str__(self):
        if self.essential == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essential == False:
            return f'{self.title}'

class TorStar(UserExcludable):
    title = models.CharField(max_length=300,blank=True)
    is_published = models.BooleanField(default=True)
    essential = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)

    class Meta:
        verbose_name        = "Toronto Star"
        verbose_name_plural = "Toronto Star"

    def __str__(self):
        if self.essential == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essential == False:
            return f'{self.title}'

class WSJournal(UserExcludable):
    title = models.CharField(max_length=300,blank=True)
    is_published = models.BooleanField(default=True)
    essential = models.BooleanField(default=False,blank=True)
    author = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    body = models.TextField(max_length=300000,blank=True)
    
    class Meta:
        verbose_name        = "WSJ"
        verbose_name_plural = "WSJ"

    def __str__(self):
        if self.essential == True:
            return f'{self.title} (ESSENTIAL)'
        if self.essential == False:
            return f'{self.title}'

class AssortedPeriodicals(models.Model):
    media_type = models.CharField(max_length=300,blank=True)   
    author_last_name = models.CharField(max_length=300,blank=True)
    publication_year = models.CharField(max_length=300,blank=True)
    address = models.CharField(max_length=300,blank=True)    
    title = models.CharField(max_length=300,blank=True) 
    
    class Meta:
        verbose_name        = "Assorted Periodicals"
        verbose_name_plural = "Assorted Periodicals"
    
    def __str__(self):
        return f'{self.author_last_name} {self.title}'

        
        
class AssortedLiterature(models.Model):
    media_type = models.CharField(max_length=300,blank=True)   
    author_last_name = models.CharField(max_length=300,blank=True)
    publication_year = models.CharField(max_length=300,blank=True)
    address = models.CharField(max_length=300,blank=True)    
    title = models.CharField(max_length=300,blank=True)    

    class Meta:
        verbose_name        = "Assorted Literature"
        verbose_name_plural = "Assorted Literature"

    def __str__(self):
        return f'{self.author_last_name} {self.title}'

class Binaurals(models.Model):
    author_last_name = models.CharField(max_length=300,blank=True)
    publication_year = models.CharField(max_length=300,blank=True)
    address = models.CharField(max_length=300,blank=True)    
    title = models.CharField(max_length=300,blank=True)    
    
    class Meta:
        verbose_name        = "Binaurals"
        verbose_name_plural = "Binaurals"
    
    def __str__(self):
        return f'{self.author_last_name} {self.title}'