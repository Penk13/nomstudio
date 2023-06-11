from django.shortcuts import render, get_object_or_404
from .models import WorkCategory, Work

def home(request):
    return render(request, "core/home.html")

def all_works(request):
    work_categories = WorkCategory.objects.all()
    context = {
        "work_categories": work_categories,
    }
    return render(request, "core/all_works.html", context)

def work_by_category(request, category_pk):
    work_category = get_object_or_404(WorkCategory, pk=category_pk)
    works = Work.objects.filter(category=work_category)
    context = {
        "work_category": work_category,
        "works": works,
    }
    return render(request, "core/work_by_category.html", context)
