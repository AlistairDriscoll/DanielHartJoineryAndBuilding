from django.shortcuts import render, redirect
from .forms import EnquiryForm
from django.core.mail import EmailMessage
from django.conf import settings


def enquiry_page(request):
    """
    View for the enquiry form. If request = get then displays the enquiry
    if request = POST then we need to validate the form, save the enquiry,
    send it as an email, then take the user to an enquiry recieved page
    """

    if request.method == "GET":
        form = EnquiryForm()

        context = {
            'form': form,
        }

        return render(
            request,
            'enquiries/enquiry_page.html',
            context,
        )

    else:
        form = EnquiryForm(request.POST)

        if form.is_valid():
            enquiry = form.save()

            name = enquiry.name
            email = enquiry.email
            location = enquiry.location
            job_title = enquiry.job_title
            description = enquiry.description

            message = (
                f"{job_title}\n"
                f"{description}\n"
                f"{email}\n"
            )
            subject = f"Enquiry from {name}, {location}"

            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ENQUIRY_RECIPIENT],
                reply_to=[enquiry.email],
            )
            email.send(fail_silently=False)

            return redirect('enquiry_success')
        else:
            return redirect('enquiry')


def enquiry_success(request):
    """ view to display the success template after user makes an enquiry """

    return render(
        request,
        'enquiries/enquiry_success.html',
    )
