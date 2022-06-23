from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("taxt",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-" #вывод для пустых колонок

admin.site.register(Post, PostAdmin)