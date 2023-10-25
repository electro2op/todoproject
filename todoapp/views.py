from django.shortcuts import render, redirect
from . models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy




class Taskdeleteview(DetailView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvindex')

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse.lazy('cbvdetails',kwargs={'pk':self.object.id})



class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


def index(request):
    task1 = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()
    return render(request, 'index.html', {'task1': task1})

# def delete(request, taskid):
#     task = Task.objects.get(id=taskid)  # Changed variable name to 'task'
#     if request.method == "POST":
#         task.delete()
#         return redirect('/')
#     return render(request, 'delete.html')
def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    t=TodoForm(request.POST or None,instance=task)
    if t.is_valid():
        t.save()
        return redirect('/')
    return render(request,'edit.html',{'t':t, 'task':task})

