from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# CRUD + L - Create, Retrieve, Update and Delete + List

class LandingPageView(TemplateView):
    template_name = 'landing_page.html'


class LeadListView(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


'''

def home_page(request):
    return render(request, "leads/home_page.html")


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context=context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context=context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context=context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        'form': form,
        'lead': lead
    }
    return render(request, 'leads/lead_update.html', context)



def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print(f"FORM IS VALID {form.cleaned_data}")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            age = form.cleaned_data["age"]
            agent = form.cleaned_data["agent"]
            phoned = form.cleaned_data["phoned"]
            source = form.cleaned_data["source"]
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent,
                phoned=phoned,
                source=source
            )
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context=context)


'''