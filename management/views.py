from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'management/index.html')

def add_report(request):
    return render(request, 'management/report.html')


def out(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        print("data sended")
    return redirect(index)