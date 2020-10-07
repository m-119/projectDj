from datetime import datetime
from django.views import View
from django.http import HttpResponse
import random
from django.shortcuts import render

# Create your views here.


class DatetimeView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)

class RandomView(View):
    def get(self, request):
        html = f"{random.randint(0, 10)}"
        return HttpResponse(html)

class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')