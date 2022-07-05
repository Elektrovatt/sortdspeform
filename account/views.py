from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib.auth.models import Group
from .forms import profile_form, ProfileForm
from .models import *
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib import auth


from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView


# Create your views here.

class MyprojectLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_page')
    success_msg = 'Пользователь успешно создан'

    def form_invalid(self, form):
        form_valid = super().form_valid(form)
        username = form.clened_data["username"]
        password = form.clened_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('home')


class ProfileView(LoginRequiredMixin, DetailView):
    """""Профиль пользователя """""
    model = ProfileUserModel
    template_name = 'account/profile.html'
    context_object_name = 'profile'
    form_class = profile_form

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context



menu = [{'title_place': "Шлифовка", 'name_form': 'Толщина Шлифованой плиты', 'url_name': 'board'},
        {'title_place': "Шлифовка", 'name_form': 'Учёт шлифовальных материалов', 'url_name': 'list-number-tapes'},
        {'title_place': "Шлифовка", 'name_form': 'Толщина пакета шлифованной плиты', 'url_name': 'pack-board'},
        {'title_place': "Пресс", 'name_form': 'Форма контроля раб. состояния форсунок САП', 'url_name': 'list-press-sap'},
        {'title_place': "Пресс", 'name_form': 'Форма очистки лент преса', 'url_name': 'list-cleaning-press-tape'},
        {'title_place': "Пресс", 'name_form': 'Толщина нешлифованой плиты', 'url_name': 'list-unpolished-board'},
        {'title_place': "Пресс", 'name_form': 'Производственные параметры для пресовщика', 'url_name': 'about-me'},
        {'title_place': "Распиловка", 'name_form': 'Учёт замены чернильной системы', 'url_name': 'about-me'},
        {'title_place': "Распиловка", 'name_form': 'Измерение покоробленности', 'url_name': 'about-me'},
        {'title_place': "Распиловка", 'name_form': 'Толщина пакета нешлифованой плиты', 'url_name': 'list-unpolished-pack-board'},
        {'title_place': "Распиловка", 'name_form': 'Лабораторные образцы', 'url_name': 'list-lab-board'},
        {'title_place': "Распиловка", 'name_form': 'Размеры нешлифованной ДСП', 'url_name': 'list-sizes-unpolished-board'},

]

class ProfileUpdate(LoginRequiredMixin, UpdateView):
        """"Редактирование профиля"""""

        model = ProfileUserModel
        template_name = "account/profile_update.html"
        context_object_name = 'profile'
        form_class = ProfileForm
        # вместо форм клсс сделано филдс, что бы не отображать юзера.
        success_url = reverse_lazy('home')
        success_msg = 'Запись успешно обнавлена'
        # fields = ['is_customer','is_customer2','value1','value2','value3']


        def get_context_data(self, **kwargs):
            kwargs['update'] = True
            context = super().get_context_data(**kwargs)
            return context

        def form_valid(self, form):
            return super().form_valid(form)
            # Переопределение формы валидации для добавления автора в базу


        def get_form_kwargs(self):
            """"Переопределяем метод для редактирования Только своей записи"""""

            kwargs = super().get_form_kwargs()
            if self.request.user != kwargs['instance'].user:
                return self.handle_no_permission()
            return kwargs


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = AuthUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,('Ваш профиль был успешно обновлен!'))
            return redirect('settings:profile')
        else:
            messages.error(request,('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = AuthUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form})