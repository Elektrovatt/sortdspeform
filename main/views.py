from django.http import HttpResponse, HttpResponseRedirect
from account.models import ProfileUserModel
from django_filters.views import FilterView

from .forms import *
from .models import *
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *
from datetime import datetime, timedelta
import django_filters

def index(request):
    #profile заменить на profile_queryset - улучшить читаемсоть
    profile = ProfileUserModel.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'profile': profile,
    }

    return render(request, 'main/index.html', context=context)




"""" Начало {'title_place': "Шлифовка",'name_form':'Толщина Шлифованой плиты', 'url_name': 'board'} """

# {% for book in books|dictsort:"author.age" %}
#  * {{ book.title }} ({{ book.author.name }})
# {% endfor %}   попробовать выводить на главную страницу профиль...


class CustomBaseThicknessBoard:
    """Базовый класс для формы по измерению Толщины Плиты
    Чтобы не повторять get_context_data, model and success_url - вынесены в этот класс
    кроме -  form_class"""
    model = Thickness_board_model
    success_url = reverse_lazy('board')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['list_records_queryset'] = Thickness_board_model.objects.all().order_by('-date_created')
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'board'
        context['menu'] = menu
        return context


class List_thickness_board_view(CustomBaseThicknessBoard, ListView):
    """" Класс для отображения всех записей. Cмена, дата измерения плиты
    таблица измерений толщины плиты"""
    template_name = 'main/shlifovka/list_board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Толщина плиты'}


class Create_thickness_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin,
                                  CustomBaseThicknessBoard, CreateView):
    """Класс для создания новой записи с измерениями толщины плиты."""
    form_class = Thickness_board_form
    template_name = 'main/shlifovka/create_new_board.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Толщина плиты'}


class Update_thickness_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin,
                                  CustomBaseThicknessBoard, CustomGetFormUpdateMixin, UpdateView):
    """Класс для редактирования записи"""
    form_class = Thickness_board_form
    success_msg = 'Запись успешно обнавлена'
    template_name = 'main/update.html'
    extra_context = {'title': 'Изменение значений толщины плиты'}


class Delete_thickness_board_view(LoginRequiredMixin, CustomPostDeleteMixin, CustomBaseThicknessBoard, DeleteView):
    template_name = 'main/delete.html'
    extra_context = {'title': 'Форма для удаления плиты.'}


"""
  Конец {'title_place': "Шлифовка",'name_form':'Толщина Шлифованой плиты', 'url_name': 'board'}
"""
"""
 Начало {'title_place': "Шлифовка",'name_form':'Толщина пакета шлифованной плиты', 'url_name': 'pack-board'} 
"""


class CustomBaseThicknessPackBoad:
    model = Thickness_pack_board_model
    success_url = reverse_lazy('pack-board')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['list_records_queryset'] = Thickness_pack_board_model.objects.all().order_by('-date_created')
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'pack-board'
        context['menu'] = menu
        return context

class List_thickness_pack_board_view(CustomBaseThicknessPackBoad, ListView):
    """ Класс для отображения всех записей. Cмена, дата измерения пачки
    таблица измерений толщины пачки    """
    template_name = 'main/shlifovka/list_pack_board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Толщина пачки шлифованой плиты'}


class Create_thickness_pack_board_view(LoginRequiredMixin,
                                       CustomSuccessMessageMixin,
                                       CustomFormValidMixin,
                                       CustomBaseThicknessPackBoad,
                                       CreateView):
    """Класс для создания новой записи с измерениями пачки. """

    template_name = 'main/shlifovka/create_new_pack_board.html'
    form_class = Thickness_pack_board_form
    success_msg = 'Запись создана'
    extra_context = {'title': 'Форма    по    добавлению   значений   отшлифованой    пачки'}


class Update_thickness_pack_board_view(LoginRequiredMixin,
                                       CustomSuccessMessageMixin,
                                       CustomFormValidMixin,
                                       CustomBaseThicknessPackBoad,
                                       CustomGetFormUpdateMixin,
                                       UpdateView):
    """Класс для редактирования записи"""
    template_name = 'main/shlifovka/create_new_pack_board.html'
    form_class = Thickness_pack_board_form
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Форма для редактирования значений толщины пачки'}


