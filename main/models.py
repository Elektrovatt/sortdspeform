import django_filters
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from account.models import ProfileUserModel


class Thickness_board_model(models.Model):
    # from main.models import Thickness_board_model импорт для shell

    #добавить 8  измерений шлифованной плиты
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    # number_shift = models.ForeignKey(ProfileUserModel, on_delete=models.PROTECT, null=True, verbose_name='Номер смены')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    # date_update=models.DateTimeField(auto_now=True, verbose_name='Дата Обновления')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=5, null=True, verbose_name='Значение 1')
    value2 = models.CharField(max_length=5, null=True, verbose_name='Значение 2')
    value3 = models.CharField(max_length=5, null=True, verbose_name='Значение 3')
    value4 = models.CharField(max_length=5, null=True, verbose_name='Значение 4')
    value5 = models.CharField(max_length=5, null=True, verbose_name='Значение 5')
    value6 = models.CharField(max_length=5, null=True, verbose_name='Значение 6')
    value7 = models.CharField(max_length=5, null=True, verbose_name='Значение 7')
    value8 = models.CharField(max_length=5, null=True, verbose_name='Значение 8')

    def __str__(self):
        return ('Смена №# %s, плита: %s, дата: %s. %s-%s-%s-%s-%s-%s-%s-%s' %(self.author, self.value0, self.date_created,
            self.value1,self.value2,self.value3,self.value4,self.value5,self.value6,self.value7,self.value8 ))

    def get_absolute_url(self):
         return f'/board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Шлифвока - Толщина шлифованной плиты'
            ordering = ('-date_created',)


class Thickness_pack_board_model(models.Model):
    #добавить 22  измеренияпачки
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=5, null=True, verbose_name='Значение 1')
    value2 = models.CharField(max_length=5, null=True, verbose_name='Значение 2')
    value3 = models.CharField(max_length=5, null=True, verbose_name='Значение 3')
    value4 = models.CharField(max_length=5, null=True, verbose_name='Значение 4')
    value5 = models.CharField(max_length=5, null=True, verbose_name='Значение 5')
    value6 = models.CharField(max_length=5, null=True, verbose_name='Значение 6')
    value7 = models.CharField(max_length=5, null=True, verbose_name='Значение 7')
    value8 = models.CharField(max_length=5, null=True, verbose_name='Значение 8')
    value9 = models.CharField(max_length=5, null=True, verbose_name='Значение 9')
    value10 = models.CharField(max_length=5, null=True, verbose_name='Значение 10')
    value11 = models.CharField(max_length=5, null=True, verbose_name='Значение 11')
    value12 = models.CharField(max_length=5, null=True, verbose_name='Значение 12')
    value13 = models.CharField(max_length=5, null=True, verbose_name='Значение 13')
    value14 = models.CharField(max_length=5, null=True, verbose_name='Значение 14')
    value15 = models.CharField(max_length=5, null=True, verbose_name='Значение 15')
    value16 = models.CharField(max_length=5, null=True, verbose_name='Значение 16')
    value17 = models.CharField(max_length=5, null=True, verbose_name='Значение 17')
    value18 = models.CharField(max_length=5, null=True, verbose_name='Значение 18')
    value19 = models.CharField(max_length=5, null=True, verbose_name='Значение 19')
    value20 = models.CharField(max_length=5, null=True, verbose_name='Значение 20')
    value21 = models.CharField(max_length=5, null=True, verbose_name='Значение 21')
    value22 = models.CharField(max_length=5, null=True, verbose_name='Значение 22')

    def __str__(self):
        return ('Смена № %s, плита: %s, дата: %s.' %(self.author, self.value0, self.date_created))

    def get_absolute_url(self):
         return f'/thickness-pack-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Шлифвока - Толщина шлифованной пачки'
            ordering = ('-date_created',)


class Thickness_unpolished_pack_board_model(models.Model):
    #добавить 22  измеренияпачки
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=5, null=True, verbose_name='Зад толщ. после пресса, мм')
    value2 = models.CharField(max_length=2, null=True, verbose_name='Плит в пакете, шт')
    value3 = models.CharField(max_length=5, null=True, verbose_name='Значение 1')
    value4 = models.CharField(max_length=5, null=True, verbose_name='Значение 2')
    value5 = models.CharField(max_length=5, null=True, verbose_name='Значение 3')
    value6 = models.CharField(max_length=5, null=True, verbose_name='Значение 4')
    value7 = models.CharField(max_length=5, null=True, verbose_name='Значение 5')
    value8 = models.CharField(max_length=5, null=True, verbose_name='Значение 6')
    value9 = models.CharField(max_length=5, null=True, verbose_name='Значение 7')
    value10 = models.CharField(max_length=5, null=True, verbose_name='Значение 8')
    value11 = models.CharField(max_length=5, null=True, verbose_name='Значение 9')
    value12 = models.CharField(max_length=5, null=True, verbose_name='Значение 10')
    value13 = models.CharField(max_length=5, null=True, verbose_name='Значение 11')
    value14 = models.CharField(max_length=5, null=True, verbose_name='Значение 12')
    value15 = models.CharField(max_length=5, null=True, verbose_name='Значение 13')
    value16 = models.CharField(max_length=5, null=True, verbose_name='Значение 14')
    value17 = models.CharField(max_length=5, null=True, verbose_name='Значение 15')
    value18 = models.CharField(max_length=5, null=True, verbose_name='Значение 16')
    value19 = models.CharField(max_length=5, null=True, verbose_name='Значение 17')
    value20 = models.CharField(max_length=5, null=True, verbose_name='Значение 18')
    value21 = models.CharField(max_length=5, null=True, verbose_name='Значение 19')
    value22 = models.CharField(max_length=5, null=True, verbose_name='Значение 20')
    value23 = models.CharField(max_length=5, null=True, verbose_name='Значение 21')
    value24 = models.CharField(max_length=5, null=True, verbose_name='Значение 22')

    def __str__(self):
        return ('Смена № %s, плита: %s, дата: %s.' %(self.author, self.value0, self.date_created))

    def get_absolute_url(self):
         return f'/thickness-unpolished-pack-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Распиловка - Толщина нешлифованой пачки'
            ordering = ('-date_created',)


