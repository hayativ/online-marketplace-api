# Python modules
from typing import Any

# Django modules
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
import pytz

counter_value = 0  # простая переменная для счётчика

def hello_view(
    request: HttpRequest,
    *args: tuple[Any, ...],
    **kwargs: dict[str, Any]
) -> HttpResponse:
    """
    Return a simple HTML page.

    Parameters:
        request: HttpRequest
            The request object.
        *args: list
            Additional positional arguments.
        **kwargs: dict
            Additional keyword arguments.
    
    Returns:
        HttpResponse
            Rendered HTML page with a name in the context.
    """

    return render(
        request=request,
        template_name="index.html",
        context={"name": "Temirbolat", "names": []},
        status=200
    )

def welcome(request):
    return render(request, 'welcome.html')

def users(request):
    users_list = [
        {"full_name": "Yeva Davydova", "age": 21},
        {"full_name": "Zemfira Ramazanove", "age": 49},
        {"full_name": "John Doe", "age": 100},
    ]
    return render(request, 'users.html', {"users": users_list})

def city_time(request):
    city = request.GET.get("city", "UTC")
    tz = pytz.timezone({
        "Almaty": "Asia/Almaty",
        "Calgary": "America/Edmonton",
        "Moscow": "Europe/Moscow",
        "UTC": "UTC",
    }.get(city, "UTC"))
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "city_time.html", {"city": city, "time": current_time})

def counter(request):
    global counter_value
    if "reset" in request.GET:
        counter_value = 0
    elif "add" in request.GET:
        counter_value += 1
    return render(request, "counter.html", {"counter": counter_value})
