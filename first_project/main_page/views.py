from django.shortcuts import render
from django.http import HttpResponse

def starting_main_page(request):

    return HttpResponse('Main page')

def all_posts(request):

    return HttpResponse('<h1>All posts</h1>')