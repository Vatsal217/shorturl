from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect

from appshort.serializers import KirrUrlSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from .models import KirrUrl
from django.shortcuts import get_object_or_404
# Create your views here.
# @api_view(["GET"])
# def Kirr_redirect_view(request, shortcode=None, *args, **kwargs):
#     obj = get_object_or_404(KirrUrl, shortcode = shortcode)
#     return HttpResponseRedirect(redirect_to=obj.url)


class KirrCBView(APIView):
    def get(self, request, shortcode=None, *args, **kwargs):
        journalists = KirrUrl.objects.all()
        serializer = KirrUrlSerializer(journalists, many=True, context={'request': request})
        
        return Response(serializer.data, )


    def post(self, request):
        serializer = KirrUrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLRedirectView(APIView):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrUrl, shortcode=shortcode)

        return HttpResponseRedirect(obj.url)