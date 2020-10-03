from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', null=True, blank=True)
    eventName = models.CharField(max_length=1000, null=True,blank=True)
    eventDate = models.CharField(max_length=1000, null=True, blank=True)
    admin_approved = models.BooleanField(default=False)

class GalleryImage(models.Model):
    images = models.ForeignKey(Gallery,on_delete = models.CASCADE,verbose_name = "Gallery",related_name="images")
    image = models.ImageField(upload_to='gallery', null=True, blank=True)
