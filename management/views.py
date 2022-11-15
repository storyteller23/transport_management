from django.shortcuts import render, redirect
from .models import *
from .forms import AddReportForm


# Create your views here.
def index(request):
    reports = Report.objects.all()
    context = {'reports': reports}
    return render(request, 'management/index.html', context=context)

def add_report(request):
    form = AddReportForm()
    context = {'form': form}
    return render(request, 'management/report.html', context=context)


def out(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        print("data sended")
    return redirect(index)