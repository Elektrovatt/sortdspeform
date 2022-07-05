from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about, name='about-me'),

    path('board', views.List_thickness_board_view.as_view(), name='board'),
    path('create-board', views.Create_thickness_board_view.as_view(), name='create-board'),
    path('update-board/<int:pk>', views.Update_thickness_board_view.as_view(), name='update-board'),
    path('delete-board/<int:pk>', views.Delete_thickness_board_view.as_view(), name='delete-board'),


    path('pack-board', views.List_thickness_pack_board_view.as_view(), name='pack-board'),
    path('create-pack-board', views.Create_thickness_pack_board_view.as_view(), name='create-pack-board'),
    path('update-pack-board/<int:pk>', views.Update_thickness_pack_board_view.as_view(), name='update-pack-board'),
    path('delete-pack-board/<int:pk>', views.Delete_thickness_pack_board_view.as_view(), name='delete-pack-board'),

    path('list-unpolished_board', views.List_thickness_unpolished_board_view.as_view(), name='list-unpolished-board'),
    path('unpolished_board_create', views.Create_thickness_unpolished_board_view.as_view(),
         name='create-unpolished-board'),
    path('unpolished_board_update/<int:pk>', views.Update_thickness_unpolished_board_view.as_view(),
         name='update-unpolished-board'),
    path('unpolished_board_delete/<int:pk>', views.Delete_thickness_unpolished_board_view.as_view(),
         name='delete-unpolished-board'),

    path('list-unpolished_pack_board', views.List_thickness_unpolished_pack_board_view.as_view(),
         name='list-unpolished-pack-board'),
    path('unpolished_board_pack_create', views.Create_thickness_unpolished_pack_board_view.as_view(),
         name='create-unpolished-pack-board'),
    path('unpolished_board_pack_update/<int:pk>', views.Update_thickness_unpolished_pack_board_view.as_view(),
         name='update-unpolished-pack-board'),
    path('unpolished_board_pack_delete/<int:pk>', views.Delete_thickness_unpolished_pack_board_view.as_view(),
         name='delete-unpolished-pack-board'),

    path('list-unpolished_pack_board', views.List_thickness_unpolished_pack_board_view.as_view(),
         name='list-unpolished-pack-board'),
    path('unpolished_board_pack_create', views.Create_thickness_unpolished_pack_board_view.as_view(),
         name='create-unpolished-pack-board'),
    path('unpolished_board_pack_update/<int:pk>', views.Update_thickness_unpolished_pack_board_view.as_view(),
         name='update-unpolished-pack-board'),
    path('unpolished_board_pack_delete/<int:pk>', views.Delete_thickness_unpolished_pack_board_view.as_view(),
         name='delete-unpolished-pack-board'),

    path('list_number_tapes', views.List_number_tapes_view.as_view(),
         name='list-number-tapes'),



    path('list_number_tapes/filter/<int:pk>', views.news_filter, name='news_filter'),

    path('number_tapes_create', views.Create_number_tapes_view.as_view(),
         name='create-number-tapes'),
    path('number_tapes_update/<int:pk>', views.Update_number_tapes_view.as_view(),
         name='update-number-tapes'),
    path('number_tapes_delete/<int:pk>', views.Delete_number_tapes_view.as_view(),
         name='delete-number-tapes'),

    path('list_lab_board', views.List_lab_board_view.as_view(),
         name='list-lab-board'),
    path('lab_board_create', views.Create_lab_board_view.as_view(),
         name='create-lab-board'),
    path('lab_board_update/<int:pk>', views.Update_lab_board_view.as_view(),
         name='update-lab-board'),
    path('lab_board_delete/<int:pk>', views.Delete_lab_board_view.as_view(),
         name='delete-lab-board'),

    path('list_sizes_unpolished_board', views.List_sizes_unpolished_board_view.as_view(),
         name='list-sizes-unpolished-board'),
    path('sizes_unpolished_board_create', views.Create_sizes_unpolished_board_view.as_view(),
         name='create-sizes-unpolished-board'),
    path('sizes_unpolished_board_update/<int:pk>', views.Update_sizes_unpolished_board_view.as_view(),
         name='update-sizes-unpolished-board'),
    path('sizes_unpolished_board_delete/<int:pk>', views.Delete_sizes_unpolished_board_view.as_view(),
         name='delete-sizes-unpolished-board'),

    path('list_cleaning_press_tape', views.List_cleaning_press_tape_view.as_view(),
         name='list-cleaning-press-tape'),
    path('cleaning_press_tape_create', views.Create_cleaning_press_tape_view.as_view(),
         name='create-cleaning-press-tape'),
    path('cleaning_press_tape_update/<int:pk>', views.Update_cleaning_press_tape_view.as_view(),
         name='update-cleaning-press-tape'),
    path('cleaning_press_tape_delete/<int:pk>', views.Delete_cleaning_press_tape_view.as_view(),
         name='delete-cleaning-press-tape'),

    path('list_press_sap', views.List_press_sap_view.as_view(),
         name='list-press-sap'),
    path('press_sap_create', views.Create_press_sap_view.as_view(),
         name='create-press-sap'),
    path('press_sap_update/<int:pk>', views.Update_press_sap_view.as_view(),
         name='update-press-sap'),
    path('press_sap_delete/<int:pk>', views.Delete_press_sap_view.as_view(),
         name='delete-press-sap'),
]