class Thickness_unpolished_board_model(models.Model):
    #добавить 8  измерений нешлифованной плиты
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=5, null=True, verbose_name='Значение 1')
    value2 = models.CharField(max_length=5, null=True, verbose_name='Значение 2')
    value3 = models.CharField(max_length=5, null=True, verbose_name='Значение 3')
    value4 = models.CharField(max_length=5, null=True, verbose_name='Значение 4')
    value5 = models.CharField(max_length=5, null=True, verbose_name='Значение 5')


    def __str__(self):
        return ('Смена № %s, плита: %s, дата: %s.' %(self.author, self.value0, self.date_created))

    def get_absolute_url(self):
         return f'/thickness-unpolished-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Пресс - Толщина нешлифованой плиты'
            ordering = ('-date_created',)


class Cleaning_press_tape_model(models.Model):
    #Очистка ленты пресса

    value_clean = (
        ('', ''),
        ('Грязная', 'Грязная'),
        ('Чистая', 'Чистая'),
        ('Очистка', 'Очистка'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value0 = models.CharField(max_length=20, choices=value_clean, verbose_name='Левая сторона ленты')
    value1 = models.CharField(max_length=20, choices=value_clean, verbose_name='Центр ленты')
    value2 = models.CharField(max_length=20, choices=value_clean, verbose_name='Правая сторона ленты')
    value3 = models.CharField(max_length=20, choices=value_clean, verbose_name='Левая сторона ленты')
    value4 = models.CharField(max_length=20, choices=value_clean, verbose_name='Центр ленты')
    value5 = models.CharField(max_length=20, choices=value_clean, verbose_name='Правая сторона ленты')


    def __str__(self):
        return ('Смена № %s, дата: %s.' %(self.author, self.date_created))

    def get_absolute_url(self):
         return f'/cleaning-press-tape/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Пресс - Очистка ленты пресса'
            ordering = ('-date_created',)



class Sizes_unpolished_board_model(models.Model):
    #добавить размеры нешлифованной плиты
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=4, null=True, verbose_name='Ширина 2070(+/- 5), мм')
    value2 = models.CharField(max_length=4, null=True, verbose_name='Длинна правая сторона в мм')
    value3 = models.CharField(max_length=4, null=True, verbose_name='Длинна левая сторона в мм ')
    value4 = models.CharField(max_length=1, null=True, verbose_name='Разница диагоналей в мм')


    def __str__(self):
        return ('Смена № %s, плита: %s, дата: %s.' %(self.author, self.value0, self.date_created))

    def get_absolute_url(self):
         return f'/sizes-unpolished-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Распиловка - Размеры нешлифованой плиты'
            ordering = ('-date_created',)


class Number_tapes_model(models.Model):
    "Учёт шлифовальных материалов"
    Agg1 = (
        ('', ''),
        ('P 50', 'P 50'),
        ('P 80', 'P 80'),
        ('P 120', 'P 120'),
    )
    Agg2 = (
        ('', ''),
        ('Foam', 'Foam'),
        ('Pes', 'Pes'),
    )
    Agg3 = (
        ('', ''),
        ('Combi', 'Combi'),
        ('Polyster', 'Polyster'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата замены лент')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    number_1_1_choices = models.CharField(max_length=20, blank=True, null=True, choices=Agg1, verbose_name='Лента 1.1')
    number_1_1_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 1.1')
    value0 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пробег ленты Agg 1.1')

    number_1_2_choices = models.CharField(max_length=20, blank=True, null=True,choices=Agg1,
                                          verbose_name='Лента 1.2')
    number_1_2_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 1.2')
    value1 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пробег ленты Agg 1.2')

    number_2_1_choices = models.CharField(max_length=20,blank=True, null=True, choices=Agg1, verbose_name='Лента 2.1')
    number_2_1_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 2.1')
    liner_2_1_choices = models.CharField(max_length=20, blank=True, null=True, choices=Agg2, verbose_name='Вставка 2.1')
    value2 = models.CharField(max_length=20,blank=True, null=True,  verbose_name='Пробег ленты Agg 2.1')

    number_2_2_choices = models.CharField(max_length=20, blank=True, null=True,choices=Agg1, verbose_name='Лента 2.2')
    number_2_2_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 2.2')
    liner_2_2_choices = models.CharField(max_length=20,  blank=True, null=True,choices=Agg2, verbose_name='Вставка 2.2')
    value3 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пробег ленты Agg 2.2')

    number_2_3_choices = models.CharField(max_length=20,  blank=True, null=True,choices=Agg1, verbose_name='Лента 2.3')
    number_2_3_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 2.3')
    liner_2_3_choices = models.CharField(max_length=20, blank=True, null=True,choices=Agg2, verbose_name='Вставка 2.3')
    value4 = models.CharField(max_length=20,blank=True, null=True,  verbose_name='Пробег ленты Agg 2.3')

    number_2_4_choices = models.CharField(max_length=20, blank=True, null=True, choices=Agg1, verbose_name='Лента 2.4')
    number_2_4_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 2.4')
    liner_2_4_choices = models.CharField(max_length=20, blank=True, null=True, choices=Agg2, verbose_name='Вставка 2.4')
    value5 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пробег ленты Agg 2.4')



    def __str__(self):
        return ('Смена № %s, дата: %s.' %(self.author, self.date_created))

    def get_absolute_url(self):
         return f'/number-tapes-liner/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Шлифвока - Учёт шлифовальных лент'
            ordering = ('-date_created',)


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Number_tapes_model
        fields = ['date_created']



class Lab_board_model(models.Model):
    """добавить лабораторную плиту"""
    Number_shift = (
        ('', ''),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата производства' )
    number_shift = models.CharField(max_length=1, choices=Number_shift, verbose_name='Смена (производства)№')
    number_path = models.CharField(max_length=1,choices=Number_shift, verbose_name='Номер партии')
    value0 = models.CharField(max_length=4,  verbose_name='Заказ')
    value1 = models.CharField(max_length=2, verbose_name='Толщина, мм')
    value2 = models.CharField(max_length=4, null=True, verbose_name='Длина, мм')
    value3 = models.CharField(max_length=1, null=True, verbose_name='Количество, шт.')
    value4 = models.CharField(max_length=30, null=True,blank=True, verbose_name='Комментарий')



    def __str__(self):
        return ('Смена производства № %s, заказ - %s, плита: %s - %s, дата производства: %s.'
                %(self.number_shift, self.value1,self.value1,self.value2, self.date_created))

    def get_absolute_url(self):
         return f'/lab-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Распиловка - Лабораторные образцы'
            ordering = ('-date_created',)


class Press_sap_model(models.Model):
    """Модель состояния форсунок САП"""

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    name_form1 = models.BooleanField("121", default=False)
    name_form2 = models.BooleanField("123", default=False)
    name_form3 = models.BooleanField("125", default=False)
    name_form4 = models.BooleanField("127", default=False)
    name_form5 = models.BooleanField("129", default=False)
    name_form6 = models.BooleanField("131", default=False)
    name_form7 = models.BooleanField("133", default=False)
    name_form8 = models.BooleanField("135", default=False)
    name_form9 = models.BooleanField("160", default=False)
    name_form10 = models.BooleanField("161", default=False)
    name_form11 = models.BooleanField("162", default=False)
    name_form12 = models.BooleanField("163", default=False)
    name_form13 = models.BooleanField("164", default=False)
    name_form14 = models.BooleanField("171", default=False)
    name_form15 = models.BooleanField("173", default=False)
    name_form16 = models.BooleanField("175", default=False)
    name_form17 = models.BooleanField("177", default=False)
    name_form18 = models.BooleanField("179", default=False)
    name_form19 = models.BooleanField("181", default=False)
    name_form20 = models.BooleanField("183", default=False)
    name_form21 = models.BooleanField("122", default=False)
    name_form22 = models.BooleanField("124", default=False)
    name_form23 = models.BooleanField("126", default=False)
    name_form24 = models.BooleanField("128", default=False)
    name_form25 = models.BooleanField("130", default=False)
    name_form26 = models.BooleanField("132", default=False)
    name_form27 = models.BooleanField("134", default=False)
    name_form28 = models.BooleanField("136", default=False)
    name_form29 = models.BooleanField("172", default=False)
    name_form30 = models.BooleanField("174", default=False)
    name_form31 = models.BooleanField("176", default=False)
    name_form32 = models.BooleanField("178", default=False)
    name_form33 = models.BooleanField("180", default=False)
    name_form34 = models.BooleanField("182", default=False)
    name_form35 = models.BooleanField("184", default=False)


    def __str__(self):
        return ('автор  %s ' % (self.author))

    def get_absolute_url(self):
        return f'/list-press-sap/{self.pk}'


    class Meta:
        verbose_name = 'поля'
        verbose_name_plural = 'Пресс - Состояние форсунок САП'
        ordering = ('-date_created',)