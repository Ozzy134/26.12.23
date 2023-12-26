from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Todo
from .forms import FormTodo, TodoModelForm

def index(request):
    info = Todo.objects.all()
    return render(request, 'app/index.html', context={'info': info})

def create(request):
    if request.method == 'POST':
        # new = Todo()
        # form = FormTodo(request.POST)
        # if form.is_valid():
        #     new.task = form.cleaned_data['task']
        #     new.data = form.cleaned_data['data']
        #     new.status = form.cleaned_data['status']
        #     new.save()
        #     return redirect('home')
        form = TodoModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/create.html', context={'form': TodoModelForm() })

def update(request, id):
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoModelForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/create.html', context={'form': TodoModelForm(instance=task) })

def delete(request, id):
    task = get_object_or_404(Todo, id=id)
    # task = Todo.objects.get(id=id)
    task.delete()
    return redirect('home')

class BaseViewClosed(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html', context={'info': Todo.objects.all()})

class BaseViewCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html', context={'info': Todo.objects.all()})

    def post(self, request, *args, **kwargs):
        form = TodoModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')
        return self.get(request, *args, **kwargs)

class BaseDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Todo, pk=pk)
        return render(request, 'app/index.html', context={'info': task})

class BaseViewDelete(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Todo, pk=pk)
        task.delete()
        return redirect('home')

class Detail(DetailView):
    model = Todo

