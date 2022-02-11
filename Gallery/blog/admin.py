from django.contrib import admin
from blog.models import Article , Category

# Register your models here.
admin.site.site_header = 'صفحه ی مدیریت'
admin.site.site_title = 'صفحه مدیریت گالری عباسیان'
admin.site.index_title = 'گالری عباسیان'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','parent','status')
    list_filter = ('status',)
    search_fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    

admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','jpublished','status','category_to_str')
    list_filter = ('published', 'status')
    search_fields = ['title', 'description']
    ordering = ('-status', '-published')
    prepopulated_fields = {"slug": ("title",)}
    
    def category_to_str(self , obj):
        return '، '.join([category.title for category in obj.category_published()])
    category_to_str.short_description = 'دسته‌بندی'
    
admin.site.register(Article,ArticleAdmin)
