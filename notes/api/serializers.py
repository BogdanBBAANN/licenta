from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id","title","content","date")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'password','groups')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }


