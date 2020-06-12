from django.urls import path , include
#from .views import ArticleAPIVIEW, Article_DetailAPI ,GenericAPIView , ArticleViewSet
#from .views import ArticleViewSetGeneric
from .views import ArticleViewSetModel
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
#router.register('', ArticleViewSet, basename='article')
#router.register('article', ArticleViewSetGeneric ,basename='article')
router.register('',ArticleViewSetModel)


urlpatterns = [

    # path('article/', views.article_list , name="api-basic-article"),
    # path('detail/<int:pk>/',views.article_Detail , name ="api-basic-article-detail")

    # path('article/', ArticleAPIVIEW.as_view()), #since we are using class we need to add .as_view()
    # path('detail/<int:id>/',Article_DetailAPI.as_view()),
    # path('generic/<int:id>/', GenericAPIView.as_view()),
    # path('generic/', GenericAPIView.as_view()),
    # path('viewset/',include(router.urls)),
    #path('viewsetgeneric/',include(router.urls)),
    path('viewsetmodel/', include(router.urls)),
]
