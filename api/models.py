from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel congue enim. Fusce nec nibh blandit, finibus tellus sit amet, eleifend neque. Nunc vehicula velit malesuada, dapibus arcu eu, convallis tellus.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50] + '...'

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'