# from django.shortcuts import render

# # Create your views here.
# def contact(request):
#     context = {'contact_active': 'active'}
#     return render(request, 'contact/contact.html', context)


from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def contact_view(request):
    if request.method == 'POST':
        print("Form submitted!")  # ✅ Debug
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # ✅ Debug
            contact = form.save()

            # Send email to yourself
            subject = f"New Contact Message from {contact.name}"
            from_email = None  # Uses DEFAULT_FROM_EMAIL
            to_email = ['bdey862002@gmail.com']  # Replace with your real email

            # HTML content
            html_content = render_to_string('contact/emails/contact_notification.html', {
                'contact': contact,
            })

            msg = EmailMultiAlternatives(subject, '', from_email, to_email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()


            # ✅ Auto-reply to sender
            reply_subject = "Thanks for contacting me!"
            from_email = "Biswajit's Portfolio <bdey862002@gmail.com>"
            reply_to = [contact.email]

            html_reply = render_to_string('contact/emails/contact_reply.html', {
                'contact': contact,
            })

            reply_msg = EmailMultiAlternatives(reply_subject, '', from_email, reply_to)
            reply_msg.attach_alternative(html_reply, "text/html")
            reply_msg.send()

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            print(form.errors)  # ✅ Debug
            messages.error(request, 'There was an error submitting the form. Please check all fields.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'contact_active': 'active',
    }
    return render(request, 'contact/contact.html', context)

