from django import forms
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from django.contrib.auth.models import User
from crispy_forms.bootstrap import StrictButton
from . import models

class UserSigninForm(forms.Form):

    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
        	Div('email', css_class='col-xs-12'),
        	Div('password', css_class='col-xs-12'),
    	),
        ButtonHolder(
        	StrictButton('Log in', css_class='btn btn-success', type="submit"),
		),
        HTML("""
            <div style="height:4px;"> </div>
            <a href="/signup">or sign up</a>
        """),
    )

class UserSignupForm(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-xs-4'
    helper.field_class = 'col-xs-8'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Div('first_name', css_class='col-xs-5'),
            Div('last_name', css_class='col-xs-5 col-xs-offset-2'),
            Div('email', css_class='col-xs-12'),
            Div('password', css_class='col-xs-12'),
            Div('confirm_password', css_class='col-xs-12'),
        ),
        ButtonHolder(
            StrictButton('Sign up', css_class='btn btn-success', type="submit"),
        ),
        HTML("""
            <div style="height:4px;"> </div>
            <a href="/login">or log in</a>
        """),
    )

class ParentForm(forms.Form):
    class Meta:
        model=models.Parent
        fields= '__all__'

class PerformerForm(forms.Form):
    class Meta:
        model=models.Performer
        fields= '__all__'

class TeacherForm(forms.Form):
    class Meta:
        model=models.Teacher
        fields= '__all__'
