from django.db import models

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Movies(models.Model):
    category = models.ForeignKey('Category', null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.name
