from rest_framework import serializers
from appshort.models import KirrUrl



class KirrUrlSerializer(serializers.ModelSerializer):

    short_url = serializers.SerializerMethodField()


    class Meta:
        model = KirrUrl
        exclude = ("id",)


    
    def get_short_url(self, object):
        shortcode = object.shortcode
        return "http://127.0.0.1:8000/{shortcode}".format(shortcode=shortcode)
