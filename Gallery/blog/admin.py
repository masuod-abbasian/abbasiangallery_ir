from django.contrib import admin
from blog.models import Article , Category
from django.contrib import messages
from django.utils.translation import ngettext


# Register your models here.
admin.site.site_header = 'صفحه ی مدیریت'
admin.site.site_title = 'صفحه مدیریت گالری عباسیان'
admin.site.index_title = 'گالری عباسیان'

class CategoryAdmin(admin.ModelAdmin):
    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d دسته‌بندی منتشر شد.',
            '%d تا از دسته‌یندی‌ها منتشر شدند.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description = 'منتشرکردن دسته‌بندی‌های انتخاب شده'

    def make_draft(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
                '%d دسته‌بندی پیش‌نویس شد.',
                '%d تا از دسته‌بندی‌ها پیش‌نوس شدند.',
                updated,
            ) % updated, messages.SUCCESS)
    make_draft.short_description = 'پیش‌نویس‌کردن دسته‌بندی‌عای انتخاب شده'

    list_display = ('position','title','slug','parent','status')
    list_filter = ('status',)
    search_fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published, make_draft]


admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):

    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d مقاله منتشر شد.',
            '%d عدد از مقاله‌ها منتشر شدند.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description = 'منتشر کردن مقالات انتخاب شده'

    def make_draft(self, request, queryset):
        updated = queryset.update(status='d')
        self.message_user(request, ngettext(
                '%d مقاله پیش‌نویس شد.',
                '%d عدد از مقاله‌ها پیش‌نویس شدند.',
                updated,
            ) % updated, messages.SUCCESS)
    make_draft.short_description = 'پیش‌نویس کردن مقالات انتخاب شده'

    list_display = ('title','thumbnail_tag','slug','author','jpublished','status','category_to_str')
    list_filter = ('published', 'status')
    search_fields = ['title', 'description']
    ordering = ('-status', '-published')
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published, make_draft]

    def category_to_str(self , obj):
        return '، '.join([category.title for category in obj.category_published()])
    category_to_str.short_description = 'دسته‌بندی'
    
admin.site.register(Article,ArticleAdmin)
