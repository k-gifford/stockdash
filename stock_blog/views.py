from django.shortcuts import render

# dummy posts
posts = [
    {
        'author': 'Kealan Gifford',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '12 February 2019'
    },
    {
        'author': 'Kealan Gifford',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '15 February 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'stock_blog/home.html', context)

def about(request):
    return render(request, 'stock_blog/about.html', {'title': 'About'})
