from django.urls import path
from .views import articles, articles_archive, article, article_archive, article_slug, main_page

urlpatterns = [
    path('', main_page, name='index'),
    path('articles/', articles, name='articles'),
    path('articles/archive', articles_archive, name='articles_archive'),
    path('article/<int:article_id>', article, name='article'),
    path('article/<int:article_id>/archive', article_archive, name='article_archive'),
    path('article/<int:article_id>/<slug:slug>', article_slug, name='article_slug'),
    # path('bla/', form_user, name='form-user'),
]
