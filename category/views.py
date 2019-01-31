from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CategoryForm
from .models import Category


def create(request):
    form = CategoryForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('category:list')
    context['form'] = form
    return render(request, 'category/create.html', context)


def update(request, pk):
    context = {}
    try:
        datas = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        messages.error(request, 'Nothing to update')
        return redirect('category:list')

    form = CategoryForm(instance=datas)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=datas)
        if form.is_valid():
            form.save()
            return redirect('category:list')

    context['form'] = form
    return render(request, 'category/create.html', context)


def delete(request, pk):
    context = {}
    choice = request.GET.get('choice')
    context['status'] = choice

    if request.method == 'POST':
        try:
            datas = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            messages.error(request, 'Category not found')
            return redirect('category:list')

        if choice == 'Undo':
            datas.is_deleted = False
            datas.save()
            messages.success(request, 'Undo Successfully')

        elif choice == 'Trash':
            datas.is_deleted = True
            datas.save()
            messages.success(request, 'Trashed successfully')

        elif choice == 'Delete' and datas.is_deleted is True:
            datas.delete()
            messages.success(request, 'Deleted successfully.')

        return redirect('category:list')

    context['url'] = reverse('category:list')
    return render(request, 'snippest/delete.html', context)


def list(request):
    context = {}
    datas = Category.objects.filter(is_deleted=False)
    context['datas'] = datas
    return render(request, 'category/list.html', context)


def trash_list(request):
    context = {}
    datas = Category.objects.filter(is_deleted=True)

    context['datas'] = datas
    return render(request, 'category/list.html', context)
