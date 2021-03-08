from django.shortcuts import render
from djangorestapp.models import Article
from djangorestapp.serializer import ArticleSirializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.


# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSirializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)



# @csrf_exempt
# def article_create(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSirializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)



# @csrf_exempt
# def article_update(request, article_id):
#     try:
#         article = Article.objects.get(id=article_id)
#     except article.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSirializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    


# @csrf_exempt
# def article_delete(register, article_id):
#     try:
#         article = Article.objects.get(id=article_id)
#         article.delete()
#         return HttpResponse(status=201)
#     except article.DoesNotExist:
#         return HttpResponse(status=404)


# Requests and Responses


@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSirializer(articles, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def article_create(request):
    if request.method == 'POST':
        article_obj_serializer = ArticleSirializer(data=request.data)
        if article_obj_serializer.is_valid():
            article_obj_serializer.save()
            return Response(article_obj_serializer.data, status=status.HTTP_201_CREATED)
        return Response(article_obj_serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def article_update(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        article_update_serializer = ArticleSirializer(article, data=request.data)
        if article_update_serializer.is_valid():
            article_update_serializer.save()
            return Response(article_update_serializer.data)
        return Response(article_update_serializer.errors, status = status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def article_delete(register, article_id):
    try:
        article_object = Article.objects.get(id=article_id)
        article_object.delete()
        return Response(status=status.HTTP_201_CREATED)
    except article_object.DoesNotExist:
        return Response(article_object.errors, status = status.HTTP_400_BAD_REQUEST)
    






