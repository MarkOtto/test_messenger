from django.conf.urls import url, include
from . import views
from rest_framework.authtoken import views as drf


urlpatterns = [
    url(r'^token/$', drf.obtain_auth_token),
    url(r'^users/$', views.UsersView.as_view(), name='messages_all'),
    url(r'^send/$',  views.SendView.as_view(), name='send_new'),
    url(r'^sent/$',  views.SentView.as_view(), name='messages_sent'),
    url(r'^inbox/$', views.InboxView.as_view(), name='messages_inbox'),
    url(r'^messages/$', views.MessagesView.as_view(), name='messages_all'),
    url(r'^message/(?P<pk>\d+)/$', views.MessageDetailView.as_view(), name='message_details'),
]