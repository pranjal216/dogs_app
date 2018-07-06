from django.shortcuts import render,redirect,HttpResponse
from .models import Dog
from .forms import NameForm

def index(request):
    dogs = Dog.objects.all()
    response = render(request,'dog_app/index.html', {'dogs':dogs})
    return response

def create(request):
    print(request.POST.get('breed'))
    dog = Dog(name=request.POST.get('h'), breed=request.POST.get('class'))
    dog.save()
    return redirect('/')

def edit(request,id):
    dog =Dog.objects.get(id=id)
    context= {'dog':dog}
    return render(request,'dog_app/edit.html',context)

def update(request,id):
    dog = Dog.objects.get(id=id)
    dog.name=request.POST['name']
    dog.breed=request.POST['breed']
    dog.save()
    return redirect('/')

def destroy(request,id):
    dog=Dog.objects.get(id=id)
    dog.delete()
    return redirect('/')

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HtttpResponse('/thanks/')
    else:
        form=NameForm()
    return render(request,'name.html',{'form':form})