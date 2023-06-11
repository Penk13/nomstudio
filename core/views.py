from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def all_works(request):
    return render(request, "core/all_works.html")

def work_by_category(request):
    return render(request, "core/work_by_category.html")

def work_detail(request):
    return render(request, "core/work_detail.html")
