import random
import string

from autoslug.fields import AutoSlugField
from django.db import models


# Meeting model stored in the database
class Meeting(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=250)
#     email = models.EmailField(max_length=75)
    url_ref = AutoSlugField(slugify=lambda instance: instance if instance != '' else ''.join(random.sample(string.uppercase + string.lowercase + string.digits, 5)), unique=True, always_update=False)
    items_discussed = models.TextField(null=True)
    decisions_made = models.TextField(null=True)
    action_items = models.TextField(null=True)
    occurred = models.DateTimeField(null=True)