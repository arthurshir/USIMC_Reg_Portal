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

class ParentForm(forms.ModelForm):
    class Meta:
        model=models.Parent
        fields= '__all__'
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Div(
                Div(
                    HTML("""
                        <h3>Parent Information</h3>
                    """),
                    Div('firstName', css_class='col-md-4'),
                    Div('middleName', css_class='col-md-4'),
                    Div('lastName', css_class='col-md-4'),
                    Div('email', css_class='col-md-12'),
                    Div('homePhone', css_class='col-md-12'),
                    Div('mobilePhone', css_class='col-md-12'),
                    css_class='row'
                ),
                css_class='col-md-7',
            ),
            Div(
                Div(
                    HTML("""
                        <h3>Location</h3>
                    """),
                    Div('address', css_class='col-md-12'),
                    Div('city', css_class='col-md-8'),
                    Div('state', css_class='col-md-4'),
                    Div('zipCode', css_class='col-md-12'),
                    css_class='row'
                ),
                css_class='col-md-4 col-md-offset-1',
            ),
            css_class='row',
        ),
        
        ButtonHolder(
            StrictButton('Submit', css_class='btn btn-success', type="submit"),
        ),
    )

class PerformerForm(forms.ModelForm):
    class Meta:
        model=models.Performer
        fields= '__all__'
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Div(
                Div(
                    HTML("""
                        <h3>Performer</h3>
                    """),
                    Div('firstName', css_class='col-md-4'),
                    Div('middleName', css_class='col-md-4'),
                    Div('lastName', css_class='col-md-4'),
                    Div('teachers', css_class='col-md-12'),
                    Div('instrument', css_class='col-md-12'),
                    Div('accompanist', css_class='col-md-12'),
                    Div('group', css_class='col-md-12'),
                    css_class='row'
                ),
                css_class='col-md-7',
            ),
            Div(
                Div(
                    HTML("""
                        <h3>Pieces</h3>
                    """),
                    Div('piece1', css_class='col-md-12'),
                    Div('piece2', css_class='col-md-12'),
                    Div('chinesePiece', css_class='col-md-12'),
                    css_class='row'
                ),
                css_class='col-md-4 col-md-offset-1',
            ),
            css_class='row',
        ),
        
        ButtonHolder(
            StrictButton('Submit', css_class='btn btn-success', type="submit"),
        ),
    )

class TeacherForm(forms.ModelForm):
    class Meta:
        model=models.Teacher
        fields= '__all__'
