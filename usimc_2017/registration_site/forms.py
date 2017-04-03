from django import forms
from . import models
import usimc_rules

from crispy_forms.helper import *
from crispy_forms.layout import *
import phonenumbers
from django.core.exceptions import ValidationError

def base_input_attrs(placeholder, required = False):
    attrs = {'placeholder': placeholder, 'class': 'application-input'}
    # if required:
    #     attrs['required'] = ''
    return attrs    
def text_input_widget(placeholder, required=False):
    attrs = base_input_attrs(placeholder=placeholder, required=required)
    return forms.TextInput(attrs=attrs)
def email_input_widget(placeholder, required=False):
    attrs = base_input_attrs(placeholder=placeholder, required=required)
    attrs['type'] = 'email'
    return forms.TextInput(attrs=attrs)
def phone_number_input_widget(placeholder, required=False):
    attrs = base_input_attrs(placeholder=placeholder, required=required)
    return forms.TextInput(attrs=attrs)
def cmtanc_birthday_input_widget():
    return forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        years=range(1980, 2017),
        attrs={'data-parsley-trigger': 'change', 'required': '', 'data-parsley-birthday': ''},
        )

class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['instrument_category', 'age_category', 'awards_applying_for']

    awards_applying_for = forms.MultipleChoiceField(choices=usimc_rules.AWARD_CHOICES, widget=forms.CheckboxSelectMultiple)

class ParentContactForm(forms.ModelForm):
    class Meta:
        model = models.ParentContact
        fields = ['first_name', 'last_name', 'email', 'phone_number',]
        widgets = {
            'first_name': text_input_widget(placeholder='First Name*', required=True ),
            'last_name': text_input_widget(placeholder='Last Name*', required=True ),
            'email': email_input_widget(placeholder='Email*', required=True ),
            'phone_number': phone_number_input_widget(placeholder='Phone Number*', required=True ),
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


class PieceForm(forms.ModelForm):
    class Meta:
        model = models.Piece
        fields = ['title', 'opus', 'movement', 'composer', 'minutes', 'seconds', 'youtube_link',]
        widgets = {
            'title': text_input_widget(placeholder='Title*', required=True ),
            'opus': text_input_widget(placeholder='Opus' ),
            'movement': text_input_widget(placeholder='Movement' ),
            'composer': text_input_widget(placeholder='Composer*', required=True ),
            'youtube_link': text_input_widget(placeholder='Youtube Link (Only needed for Young Artist Award Entry)' ),
            'minutes': text_input_widget(placeholder='min*', required=True ),
            'seconds': text_input_widget(placeholder='sec*', required=True ),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['first_name', 'last_name', 'instrument', 'address', 'city', 'state', 'zip_code', 'country', 'month', 'day', 'year']
        widgets = {
            'first_name': text_input_widget(placeholder='First Name*', required=True ),
            'last_name': text_input_widget(placeholder='Last name*', required=True ),
            'instrument': text_input_widget(placeholder='Instrument*', required=True ),
            'address': text_input_widget(placeholder='Address*', required=True ),
            'city': text_input_widget(placeholder='City*', required=True ),
            'state': text_input_widget(placeholder='State*', required=True ),
            'zip_code': text_input_widget(placeholder='Zip code*', required=True ),
            'country': text_input_widget(placeholder='Country*', required=True ),
            'month': text_input_widget(placeholder='MM', required=True ),
            'day': text_input_widget(placeholder='DD', required=True ),
            'year': text_input_widget(placeholder='YYYY', required=True ),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['first_name', 'last_name', 'email', 'cmtanc_code',]
        widgets = {
            'first_name': text_input_widget(placeholder='First Name*', required=True ),
            'last_name': text_input_widget(placeholder='Last Name*', required=True ),
            'email': email_input_widget(placeholder='Email*', required=True ),
            'cmtanc_code': text_input_widget(placeholder='CMTANC Code' ),
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
            Div('cmtanc_code', css_class="col-md-12"),
            css_class="row"
        ),
    )

class EnsembleMemberForm(forms.ModelForm):
    class Meta:
        model = models.EnsembleMember
        fields = ['first_name', 'last_name', 'instrument', 'month', 'day', 'year']
        widgets = {
            'first_name': text_input_widget(placeholder='First Name*', required=True ),
            'last_name': text_input_widget(placeholder='Last Name*', required=True ),
            'instrument': text_input_widget(placeholder='Instrument*', required=True ),
            'month': text_input_widget(placeholder='MM', required=True ),
            'day': text_input_widget(placeholder='DD', required=True ),
            'year': text_input_widget(placeholder='YYYY', required=True ),
        }

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
            Submit('submit', 'Log in', css_class='btn btn-submit')
        ),
        HTML("""
            <div style="height:5px;"></div>
            <a href="{% url 'registration_site:register' %}">or register</a>
        """),
    )

class RegistrationForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    # class Meta:
    #     labels = {'password2': 'confirm password'}

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
            Submit('submit', 'Register', css_class='btn btn-submit')
        ),
        HTML("""
            <div style="height:5px;"></div>
            <a href="{% url 'registration_site:login' %}">or log in</a>
        """),
    )