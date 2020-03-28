from rest_framework import serializers
from .models import Head, SubHead, AccountSubHead, Entry


class HeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Head
        fields = '__all__'


class SubHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubHead
        fields = '__all__'


class AccountSubHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSubHead
        fields = '__all__'


class EntryGetSerializer(serializers.ModelSerializer):
    head = HeadSerializer(read_only=True)
    subhead = SubHeadSerializer(read_only=True)
    account_subhead = AccountSubHeadSerializer(read_only=True)

    class Meta:
        model = Entry
        fields = '__all__'

class EntryPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Entry
        fields = '__all__'