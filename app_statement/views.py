from django.shortcuts import render
from rest_framework import generics, views
from app_general_journal.serializers import EntryGetSerializer
from app_general_journal.models import Entry
from django.db.models import Max
from rest_framework.response import Response
# Create your views here.


class IncomeStatement(generics.ListAPIView):
    serializer_class = EntryGetSerializer

    def get_queryset(self):
        start = self.request.GET.get('start')
        if start == None: start = '2000-01-01'
        end = self.request.GET.get('end')
        if end == None: end = '3000-01-01'

        entries =Entry.objects.filter(dated__range = [start, end], head__in = [2,4])

        return entries

    def get(self, request):
        queryset = self.get_queryset()
        queryset = EntryGetSerializer(queryset, many=True)
        dataset = {'statement':{}, 'data':queryset.data}

        for entry in queryset.data:
            if entry['head']['title'] not in dataset['statement'].keys():
                dataset['statement'][entry['head']['title']] = {}
                dataset['statement'][entry['head']['title']]['Total'] = 0
            
            if entry['subhead']['title'] not in dataset['statement'][entry['head']['title']].keys():
                dataset['statement'][entry['head']['title']][entry['subhead']['title']] = {}
                dataset['statement'][entry['head']['title']][entry['subhead']['title']]['Total'] = 0

            if entry['account_subhead']['title'] not in dataset['statement'][entry['head']['title']][entry['subhead']['title']].keys():
                dataset['statement'][entry['head']['title']][entry['subhead']['title']][entry['account_subhead']['title']] = {}
                dataset['statement'][entry['head']['title']][entry['subhead']['title']][entry['account_subhead']['title']]['Total'] = 0
            #     dataset['statement'][entry['head']['title']][entry['subhead']['title']][entry['account_subhead']['title']]['entries'] = []
            
            # dataset['statement'][entry['head']['title']][entry['subhead']['title']][entry['account_subhead']['title']]['entries'].append(
            #     {
            #         'id':entry['id'],
            #         'dated':entry['dated'],
            #         "entry_type": entry['entry_type'],
            #         "amount": entry['amount'],
            #         "description": entry['description'],
            #         "created_on": entry['created_on'],
            #         "modified_on": entry['modified_on']
            #     }
            #     )
            dataset['statement'][entry['head']['title']]['Total'] += float(entry['amount'])
            dataset['statement'][entry['head']['title']][entry['subhead']['title']]['Total'] += float(entry['amount'])
            dataset['statement'][entry['head']['title']][entry['subhead']['title']][entry['account_subhead']['title']]['Total'] += float(entry['amount'])
        return Response(dataset)
    

def income_statement(request):
    return render(request, 'income_statement.html')