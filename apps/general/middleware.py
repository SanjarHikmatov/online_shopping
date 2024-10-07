# from django.utils import translation
#
#
# class CurrLangMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         old_currency = request.session.get('currency')
#         currency = request.GET.get('currency', old_currency)
#         if currency != '1':
#             currency = '2'
#         request.session['currency'] = currency
#
#         old_language = request.session.get('language')
#         language = request.POST.get('language', old_language)
#         if language != '1':
#             language = '2'
#         request.session['language'] = language
#
#         language_code = 'uz' if language == '1' else 'en'
#
#         translation.activate(language_code)
#
#         response = self.get_response(request)
#
#         return response
