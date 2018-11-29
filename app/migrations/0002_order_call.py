# Generated by Django 2.1.3 on 2018-11-26 22:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата подачи заявки')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='Имя')),
                ('tel_num', models.CharField(max_length=128, verbose_name='Телефон *')),
                ('commentary', models.TextField(blank=True, verbose_name='Примечание')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]