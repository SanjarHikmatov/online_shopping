
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # =============Debug TOOLBAR MIDDLEWARE=================
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # ===========modeltranslation==========
    'django.middleware.locale.LocaleMiddleware',

    # 'apps.general.middleware.CurrLangMiddleware'
]
