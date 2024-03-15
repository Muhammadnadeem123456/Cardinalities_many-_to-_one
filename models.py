from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    #because of that cannot directly delete user....but can delete any post related to that user
    # user=models.ForeignKey(User,on_delete=models.PROTECT)
    #we can delete any user without delete it's post....using models.set_null,null=true
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post_title=models.CharField(max_length=100)
    post_cat=models.CharField(max_length=50)
    post_publish=models.DateField()
