from django.conf.urls import patterns, include, url

from django.contrib import admin

from currency.views import get_quotation_of_currency, get_currency_info

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # страницы с данными по изменению курсов валют за определённый период
    url(r'^$', get_quotation_of_currency),
    url(r'^index/$', get_quotation_of_currency),

    url(r'^currency_info/$', get_currency_info),

)
