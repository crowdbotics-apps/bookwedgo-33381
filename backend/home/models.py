from django.conf import settings
from django.db import models


class TodoList(models.Model):
    "Generated Model"
    taskname = models.CharField(
        max_length=256,
    )
    taskdescription = models.TextField()
    duedate = models.DateTimeField()
    username = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="todolist_username",
    )
