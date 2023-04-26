from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import Question,Answer
from .serializers import QuestionSerializer,AnswerSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from .permissions import IsAuthor




class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,IsAuthor)
    # authentication_classes = [TokenAuthentication,SessionAuthentication,]

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        print('self.request.user',self.request.user)
        serializer.save(author=self.request.user)


class AnswerCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,IsAuthor)
    # authentication_classes = [TokenAuthentication, SessionAuthentication, ]

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        author = self.request.user
        slug = self.kwargs.get('slug')
        question  = get_object_or_404(Question,slug=slug)
        serializer.save(question = question,author = author)

class AnswerList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,IsAuthor)
    # authentication_classes = [TokenAuthentication, SessionAuthentication, ]

    serializer_class = AnswerSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug = slug)

class AnswerDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    # authentication_classes = [TokenAuthentication, SessionAuthentication, ]

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

