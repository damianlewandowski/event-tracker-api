from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=32)
    body = models.CharField(max_length=128)
    owner = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']


class Comment(models.Model):
    body = models.CharField(max_length=128)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['owner']


class Rating(models.Model):
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    owner = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    event = models.OneToOneField(
        Event,
        related_name='ratings',
        default=None,
        on_delete=models.CASCADE,
    )
    comment = models.OneToOneField(
        Comment,
        related_name='ratings',
        default=None,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.event.name} rating'

    class Meta:
        ordering = ['owner']
