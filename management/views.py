from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import ReportCreationForm
from .models import Report

def home(request):
    return render(request, 'management/index.html')

def reports_view(request):
    reports = Report.objects.all()
    context = {'reports': reports}
    return render(request, 'management/reports.html', context=context)

class ReportCreateView(CreateView):
    form_class = ReportCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'management/add_report.html'

    def post(self, request, *args, **kwargs):
        form = ReportCreationForm(request.POST)
        form.employee = request.user
        if form.is_valid():            
            report = form.save(commit=False)
            report.employee = request.user
            report.save()

            return redirect('homepage')
        else:
            return render(request, self.template_name, {'form': form})