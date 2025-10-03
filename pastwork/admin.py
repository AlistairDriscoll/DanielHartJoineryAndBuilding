from django.contrib import admin
from .models import CATReview, PastWorkAlbum, ProjectImage


admin.site.register(CATReview)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # show 1 empty form by default
    max_num = 15  # ✅ limit to 15 images
    fields = ["image"]  # only show image field


@admin.register(PastWorkAlbum)
class PastWorkAlbumAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ProjectImageInline]
