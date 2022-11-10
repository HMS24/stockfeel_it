from django.db import models

# Create your models here.

class Coffee(models.Model):
    """Model for representing a coffee"""

    name = models.CharField(max_length=10)
    bean_from = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        """String for representing the Model object."""

        return f'{self.name}, {self.bean_from}, {self.price})'
        