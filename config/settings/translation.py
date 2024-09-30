from django.conf import settings
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en'

LOCALE_PATHS = [
    settings.BASE_DIR / 'translations'
]


USE_I18N = True
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LANGUAGES = (
    ('uz', _('Uzbek')),
    ('ru', _('Russian')),
    ('en', _('English')),
)

MODELTRANSLATION_LANGUAGE = ('uz', 'ru', 'en')
