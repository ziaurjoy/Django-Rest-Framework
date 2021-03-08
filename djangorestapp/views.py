from django.shortcuts import render
from djangorestapp.models import Article
from djangorestapp.serializer import ArticleSirializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSirializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def article_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSirializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def article_update(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except article.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSirializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    

    
@csrf_exempt
def article_delete(register, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.delete()
        return HttpResponse(status=201)
    except article.DoesNotExist:
        return HttpResponse(status=404)
    


