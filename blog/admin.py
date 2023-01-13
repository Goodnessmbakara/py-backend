from django.contrib import admin
from blog.models import BlogPost,Comments

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}
    

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comments)