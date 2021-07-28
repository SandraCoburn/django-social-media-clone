from django.db import models
from django.urls import reverse
from django.utils.text import slugify #allows us to remove any characters like underscore and spaces to use string in urls
# Groups models.py file

import misaka #link embedding to use markup inside our posts

from django.contrib.auth import get_user_model #returns active user
User = get_user_model()

# This is for the in_group_members check template tag
from django import template
register = template.Library()

class Group(models.Model):
  name = models.CharField(max_length=255, unique=True)
  slug = models.SlugField(allow_unicode=True, unique=True)
  description = models.TextField(blank=True, default='')
  description_html = models.TextField(editable=False,default='', blank=True)
  members = models.ManyToManyField(User, through='GroupMember')

  def __str__(self) -> str:
      return self.name
    
  def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      self.description_html = misaka.html(self.description)
      super().save(*args, **kwargs)

  def get_absolute_url(self):
      return reverse('groups:single', kwargs={'slug':self.slug})

  class Meta:
      ordering = ["name"]


class GroupMember(models.Model):
  group = models.ForeignKey(Group, related_name="memberships", on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name='user_groups',on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.user.username

  class Meta:
      unique_together = ('group','user')

