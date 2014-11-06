from django.shortcuts import render_to_response, RequestContext
from django.views.decorators.csrf import csrf_protect
from cbrf_parser.management.commands._cbrf_parser import CbrfParser
import threading


#Отображает страницу настроек парсера
@csrf_protect
def cbrf_parser_settings(request):
    if request.is_ajax() and request.method == 'POST':
        if "days" in request.POST and request.POST["days"]:
            days = int(request.POST["days"])
        else:
            days = 1
        parser = CbrfParser()
        thread = threading.Thread(target=parser.load_data, args=(days,))
        thread.start()
        return render_to_response(
            "cbrf_parser/cbrf_parser.html",
            {},
            context_instance=RequestContext(request),
        )
    else:
        return render_to_response(
            "cbrf_parser/cbrf_parser.html",
            {},
            context_instance=RequestContext(request),
        )