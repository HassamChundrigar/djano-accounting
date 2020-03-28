from django.contrib import admin
from .models import Head, SubHead, AccountSubHead, Entry
# Register your models here.


@admin.register(Head)
class HeadAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(SubHead)
class SubHeadAdmin(admin.ModelAdmin):
    list_display = ['title', 'head', 'description']

@admin.register(AccountSubHead)
class AccountSubHeadAdmin(admin.ModelAdmin):
    list_display = ['title', 'subhead','description']
    list_filter = ['subhead']

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['dated','head', 'subhead', 'account_subhead', 'entry_type', 'amount']
    list_filter = ['dated', 'head','subhead', 'account_subhead', 'entry_type', 'amount']
