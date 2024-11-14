# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from apps.orders.models import Order
#
# #
# # @receiver(post_save, sender=Order)
# # def send_order_email(sender, instance, created, **kwargs):
# #     if created:
# #         send_mail(
# #             'Order Confirmation',
# #             f'Your order {instance.created_at} has been created successfully.',
# #             'from@example.com',
# #             [instance.user.email],
# #             fail_silently=False,
# #         )
#         # print(f"Confirmation email sent to {instance.user.email}")