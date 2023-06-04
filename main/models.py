from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Department(models.Model):
    """
    Модель: Департамент
    """
    id_department = models.AutoField(primary_key=True, verbose_name='id департамента')
    name_department = models.CharField(max_length=256, verbose_name='Наименование департамента')

    def __str__(self):
        return self.name_department

    class Meta:
        db_table = 'Department'
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Employee(models.Model):
    """
    Модель: сотрудники
    """
    id_employee = models.AutoField(primary_key=True, verbose_name='id сотрудника')
    name = models.CharField(max_length=256, verbose_name='ФИО')
    photo = models.ImageField(blank=True, null=True, verbose_name='Фотография', upload_to='foto/', max_length=256)
    post = models.CharField(max_length=256, verbose_name='Должность')
    salary = models.FloatField(max_length=10, verbose_name='Оклад')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст',
                                           validators=[MinValueValidator(0), MaxValueValidator(120)])

    id_department = models.ForeignKey('Department', models.DO_NOTHING,
                                      blank=True, null=True,
                                      related_name='employee',
                                      verbose_name='Департамент')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
