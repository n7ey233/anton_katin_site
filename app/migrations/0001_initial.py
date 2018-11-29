# Generated by Django 2.1.3 on 2018-11-26 02:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order_part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата подачи заявки')),
                ('car_brand', models.CharField(blank=True, choices=[('', 'Выберите марку'), ('DAIHATSU', 'DAIHATSU'), ('HINO', 'HINO'), ('HONDA', 'HONDA'), ('INFINITY', 'INFINITY'), ('ISUZU', 'ISUZU'), ('LEXUS', 'LEXUS'), ('MAZDA', 'MAZDA'), ('MITSUBISHI', 'MITSUBISHI'), ('NISSAN', 'NISSAN'), ('SUBARU', 'SUBARU'), ('SUZUKI', 'SUZUKI'), ('TOYOTA', 'TOYOTA')], max_length=128, verbose_name='Марка автомобиля')),
                ('car_model', models.CharField(blank=True, max_length=128, verbose_name='Модель')),
                ('car_year', models.CharField(blank=True, max_length=128, verbose_name='Год выпуска')),
                ('car_transmission', models.CharField(blank=True, choices=[('', 'Выберите трансмиссию'), ('АКПП', 'Автоматическая'), ('МКПП', 'Ручная'), ('Вариатор', 'Вариатор')], max_length=128, verbose_name='Трансмиссия')),
                ('car_privod', models.CharField(blank=True, choices=[('', 'Выберите привод'), ('Передний', 'Передний 2WD'), ('4WD', 'Полный привод 4WD'), ('Задний', 'Задний 2WD')], max_length=128, verbose_name='Привод')),
                ('engine_model', models.CharField(blank=True, max_length=128, verbose_name='Модель, марка двигателя')),
                ('car_model_num', models.CharField(blank=True, max_length=128, verbose_name='Номер кузова, шасси, VIN')),
                ('fio', models.CharField(blank=True, max_length=128, verbose_name='ФИО')),
                ('place', models.CharField(blank=True, max_length=128, verbose_name='Город')),
                ('tel_num', models.CharField(max_length=128, verbose_name='Телефон *')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта (E-mail) *')),
                ('parts', models.CharField(max_length=128, verbose_name='Необходимые запчасти **')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
