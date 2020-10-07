from datetime import datetime
from django.views import View
from django.http import HttpResponse
import random
from django.shortcuts import render


class HelloView(View):
    def get(self, request):
        html = f"<h1>Hello, World</h1>"
        return HttpResponse(html)