from django.db import models
from ckeditor.fields import RichTextField
from trix.fields import TrixField

# Create your models here.

class Article(models.Model):
    author =models.CharField(max_length = 500,verbose_name = "Writer")
    title = models.CharField(max_length = 500,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
    article_image = models.FileField(upload_to='img', blank = True,null = True,verbose_name="Add Photos to Article")
    published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=100,blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Name")
    comment_content = models.CharField(max_length = 200,verbose_name = "Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

class Program(models.Model):
    program_company = models.CharField(max_length=100, null=True)
    diversity_program = models.CharField(max_length=100, null=True)
    diversity_link = models.CharField(max_length=100, null=True)
    diversity_industry = models.CharField(max_length=100, null=True)
    diversity_population = models.CharField(max_length=100, null=True)
    date_posted = models.DateTimeField(auto_now_add=True,verbose_name="Posted Date")
    admin_approved = models.BooleanField(default=False)

class Internship(models.Model):
    internship_company = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
    industry = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    date_posted = models.DateTimeField(auto_now_add=True,verbose_name="Date")
    admin_approved = models.BooleanField(default=False)

class Fellowship(models.Model):
    name = models.CharField(max_length=100, null=True)
    link =  models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    date_posted = models.DateTimeField(auto_now_add=True,verbose_name="Posted")
    admin_approved = models.BooleanField(default=False)

class Resource(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    content = RichTextField()
    admin_approved = models.BooleanField(default=False)

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', null=True, blank=True)
    eventName = models.CharField(max_length=1000, null=True,blank=True)
    eventDate = models.CharField(max_length=1000, null=True, blank=True)
    admin_approved = models.BooleanField(default=False)

class Post(models.Model):
    content = TrixField('Content')
