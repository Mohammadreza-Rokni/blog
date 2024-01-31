from django.shortcuts import render
from blog_post.models import Article
# Create your views here.
def home (request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()[:3]
    return render(request, "home/index.html", {'articles': articles})

# custom 404 view
def custom_404(request, exception):
    return render(request, '404/404.html', status=404)