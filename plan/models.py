from django.db import models

# Plan Model


class Plan(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['is_done', '-created_at']

    def __str__(self):
        return self.title