class Delete_thickness_pack_board_view(LoginRequiredMixin,
                                       CustomPostDeleteMixin,
                                       CustomBaseThicknessPackBoad,
                                       DeleteView):
    template_name = 'main/delete.html'
    extra_context = {'title': 'Форма для удаления значений толщины пачки.'}


"""
Конец {'title_place': "Шлифовка",'name_form':'Толщина пакета шлифованной плиты', 'url_name': 'pack-board'}
"""
"""
Начало {'title_place': "Шлифовка",'name_form':'Учёт шлифовальных материалов', 'url_name': 'number-tapes'}
"""


class BaseNumberTapes:
    model = Number_tapes_model
    success_url = reverse_lazy('list-number-tapes')

    def get_context_data(self, *, object_list=None, **kwargs):
        now = datetime.today() - timedelta(minutes=60 * 24 * 7)
        # filter = filter.filter(date_created__gte=now)
        kwargs['list_records_queryset'] = Number_tapes_model.objects.all().order_by('-date_created')
        # kwargs['list'] = Number_tapes_model.objects.all().filter(date_created='2021-06-08')
        # kwargs['list'] = Number_tapes_model.objects.filter(date_created__gte=now)
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-number-tapes'
        context['menu'] = menu
        return context

    def get_queryset(self):
        now = datetime.today() - timedelta(minutes=60 * 24 * 7)
        return Number_tapes_model.objects.filter(date_created__gte=now)

def news_filter(request, pk):
    filter = Number_tapes_model.objects.all()
    if pk == 1:
        now = datetime.today() - timedelta(minutes=60 * 24 * 7)
        filter = filter.filter(date_created__gte=now)
    elif pk == 2:
        now = datetime.today() - timedelta(minutes=60 * 24 * 30)
        filter = filter.filter(date_created__gte=now)
    elif pk == 3:
        filter = filter
    return render(request, 'main/shlifovka/list.html', {'filter': filter})




class List_number_tapes_view(BaseNumberTapes, ListView):
    template_name = 'main/shlifovka/list_number_tapes.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Шлифовальные ленты'}



class Create_number_tapes_view(LoginRequiredMixin,
                               CustomSuccessMessageMixin,
                               CustomFormValidMixin,
                               BaseNumberTapes,
                               CreateView):
    form_class = Number_tapes_form
    template_name = 'main/shlifovka/create_new_number_tapes.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Шлифовальные ленты'}


class Update_number_tapes_view(LoginRequiredMixin,
                               CustomSuccessMessageMixin,
                               CustomFormValidMixin,
                               BaseNumberTapes,
                               CustomGetFormUpdateMixin,
                               UpdateView):
    form_class = Number_tapes_form
    template_name = 'main/shlifovka/create_new_number_tapes.html'
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений пробега лент'}

        # context = super(BookListView, self).get_context_data(**kwargs)
        # # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        # context['some_data'] = 'This is just some data'
        # return context


class Delete_number_tapes_view(LoginRequiredMixin,
                               CustomPostDeleteMixin,
                               BaseNumberTapes,
                               DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления записи'}


"""
Конец {'title_place': "Шлифовка",'name_form':'Учёт шлифовальных лент', 'url_name': 'number-tapes'}
"""
"""
Начало {'title_place': "Пресс",'name_form':'Толщина нешлифованой плиты', 'url_name': 'list-unpolished-board'}
"""


class CustomBaseThicknessUnpolishedBoad:
    model = Thickness_unpolished_board_model
    success_url = reverse_lazy('list-unpolished-board')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['list_records_queryset'] = Thickness_unpolished_board_model.objects.all().order_by('-date_created')
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-unpolished-board'
        context['menu'] = menu
        return context


class List_thickness_unpolished_board_view(CustomBaseThicknessUnpolishedBoad,
                                           ListView):
    """ Класс для отображения всех записей. Cмена, дата измерения плиты
    таблица измерений толщины плиты, тоже самое что и def add_table_thickness_ground_plate(request):"""
    template_name = 'main/press/list_unpolished_board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Толщина нешлифованой плиты'}


