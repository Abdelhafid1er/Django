from django.db import models

# Create your models here.
#Création de la table product
class Product(models,Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits-10, decimal_places=2)
    description = models.TextField(blank=True,nul=True)
    quantity = models.PostitiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
