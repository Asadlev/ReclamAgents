from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Employee, Client, Company


class EmployeeRegistrationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'role'
        ]


class ClientRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    company_code = forms.CharField(label='Код компании')

    class Meta:
        model = Employee
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'company_code'
        ]

    def clean_company_code(self):
        company_code = self.cleaned_data['company_code']
        try:
            Company.objects.get(unique_code=company_code)
        except Company.DoesNotExist:
            raise forms.ValidationError('Неверный код компании.')
        return company_code

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.role = 'client'
        if commit:
            user.save()
            company = Company.objects.get(unique_code=self.cleaned_data['company_code'])
            Client.objects.create(user=user, company=company)
        return user


class EmployeeLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Employee
        fields = [
            'username',
            'password'
        ]


class ClientLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Client
        fields = [
            'user',
            'company',
        ]


class EmployeeProfileForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = [
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
            'role',
        ]


class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user.first_name = self.cleaned_data.get('first_name', instance.user.first_name)
        instance.user.last_name = self.cleaned_data.get('last_name', instance.user.last_name)
        instance.user.username = self.cleaned_data.get('username', instance.user.username)
        instance.user.email = self.cleaned_data.get('email', instance.user.email)
        if commit:
            instance.user.save()
            instance.save()
        return instance
