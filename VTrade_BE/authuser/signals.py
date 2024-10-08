from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import CustomUser


@receiver(user_signed_up)
def populate_profile_from_google(sender, request, user, **kwargs):
    social_account = user.socialaccount_set.filter(provider="google").first()
    if social_account:
        extra_data = social_account.extra_data
        user.first_name = extra_data.get("given_name")
        user.last_name = extra_data.get("family_name")
        user.profile_image = extra_data.get("picture")
        user.save()