class Create_thickness_unpolished_board_view(LoginRequiredMixin,
                                             CustomSuccessMessageMixin,
                                             CustomFormValidMixin,
                                             CustomBaseThicknessUnpolishedBoad,
                                             CreateView):
    """"Класс для создания новой записи с измерениями толщины плиты. :"""
    template_name = 'main/press/create_new_thickness_unpolished_board.html'
    form_class = Thickness_unpolished_board_form
    success_msg = 'Запись создана'
    extra_context = {'title': 'Толщина нешлифованой плиты'}


class Update_thickness_unpolished_board_view(LoginRequiredMixin,
                                             CustomSuccessMessageMixin,
                                             CustomFormValidMixin,
                                             CustomGetFormUpdateMixin,
                                             CustomBaseThicknessUnpolishedBoad,
                                             UpdateView):
    template_name = 'main/press/create_new_thickness_unpolished_board.html'
    form_class = Thickness_unpolished_board_form
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений  толщины нешлифованой плиты'}


class Delete_thickness_unpolished_board_view(LoginRequiredMixin,
                                             CustomPostDeleteMixin,
                                             CustomBaseThicknessUnpolishedBoad,
                                             DeleteView):
    template_name = 'main/delete.html'
    extra_context = {'title': 'Форма для удаления значений нешлифованой плиты.'}


"""
Конец {'title_place': "Пресс",'name_form':'Толщина нешлифованой плиты', 'url_name': 'list-unpolished-board'}
"""


""" 
Начало {'title_place': "Распиловка",'name_form':'Толщина пакета нешлифованой плиты', 'url_name': 'list-unpolished-pack-board'} 
"""


class BaseThicknessUnpolishedPackBoard:
    model = Thickness_unpolished_pack_board_model
    success_url = reverse_lazy('list-unpolished-pack-board')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['list_records_queryset'] = Thickness_unpolished_pack_board_model.objects.all().order_by('-date_created')
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-unpolished-pack-board'
        context['menu'] = menu
        return context


class List_thickness_unpolished_pack_board_view(BaseThicknessUnpolishedPackBoard,
                                                ListView):
    """ Класс для отображения всех записей. Cмена, дата измерения плиты
        таблица измерений толщины нешлифованой пачки
    """

    template_name = 'main/raspilovka/list_pack_unpolished_board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Толщина пакета нешлифованой плиты'}


class Create_thickness_unpolished_pack_board_view(LoginRequiredMixin,
                                                  CustomSuccessMessageMixin,
                                                  CustomFormValidMixin,
                                                  BaseThicknessUnpolishedPackBoard,
                                                  CreateView):
    """"Класс для создания новой записи с измерениями толщины пакета нешлифованой плиты."""""

    template_name = 'main/raspilovka/create_new_pack_unpolished_board.html'
    form_class = Thickness_unpolished_pack_board_form
    success_msg = 'Запись создана'
    extra_context = {'title': 'Толщина пакета нешлифованой плиты'}


class Update_thickness_unpolished_pack_board_view(LoginRequiredMixin,
                                                  CustomSuccessMessageMixin,
                                                  CustomFormValidMixin,
                                                  BaseThicknessUnpolishedPackBoard,
                                                  CustomGetFormUpdateMixin,
                                                  UpdateView):
    template_name = 'main/raspilovka/create_new_pack_unpolished_board.html'
    form_class = Thickness_unpolished_pack_board_form
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений  толщины пакета нешлифованой плиты'}


