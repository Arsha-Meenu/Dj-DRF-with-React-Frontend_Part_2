from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Articles
from django.utils.text import slugify

@receiver(pre_save,sender = Articles)
def add_sLug(sender,instance,*args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug

