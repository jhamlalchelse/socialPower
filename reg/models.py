from urllib import request
from django.db import models
from django.contrib.auth.models import User


class PostDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    post_image=models.FileField(upload_to='userimg',null=True)
    desc = models.CharField(max_length=120)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class MessageModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    postid = models.IntegerField(null=True)


class FollowerModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fweruserid = models.PositiveIntegerField(default=0)

class FollowingModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fwinguserid = models.PositiveIntegerField(default=0)

