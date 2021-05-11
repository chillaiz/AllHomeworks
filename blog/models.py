from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="курс")

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField()
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text