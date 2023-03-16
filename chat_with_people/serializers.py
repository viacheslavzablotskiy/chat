# from django.contrib.auth.models import User
# from django.contrib.messages.storage.cookie import MessageSerializer
#
# from .models import  Conversation
# from rest_framework import serializers
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
#
#
# class ConversationListSerializer(serializers.ModelSerializer):
#     initiator = UserSerializer()
#     receiver = UserSerializer()
#     last_message = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Conversation
#         fields = ['initiator', 'receiver', 'last_message']
#
#     def get_last_message(self, instance):
#         message = instance.message_set.first()
#         return MessageSerializer()
#
#
# class ConversationSerializer(serializers.ModelSerializer):
#     initiator = UserSerializer()
#     receiver = UserSerializer()
#     message_set = MessageSerializer()
#
#     class Meta:
#         model = Conversation
#         fields = ['initiator', 'receiver', 'message_set']
