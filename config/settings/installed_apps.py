
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
    'apps.general',
    'apps.categories',
    'apps.authentication',
    'apps.abouts',
    'apps.sellers',
    'apps.users',
    'apps.products',
    'apps.ratings',
    'apps.comments',
    'apps.coupons',
    'apps.orders',
    'apps.features',
    'apps.wishlists',
    'apps.carts',
    'apps.product_features',
    'apps.contact',

    # =============modeltranslation=========
    # 'modeltranslation',

]
