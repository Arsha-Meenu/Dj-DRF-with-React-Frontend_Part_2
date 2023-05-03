from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('questions',QuestionViewSet,basename = 'questions')


urlpatterns = [
    path('',include(router.urls)),
    path('answer-create/<slug:slug>/',AnswerCreate.as_view(),name= 'answer-create'),
    path('answer-list/<slug:slug>/', AnswerList.as_view(), name='answer-list'),
    path('answer-update-delete/<int:pk>/', AnswerDeleteUpdate.as_view(), name='answer-update-delete'),

]





