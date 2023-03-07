from django.shortcuts import render


def index(request):
    context = {
        'judul': 'tentang',
        'nama': 'hamdi abdul azz',
        'banner': 'img/banner_about.png',

    }
    return render(request, 'index.html', context)


# def index(request):
#     context = {
#         'judul': 'si pitung',
#         'nama': 'PT.Aduglajer',
#     }
#     return render(request, 'about/index.html', context)
