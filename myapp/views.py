import random
import string

from django.http import HttpResponse
from django.shortcuts import render
from random import randint, choice


def main_page(request):
    return render(request, 'index.html', {
        "article_id": randint(1, 1000),
        "slug": ''.join(choice(string.ascii_lowercase) for i in range(randint(3, 10)))
    })


def phone_number(request, phone):
    return HttpResponse(f"Phone number is: {phone}")


def uuid_short(request, uuid):
    return HttpResponse(f"UUID is: {uuid}")


def articles(request):
    return render(request, 'articles.html')


def articles_archive(request):
    return render(request, 'articles_archive.html')


def article(request, article_id):
    return render(request, 'article.html', {
        'article_id': article_id,
    })


def article_archive(request, article_id):
    return HttpResponse(f'Article archive for: {article_id}')


def article_slug(request, article_id, slug):
    return render(request, 'article.html', {
        'article_id': article_id,
        'slug': slug
    })


def users(request):
    return render(request, 'users.html')


def user(request, user_id):
    return HttpResponse(f'User id is: {user_id}')


# def form_user(request):
#     render(request, 'form_user.html')
