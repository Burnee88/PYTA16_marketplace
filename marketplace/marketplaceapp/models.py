from django.db import models

#coloane: name, desription, ingredients, price, weight_grams,
# available_quantity, image


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.IntegerField()
    available_quantity = models.IntegerField()
    image = models.ImageField(upload_to="product_images", null=True, blank=True)

    def __str__(self):
        return self.name


