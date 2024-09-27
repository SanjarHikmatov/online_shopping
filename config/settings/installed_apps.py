
# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ==========debug=========
    'debug_toolbar',

    # ==================Apps================
    'apps.generals',
    'apps.categories',
    'apps.authentication',
    'apps.abouts',
    'apps.sellers',
    # =============modeltranslation=========
    # 'modeltranslation',

]
