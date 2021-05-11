from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'
    name = models.CharField(max_length=200, verbose_name="добавить")

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукт'
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="описание")
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Review(models.Model):
    class Meta:
        verbose_name = 'обзор'
        verbose_name_plural = 'обзор'
    text = models.TextField()
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text