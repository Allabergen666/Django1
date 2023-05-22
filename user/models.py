from django.db import models

# Create your models here.
class Human(models.Model):

    # CharField макс длина строки, verbose_name это типо значение
    name = models.CharField(max_length=50, verbose_name='Имя')

    # PositiveBigIntegerField не можые быть меньше 0, он начинается с 1
    age = models.PositiveBigIntegerField(verbose_name='Возраст')

    def __str__(self) -> str:
        return self.name + " " + str(self.age)
    
    class Meta:
        verbose_name = "Человека"
        verbose_name_plural = "Люди"