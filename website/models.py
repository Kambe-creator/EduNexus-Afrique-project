from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    author = models.CharField(max_length=100)  
    categories = models.CharField(max_length=100, blank=True)  
    tags = models.CharField(max_length=200, blank=True)  

    def __str__(self):  
        return self.title  
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"



