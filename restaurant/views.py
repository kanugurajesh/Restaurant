# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
import requests
import random

execute = 1

def random_gen():
    return random.randint(50,200)

# the below function send request to the free meal api and gets relevant data
def request_sender(letter):
        try:
            Menu.objects.all().delete()
            print(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
            response = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
            if response.status_code == 200:
                data = response.json()
                if data["meals"] != "null":
                    try:
                        for item in data["meals"]:   
                            menu_item = Menu(name=item["strMeal"], category=item["strCategory"], image_url=item["strMealThumb"], price=random_gen())
                            menu_item.save()
                            print(item["strMeal"],item["strCategory"],item["strMealThumb"],item["strMealThumb"])
                    except requests.exceptions.RequestException as e:
                        pass
                else:
                    print("API request failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("An error occurred during the API request:", str(e))

# Create your views here.
def home(request):
    # the below code is used to send request multiple times with multiple inputs
    global execute
    if execute==1:
        letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        for letter in letters_list:
            request_sender(letter)
        execute = 0
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    print(menu_data)
    main_data = {"menu":menu_data}
    print(main_data)
    return render(request, "menu.html",{"menu":main_data})

def display_menu_item(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""

    return render(request,"menu_item.html",{"menu_item":menu_item})

def submit(request):
    return """
    <h1>Thank you for your feedback</h1>
    """
