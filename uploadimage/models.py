from django.db import models
from django.utils.html import format_html

# Create your models here.
class Image(models.Model):
    
    Day = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    Circuit = models.CharField(max_length=100, blank=True, null=True)
    Category = models.CharField(max_length=100, blank=True, null=True)
    Category1 = models.CharField(max_length=100, blank=True, null=True)
    Category2 = models.CharField(max_length=100, blank=True, null=True)
   
    Accessory = models.CharField(max_length=100, blank=True, null=True)
    Accessory1 = models.CharField(max_length=100, blank=True, null=True)
    Accessory2 = models.CharField(max_length=100, blank=True, null=True)
   
    Case = models.CharField(max_length=100, blank=True, null=True)
    Case1 = models.CharField(max_length=100, blank=True, null=True)
    Case2 = models.CharField(max_length=100, blank=True, null=True)
  
    Customer_number = models.CharField(max_length=100, blank=True, null=True)
    nameimageold = models.CharField(max_length=100, blank=True, null=True)
    nameimagenew = models.CharField(max_length=100, blank=True, null=True)
    pathimage = models.CharField(max_length=100, blank=True, null=True) #เพิ่ม
    pathoraclecloud = models.URLField(max_length=500, blank=True, null=True)
    image = models.FileField(upload_to='media/', null=True, blank=True)
    

    def show_image(self): 
        if self.image:
            return format_html('<img src="%s" height="40px">' % self.image.url) 
        return ''
    show_image.allow_tags = True 
    show_image.short_description = 'Image'
