from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

# VIEWSETS
router = DefaultRouter()
router.register('articles',ArticleViewset,basename='articles')


urlpatterns = [
# FUNCTION BASED VIEWS SECTION
    # path('list/', article_list,name = 'article_list'),
    # path('details/<slug:slug>/', article_details, name='article_details'),

# CLASS BASED VIEWS SECTION
    # path('list/', ArticlesList.as_view(),name = 'article_list'),
    # path('details/<slug:slug>/', ArticleDetails.as_view(), name='article_details'),

# VIEWSETS
    path('',include(router.urls)),

]
