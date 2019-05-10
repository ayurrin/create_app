from django.db import models

from django.utils import timezone
class Post(models.Model):
   title = models.TextField()
   author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   published_date = models.DateTimeField(default=timezone.now)
   created_date = models.DateTimeField(blank=True,null=True)
   def publish(self):
      self.published_date = timezone.now()
      self.save()

   def __str__(self):
      return self.title