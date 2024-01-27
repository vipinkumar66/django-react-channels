from django.db import models
from django.contrib.auth import get_user_model

class Topic(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, related_name="channels", on_delete=models.CASCADE)

    class Meta:
        # so that the name of the channel will always be unique
        # took both field because there combination should be unique
        unique_together = ("name", "topic")

    def __str__(self) -> str:
        return f"{self.name}({self.topic.name})"

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), related_name="Message_Sender", on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, related_name="messages", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    is_read = models.BooleanField(default=False)
    content = models.TextField()

    def __str__(self) -> str:
        return f"message from {self.sender.username} in {self.channel.name}"