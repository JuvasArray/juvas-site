from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect, redirect


from posts.models import Post
from posts.forms import PostForm

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Succeffuly created')
        return HttpResponsePermanentRedirect(instance.get_absolute_url())
    context = {
            'form': form
            }
    return render(request, 'post_form.html', context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
            'title': instance.title,
            'instance': instance,
            }
    return render(request, 'post_detail.html', context)

def post_list(request):
    queryset_list = Post.objects.all()
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

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Succeffuly updated')
        return HttpResponsePermanentRedirect(instance.get_absolute_url())

    context = {
            'title': instance.title,
            'instance': instance,
            'form': form
            }
    return render(request, 'post_form.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Succeffuly deleted')
    return redirect('list')


