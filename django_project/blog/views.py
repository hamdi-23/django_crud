from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'judul': 'si pitung',
        'penerbit': 'PT.Aduglajer',
        'banner': 'img/banner_blog.png',
    }
    return render(request, 'index.html', context)


def cerita(request):
    context = {
        'judul': 'si pitung dari dalam teko',
        'penulis': 'mandra',
    }
    return render(request, 'blog/cerita.html', context)


def news(request):
    context = {
        'judul': 'si pitung naik tangkal',
        'penulis': 'mang odading',
    }
    return render(request, 'blog/cerita.html', context)