class Delete_thickness_unpolished_pack_board_view(LoginRequiredMixin,
                                                  BaseThicknessUnpolishedPackBoard,
                                                  CustomPostDeleteMixin,
                                                  DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления значений пачки нешлифованой плиты.'}


"""
Конец {'title_place': "Распиловка",'name_form':'Толщина пакета нешлифованой плиты', 'url_name': 'list-unpolished-pack-board'}
"""

"""
Начало {'title_place': "Распиловка",'name_form':'Лабораторные образцы', 'url_name': 'list-lab-board'}
"""


class BaseLabBoard:
    model = Lab_board_model
    success_url = reverse_lazy('list-lab-board')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['list_records_queryset'] = Lab_board_model.objects.all().order_by('-date_created')
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-lab-board'
        context['menu'] = menu
        return context


class List_lab_board_view(BaseLabBoard, ListView):
    template_name = 'main/raspilovka/list_lab_board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Лабораторные образцы'}


class Create_lab_board_view(LoginRequiredMixin,
                            CustomSuccessMessageMixin,
                            CustomFormValidMixin,
                            BaseLabBoard,
                            CreateView):
    form_class = Lab_board_form
    template_name = 'main/raspilovka/create_new_lab_board.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Лабораторные образцы'}


class Update_lab_board_view(LoginRequiredMixin,
                            CustomSuccessMessageMixin,
                            CustomFormValidMixin,
                            BaseLabBoard,
                            CustomGetFormUpdateMixin,
                            UpdateView):
    form_class = Lab_board_form
    template_name = 'main/raspilovka/create_new_lab_board.html'
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений о лабораторном образце'}


class Delete_lab_board_view(LoginRequiredMixin,
                            CustomPostDeleteMixin,
                            BaseLabBoard,
                            DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления записи лабораторного образца'}


"""
Конец {'title_place': "Распиловка",'name_form':'Лабораторные образцы', 'url_name': 'list-lab-board'}
"""



"""
Начало {'title_place': "Распиловка",'name_form':'Размеры нешлифованной ДСП', 'url_name': 'list-sizes-unpolished-board'}
"""


class BaseSizesUnpolishedBoard:
    model = Sizes_unpolished_board_model
    success_url = reverse_lazy('list-sizes-unpolished-board')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['list_records_queryset'] = Sizes_unpolished_board_model.objects.all().order_by('-date_created')
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-sizes-unpolished-board'
        context['menu'] = menu
        return context


class List_sizes_unpolished_board_view(BaseSizesUnpolishedBoard, ListView):
    template_name = 'main/raspilovka/list_sizes_unpolished_board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Размеры нешлифованной ДСП'}


class Create_sizes_unpolished_board_view(LoginRequiredMixin,
                                         CustomSuccessMessageMixin,
                                         CustomFormValidMixin,
                                         BaseSizesUnpolishedBoard,
                                         CreateView):
    form_class = Sizes_unpolished_board_form
    template_name = 'main/raspilovka/create_new_sizes_unpolished_board.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Размеры нешлифованной ДСП'}


class Update_sizes_unpolished_board_view(LoginRequiredMixin,
                                         CustomSuccessMessageMixin,
                                         CustomFormValidMixin,
                                         BaseSizesUnpolishedBoard,
                                         CustomGetFormUpdateMixin,
                                         UpdateView):
    form_class = Sizes_unpolished_board_form
    template_name = 'main/raspilovka/create_new_sizes_unpolished_board.html'
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений размеров нешлифованной ДСП'}


class Delete_sizes_unpolished_board_view(LoginRequiredMixin,
                                         CustomPostDeleteMixin,
                                         BaseSizesUnpolishedBoard,
                                         DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления записи'}


"""
Конец {'title_place': "Распиловка",'name_form':'Размеры нешлифованной ДСП', 'url_name': 'list-sizes-unpolished-board'}
"""




"""
Начало {'title_place': "Пресс", 'name_form': 'Форма очистки лент преса', 'url_name': 'cleaning-press-tape'},
"""


class BaseCleaningPressTape:
    model = Cleaning_press_tape_model
    success_url = reverse_lazy('list-cleaning-press-tape')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['list_records_queryset'] = Cleaning_press_tape_model.objects.all().order_by('-date_created')
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-cleaning-press-tape'
        context['menu'] = menu
        return context


class List_cleaning_press_tape_view(BaseCleaningPressTape, ListView):
    template_name = 'main/press/list_cleaning_press_tape.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Форма очистки ленты пресса'}


