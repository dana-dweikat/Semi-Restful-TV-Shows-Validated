from django.db import models


class ShowManger(models.Manager):
    def validate_input(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = 'Title should be at least 2 charters'
        if len(post_data['network']) < 3:
            errors['network'] = 'Network should be at least 3 charters'
        if len(post_data['description']) < 10:
            errors['description'] = 'description should be at least 10 charters'
        
        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManger()
    def __str__(self):
        return self.title
