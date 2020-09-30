from django.contrib import admin

from .models import Article,Comment, Program, Internship, Fellowship, Resource, Gallery, Post

# Register your models here.

admin.site.register(Comment)
admin.site.register(Program)
admin.site.register(Internship)
admin.site.register(Fellowship)
admin.site.register(Resource)
admin.site.register(Gallery)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]

    prepopulated_fields = {'slug':('title',)}

    class Meta:
        model = Article

class GalleryInline(admin.TabularInline):
    model = Gallery
    fields = ['picture',]

from trix.admin import TrixAdmin

@admin.register(Post)
class PostAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('content',)
