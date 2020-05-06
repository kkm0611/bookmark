from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL') #'Site URL'없으면 rul가지고 이름 만듦

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        #객체를 출력할 때 나타날 값
        return "이름: " + self.site_name + ", 주소:" + self.url
# Create your models here.
