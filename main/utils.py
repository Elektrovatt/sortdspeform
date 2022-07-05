from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages


menu = [{'title_place': "Шлифовка", 'name_form': 'Толщина Шлифованой плиты', 'url_name': 'board'},
        {'title_place': "Шлифовка", 'name_form': 'Учёт шлифовальных материалов', 'url_name': 'list-number-tapes'},
        {'title_place': "Шлифовка", 'name_form': 'Толщина пакета шлифованной плиты', 'url_name': 'pack-board'},
        {'title_place': "Пресс", 'name_form': 'Форма контроля раб. состояния форсунок САП', 'url_name': 'list-press-sap'},
        {'title_place': "Пресс", 'name_form': 'Форма очистки лент преса', 'url_name': 'list-cleaning-press-tape'},
        {'title_place': "Пресс", 'name_form': 'Толщина нешлифованой плиты', 'url_name': 'list-unpolished-board'},
        {'title_place': "Пресс", 'name_form': 'Производственные параметры для пресовщика', 'url_name': 'home'},
        {'title_place': "Распиловка", 'name_form': 'Учёт замены чернильной системы', 'url_name': 'home'},
        {'title_place': "Распиловка", 'name_form': 'Измерение покоробленности', 'url_name': 'home'},
        {'title_place': "Распиловка", 'name_form': 'Толщина пакета нешлифованой плиты', 'url_name': 'list-unpolished-pack-board'},
        {'title_place': "Распиловка", 'name_form': 'Лабораторные образцы', 'url_name': 'list-lab-board'},
        {'title_place': "Распиловка", 'name_form': 'Размеры нешлифованной ДСП', 'url_name': 'list-sizes-unpolished-board'},

]


class CustomSuccessMessageMixin:
    """для появления записи о обновления поля или добавлении нового  подсвечивается редактированая запись."""

    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class CustomFormValidMixin:


    def form_valid(self, form):
        """"
        Переопределение формы валидации для добавления автора в базу
        """""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class CustomGetFormUpdateMixin:
    success_msg = 'Запись успешно обнавлена'

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_form_kwargs(self):
        """"Переопределяем метод для редактирования Только своей записи"""""
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class CustomPostDeleteMixin:
    success_msg = 'Запись удалена'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['update'] = True
    #     context['menu'] = menu
    #     return context

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
