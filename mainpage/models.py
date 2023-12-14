from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class ExtendedUser(User):
        user=models.OneToOneField(User,parent_link=True,primary_key=True,on_delete=models.CASCADE)
        phone=models.IntegerField(default=0)
        adress=models.CharField(max_length=80)
        def __str__(self):
            return self.user.username
class images(models.Model):
      image=models.ImageField(upload_to='gallery')
      image1=models.ImageField(upload_to="gallery")
      image2=models.ImageField(upload_to="gallery")
      image3=models.ImageField(upload_to="gallery")
      image4=models.ImageField(upload_to="gallery")
      image5=models.ImageField(upload_to="gallery")
      image6=models.ImageField(upload_to="gallery")
      image7=models.ImageField(upload_to="gallery")
      image8=models.ImageField(upload_to="gallery")
      image9=models.ImageField(upload_to="gallery")
      image10=models.ImageField(upload_to="gallery")
      image11=models.ImageField(upload_to="gallery")
      image12=models.ImageField(upload_to="gallery")
      image13=models.ImageField(upload_to="gallery")
      image14=models.ImageField(upload_to="gallery")
      
class gmail1(models.Model):
      mail=models.EmailField()
class product(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to='gallery') 
    image1=models.ImageField(upload_to='gallery')
    image2=models.ImageField(upload_to='gallery')
    image3=models.ImageField(upload_to='gallery')
    image4=models.ImageField(upload_to='gallery')
    description=RichTextField()      
class review(models.Model):
      name=models.CharField(max_length=40)
      message=RichTextField()
      def __str__(self):
            return self.name      
    