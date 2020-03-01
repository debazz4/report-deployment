from django.conf import settings
from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib import messages
from django.views.generic import (View, ListView, CreateView,TemplateView, 
                        DetailView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import CreateRecord
from .forms import CreateRecordForm
 

class HomeView(TemplateView):
    template_name = "home.html"

class TableListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = CreateRecord
    template_name = "createrecord.html"

    def get_queryset(self):
        return CreateRecord.objects.filter(user=self.request.user)



class NewRecordView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    login_url = '/accounts/login'
    template_name = 'new_record.html'
    model = CreateRecord
    form_class = CreateRecordForm
    success_url= reverse_lazy('rp_app:table-list')
    def get_success_message(self, cleaned_data):
        return "Record has been added!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SingleRecordView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    context_object_name = 'single'
    model = CreateRecord
    template_name = 'singleRecord.html'

class UpdateRecord(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    login_url = '/accounts/login'
    
    form_class = CreateRecordForm
    model = CreateRecord
    template_name = 'edit_record.html'
    success_url = reverse_lazy('rp_app:table-list')

    def get_success_message(self, cleaned_data):
        return "Record has been updated!"
    
class RecordDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = CreateRecord
    template_name = 'createrecord_delete.html'
    success_url = reverse_lazy('rp_app:table-list')



def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(suspect_name__icontains=query, user=request.user) | Q(complaint_name__icontains=query, user=request.user)

            results= CreateRecord.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')
