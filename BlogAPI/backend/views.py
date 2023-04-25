from django.shortcuts import render,HttpResponse
from .models import Articles
from .serializers import ArticleSerializer,ArticleModelSerializer
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor



#  % FUNCTION BASED API VIEW SECTION %
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

#  %   @API_VIEW DECORATOR SECTION  %
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#  % CLASS BASED APIVIEW SECTION  %
from rest_framework.views import APIView
from django.http import Http404


#  % MIXINS AND GENERICS APIVIEW SECTION  %
from rest_framework import mixins
from rest_framework import generics

#  % VIEWSETS APIVIEW SECTION  %
from rest_framework import viewsets



# % MODEL VIEWSETS APIVIEW SECTION   %
class ArticleViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsAuthor, ]
    authentication_classes = (TokenAuthentication, SessionAuthentication,)

    queryset = Articles.objects.all()
    lookup_field = 'slug'
    serializer_class = ArticleModelSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

'''
# % GENERIC VIEWSETS APIVIEW SECTION   %
class ArticleViewset(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Articles.objects.all()
    lookup_field = 'slug'
    serializer_class = ArticleModelSerializer
'''


'''
# % VIEWSETS APIVIEW SECTION   %
class ArticleViewset(viewsets.ViewSet):
    def list(self,request):
        articles = Articles.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
'''


'''
# % GENERICS APIVIEW SECTION   %
class ArticlesList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleModelSerializer

class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Articles.objects.all()
    serializer_class = ArticleModelSerializer
'''


'''
# % MIXINS APIVIEW SECTION   %
class ArticlesList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = Articles.objects.all()
    serializer_class = ArticleModelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class ArticleDetails(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):

    queryset = Articles.objects.all()
    lookup_field = 'slug'
    serializer_class = ArticleModelSerializer

    def get(self, request,slug, *args, **kwargs):
        return self.retrieve(request,slug ,*args, **kwargs)

    def put(self,request,slug,*args,**kwargs):
        return self.update(request,slug,*args,**kwargs)

    def delete(self, request, slug, *args, **kwargs):
        return self.destroy(request, slug, *args, **kwargs)
'''


'''
# % CLASS BASED APIVIEW SECTION  %
class ArticlesList(APIView):
    def get(self,request):
        articles = Articles.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_object(self,slug):
        try:
            return Articles.objects.get(slug = slug)
        except Articles.DoesNotExist:
            raise Http404


    def get(self,request,slug):
        article = self.get_object(slug)
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    def put(self,request,slug):
        article = self.get_object(slug)
        serializer = ArticleModelSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,slug):
        article = self.get_object(slug)
        article.delete()
        return Response('article deleted',status=status.HTTP_204_NO_CONTENT)
'''


'''
# %   @API_VIEW DECORATOR SECTION   %

@api_view(['GET','POST'])
def article_list(request):
    if request.method =='GET':
        article = Articles.objects.all()
        serializer = ArticleModelSerializer(article,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def article_details(request,slug):
    try:
        article = Articles.objects.get(slug=slug)
    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = ArticleModelSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response('article deleted', status=status.HTTP_204_NO_CONTENT)
'''


'''
# % FUNCTION BASED API VIEW SECTION %

@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Articles.objects.all()
        serializer = ArticleModelSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@csrf_exempt
def article_details(request,slug):
    try:
        article = Articles.objects.get(slug =slug)
    except Articles.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleModelSerializer(article)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(article,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)

        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse('article deleted',status=204)
'''