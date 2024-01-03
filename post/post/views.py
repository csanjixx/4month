from django.shortcuts import redirect, render
from django.http import HttpResponse
from post.models import Post, Comments, Hashtag
from post.forms import PostForm, PostForm2


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(
            request,
            'post/list.html',
            context=context
        )


def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return render(request, '404.html')

        context = {
            'post': post,
        }
        return render(
            request,
            'post/detail.html',
            context=context
        )


def hashtag_list_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()
        context = {
            'hashtags': hashtags,
        }
        return render(
            request,
            'hashtag/list.html',
            context=context
        )


def posts_create_view(requests):
    if requests.method == 'GET':
        context = {
            'form': PostForm2,
        }
        return render(requests, 'post/create.html', context=context)
    if requests.method == 'POST':
        form = PostForm2(requests.POST, requests.FILES)

        if form.is_valid():
            form.save()

            return redirect('/posts/')
        else:
            context = {
                'form': form,
            }
            return render(requests, 'post/create.html', context=context)