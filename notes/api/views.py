from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from notes.api.serializers import NoteSerializer, UserSerializer
from notes.models import Note


class NoteListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailsView(RetrieveAPIView):
    # permission_classes = [IsAdminUser]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteCreateView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDeleteView(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteUpdateView(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class AllowPostAnyReadAuthenticatedUser(permissions.BasePermission):

    def has_permission(self, request, view):
        # Allow anyone to register
        if request.method == "POST":
            return True
        # Must be authenticated to view
        else:
            return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Any view method requires you to be the user
        return obj.id == request.user.id or request.user.is_superuser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowPostAnyReadAuthenticatedUser,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(username=user.username)

    def get_object(self):
        obj = get_object_or_404(User.objects.filter(id=self.kwargs["pk"]))
        self.check_object_permissions(self.request, obj)
        return obj
