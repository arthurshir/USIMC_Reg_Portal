from django import forms
from . import models
import usimc_rules

from crispy_forms.helper import *
from crispy_forms.layout import *
import phonenumbers
from django.core.exceptions import ValidationError


class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['is_not_international', 'instrument_category', 'age_category', 'awards_applying_for']
        labels = {
            'is_not_international': 'Does at least one of your competitors live in the United States'
            }

    awards_applying_for = forms.MultipleChoiceField(choices=usimc_rules.AWARD_CHOICES, widget=forms.CheckboxSelectMultiple)

class ParentContactForm(forms.ModelForm):
    class Meta:
        model = models.ParentContact
        fields = ['first_name', 'last_name', 'email', 'phone_number',]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'application-input'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'application-input'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'application-input'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'application-input'}),
        }
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Div('first_name', css_class="col-md-6"),
            Div('last_name', css_class="col-md-6"),
            Div('email', css_class="col-md-12"),
            Div('phone_number', css_class="col-md-12"),
            css_class="row"
        ),
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number:
            phone_number = phonenumbers.parse(phone_number, "US")
            if phonenumbers.is_valid_number(phone_number):
                print phone_number.national_number
                return phone_number.national_number
            else:
                raise ValidationError('Not in valid format')
        else:
            return phone_number


class PieceForm(forms.ModelForm):
    class Meta:
        model = models.Piece
        fields = ['title', 'opus', 'movement', 'composer', 'length', 'is_chinese']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'application-input'}),
            'opus': forms.TextInput(attrs={'placeholder': 'Opus', 'class': 'application-input'}),
            'movement': forms.TextInput(attrs={'placeholder': 'Movement', 'class': 'application-input'}),
            'composer': forms.TextInput(attrs={'placeholder': 'Composer', 'class': 'application-input'}),
            'length': forms.TextInput(attrs={'placeholder': 'Length', 'class': 'application-input'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'application-input'}),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['first_name', 'last_name', 'instrument', 'address', 'city', 'state', 'zip_code', 'country', 'birthday']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'application-input'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last_name','class': 'application-input'}),
            'instrument': forms.TextInput(attrs={'placeholder': 'Instrument','class': 'application-input'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address','class': 'application-input'}),
            'city': forms.TextInput(attrs={'placeholder': 'City','class': 'application-input'}),
            'state': forms.TextInput(attrs={'placeholder': 'State','class': 'application-input'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip_code','class': 'application-input'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country','class': 'application-input'}),
            'birthday': forms.SelectDateWidget(
                empty_label=("Choose Year", "Choose Month", "Choose Day"),
                years=range(1980, 2017),
            ),
        }

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Div('first_name', css_class="col-md-6"),
            Div('last_name', css_class="col-md-6"),
            Div('instrument', css_class="col-md-12"),
            Div('address', css_class="col-md-12"),
            Div('city', css_class="col-md-6"),
            Div('state', css_class="col-md-4"),
            Div('zip_code', css_class="col-md-2"),
            Div('country', css_class="col-md-12"),
            Div('birthday', css_class="col-md-12"),
            css_class="row"
        ),
    )

class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'cmtanc_code',]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'application-input'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'application-input'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'application-input'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'application-input'}),
            'cmtanc_code': forms.TextInput(attrs={'placeholder': 'CMTANC Code', 'class': 'application-input'}),
        }
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Div('first_name', css_class="col-md-6"),
            Div('last_name', css_class="col-md-6"),
            Div('email', css_class="col-md-12"),
            Div('phone_number', css_class="col-md-12"),
            Div('cmtanc_code', css_class="col-md-12"),
            css_class="row"
        ),
    )

class EnsembleMemberForm(forms.ModelForm):
    class Meta:
        model = models.EnsembleMember
        fields = ['first_name', 'last_name', 'instrument', 'birthday']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'application-input'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'application-input'}),
            'instrument': forms.TextInput(attrs={'placeholder': 'Instrument', 'class': 'application-input'}),
        }
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
            years=range(1980, 2017),
        ),
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
        	Div('email', css_class="container-fluid"),
        	Div('password', css_class="container-fluid"),
    	),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-default')
        ),
        HTML("""
            <a href="{% url 'registration_site:register' %}">or register</a>
        """),
    )

class RegistrationForm(forms.Form):

    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Div('email', css_class="container-fluid"),
            Div('password', css_class="container-fluid"),
            Div('password2', css_class="container-fluid"),
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn btn-default')
        ),
        HTML("""
            <a href="{% url 'registration_site:login' %}">or log in</a>
        """),
    )
