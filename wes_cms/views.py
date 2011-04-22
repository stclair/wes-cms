from django.views.generic.list_detail import object_detail

from wes_cms.models import Article, Navigation, NavigationHeader

nav_headers = NavigationHeader.objects.all()

def index(request):
    nav = Navigation.objects.get_first()
    return object_detail(request, Article.objects.all(), slug=nav.article.slug, extra_context={'nav_headers': nav_headers})