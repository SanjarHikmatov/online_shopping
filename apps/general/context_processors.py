from apps.categories.models import Category
from apps.general.models import General, GeneralSocialMedia


def general_context(request):
    context = {
        'general': General.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all(),
    }
    return context