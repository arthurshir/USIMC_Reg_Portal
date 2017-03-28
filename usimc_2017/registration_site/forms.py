from django import forms
from . import models
import usimc_rules

from crispy_forms.helper import *
from crispy_forms.layout import *
import phonenumbers
from django.core.exceptions import ValidationError

def base_input_attrs(placeholder, required = False):
    attrs = {'placeholder': placeholder, 'class': 'application-input', 'data-parsley-trigger': 'change'}
    if required:
        attrs['required'] = ''
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
            'first_name': text_input_widget(placeholder='First Name', required=True ),
            'last_name': text_input_widget(placeholder='Last Name', required=True ),
            'email': email_input_widget(placeholder='Email', required=True ),
            'phone_number': phone_number_input_widget(placeholder='Phone Number', required=True ),
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
        fields = ['title', 'opus', 'movement', 'composer', 'length', 'youtube_link',]
        widgets = {
            'title': text_input_widget(placeholder='Title', required=True ),
            'opus': text_input_widget(placeholder='Opus' ),
            'movement': text_input_widget(placeholder='Movement' ),
            'composer': text_input_widget(placeholder='Composer', required=True ),
            'youtube_link': text_input_widget(placeholder='Youtube Link (Only needed for Young Artist Award Entry)' ),
            'length': text_input_widget(placeholder='Length' ),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['first_name', 'last_name', 'instrument', 'address', 'city', 'state', 'zip_code', 'country', 'birthday']
        widgets = {
            'first_name': text_input_widget(placeholder='First Name', required=True ),
            'last_name': text_input_widget(placeholder='Last_name', required=True ),
            'instrument': text_input_widget(placeholder='Instrument', required=True ),
            'address': text_input_widget(placeholder='Address', required=True ),
            'city': text_input_widget(placeholder='City', required=True ),
            'state': text_input_widget(placeholder='State', required=True ),
            'zip_code': text_input_widget(placeholder='Zip_code', required=True ),
            'country': text_input_widget(placeholder='Country', required=True ),
            'birthday': cmtanc_birthday_input_widget(),
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
            'first_name': text_input_widget(placeholder='First Name', required=True ),
            'last_name': text_input_widget(placeholder='Last Name', required=True ),
            'email': email_input_widget(placeholder='Email', required=True ),
            'phone_number': phone_number_input_widget(placeholder='Phone Number', required=True ),
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
            'first_name': text_input_widget(placeholder='First Name', required=True ),
            'last_name': text_input_widget(placeholder='Last Name', required=True ),
            'instrument': text_input_widget(placeholder='Instrument', required=True ),
            'birthday': cmtanc_birthday_input_widget(),
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
            Submit('submit', 'Register', css_class='btn btn-submit')
        ),
        HTML("""
            <div style="height:5px;"></div>
            <a href="{% url 'registration_site:login' %}">or log in</a>
        """),
    )

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)
