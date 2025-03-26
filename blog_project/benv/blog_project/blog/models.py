from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Links each post to a User (author).if User deleted all the posts are also deleted
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # link post to catagory. Is catagory deleted Post will still exist without catagory
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment') # link each comment to specific Post. If Post delete all it is comments are also deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE) # link Comment to User. If User deleted all his comments are also deleted
    text = models.TextField()
    created_at = models.DateTimeField()
    
    def __str__(self):
        return f"Commented by {self.author} on {self.post}"
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('post', 'user') # here user can like post only once.
