from django.db import models
from django.contrib.auth.models import User


class FoodType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Taom turi"
        verbose_name_plural = "Taom turlari"

    def __str__(self):
        return self.name


class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=200)
    tarkibi = models.CharField(max_length=200)
    narxi = models.IntegerField()

    class Meta:
        verbose_name = "Taom"
        verbose_name_plural = "Taomlar"

        def __str__(self):
            return self.nomi


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name="Taom")
    text = models.TextField(verbose_name="Izoh")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qoshilgan vaqti")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.text[:30]}"
       


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     food = models.ForeignKey(Food, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)