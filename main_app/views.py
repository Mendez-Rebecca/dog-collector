from django.shortcuts import render

dogs = [
    {'name': 'Brutus', 'breed': 'Staffordshire Terrier', 'description': 'Old and grumpy', 'age': 11},
    {'name': 'Ike', 'breed': 'Dutch Shepherd', 'description': 'Barks a lot', 'age': 9},
    {'name': 'Patton', 'breed': 'Belgian Malinois', 'description': 'Cuddle bug', 'age': 7},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
