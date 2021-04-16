from rest_framework import serializers

from common.drf.serializers import BulkModelSerializer
from .models import Subscription, Backend, Message


class SubscriptionSerializer(BulkModelSerializer):

    class Meta:
        model = Subscription
        fields = ('id', 'users', 'groups', 'messages', 'receive_backends')


class SubscriptionUserRelationSerializer(BulkModelSerializer):
    class Meta:
        model = Subscription.users.through
        fields = [
            'id', 'subscription_id', 'user_id'
        ]


class SubscriptionGroupRelationSerializer(BulkModelSerializer):
    class Meta:
        model = Subscription.groups.through
        fields = [
            'id', 'subscription_id', 'usergroup_id'
        ]


class SubscriptionMessageRelationSerializer(BulkModelSerializer):
    class Meta:
        model = Subscription.messages.through
        fields = [
            'id', 'subscription_id', 'message_id'
        ]


class SubscriptionBackendRelationSerializer(BulkModelSerializer):
    class Meta:
        model = Subscription.receive_backends.through
        fields = [
            'id', 'subscription_id', 'backend_id'
        ]


class BackendSerializer(BulkModelSerializer):
    class Meta:
        model = Backend
        fields = ('id', 'name',)


class MessageSerializer(BulkModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'app', 'message', 'app_label', 'message_label')