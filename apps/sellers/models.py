from django.db import models
from apps.general.choices import SocialMedia
from django.core.validators import MinValueValidator, MaxValueValidator




class Seller(models.Model):
    class Gender(models.TextChoices):
        MALE = '0', 'MALE'
        FEMALE = '1', 'FEMALE'

    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)])
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class SellerSocialLink(models.Model):
    social_media = models.PositiveSmallIntegerField(
        choices=SocialMedia.choices,
        default=SocialMedia.TELEGRAM
    )
    link = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.social_media



























# from django.utils.translation.trans_null import gettext_lazy as _, get_language
# from django.utils.translation.trans_real import gettext

#
#     @property
#     def name_deyail(self):
#         """
#         biz bu propertydan kelayotgan obj ni
#         tarajima qiladiga fildlarini ushlab olish uchun f
#         ordalanamiz
#
#         returunda tarjima qilinadigan fildlarni qaytarganmiz
#
#         """
#         obj = SellerDetails.objects.get(pk=self.pk, language_id=get_language())
#         return {
#             'name': obj.name,
#             'gender': obj.gender,
#             'description': obj.description,
#         }
#
#
# class SellerDetails(models.Model):
#     """
#     biz bu class dan sellerni detaillarini
#
#     """
#     class Language(models.TextChoices):
#         UZ = 'UZ',
#         EN = 'EN',
#         RU = 'RU',
#
#     seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
#     language = models.CharField(max_length=10, choices=Language.choices)
#

"""biz seller app da translation ni
qo'lda yozganmiz qolganlarini
modeltranslation dan foydalandim
"""
# from random import choices
