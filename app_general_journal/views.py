from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Head, SubHead, AccountSubHead, Entry
from .serializers import HeadSerializer, SubHeadSerializer, AccountSubHeadSerializer, EntryGetSerializer, EntryPostSerializer

# Create your views here.


class HeadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Head.objects.all()
    serializer_class = HeadSerializer

class SubHeadViewSet(viewsets.ModelViewSet):
    queryset = SubHead.objects.all()
    serializer_class = SubHeadSerializer

    def get_queryset(self):
        queryset = self.queryset
        head = self.request.GET.get('head')
        if(head!=None): queryset = queryset.filter(head=head)
        return queryset

class AccountSubHeadViewSet(viewsets.ModelViewSet):
    queryset = AccountSubHead.objects.all()
    serializer_class = AccountSubHeadSerializer

    def get_queryset(self):
        queryset = self.queryset
        subhead = self.request.GET.get('subhead')
        if(subhead!=None): queryset = queryset.filter(subhead=subhead)
        return queryset

class EntryGetViewset(generics.ListAPIView):
    serializer_class = EntryGetSerializer

    def get_queryset(self):
        start = self.request.GET.get('start')
        if start == None: start = '2000-01-01'
        end = self.request.GET.get('end')
        if end == None: end = '3000-01-01'
        head = self.request.GET.get('head')
        subhead = self.request.GET.get('subhead')
        account_subhead = self.request.GET.get('account_subhead')
        entry_type = self.request.GET.get('entry_type')

        entries = Entry.objects.filter(dated__range = [start, end])
        if (head!=None): entries = entries.filter(head = head)
        if (subhead!=None): entries = entries.filter(subhead = subhead)
        if (account_subhead!=None): entries = entries.filter(account_subhead = account_subhead)
        if (entry_type!=None): entries = entries.filter(entry_type = entry_type)
        
        return entries

class EntryPostViewset(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntryPostSerializer
