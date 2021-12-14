from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import language_tool_python
import requests
import json


@require_http_methods(["GET"])
def checker(request):
    response = {}
    try:
        lang = request.GET.get('lang')
        tool = language_tool_python.LanguageTool(lang)
        text = request.GET.get('text')
        response['correctText'] = tool.correct(text)

        response['msg'] = 'success'
        response['error_num'] = 0

    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
