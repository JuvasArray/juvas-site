from django.urls import path
from posts.views import post_create, post_detail, post_list, post_update, post_delete


urlpatterns = [
        path('create', post_create, name='create'),
        path('detail/<int:id>', post_detail, name='detail'),
        path('home', post_list, name='list'),
        path('<int:id>/edit', post_update, name='update'),
        path('<int:id>/delete', post_delete, name='delete')
        ]
