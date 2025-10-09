from django.shortcuts import render
from .forms import EnquiryForm


def enquiry_page(request):
    """
    View for the enquiry form. If request = get then displays the enquiry
    if request = POST then we need to validate the form, save the enquiry,
    send it as an email, then take the user to an enquiry recieved page
    """

    form = EnquiryForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'enquiries/enquiry_page.html',
        context,
    )
