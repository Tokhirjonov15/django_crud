from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from .models import Plan

# Plan Controller


def get_home(request):
    try:
        plans = Plan.objects.all()
        return render(
            request,
            "home.html",
            {'plans': plans, 'active_page': 'home'},
            status=200,
        )
    
    except Exception as err:
        print("Error in get_home:", err)
        return HttpResponseServerError("Something went wrong")


def create_plan(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        if title:
            Plan.objects.create(title=title, description=description)

    return redirect('get_home')


def update_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)

    if request.method == 'POST':
        plan.title = request.POST.get('title', '').strip() or plan.title
        plan.description = request.POST.get('description', '').strip()
        plan.is_done = request.POST.get('is_done') == 'on'
        plan.save()

    return redirect('get_home')


def delete_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)

    if request.method == 'POST':
        plan.delete()

    return redirect('get_home')
