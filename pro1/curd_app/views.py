from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company
from django.http import HttpResponse


def create_view(request):
    template_name = "curd_app/create.html"
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("register successfully!!!" )
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = Company.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def updated_view(request, pk):
    template_name = "curd_app/create.html"
    obj = Company.objects.get(id=pk)
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def delete_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = Company.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)



