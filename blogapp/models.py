from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    # id created automatically
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # other way --  ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    # other way --      DateTimeField(auto_now_add=True)
    # auto_now=True updates every time Model is saved
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved=True)

    # special django function, needs exact name
    def get_absolute_url(self):
        # after creating a post, direct to post detail view of that post
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.CharField(max_length=200)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
