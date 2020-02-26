from rest_framework import serializers
from .models import Event, Comment, Rating
from django.contrib.auth.models import User


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ['url', 'id', 'owner',
                  'body', 'event']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    due_date = serializers.DateField(format=None, input_formats=None)
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = Event
        fields = ['url', 'id', 'comments', 'owner',
                  'title', 'body', 'created', 'due_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'events', 'comments']


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(view_name='event-detail', queryset=Event.objects.all())
    comment = serializers.HyperlinkedRelatedField(view_name='comment-detail', queryset=Comment.objects.all())
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())

    class Meta:
        model = Rating
        fields = ['url', 'id', 'owner', 'upvotes', 'downvotes', 'event', 'comment']

