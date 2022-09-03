from multiprocessing import context
from django.shortcuts import render
from job_search.models import Job
from .forms import SearchBarForm

from django.db.models import Q

from functools import reduce
import operator


def job_search_index(request):
    jobs = Job.objects.all()

    query = ""
    results = None

    form = SearchBarForm()
    if request.method == 'POST':
        form = SearchBarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            if ',' in query:
                query = query.split(',')
            else:
                query = query.split(' ')

            print(query)

            titleResults = Job.objects.filter(reduce(operator.and_, [Q(title__icontains=term) for term in query]))
            compnameResults = Job.objects.filter(reduce(operator.and_, [Q(company_name__icontains=term) for term in query]))
            locationResults = Job.objects.filter(reduce(operator.and_, [Q(location__icontains=term) for term in query]))
            experienceResults = Job.objects.filter(reduce(operator.and_, [Q(experience__icontains=term) for term in query]))
            skillsResults = Job.objects.filter(reduce(operator.and_, [Q(skills__icontains=term) for term in query]))
            results = titleResults | compnameResults | locationResults | experienceResults | skillsResults
    else:
        form = SearchBarForm()\

    context = {
        'jobs': jobs,
        'form': form,
        'query': query if query else "",
        'results': results            
        }    
    return render(request, 'job_search_index.html', context)


def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    context = {
        'job': job
    }
    return render(request, 'job_detail.html', context)
