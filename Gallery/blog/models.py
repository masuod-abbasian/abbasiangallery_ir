from turtle import update
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    STATUS_CHOICES =(
        ('d','Draft'),
        ('p','Published'),
    )
    title = models.CharField(max_length=250, verbose_name ='عنوان')
    slug = models.SlugField(max_length=250, unique=True, verbose_name ='آدرس')
    thumbnail = models.ImageField(upload_to='images', verbose_name ='تصویر')
    description = models.TextField(verbose_name = 'شرح')
    published = models.DateTimeField(default=timezone.now, verbose_name = 'تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name ='وضعیت')

    class Meta:
        verbose_name = 'نوشته'
        verbose_name_plural = 'نوشته ها'

    def __str__(self):
        return self.title

    