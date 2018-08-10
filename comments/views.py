from django.shortcuts import render, get_object_or_404

# Create your views here.

from comments.models import Comment

def comment_thread(request, id):
    comment = get_object_or_404(Comment, id=id)
    context = {
            'comment': comment,
            }

    return render(request, 'comment_thread.html', context)
