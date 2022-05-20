from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    SCHOOL = (
        ('1', 'БИЛ №1'),
        ('2', 'Дарын'),
        ('3', 'СШИ "Мурагер"'),
        ('4', 'СМШИ'),
        ('5', 'СШИ им. Жамбыла'),
        ('6', 'ЖезБИЛ'),
        ('7', 'БИЛ №2 '),
        ('8', 'СШИ "Зияткер"'),
        ('9', 'СШИ "Өркен"'),
        ('10', 'СШИ Н.Нұрмақов '),
        ('11', 'СШИ "Информационных технологий"'),
        ('12', 'СШИ Озат')
    )

    REGION = (
        ('1', "Абай"),
        ('2', 'Актогай'),
        ('3', 'Балхаш'),
        ('4', 'Бухаржырау'),
        ('5', 'Жанаарка'),
        ('6', 'Жезказган'),
        ('7', 'Караганда'),
        ('8', 'Каражал'),
        ('9', 'Каркаралинск'),
        ('10', 'Нуринский'),
        ('11', 'Осакаровка'),
        ('12', 'Приозерск'),
        ('13', 'Сарань'),
        ('14', 'Сатпаев'),
        ('15', 'Темиртау'),
        ('16', 'Улытау'),
        ('17', 'Шахтинск'),
        ('18', 'Шетский'),
    )


    fio = models.CharField(max_length=50, verbose_name='Фамилия', default='')
    patronymic = models.CharField(max_length=50, verbose_name='Отчества', default='')
    # phone = models.CharField(max_length=10, default='')
    email = models.EmailField(max_length=50, unique=True, default='')
    region = models.CharField(max_length=11, choices=REGION, default='Абай', verbose_name='Район')
    school = models.CharField(max_length=2, choices=SCHOOL, default='Улытау', verbose_name='Школа')