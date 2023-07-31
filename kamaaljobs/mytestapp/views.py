from django.shortcuts import render
from mytestapp.models import HydJobs,PuneJobs,BngJobs

# Create your views here.
def homepage_view(request):
    return render(request,'mytestapp/index.html')

def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'mytestapp/hydjobs.html',my_dict)

def punejobs_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'mytestapp/punejobs.html',my_dict)

def bngjobs_view(request):
    jobs_list = BngJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'mytestapp/bngjobs.html',my_dict)