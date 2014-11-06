from django.shortcuts import render_to_response, RequestContext
from django.views.decorators.csrf import csrf_protect

#Отображает страницу настроек парсера
@csrf_protect
def cbrf_parser_settings(request):
    return render_to_response(
        "cbrf_parser/cbrf_parser.html",
        {
            "text" : request,
        },
        context_instance=RequestContext(request),
    )