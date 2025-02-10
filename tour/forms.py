from django.forms import ModelForm, TextInput, EmailInput, DateInput
from .models import Contact
from django.core.mail import send_mail

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "email", "phone", "message", "date", "place"]
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
            "date": DateInput(

                format="%d.%m.%Y",
                attrs={
                "class": "form-control",
                "type": "date",
            }),
            "place": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Гагра, Абазгаа 55/1"
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
Место: {self.cleaned_data['place']}
Дата: {self.cleaned_data['date']}
Сообщение: {self.cleaned_data['message']}
        """
        send_mail(subject, message, "djafarovemil04@mail.ru", ["djafarovemil04@mail.ru"])

