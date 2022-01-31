import os
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from ..models import MMessage
from .serializers import MessageSerializer, NewMessageSerializer, UserSerializer


class Pagination3(PageNumberPagination):
    pagination = int(os.environ.get("PAGINATION", default=3))
    page_size = pagination


class SendView(APIView):
    """
    View for messages creation
    """
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = self.request.user
        message = request.data.get('message')
        message['user_from'] = user.id
        try:
            user_to = User.objects.get(username=message['user'])
            message['user_to'] = user_to.id
        except:
            raise Http404()
        serializer = NewMessageSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()
            return Response({"success": "Message '{}' created successfully".format(saved.title)})


class UsersView(generics.ListAPIView):
    """
    View for the list of recipients
    """
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class MessagesView(generics.ListAPIView):
    """
    View for the list of messages
    """
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = MMessage.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pagination3

    def get_queryset(self):  # filter messages: only sent or received by user
        user = self.request.user
        queryset = super(MessagesView, self).get_queryset()
        queryset = queryset.filter(
            Q(user_to=user) | Q(user_from=user)
        ).order_by('-sent')
        return queryset


class InboxView(generics.ListAPIView):
    """
    View for the list of incoming messages
    """
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = MMessage.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pagination3

    def get_queryset(self):
        queryset = super(InboxView, self).get_queryset()
        queryset = queryset.filter(user_to=self.request.user).order_by('-sent')
        return queryset


class SentView(generics.ListAPIView):
    """
    View for the list of sent messages
    """
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = MMessage.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pagination3

    def get_queryset(self):
        queryset = super(SentView, self).get_queryset()
        queryset = queryset.filter(user_from=self.request.user).order_by('-sent')
        return queryset


class MessageDetailView(generics.RetrieveAPIView):
    """
    View for the message details
    """
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = MMessage.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):  # shows message only if it was sent or received by user
        user = self.request.user
        queryset = super(MessageDetailView, self).get_queryset()
        queryset = queryset.filter(
            Q(user_to=user) | Q(user_from=user)
        )
        return queryset
