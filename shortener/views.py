import json

from django.http import Http404
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from .utils import encode, url_validator


class Home(TemplateView):
    template_name = "index.html"


@csrf_exempt
def shotify(request):
    if not request.is_ajax():
        raise Http404()

    data = json.loads(request.body)
    long_url = data.get('url')

    try:
        url_validator(data.get('url'))
    except ValidationError:
        return JsonResponse({'error': 'Please enter a URL!'})

    index = cache.incr('count', ignore_key_check=True)
    path = encode(index)
    key = "shortify:{}".format(path)
    cache.set(key, long_url, timeout=None)

    url = f"http://{request.get_host()}/{path}"

    return JsonResponse({'url': url})


def redirect_to_original(request, short_id):
    key = 'shortify:{}'.format(short_id)
    original_url = cache.get(key)
    if not original_url:
        raise Http404()
    return redirect(original_url)
