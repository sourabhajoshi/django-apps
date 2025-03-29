# from django.contrib import admin
# from .models import Post, Comment, Like, Category

# # Registering models in Django admin
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'author', 'category', 'created_at')
#     search_fields = ('title', 'author__username')
#     list_filter = ('category', 'created_at')
#     ordering = ('-created_at',)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'post', 'author', 'created_at')
#     search_fields = ('post__title', 'author__username')
#     list_filter = ('created_at',)
    
# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'post', 'user')
#     search_fields = ('post__title', 'user__username')

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)
