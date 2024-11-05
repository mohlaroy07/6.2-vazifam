from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CommentForm, FoodForm, LoginForm, RegisterForm
from .models import Food, FoodType, Comment


class FoodTypeListView(ListView):
    model = FoodType
    template_name = "home.html"


class FoodListView(ListView):
    model = Food
    template_name = "home.html"
    context_object_name = "foods"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foodtypes"] = FoodType.objects.all()

        return context


class FoodDetailView(DetailView):
    model = Food
    template_name = "food_detail.html"

    def post(self, request, pk):
        print(f"Post request {pk}")

        user = request.user

        text = request.POST.get("text")

        Comment.objects.create(text=text, user=user, food=Food.objects.get(pk=pk))

        return self.get(request, pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get("pk")

        context["comments"] = Comment.objects.filter(food_id=pk)

        return context


class FoodCreateView(CreateView):
    model = Food
    template_name = "food_create.html"
    fields = ["food_type", "nomi", "tarkibi", "narxi"]
    success_url = reverse_lazy("home")


class FoodUpdateView(UpdateView):
    model = Food
    template_name = "food_edit.html"
    fields = ["nomi", "tarkibi", "narxi"]
    success_url = reverse_lazy("home")


class FoodDeleteView(DeleteView):
    model = Food
    template_name = "food_delete.html"
    success_url = reverse_lazy("home")


class Register(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return self.get(request)


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect("home")

        return self.get(request)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("home")
