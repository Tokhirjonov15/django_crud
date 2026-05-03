from django.http import HttpResponseServerError
from django.shortcuts import render

# Plan Controller


def get_home(request):
    try:
        print("\n get_home")
        data = "MIT Sila"
        return render(request, "home.html", {'plans': data}, status=200)
    
    except Exception as err:
        print("Error in get_home:", err)
        return HttpResponseServerError("Something went wrong")
