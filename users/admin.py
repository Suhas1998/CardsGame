from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser
from .models import Profile
from schedule.models import Category, TodoList


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
