# from django.db import models
# from django.contrib.auth import get_user_model
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import User, PermissionsMixin
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db import models
#
#
# # class UserAccountManager(BaseUserManager):
# #     use_in_migrations = True
# #
# #     def _create_user(self, email, password, **extra_fields):
# #         if not email:
# #             raise ValueError('Email address must be provided')
# #
# #         if not password:
# #             raise ValueError('Password must be provided')
# #
# #         email = self.normalize_email(email)
# #         user = self.model(email=email, **extra_fields)
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user
# #
# #     def create_user(self, email=None, password=None, **extra_fields):
# #         return self._create_user(email, password, **extra_fields)
# #
# #     def create_superuser(self, email, password, **extra_fields):
# #         extra_fields['is_staff'] = True
# #         extra_fields['is_superuser'] = True
# #
# #         return self._create_user(email, password, **extra_fields)
#
#
# # class User(AbstractBaseUser):
# #     pass
#     # REQUIRED_FIELDS = []
#     # USERNAME_FIELD = 'email'
#     #
#     # objects = UserAccountManager()
#     #
#     # email = models.EmailField('email', unique=True, blank=False, null=False)
#     # full_name = models.CharField('full name', blank=True, null=True, max_length=400)
#     # is_staff = models.BooleanField('staff status', default=False)
#     # is_active = models.BooleanField('active', default=True)
#     # is_verified = models.BooleanField('verified', default=False)  # Add the `is_verified` flag
#     #
#     # # def access_token(self):
#     # #     return str(RefreshToken.for_user(self).access_token)
#     # #
#     # # def refresh_token(self):
#     # #     return str(RefreshToken.for_user(self))
#     #
#     # def __str__(self):
#     #     return f"{self.email}"
#
#
# class Conversation(models.Model):
#     initiator = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, related_name="convo_starter"
#     )
#     receiver = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, related_name="convo_participant"
#     )
#     start_time = models.DateTimeField(auto_now_add=True)
#
#
# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.SET_NULL,
#                                null=True, related_name='message_sender')
#     text = models.CharField(max_length=200, blank=True)
#     attachment = models.FileField(blank=True)
#     conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, )
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('-timestamp',)
