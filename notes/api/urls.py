from django.conf.urls import url
from django.urls import path
from .views import NoteListView, NoteDetailsView, NoteCreateView, NoteUpdateView, NoteDeleteView,UserViewSet

userList = UserViewSet.as_view({
    'get': 'list'
    # 'post': 'create'
})

userDetail = UserViewSet.as_view({
    'get': 'retrieve'
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})

urlpatterns = [
    path('',NoteListView.as_view()),
    path('<pk>',NoteDetailsView.as_view()),
    path('create/',NoteCreateView.as_view()),
    path('delete/<pk>',NoteDeleteView.as_view()),
    path('update/<pk>',NoteUpdateView.as_view()),
    #url(r'^$', userList, name='users'),
    #url(r'^(?P<pk>\d+)$', userDetail, name='user'),
    path('usrs/',userList, name='users'),
    path('usrs/<pk>',userDetail, name='user'),
]