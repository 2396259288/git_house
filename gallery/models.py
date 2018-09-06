from django.db import models

# Create your models here.


class Gallery(models.Model):
	description = models.CharField(default='介绍', max_length=100)
	img = models.ImageField(default='default.png',upload_to='images/')
	title = models.CharField(default='作品标题', max_length=20)
	
	def __str__(self):
		return self.title



    
    

