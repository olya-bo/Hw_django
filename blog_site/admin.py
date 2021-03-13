from django.contrib import admin
from blog_site.models import Post, Comment, LikeDislike


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "author"]


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'post', 'user', 'created_at', 'parent']


class LikeDislikeModelAdmin(admin.ModelAdmin):
    list_display = ['target', 'user', 'created_at', 'is_like']


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(LikeDislike, LikeDislikeModelAdmin)
