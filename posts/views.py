from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect, redirect, Http404
from django.utils import timezone

from posts.models import Post
from posts.forms import PostForm

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Succeffuly created')
        return HttpResponsePermanentRedirect(instance.get_absolute_url())
    context = {
            'form': form
            }
    return render(request, 'post_form.html', context)

def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
            'title': instance.title,
            'instance': instance,
            }
    return render(request, 'post_detail.html', context)

def post_list(request):
    queryset_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    query = request.GET.get('query')
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains=query) |
               Q(content__icontains=query) | 
               Q(user__first_name__icontains=query) |
               Q(user__last_name__icontains=query) ).distinct()
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.get_page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
            'object_list': queryset,
            'title': 'List',
            }
    return render(request, 'post_list.html', context)

def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Succeffuly updated')
        return HttpResponsePermanentRedirect(instance.get_absolute_url())

    context = {
            'title': instance.title,
            'instance': instance,
            'form': form
            }
    return render(request, 'post_form.html', context)

def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'Succeffuly deleted')
    return redirect('list')


