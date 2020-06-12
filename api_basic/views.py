from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404






#CLASS BASED VIEWS

"""
class ArticleAPIVIEW(APIView):

    def get(self, request):
        articles = Article.objects.all()

        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Article_DetailAPI(APIView):

#list
    def get_object(self,id):

        try:
           return Article.objects.get(id=id)

        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):

        article = self.get_object(id)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def put(self,request , id):
        article = self.get_object(id)
        serializer = ArticleSerializers(article,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializers(article, data=request.data , partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        article = self.get_object(id)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



"""


"""
                                    Function based Views


@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()

        #when you want to serialize a queryset set many=True

        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE','PATCH'])
def article_Detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = ArticleSerializers(article,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ArticleSerializers(article, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
"""


"""
                              GENERIC VIEWS 

class GenericAPIView(generics.GenericAPIView , mixins.ListModelMixin , mixins.CreateModelMixin , mixins.UpdateModelMixin
                     ,mixins.RetrieveModelMixin , mixins.DestroyModelMixin):

    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    lookup_field = 'id'
    #authentication_classes = [SessionAuthentication, BasicAuthentication] #first check for Session and then basic
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] #atleast one authentication class


    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def patch(self,request, id=None):
        return self.update(request,id, partial=True)

    def delete(self,request,id=None):
        return self.destroy(request,id)
"""





# View Sets




"""
class ArticleViewSet(viewsets.ViewSet):  # this is simple view set here we need to write all the functionality manually

#get
    def list(self, request):

        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):

        queryset = Article.objects.all()
        article =get_object_or_404(queryset,pk=pk)

        #article = Article.objects.get(pk=pk) #this will raise doesnt
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
#post
    def create(self,request):

        serializer = ArticleSerializers(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 #put
    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializers(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #patch
    def partial_update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializers(article, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def destroy(self, request, pk=None):

        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

"""


#Generic ViewSet


"""

class ArticleViewSetGeneric(viewsets.GenericViewSet, mixins.ListModelMixin , mixins.CreateModelMixin , mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
   
   
    
    """


#ModelViewSet

class ArticleViewSetModel(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
