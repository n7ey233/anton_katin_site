from django.db import models
from django.utils import timezone

class order_part(models.Model):
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата подачи заявки')
    car_list = (
    ('', 'Выберите марку'),
    ('DAIHATSU', 'DAIHATSU'),
    ('HINO', 'HINO'),
    ('HONDA', 'HONDA'),
    ('INFINITY', 'INFINITY'),
    ('ISUZU', 'ISUZU'),
    ('LEXUS', 'LEXUS'),
    ('MAZDA', 'MAZDA'),
    ('MITSUBISHI', 'MITSUBISHI'),
    ('NISSAN', 'NISSAN'),
    ('SUBARU', 'SUBARU'),
    ('SUZUKI', 'SUZUKI'),
    ('TOYOTA', 'TOYOTA'),
    )

    transmission_list = (
    ('', 'Выберите трансмиссию'),
    ('АКПП', 'Автоматическая'),
    ('МКПП', 'Ручная'),
    ('Вариатор', 'Вариатор'),    
    )

    privod_list = (
    ('', 'Выберите привод'),
    ('Передний', 'Передний 2WD'),
    ('4WD', 'Полный привод 4WD'),
    ('Задний', 'Задний 2WD'),
    )
    car_brand = models.CharField(max_length=128, blank=True, choices=car_list, verbose_name='Марка автомобиля')
    car_model = models.CharField(max_length=128, blank=True, verbose_name='Модель')
    #например Land Cruiser
    car_year = models.CharField(max_length=128, blank=True, verbose_name='Год выпуска')
    #Укажите год выпуска авто
    car_transmission = models.CharField(max_length=128, blank=True, choices=transmission_list, verbose_name='Трансмиссия')
    car_privod = models.CharField(max_length=128, blank=True, choices=privod_list, verbose_name='Привод')
    engine_model = models.CharField(max_length=128, blank=True, verbose_name='Модель, марка двигателя')
    #например 2UZ-FE
    car_model_num = models.CharField(max_length=128, blank=True, verbose_name='Номер кузова, шасси, VIN')
    #Укажите данные с ПТС либо СОР
    fio = models.CharField(max_length=128, blank=True, verbose_name='ФИО')
    #Представьтесь (Необязательно)
    place = models.CharField(max_length=128, blank=True, verbose_name='Город')
    #Укажите город доставки
    tel_num = models.CharField(max_length=128, blank=False, verbose_name='Телефон')
    #Укажите номер телефона
    email = models.EmailField(max_length=254, blank = False, verbose_name='Электронная почта (E-mail)')
    #Укажите ВЕРНЫЙ адрес
    parts = models.CharField(max_length=128, blank=False, verbose_name='Необходимые запчасти')
    #Укажите список необходимых запчастей (например, двигатель в сборе)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return str(self.created_date)

class order_call(models.Model):
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата подачи заявки')
    name = models.CharField(max_length=128, blank=True, verbose_name='Имя')
    tel_num = models.CharField(max_length=128, blank=False, verbose_name='Телефон')
    commentary = models.TextField(blank = True, verbose_name='Примечание')
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return str(self.created_date)
