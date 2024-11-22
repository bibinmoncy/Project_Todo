from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from . models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class taskdeleteview(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url=reverse_lazy('tasklistview')

class taskupdateview(UpdateView):
    model=task
    template_name = 'edit.html'
    context_object_name = 'result2'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('taskdetailview',kwargs={'pk':self.object.id})
class taskdetailview(DetailView):
    model=task
    template_name = 'details.html'
    context_object_name = 'result1'

class tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'result'

# Create your views here.
def add(request):
    result = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('taskname','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        obj=task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'home.html',{'result':result})

# def details(request):
#     result=task.objects.all()
#     return render (request,'details.html',{'result':result})


def delete(request,taskid):
    obj=task.objects.get(id=taskid)
    if request.method=="POST":
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    obj1=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=obj1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'obj1':obj1,'f':f})



