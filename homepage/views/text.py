from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from homepage import models as cmod
from .. import dmp_render, dmp_render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django import forms
from twilio.rest import Client
from phonenumber_field.modelfields import PhoneNumberField

class MessageInfo(forms.Form):
	name = forms.CharField(max_length=300, required=True, widget=forms.TextInput({ "placeholder": "Name"}), label="Name")
	number = forms.CharField(max_length=12, required=True, widget=forms.TextInput({ "placeholder": "Phone Number"}), label="Phone")

@view_function
def process_request(request):

	form = MessageInfo()

	if request.method == "POST":

		form = MessageInfo(request.POST)

		if form.is_valid():

			account_sid = "AC4353782975dde76ecb07854668937a5d"
			# Your Auth Token from twilio.com/console
			auth_token  = "085e4acb01c38f697a69017bac45249f"

			client = Client(account_sid, auth_token)

			text = form.cleaned_data.get("name") + ", Thank you for supporting our business! We invite you to leave a review for us at [Insert Link Here]"

			message = client.messages.create(
				to=form.cleaned_data.get("number"), 
				from_="+13852460276",
				body=text)

	context = {
		'form': form,
	}
	return dmp_render(request, 'text.html', context)