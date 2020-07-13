from django.urls import path
from django.conf.urls import url
from appshort.views import KirrCBView,URLRedirectView

urlpatterns = [
    # url("a/(?P<shortcode>[\w-]+)$", Kirr_redirect_view),

    url("(?P<shortcode>[\w-]+)$", URLRedirectView.as_view(), name="URLRedirectView"),
    url("b/", KirrCBView.as_view(), name="KirrCBView"),



]