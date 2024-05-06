from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile, Product, Person
from django.contrib import messages

def index(request):
    profiles = Profile.objects.all()
    products = Product.objects.all()
    user =request.user
    persons = Person.objects.all()
    return render(request, 'index.html', {'profiles': profiles ,'products': products ,'persons':persons, 'user':user})




def profile_add(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('index')
    return render(request, 'profile_add.html', {'form': form} )



def person_add(request):
   
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        
        person = Person(
            name=name ,
            place=place,
            height=height,
            weight=weight,
        )
        person.save()
        messages.success(request, f"{person.name} added successfully")
        
        return redirect('index')
    

    return render(request, 'person_add.html')



def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        product = Product(
            name=name ,
            address=address,
            phone=phone,
            email=email,
        )
        product.save()
        messages.success(request, f"{product.name} added successfully")
        return redirect('index')
    

    return render(request, 'product_add.html', )
    

    





def person_list(request):
    persons = Person.objects.all( )
    return render(request, 'person_list.html',{'persons':persons})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def person_view(request,person_id):
    persons = Person.objects.get(id=person_id)
    return render(request, 'person_detail.html', {'persons': persons})




def product_view(request,product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'products': products})


def product_edit(request,product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        product.name = name
        product.email= email
        product.address= address
        product.phone = phone
        product.save()
        return redirect('index')

    return render(request, 'product_edit.html', {'product': product})




def person_edit(request,person_id):
    person = Person.objects.get(id=person_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        
        person.name = name
        person. place= place
        person.weight= weight
        person.height = height
        person.save()
        return redirect('index')

    return render(request, 'person_edit.html', {'person': person})





def profile_view(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    education = profile.education.all()
    return render(request, 'profile_view.html', {'profile': profile, 'educaions': education})




def profile_edit(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after successful update
    
    return render(request, 'profile_edit.html', {'form': form})



def delete_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    profile.delete()

    return redirect('index') 

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

    return redirect('index') 

def delete_person(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()

    return redirect('index') 

