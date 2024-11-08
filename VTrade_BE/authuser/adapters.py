from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form=form)
        # Customize initial data for new users, like setting a default role
        if sociallogin.is_new:
            user.role = "CUSTOMER"
            user.save()
        return user
