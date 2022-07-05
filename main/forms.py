from django import forms
from .models import *
from django.forms import ModelForm, TextInput



class Thickness_board_form(ModelForm):
        class Meta:
            model = Thickness_board_model
            fields = ['value0','value1','value2','value3','value4','value5','value6','value7','value8']
            widgets = {
                "is_customer": TextInput(attrs={'class': 'form-control','placeholder': 'Автор'}),
                "value0": TextInput(attrs={'class': 'form-control','placeholder': 'Толщина плиты, мм'}),
                "value1": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 1' }),
                "value2": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 2'}),
                "value3": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 3'}),
                "value4": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 4'}),
                "value5": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 5'}),
                "value6": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 6'}),
                "value7": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 7'}),
                "value8": TextInput(attrs={'class': 'form-control','placeholder': 'Значение 8'})

            }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'


class Sizes_unpolished_board_form(ModelForm):
    class Meta:
        model = Sizes_unpolished_board_model
        fields = ['value0', 'value1', 'value2', 'value3', 'value4']
        widgets = {
            "is_author": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина плиты'}),
            "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ширина 2070(+/- 5), мм'}),
            "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Длинна правая сторона, мм'}),
            "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Длинна левая сторона, мм'}),
            "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Разница диагоналей, мм'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class Сleaning_press_tape_form(ModelForm):
    value_clean = (
        ('', ''),
        ('Грязная', 'Грязная'),
        ('Чистая', 'Чистая'),
        ('Очистка', 'Очистка'),
    )
    value0 = forms.ChoiceField(choices=value_clean)
    value1 = forms.ChoiceField(choices=value_clean)
    value2 = forms.ChoiceField(choices=value_clean)
    value3 = forms.ChoiceField(choices=value_clean)
    value4 = forms.ChoiceField(choices=value_clean)
    value5 = forms.ChoiceField(choices=value_clean)

    class Meta:
        model = Cleaning_press_tape_model
        fields = [
            'value0', 'value1', 'value2',
            'value3', 'value4', 'value5']
        widgets = {

            "value0": TextInput(attrs={'class': 'form-control', 'placeholder': ' 1.1'}),
            "value1": TextInput(attrs={'class': 'form-control', 'placeholder': ' 1.2'}),
            "value2": TextInput(attrs={'class': 'form-control', 'placeholder': ' 2.1'}),
            "value3": TextInput(attrs={'class': 'form-control', 'placeholder': ' 2.2'}),
            "value4": TextInput(attrs={'class': 'form-control', 'placeholder': ' 2.3'}),
            "value5": TextInput(attrs={'class': 'form-control', 'placeholder': ' 2.4'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class Thickness_pack_board_form(ModelForm):
    class Meta:
        model = Thickness_pack_board_model
        fields = ['value0', 'value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8',
                  'value9','value10','value11','value12','value13','value14','value15','value16','value17','value18',
                  'value19','value20','value21','value22']
        widgets = {
            "is_customer": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина плиты, мм'}),
            "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 1'}),
            "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 2'}),
            "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 3'}),
            "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 4'}),
            "value5": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 5'}),
            "value6": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 6'}),
            "value7": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 7'}),
            "value8": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 8'}),
            "value9": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 9'}),
            "value10": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 10'}),
            "value11": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 11'}),
            "value12": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 12'}),
            "value13": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 13'}),
            "value14": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 14'}),
            "value15": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 15'}),
            "value16": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 16'}),
            "value17": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 17'}),
            "value18": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 18'}),
            "value19": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 19'}),
            "value20": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 20'}),
            "value21": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 21'}),
            "value22": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 22'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class Thickness_unpolished_pack_board_form(ModelForm):
    class Meta:
        model = Thickness_unpolished_pack_board_model
        fields = ['value0', 'value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8',
                  'value9','value10','value11','value12','value13','value14','value15','value16','value17','value18',
                  'value19','value20','value21','value22','value23','value24']
        widgets = {
            "is_customer": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина плиты, мм'}),
            "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Зад толщ. после пресса, мм'}),
            "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Плит в пакете, шт'}),
            "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 1'}),
            "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 2'}),
            "value5": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 3'}),
            "value6": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 4'}),
            "value7": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 5'}),
            "value8": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 6'}),
            "value9": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 7'}),
            "value10": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 8'}),
            "value11": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 9'}),
            "value12": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 10'}),
            "value13": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 11'}),
            "value14": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 12'}),
            "value15": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 13'}),
            "value16": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 14'}),
            "value17": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 15'}),
            "value18": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 16'}),
            "value19": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 17'}),
            "value20": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 18'}),
            "value21": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 19'}),
            "value22": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 20'}),
            "value23": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 21'}),
            "value24": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 22'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class Thickness_unpolished_board_form(ModelForm):
    class Meta:
        model = Thickness_unpolished_board_model
        fields = ['value0', 'value1', 'value2', 'value3', 'value4', 'value5']
        widgets = {
                "is_customer": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
                "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина плиты, мм'}),
                "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 1'}),
                "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 2'}),
                "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 3'}),
                "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 4'}),
                "value5": TextInput(attrs={'class': 'form-control', 'placeholder': 'Значение 5'}),
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class Number_tapes_form(ModelForm):
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
    number_1_1_choices = forms.ChoiceField(choices=Agg1, label='Выберите зернистость', required=False)
    number_1_1_choices2 = forms.ChoiceField(choices=Agg3, label='Выберите тип ленты', required=False)
    value0 = forms.CharField(max_length=25, label='Введите пробег ленты 1.1', empty_value="", required=False)

    number_1_2_choices = forms.ChoiceField(choices=Agg1, label='Выберите зернистость', required=False)
    number_1_2_choices2 = forms.ChoiceField(choices=Agg3, label='Выберите тип ленты' ,required=False)
    value1 = forms.CharField(max_length=25, label='Введите пробег ленты 1.2', empty_value="", required=False)

    number_2_1_choices = forms.ChoiceField(choices=Agg1, label='Выберите зернистость', required=False)
    number_2_1_choices2 = forms.ChoiceField(choices=Agg3, label='Выберите тип ленты', required=False)
    liner_2_1_choices = forms.ChoiceField(choices=Agg2, label='Выберите вкладыш', required=False)
    value2 = forms.CharField(max_length=25, label='Введите пробег ленты 2.1', empty_value="", required=False)

    number_2_2_choices = forms.ChoiceField(choices=Agg1, label='Выберите зернистость', required=False)
    number_2_2_choices2 = forms.ChoiceField(choices=Agg3, label='Выберите тип ленты', required=False)
    liner_2_2_choices = forms.ChoiceField(choices=Agg2, label='Выберите вкладыш', required=False)
    value3 = forms.CharField(max_length=25, label='Введите пробег ленты 2.2', empty_value="", required=False)

    number_2_3_choices = forms.ChoiceField(choices=Agg1, label='Выберите зернистость', required=False)
    number_2_3_choices2 = forms.ChoiceField(choices=Agg3, label='Выберите тип ленты', required=False)
    liner_2_3_choices = forms.ChoiceField(choices=Agg2, label='Выберите вкладыш', required=False)
    value4 = forms.CharField(max_length=25, label='Введите пробег ленты 2.3', empty_value="", required=False)

    number_2_4_choices = forms.ChoiceField(choices=Agg1, label='Выберите зернистость', required=False)
    number_2_4_choices2 = forms.ChoiceField(choices=Agg3, label='Выберите тип ленты', required=False)
    liner_2_4_choices = forms.ChoiceField(choices=Agg2, label='Выберите вкладыш', required=False)
    value5 = forms.CharField(max_length=25, label='Введите пробег ленты 2.4', empty_value="", required=False)

    class Meta:
        model = Number_tapes_model
        fields = [
                  'number_1_1_choices', 'number_1_1_choices2','value0',
                  'number_1_2_choices', 'number_1_2_choices2','value1',
                  'number_2_1_choices','number_2_1_choices2','value2','liner_2_1_choices',
                  'number_2_2_choices','number_2_2_choices2','value3','liner_2_2_choices',
                  'number_2_3_choices','number_2_3_choices2','value4', 'liner_2_3_choices',
                  'number_2_4_choices','number_2_4_choices2','value5','liner_2_4_choices']
        widgets = {

            "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Пробег 1.1'}),
            "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Пробег 1.2'}),
            "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Пробег 2.1'}),
            "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Пробег 2.2'}),
            "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Пробег 2.3'}),
            "value5": TextInput(attrs={'class': 'form-control', 'placeholder': 'Пробег 2.4'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class Lab_board_form(ModelForm):
    # Number_shift = (
    #     ('choice', 'Выберите смену'),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    # )
    # Number_shift1 = (
    #     ('choice', 'Выберите партию'),
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    # )
    # date_created = forms.DateField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата производства'}),
    #     label="Дата производства")
    # number_shift = forms.ChoiceField(choices=Number_shift,label="Смена производства")
    # number_path = forms.ChoiceField(choices=Number_shift1,label="Партия")
    # value0 = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Заказ'}),
    #                          max_length=4,label="Заказ")
    # value1 = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина, мм'}),
    #                          max_length=2,label="Толщина, мм")
    # value2 = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Длинна, мм'}),
    #                          max_length=4,label="Длинна, мм")
    # value3 = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Количество, шт.'}),
    #                          max_length=1,label="Количество, шт.")
    # value4 = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}),
    #                         max_length=30,required=False,label="Комментарий"),

    class Meta:
        model = Lab_board_model
        fields = ['date_created', 'number_shift', 'number_path', 'value0', 'value1', 'value2','value3','value4' ]
        widgets = {
                "date_created": TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата производства'}),
                # "number_shift": TextInput(attrs={'choices': 'form-control', 'placeholder': 'Смена производства'}),
                # "number_path": TextInput(attrs={'class': 'form-control', 'placeholder': 'Партия'}),
                "value0": TextInput(attrs={'class': 'form-control', 'placeholder': 'Заказ'}),
                "value1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина, мм'}),
                "value2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Длинна, мм'}),
                "value3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Количество, шт.'}),
                "value4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class Press_sap_form(forms.ModelForm):
    """Форма пресс состояние форсунок САП"""

    class Meta:
        model = Press_sap_model
        fields = ['name_form1',
                  'name_form2', 'name_form3', 'name_form4', 'name_form5', 'name_form6',
                  'name_form7', 'name_form8', 'name_form9', 'name_form10', 'name_form11',
                  'name_form12','name_form13','name_form14','name_form15','name_form16',
                  'name_form17','name_form18','name_form19','name_form20','name_form21',
                  'name_form22','name_form23','name_form24','name_form25','name_form26',
                  'name_form27','name_form28','name_form29','name_form30','name_form31',
                  'name_form32','name_form33','name_form34','name_form35']
        # fields = ('__all__')


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'