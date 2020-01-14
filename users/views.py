from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from schedule.models import Category, TodoList

import requests

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance = request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, f'Your profile has been updated')
      return redirect('portfolio')
  else:
    u_form = UserUpdateForm(instance = request.user)
    p_form = ProfileUpdateForm(instance = request.user.profile)

  context = {
    'u_form' :  u_form,
    'p_form' :  p_form,
  }

  return render(request, 'registration/profile.html', context)

@login_required
def createdashboard(request):
  # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4b4857337408a4e1fe365b3bfdc7374d'
  # city = 'Guwahati'
  # city_weather  = requests.get(url.format(city)).json()

  # weather = {
  #       'city' : city,
  #       'temperature' : city_weather['main']['temp'],
  #       'description' : city_weather['weather'][0]['description'],
  #       'icon' : city_weather['weather'][0]['icon']
  #   }

  # context = {'weather' : weather}
  todos = TodoList.objects.all() #quering all todos with the object manager
  categories = Category.objects.all() #getting all categories with object manager
  if request.method == "POST": #checking if the request method is a POST
    if "taskAdd" in request.POST: #checking if there is a request to add a todo
      title = request.POST["description"] #title
      date = str(request.POST["date"]) #date
      category = request.POST["category_select"] #category
      content = title + " -- " + date + " " + category #content
      Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
      Todo.save() #saving the todo
      return redirect("/") #reloading the page
    if "taskDelete" in request.POST: #checking if there is a request to delete a todo
      checkedlist = request.POST["checkedbox"] #checked todos to be deleted
      for todo_id in checkedlist:
        todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
        todo.delete() #deleting todo

  context = {
              "todos": todos,
              "categories":categories
              }
  return render(request, 'dashboard.html', context) #returns the dashboard.html template
