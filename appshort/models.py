from django.db import models
from .utils import code_generator, create_shortcode
from django.conf import settings
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX",15)

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = KirrUrl.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made :{i}".format(i=new_codes)


class KirrUrl(models.Model):
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()


    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            print("something")
            self.shortcode = create_shortcode(self)
        super(KirrUrl, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = '-id'
         


    def __str__(self):
        return str(self.url)


    
    
   