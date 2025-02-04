from django.forms import ModelForm, TextInput, EmailInput
from .models import Contact
from django.core.mail import send_mail

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "email", "phone", "message"]
        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите имя"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "placeholder": "example@mail.com"
            }),
            "phone": TextInput(attrs={
                "class": "form-control",
                "placeholder": "+7 (XXX) XXX-XX-XX"
            }),
            "message": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Дополнительная информация"
            }),
        }

    def email(self):
        """Отправка данных на почту"""
        subject = "Новая заявка на тур"
        message = f"""
Имя: {self.cleaned_data['first_name']}
Email: {self.cleaned_data['email']}
Телефон: {self.cleaned_data['phone']}
Сообщение: {self.cleaned_data['message']}
        """
        send_mail(subject, message, "djafarovemil04@mail.ru", ["djafarovemil04@mail.ru"])

