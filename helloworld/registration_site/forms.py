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
            HTML("""<div class="rowspacer" style="height:10px;"></div>"""),
        	Div('email', css_class="container-fluid"),
            HTML("""<div class="rowspacer" style="height:10px;"></div>"""),
        	Div('password', css_class="container-fluid"),
            HTML("""<div class="rowspacer" style="height:10px;"></div>"""),
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
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.label_class = 'hidden'
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Div(
                HTML("""<div class="rowspacer" style="height:10px;"></div>"""),
                Div('email', css_class="container-fluid"),
                HTML("""<div class="rowspacer" style="height:10px;"></div>"""),
                Div('password', css_class="container-fluid"),
                HTML("""<div class="description">Must be between 5 and 15 characters. Should only include letters and numbers.</div>"""),
                HTML("""<div class="rowspacer" style="height:10px;"></div>"""),
                Div('confirm_password', css_class="container-fluid"),
                HTML("""<div class="rowspacer" style="height:20px;"></div>"""),
            ),
            ButtonHolder(
                StrictButton('Sign up', css_class='btn btn-success', type="submit"),
            ),
            HTML("""
                <div style="height:4px;"> </div>
                <a href="/login">or log in</a>
            """),
            
        )
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
    )

class PerformerForm(forms.ModelForm):
    class Meta:
        model=models.Performer
        fields= ('firstName', 'middleName', 'lastName', 'instrument', 'accompanist', 'group',)
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
                    Div('instrument', css_class='col-md-12'),
                    Div('accompanist', css_class='col-md-12'),
                    Div('group', css_class='col-md-12'),
                    css_class='row'
                ),
                css_class='col-md-12',
            ),
            css_class='row',
        ),
    )

class TeacherForm(forms.ModelForm):
    class Meta:
        model=models.Teacher
        fields= '__all__'
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.layout = Layout (
        HTML("""
            <h3>Teacher</h3>
        """),
        "firstName",
        "middleName",
        "lastName",
        "contactId",
        "email",
        "homePhone",
        "mobilePhone",
        "locationId",
        "address",
        "city",
        "state",
        "zipCode",
    )

class PieceForm(forms.ModelForm):
    class Meta:
        model=models.Piece
        fields= '__all__'
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.layout = Layout (
        HTML("""
            <h3>Piece</h3>
        """),
        'pieceId',
        'catalogue',
        'title',
        'composer',
    )

class ChinesePieceForm(forms.ModelForm):
    class Meta:
        model=models.Piece
        fields= '__all__'
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.layout = Layout (
        HTML("""
            <h3>Chinese Piece</h3>
        """),
        'pieceId',
        'catalogue',
        'title',
        'composer',
    )

class PieceFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PieceFormSetHelper, self).__init__(*args, **kwargs)
        self.form_class = 'form-horizontal'
        self.field_template = 'bootstrap3/layout/inline_field.html'
