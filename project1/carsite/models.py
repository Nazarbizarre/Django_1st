from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    class Status(models.TextChoices):
        USED = 'U', 'Draft'
        NEW = 'N', 'Published'
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    status = models.CharField(
        max_length=2, 
        choices=Status,
        default=Status.DRAFT
    )
    category = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='cars',
    )
    
    class Meta:
        ordering = ['-price']
        indexes= [
            models.Index(fields=['-price'])
        ]
        
    def __str__(self):
        return self.name
    