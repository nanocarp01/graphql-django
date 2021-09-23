from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.core.mail import send_mail, BadHeaderError
from .forms import RegisterUserForm
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q

def register(request):
    if request.user.is_authenticated:
        print('Already authenticated')
        return HttpResponseRedirect(reverse('logs:index'))
    else:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            # RegisterUserForm is created from User model, all model field restrictions are checked to considerate it a valid form
            if form.is_valid():
                print('Valid form')
                # Save user to database but with is_active = False
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                # Send confirmation email
                current_site = get_current_site(request)
                subject = 'Activate Your ' + current_site.domain + ' Account'
                message = render_to_string('api_reg/email_confirmation.html',
                    {
                        "domain": current_site.domain,
                        "user": user,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                    },
                )
                to_email = form.cleaned_data.get('email')
                send_mail(subject, message, 'fe@gmail.com', [to_email])

                # Redirect user to login
                messages.success(request, 'Please Confirm your email to complete registration before Login.')
                return HttpResponseRedirect(reverse('login'))
            else:
                #print('Invalid form: %s' % form.errors.as_data())
                #print(type(form.errors.as_data()))
                if form.errors:
                    #messages.info(request, 'Input field errors:')
                    for key, values in form.errors.as_data().items():
                        #print("Bad value: %s - %s" % (key, values))
                        if key == 'username':
                            messages.info(request, 'Error input fields')
                            break
                        else:
                            for error_value in values:
                                print(error_value)
                                #print(type(error_value))
                                messages.info(request, '%s' % (error_value.message))

                return HttpResponseRedirect(reverse('authi:register'))
        else:
            form = RegisterUserForm()

            context = {
                'form': form
            }
            return render(request, 'api_reg/register.html', context)

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Redirect user to login
        messages.success(request, 'Successful email confirmation, you can proceed to login.')
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponse('Activation link is invalid!')


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
                   
					return redirect ("password_reset/done")
                   
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset_form.html", context={"password_reset_form":password_reset_form})