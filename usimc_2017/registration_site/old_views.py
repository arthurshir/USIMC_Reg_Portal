



# def login(self):
#     self.user = self.serializer.validated_data['user']

#     if getattr(settings, 'REST_USE_JWT', False):
#         self.token = jwt_encode(self.user)
#     else:
#         self.token = create_token(self.token_model, self.user,
#                                   self.serializer)

#     if getattr(settings, 'REST_SESSION_LOGIN', True):
#         self.process_login()

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return super(LoginView, self).form_valid(form)
#         else:
#             try:
#                 user = User.objects.get(username=username)
#                 messages.add_message(request, messages.ERROR, 'Wrong email and password combination')
#                 redirect('login')
#             except User.DoesNotExist:
#                 messages.add_message(request, messages.ERROR, 'A user with the email ' + username + ' does not exist')
#                 redirect('login')


# #
# # Account Management Functions
# #

# def login(self):
#     self.user = self.serializer.validated_data['user']

#     if getattr(settings, 'REST_USE_JWT', False):
#         self.token = jwt_encode(self.user)
#     else:
#         self.token = create_token(self.token_model, self.user,
#                                   self.serializer)

#     if getattr(settings, 'REST_SESSION_LOGIN', True):
#         self.process_login()

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return super(LoginView, self).form_valid(form)
#         else:
#             try:
#                 user = User.objects.get(username=username)
#                 messages.add_message(request, messages.ERROR, 'Wrong email and password combination')
#                 redirect('login')
#             except User.DoesNotExist:
#                 messages.add_message(request, messages.ERROR, 'A user with the email ' + username + ' does not exist')
#                 redirect('login')


# class LoginView(FormView):
#     template_name = 'login.html'
#     form_class = forms.LoginForm
#     success_url = '/dashboard/'

#     def form_valid(self, form):
#         username = form.username
#         password = form.password
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return super(LoginView, self).form_valid(form)
#         else:
#             try:
#                 user = User.objects.get(username=username)
#                 messages.add_message(request, messages.ERROR, 'Wrong email and password combination')
#                 redirect('login')
#             except User.DoesNotExist:
#                 messages.add_message(request, messages.ERROR, 'A user with the email ' + username + ' does not exist')
#                 redirect('login')

# class RegistrationView(FormView):
#     template_name = 'register.html'
#     form_class = forms.RegistrationForm
#     success_url = '/dashboard/'

#     def form_valid(self, form):
#         first_name = forms.first_name
#         last_name = forms.last_name
#         username = forms.username
#         password = forms.password
#         confirm_password = forms.confirm_password

#         if password != confirm_password:
#             messages.add_message(request, messages.ERROR, 'Passwords do not match')
#             redirect('login')

#         # Try to log in first
#         user = authenticate(username=form.username, password=form.password)
#         if user is not None:
#             messages.add_message(request, messages.INFO, 'Logged into preexisting accoutn with email ' + username )
#             login(request, user)
#             return super(LoginView, self).form_valid(form)
#         else:
#             try:
#                 user = User.objects.get(username=username)
#                 messages.add_message(request, messages.ERROR, 'A user with the email ' + username + ' already exists')
#                 redirect('login')
#             except User.DoesNotExist:
#                 user = User.objects.create_user(username=username, password=password)
#                 user.save()
#                 user = authenticate(username=username, password=password)
#                 USIMCUserManager.create_user(user)
#                 login(request, user)
#                 return super(LoginView, self).form_valid(form)

# #
# # Dashboard Views
# #

# class DashboardView(View):

#     # @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(DashboardView, self).dispatch(*args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         context = {}
#         context['entry_form'] = forms.EntryForm()
#         context['piece_form'] = forms.PieceForm()
#         context['person_form'] = forms.PersonForm()
#         return render(request, 'dashboard.html', context)

# def new_entry(request):
#     context = {}
#     if request.method == 'POST':
#         form = forms.EntryForm(request.POST)
#         if form.is_valid():    
#             Entry.create( usimc_user=request.user.usimc_user, instrument_category=form.instrument_category, age_category = form.age_category, awards_applying_for=form.awards_applying_for )
#             return JsonResponse({'success': 'true', 'message', 'Successfully created!'})
#         else:
#             return JsonResponse({'success': 'false', 'message': 'Something was missing from your submission'})



# from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.decorators import login_required
# from .forms import UserSigninForm, UserSignupForm, ParentForm, PerformerForm, TeacherForm, PieceForm, ChinesePieceForm
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.forms.models import formset_factory
# from .models import Performer, Profile, Parent, Teacher, Piece, ChinesePiece
# import json

# def index(request):
#     return HttpResponse("Hello, world!")

# def dashboard(request):
#     profile = Profile.objects.get(user = request.user)
#     performer = Performer.objects.get(owningProfile = profile)

