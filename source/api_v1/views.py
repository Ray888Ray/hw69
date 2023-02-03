import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


def sub(request, *args, **kwargs):
    if request.body:
        try:
            answer = json.loads(request.body)
            a = list(answer.values())
            f = {
                "answer": int(a[0]) - int(a[1])
            }
        except ValueError:
            f = {
                "errors": "Can not do any operation with str"
            }
        return JsonResponse({"ans": f})


def mul(request, *args, **kwargs):
    if request.body:
        try:
            answer = json.loads(request.body)
            a = list(answer.values())
            f = {
                "answer": int(a[0]) * int(a[1])
            }
        except ValueError:
            f = {
                "errors": "Can not do any operation with str"
            }
        return JsonResponse({"ans": f})


def div(request, *args, **kwargs):
    if request.body:
        try:
            answer = json.loads(request.body)
            a = list(answer.values())
            f = {
                "answer": int(a[0]) / int(a[1])
            }
        except ValueError:
            f = {
                "errors": "Can not do any operation with str"
            }
        except ZeroDivisionError:
            f = {
                "errors": "Division by zero!"
            }
        return JsonResponse({"ans": f})


def add(request, *args, **kwargs):
    if request.body:
        try:
            answer = json.loads(request.body)
            a = list(answer.values())
            f = {
                "answer": int(a[0]) + int(a[1])
            }
        except ValueError:
            f = {
                "errors": "Can not do any operation with str"
            }
        return JsonResponse({"ans": f})


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


