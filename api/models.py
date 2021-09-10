from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="productImages")
    name = models.CharField(max_length=100, blank=False, null=False)
    entryDate = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isSpecial = models.BooleanField(default=False)
    # space separated choices
    hasToppings = models.BooleanField(default=False)
    hasSizes = models.BooleanField(default=False)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}   {self.name}"


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    mode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id}| {self.rating} for {self.mode}"
