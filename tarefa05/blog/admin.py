from django.contrib import admin
from .models import Post

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo',)
    list_filter = ('data_publicacao',)
