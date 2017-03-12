from django import forms
from . import models

from crispy_forms.helper import *
from crispy_forms.layout import *


class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['awards_applying_for', 'instrument_category', 'age_category']

    awards_applying_for = forms.MultipleChoiceField(choices=models.AWARD_CATEGORIES, widget=forms.CheckboxSelectMultiple)

class ParentContactForm(forms.ModelForm):
    class Meta:
        model = models.ParentContact
        fields = ['first_name', 'last_name', 'email', 'phone_number',]

class PieceForm(forms.ModelForm):
    class Meta:
        model = models.Piece
        fields = ['title', 'opus', 'movement', 'composer', 'length', 'is_chinese']

class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument', 'address', 'city', 'state', 'zip_code', 'country', 'birthday']
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

class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'cmtanc_code',]
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'

class EnsembleMemberForm(forms.ModelForm):
    class Meta:
        model = models.EnsembleMember
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument', 'birthday']
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
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
            Submit('submit', 'Submit', css_class='button white')
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
            Submit('submit', 'Submit', css_class='button white')
        ),
        HTML("""
            <a href="{% url 'registration_site:login' %}">or log in</a>
        """),
    )
