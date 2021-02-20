from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


# Create your views here.
def home_page(request):
    return render(request, "leads/home_page.html")


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context=context)


def lead_detail(request, pk):
    print(f"PK {pk}")
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request,"leads/lead_detail.html",context=context)
