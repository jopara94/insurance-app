from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('members/<int:pk>', views.member_detail, name='member_detail'),
    path('members/new', views.member_create, name='member_create'),
    path('members/<int:pk>/edit', views.member_edit, name='member_edit'),
    path('members/<int:pk>/delete', views.member_delete, name='member_delete'),


    path('dependents', views.dependent_list, name='dependent_list'),
    path('dependents/<int:pk>', views.dependent_detail, name='dependent_detail'),
    path('dependents/new', views.dependent_create, name='dependent_create'),
    path('dependents/<int:pk>/edit', views.dependent_edit, name='dependent_edit'),
    path('dependents/<int:pk>/delete', views.dependent_delete, name='dependent_delete')
]
