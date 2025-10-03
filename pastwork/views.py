from django.shortcuts import render
from .models import CATReview, PastWorkAlbum


def reviews(request):
    """ Displays the reviews from checkatrade """

    reviews = CATReview.objects.all()

    context = {
        "reviews": reviews,
    }
    return render(
        request,
        "pastwork/reviews.html",
        context,
    )


def pastwork(request):
    """ Displays photo albums of past work at older jobs """

    past_work_albums = PastWorkAlbum.objects.all()

    context = {
        'past_work_albums': past_work_albums,
    }

    return render(
        request,
        "pastwork/pastwork.html",
        context,
    )