class Create_cleaning_press_tape_view(LoginRequiredMixin,
                                      CustomSuccessMessageMixin,
                                      CustomFormValidMixin,
                                      BaseCleaningPressTape,
                                      CreateView):
    form_class = Сleaning_press_tape_form
    template_name = 'main/press/create_cleaning_press_tape.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Новая форма очистки ленты пресса'}


class Update_cleaning_press_tape_view(LoginRequiredMixin,
                                      CustomSuccessMessageMixin,
                                      CustomFormValidMixin,
                                      BaseCleaningPressTape,
                                      CustomGetFormUpdateMixin,
                                      UpdateView):
    form_class = Сleaning_press_tape_form
    template_name = 'main/press/create_cleaning_press_tape.html'
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений  формы очистки ленты пресса'}


class Delete_cleaning_press_tape_view(LoginRequiredMixin,
                                      CustomPostDeleteMixin,
                                      BaseCleaningPressTape,
                                      DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления записи'}


"""
Конец {'title_place': "Пресс", 'name_form': 'Форма очистки лент преса', 'url_name': 'cleaning-press-tape'},
"""




"""
Начало {'title_place': "Пресс", 'name_form': 'Форма sap', 'url_name': 'press-sap'},
"""


class BasePressSap:
    model = Press_sap_model
    success_url = reverse_lazy('list-press-sap')

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['list_records_queryset'] = Press_sap_model.objects.all().order_by('-date_created')
        kwargs['update'] = True
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-press-sap'
        context['menu'] = menu
        return context


class List_press_sap_view(BasePressSap,
                          ListView):
    template_name = 'main/press/list_press_sap.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Форма контроля рабочего состояния форсунок САП'}


class Create_press_sap_view(LoginRequiredMixin,
                            CustomSuccessMessageMixin,
                            CustomFormValidMixin,
                            BasePressSap,
                            CreateView):
    form_class = Press_sap_form
    template_name = 'main/press/create_press_sap.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Новая Форма контроля рабочего состояния форсунок САП'}


class Update_press_sap_view(LoginRequiredMixin,
                            CustomSuccessMessageMixin,
                            CustomFormValidMixin,
                            BasePressSap,
                            CustomGetFormUpdateMixin,
                            UpdateView):
    form_class = Press_sap_form
    template_name = 'main/press/create_press_sap.html'
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений  формы оконтроля рабочего состояния форсунок САП'}


class Delete_press_sap_view(LoginRequiredMixin,
                            CustomPostDeleteMixin,
                            BasePressSap,
                            DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления записи'}


"""
Конец {'title_place': "Пресс", 'name_form': 'Форма очистки лент преса', 'url_name': 'press-sap'},
"""



def about(request):
    return render(request, 'main/about.html')








# def delete(request,pk):
#     get_plate = table_thickness_ground_plate_model.objects.get(pk=pk)
#     get_plate.delete()
#     return redirect(reverse('plate'))

# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = create_thickness_ground_plate_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('plate')
#         else: 'Форма была не верной'
#     form = create_thickness_ground_plate_form()
#     context = {
#         'form': form,
#         'error': error
#                 }
#     return render(request, 'main/create_new_thickness_ground_plate.html', context)

# def add_table_thickness_ground_plate(request):
#   тоже самое что и class table_thickness_ground_plate_view(ListView):
#     list_value = Add_table_thickness_ground_plate.objects.all()
#     context = {
#     'list_value':list_value,
#        }
#     return render(request, 'main/plate.html', context)

# def update_table(request, pk):
#     get_plate = table_thickness_ground_plate_model.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = create_thickness_ground_plate_form(request.POST, instance = get_plate)
#         if form.is_valid():
#             form.save()
#             return redirect('plate')
#     template = 'main/update.html'
#     context = {
#             'get_plate': get_plate,
#             'update':True,
#             'form':create_thickness_ground_plate_form(instance = get_plate),
#     }
#     return render(request, template, context)