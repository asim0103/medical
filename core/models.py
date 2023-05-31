from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

# Create your models here.

class AbstractBaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    uptadet_at=models.DateTimeField(auto_now=True)
    
    class Meta():
        abstract=True
        

        
class Category(AbstractBaseModel):
    title = models.CharField(max_length=100)

    
    def __str__(self) :
        return self.title
    
    class Meta():
   
        verbose_name_plural=_("category")
        
        
class News(AbstractBaseModel):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    images=models.ImageField(upload_to='media/news')
    slug = models.SlugField(max_length=100, blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.title
    
    class Meta():

        verbose_name_plural=_("news")
        
    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '_')
        super(News,self).save(*args, **kwargs)
        


class Settings(AbstractBaseModel):
    logo=models.ImageField(upload_to='media/settings')
    number=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    twitter=models.URLField()
    instagram=models.URLField()
    
    class Meta:
        verbose_name_plural=_('Settings')
        
    def __str__(self) :
        return self


class About(AbstractBaseModel):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
class Contact(AbstractBaseModel):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
     
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= _("Contact")
    
    
    
class Blog(AbstractBaseModel):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='media/blog')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= _("Blog")
    


class FAQ(AbstractBaseModel):
    question = models.CharField(max_length=300, verbose_name=("Sual"))
    answer = models.CharField(max_length=1000, verbose_name=("Cavab"))
    order = models.IntegerField(default=0, verbose_name=("Sıra"))

    def __str__(self):
        return "{}".format(self.question)

    class Meta:
        ordering = ("order",)

class Doctors(AbstractBaseModel):
	title = models.CharField(max_length=200, verbose_name=("Başliq"))
	images = models.FileField(upload_to="uploads/%Y/%m/%d/", null=True)
	
	description =models.TextField()
	slug = models.SlugField(max_length=100, blank=True, null=True, unique=True,)
	category = models.ForeignKey("DoctorsCategory", on_delete=models.CASCADE)

	def __str__(self):
		return self.title 
		
		
	def get_absolute_url(self):
		return f'/doctors/{self.slug}'
	
	
	class Meta:
		verbose_name = _('Doctors')
		verbose_name_plural = _('Doctors')

	def save(self, *args, **kwargs):
		self.slug = self.title.replace(' ', '-').lower()
		super().save(*args, **kwargs)

  

class Service(AbstractBaseModel):
	title = models.CharField(max_length=200, verbose_name=("Başliq"))
	images = models.FileField(upload_to="uploads/%Y/%m/%d/", null=True)
	
	description =models.TextField()
	slug = models.SlugField(max_length=100, blank=True, null=True, unique=True,)
	servicecategory = models.ForeignKey("ServiceCategory", on_delete=models.CASCADE)

	def __str__(self):
		return self.title 
		
		
	def get_absolute_url(self):
		return f'/service/{self.slug}'
	
	
	class Meta:
		verbose_name = _('Service')
		verbose_name_plural = _('Service')

	def save(self, *args, **kwargs):
		self.slug = self.title.replace(' ', '-').lower()
		super().save(*args, **kwargs)


class  ServiceCategory(AbstractBaseModel):
	title = models.CharField(max_length=200, verbose_name=("Başliq"))
	
	class  Meta:
		verbose_name_plural = "Category"

	def  __str__(self):
		return  str(self.title) if  self.title  else  " "



class  DoctorsCategory(AbstractBaseModel):
	title = models.CharField(max_length=200, verbose_name=("Başliq"))
	
	class  Meta:
		verbose_name_plural = "Category"

	def  __str__(self):
		return  str(self.title) if  self.title  else  " "