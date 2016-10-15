from django import forms
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from django.contrib.auth.models import User
from crispy_forms.bootstrap import StrictButton

class UserSigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.layout = Layout(
        Div(
        	Div('email', css_class='col-xs-12'),
        	Div('password', css_class='col-xs-12'),
    	),
        ButtonHolder(
        	StrictButton('Sign in', css_class='btn btn-success', type="submit"),
        	StrictButton('Sign up', css_class='btn btn-info', style="float: right;"),
		),
    )

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.layout = Layout(
        HTML("""
            <div class="rowspacer" style="height:20px;"> </div>
            <h4>Sign up</h4>
            <div class="rowspacer" style="height:20px;"> </div>
        """),
        Div(
        	Div('first_name', css_class='col-xs-12'),
        	Div('last_name', css_class='col-xs-12'),
        	Div('email', css_class='col-xs-12'),
        	Div('password', css_class='col-xs-12'),
        	)
    )

