# myapp/forms.py
from django import forms
from .models import ExampleModel


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = ["name", "email"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("Le nom est obligatoire.")
        if len(name) < 3:
            raise forms.ValidationError(
                "Le nom doit comporter au moins 3 caractères."
            )
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("L'email est obligatoire.")

        # Vérifier le domaine de l'email et interdire certains domaines
        forbidden_domains = ["gmail.com", "hotmail.com"]
        domain = email.split("@")[-1]
        if domain in forbidden_domains:
            raise forms.ValidationError(
                f"Les adresses emails provenant de {', '.join(forbidden_domains)} ne sont pas autorisées."
            )

        return email