#     if request.method == "POST":
#         performerForm = PerformerForm(request.POST, instance=performer, prefix="performer")
#         teacherForm = TeacherForm(request.POST, instance=performer._teacher, prefix="teacher")
#         pieceForm1 = PieceForm(request.POST, instance=performer.piece1, prefix="piece1")
#         pieceForm2 = PieceForm(request.POST, instance=performer.piece2, prefix="piece2")
#         chinesePieceForm = ChinesePieceForm(request.POST, instance=performer.chinesePiece, prefix="chinesePiece")
#         parentForm = ParentForm(request.POST, instance=profile.parent, prefix="parent")

#         data = {}
#         if performerForm.is_valid() and teacherForm.is_valid() and pieceForm1.is_valid() and pieceForm2.is_valid() and chinesePieceForm.is_valid() and parentForm.is_valid():
#             performerForm.save()
#             teacherForm.save()
#             pieceForm1.save()
#             pieceForm2.save()
#             chinesePieceForm.save()
#             parentForm.save()
#             data['success'] = True
#             print("Form should be saved")
#         else:
#             data['success'] = False
#             data['error'] = "Invalid Form:\n performerForm: {}\nteacherForm: {}\npieceForm1: {}\npieceForm2: {}\nchinesePieceForm: {}\nparentForm: {}\n".format(performerForm.errors,teacherForm.errors,pieceForm1.errors,pieceForm2.errors,chinesePieceForm.errors,parentForm.errors)
            
#         return HttpResponse(json.dumps(data), content_type="application/json")

#     else:
#         context = {}
#         context['performerForm'] = PerformerForm(instance=performer, prefix="performer")
#         context['teacherForm'] = TeacherForm(instance=performer._teacher, prefix="teacher")
#         context['pieceForm1'] = PieceForm(instance=performer.piece1, prefix="piece1")
#         context['pieceForm2'] = PieceForm(instance=performer.piece2, prefix="piece2")
#         context['chinesePieceForm'] = ChinesePieceForm(instance=performer.chinesePiece, prefix="chinesePiece")

#         context['parentForm'] = ParentForm(instance=profile.parent, prefix="parent")
#         return render(request, 'registration_site/dashboard.html', context)

# def login_view(request):
#     if request.method == "POST":
#         form = UserSigninForm(request.POST)
#         if form.is_valid():
#             email = request.POST.get('email', '')
#             password = request.POST.get('password', '')

#             user = authenticate(username=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('registration_site:dashboard')
#             else:
#                 messages.warning(request, 'Wrong Login Information', extra_tags='login')
#                 return redirect('registration_site:login')
#         else:
#             messages.warning(request, 'Wrong Login Information', extra_tags='login')
#             return redirect('registration_site:login')
#     else:
#         context = {}
#         context['user_form'] = UserSigninForm()
#         context['panel_title'] = 'Sign in'
#         return render(request, 'registration_site/sign_in.html', context)

# def signup_view(request):
#     if request.method == "POST":
#         form = UserSignupForm(request.POST)
#         if form.is_valid():
#             first_name = request.POST.get('first_name', '')
#             last_name = request.POST.get('last_name', '')
#             email = request.POST.get('email', '')
#             password = request.POST.get('password', '')
#             confirm_password = request.POST.get('confirm_password', '')

#             if not '@' in email:
#                 messages.warning(request, 'Not an email address', extra_tags='signup')
#                 return redirect('registration_site:signup')

#             if User.objects.filter(username=email).exists():
#                 messages.warning(request, 'A User for {} already exists'.format(email), extra_tags='signup')
#                 return redirect('registration_site:signup')

#             if password != confirm_password: 
#                 messages.warning(request, 'Passwords do not match', extra_tags='signup')
#                 return redirect('registration_site:signup')

#             ## Instantiate Initial User Objects
#             # Profile
#             user = createOrUpdateDjangoUser(email, password, first_name, last_name)
#             parent = Parent.objects.create()
#             profile = Profile.objects.create(user = user, parent=parent)
#             # Performer
#             teacher = Teacher.objects.create()
#             piece1 = Piece.objects.create()
#             piece2 = Piece.objects.create()
#             chinesePiece = ChinesePiece.objects.create()
#             performer = Performer.objects.create(_teacher=teacher, piece1=piece1, piece2=piece2, chinesePiece=chinesePiece, owningProfile=profile)


#             login(request, user)
#             return redirect('registration_site:dashboard')
#         else:
#             messages.warning(request, 'Wrong Signup Information', extra_tags='signup')
#             return redirect('registration_site:signup')
#     else:
#         context = {}
#         context['user_form'] = UserSignupForm()
#         context['panel_title'] = 'Sign up'
#         return render(request, 'registration_site/sign_in.html', context)

# def createOrUpdateDjangoUser(email, password, first_name, last_name):
#     try:
#         user = User.objects.get(username=email)
#         user.set_password(password)
#     except User.DoesNotExist:
#         user = User.objects.create_user(username=email, password=password)
#     user.first_name = first_name
#     user.last_name = last_name
#     user.save()
#     return user


