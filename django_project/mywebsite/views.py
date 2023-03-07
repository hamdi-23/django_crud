from django.shortcuts import render


def index(request):
    context = {
        'judul': 'kelas terbuka',
        'kontributor': 'hamdi abdul aziz',
        'banner': 'img/banner_home.png',
        # 'nav': [
        #     ['/', 'home'],
        #     ['/blog', 'blog'],
        #     ['/ about', 'about'],
        # ]

    }

    return render(request, 'index.html', context)
