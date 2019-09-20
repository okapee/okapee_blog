from django.contrib import admin
from .models import Post, Comment  # Comment追加

admin.site.register(Post)
admin.site.register(Comment)  # この行追加
