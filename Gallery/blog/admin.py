from django.contrib import admin
from blog.models import Article

# Register your models here.
admin.site.site_header = 'صفحه ی مدیریت'
admin.site.site_title = 'صفحه مدیریت گالری عباسیان'
admin.site.index_title = 'گالری عباسیان'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','published','status')
    list_filter = ('published', 'status')
    search_fields = ['title', 'description']
    ordering = ('-status', '-published')
    prepopulated_fields = {"slug": ("title",)}
    

admin.site.register(Article,ArticleAdmin)
