# Generated by Django 4.0.4 on 2022-05-20 09:43

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Имя')),
                ('fio', models.CharField(default='', max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(default='', max_length=50, verbose_name='Отчества')),
                ('email', models.EmailField(default='', max_length=50, unique=True)),
                ('region', models.CharField(choices=[('1', 'Абай'), ('2', 'Актогай'), ('3', 'Балхаш'), ('4', 'Бухаржырау'), ('5', 'Жанаарка'), ('6', 'Жезказган'), ('7', 'Караганда'), ('8', 'Каражал'), ('9', 'Каркаралинск'), ('10', 'Нуринский'), ('11', 'Осакаровка'), ('12', 'Приозерск'), ('13', 'Сарань'), ('14', 'Сатпаев'), ('15', 'Темиртау'), ('16', 'Улытау'), ('17', 'Шахтинск'), ('18', 'Шетский')], default='Абай', max_length=11, verbose_name='Район')),
                ('school', models.CharField(choices=[('1', 'БИЛ №1'), ('2', 'Дарын'), ('3', 'СШИ "Мурагер"'), ('4', 'СМШИ'), ('5', 'СШИ им. Жамбыла'), ('6', 'ЖезБИЛ'), ('7', 'БИЛ №2 '), ('8', 'СШИ "Зияткер"'), ('9', 'СШИ "Өркен"'), ('10', 'СШИ Н.Нұрмақов '), ('11', 'СШИ "Информационных технологий"'), ('12', 'СШИ Озат')], default='Улытау', max_length=2, verbose_name='Школа')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
