from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import CATReview, PastWorkAlbum


class ReviewList(generic.ListView):
    """Display and paginate all reviews"""

    model = CATReview  # ✅ clearer than using `queryset`
    template_name = "pastwork/reviews.html"
    context_object_name = "reviews"  # ✅ optional, makes template cleaner
    paginate_by = 6
    ordering = ["-id"]


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


def pastwork_detail(request, slug):
    """ Displays the full photo album from a past job """

    past_work_album = get_object_or_404(PastWorkAlbum, slug=slug)
    images = past_work_album.images.all()

    context = {
        'past_work_album': past_work_album,
        'images': images,
    }

    return render(
        request,
        "pastwork/pastwork_detail.html",
        context,
    )
