from django.urls import re_path
from comments.views import comment_thread#, comment_delete


urlpatterns = [
        re_path(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
   #     re_path(r'^(?P<id>[\w-]+)/delete/$', comment_delete, name='delete')
        ]

