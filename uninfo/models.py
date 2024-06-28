from django.db import models

class Post(models.Model):
  name = models.CharField(max_length = 80, primary_key=True)
  description = models.TextField()

  def __str__(self):
    return self.name

class comment(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
  name = models.CharField(max_length = 80)
  body = models.TextField()
  user_icon = models.CharField(max_length = 2000)
  created_on = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['created_on']

  def __str__(self):
    return 'Comment by {}'.format(self.name)