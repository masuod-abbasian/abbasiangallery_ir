from turtle import update
from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter

# Create your models here.

class ArticleManager(models.Manager):
    def article_publish(self):
        return self.filter(status="p")
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیر‌دسته')
    title = models.CharField(max_length=250, verbose_name ='عنوان دسته‌بندی')
    slug = models.SlugField(max_length=250, unique=True, verbose_name ='آدرس دسته‌بندی')
    status = models.BooleanField(default=True, verbose_name='آیا این دسته‌بندی نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')
    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ['parent__id','position']
    def __str__(self):
        return self.title

    objects = CategoryManager()
class Article(models.Model):
    STATUS_CHOICES =(
        ('d','پیش‌نویس'),
        ('p','منتشرشده'),
    )
    title = models.CharField(max_length=250, verbose_name ='عنوان')
    slug = models.SlugField(max_length=250, unique=True, verbose_name ='آدرس')
    category = models.ManyToManyField(Category, verbose_name='دسته‌بندی', related_name='articles')
    thumbnail = models.ImageField(upload_to='images', verbose_name ='تصویر')
    description = models.TextField(verbose_name = 'شرح')
    published = models.DateTimeField(default=timezone.now, verbose_name = 'تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name ='وضعیت')

    class Meta:
        verbose_name = 'نوشته'
        verbose_name_plural = 'نوشته ها'
        ordering = ['published']
    def __str__(self):
        return self.title

    def jpublished(self):
        return jalali_converter(self.published)
    jpublished.short_description = 'زمان انتشار'

    def category_published(self):
        return self.category.filter(status=True)
    
    objects = ArticleManager()