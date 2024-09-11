from django.shortcuts import render, redirect

from .forms import ExampleForm
from .models import ExampleModel


def example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Simulons un appel à la base de données
            ExampleModel.objects.create(**form.cleaned_data)
            return redirect("success_url")
    else:
        form = ExampleForm()

    return render(request, "example_template.html", {"form": form})
