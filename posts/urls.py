from django.urls import path, re_path, include
from posts.views import post_create, post_detail, post_list, post_update, post_delete


urlpatterns = [
        path('create', post_create, name='create'),
        re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
        re_path('list', post_list, name='list'),
        re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
        re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
        path('froala_editor', include('froala_editor.urls')),
        ]
