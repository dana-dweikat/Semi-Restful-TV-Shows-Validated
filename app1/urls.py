from django.urls import path

from . import views
app_name = 'app1'

urlpatterns = [
    path('', views.main, name='shows'),
    path('shows', views.shows, name='shows'),
    path('shows/add', views.add, name='add'),
    path('shows/<str:pk>', views.show, name='show'),
    path('shows/<str:pk>/edit', views.edit_show, name='edit_show'),
    path('shows/<str:pk>/destroy', views.delete_show, name='delete')
]
