from django.forms import ModelForm
from .models import Contact
from django.core.mail import send_mail

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "email", "phone"]

    def email(self):
        """Отправка данных на почту"""
        subject = "Новая заявка на тур"
        message = f"""
            Имя: {self.cleaned_data['first_name']}
            Email: {self.cleaned_data['email']}
            Телефон: {self.cleaned_data['phone']}
        """
        send_mail(subject, message, "djafarovemil04@mail.ru", ["djafarovemil04@mail.ru"])

