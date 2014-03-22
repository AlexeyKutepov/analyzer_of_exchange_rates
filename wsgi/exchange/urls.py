from django.conf.urls import patterns, include, url

from django.contrib import admin

from currency_to_rub.views import period_1d, period_1w, period_1m, period_3m, period_6m, period_1y, period_5y, period_10y
from chart_currency.views import chart_handler

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exchange.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', period_1d),
    url(r'^index/$', period_1d),
    url(r'^1d/$', period_1d),
    url(r'^1w/$', period_1w),
    url(r'^1m/$', period_1m),
    url(r'^3m/$', period_3m),
    url(r'^6m/$', period_6m),
    url(r'^1y/$', period_1y),
    url(r'^5y/$', period_5y),
    url(r'^10y/$', period_10y),

    #сылки на графики курсов валют
    url(r'^build_chart/$', chart_handler),
    url(r'^chart/$', chart_handler),
)
