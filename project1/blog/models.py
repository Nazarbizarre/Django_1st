from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, 
        choices=Status,
        default=Status.DRAFT
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    
    class Meta:
        ordering = ['-created']
        indexes= [
            models.Index(fields=['-created'])
        ]
        
    def __str__(self):
        return self.title
    