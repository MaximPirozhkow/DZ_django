from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest

from django.shortcuts import render, get_object_or_404


from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

def index(request):
    return render(request, 'quality_control/index.html')


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})




class BugReportView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bugs_id'
 #   template_name = 'quality_control/Bug_detail.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/Bug_detail.html')


class FeatureReportView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'features_id'
    template_name = 'quality_control/feature_detail.html'



def add_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})



def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})





class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs')
    template_name = 'quality_control/bug_confirm_delete.html'

class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'features_id'
    success_url = reverse_lazy('quality_control:features')
    template_name = 'quality_control/feature_confirm_delete.html'

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/Bug_detail.html'

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'features_id'
    template_name = 'quality_control/feature_detail.html'


def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bugs')
def delete_feature(request, features_id):
    feature = get_object_or_404(FeatureRequest, pk=features_id)
    feature.delete()
    return redirect('quality_control:features')


def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_id', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})


def update_feature(request, features_id):
    feature = get_object_or_404(FeatureRequest, pk=features_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_id', features_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'features': feature})

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs')

class FeagureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'features_id'
    success_url = reverse_lazy('quality_control:features')




class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs')

class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features')

class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'

class FeatureListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'









#def index(request):
#   bugs_url = reverse('quality_control:bugs')
#    features_url = reverse('quality_control:features')

#    html = f"<h1>Система контроля качества</h1><a href='{bugs_url}'>Список всех багов</a><br><a href='{features_url}'>Запросы на улучшение</a>"
#    return HttpResponse(html)



#def bug_list(request):
#    bug_list_url = reverse('quality_control:bug_list')
#    html = f"<a href='{bug_list_url}'>Список багов</a>"
#    return HttpResponse(html)

#def feature_list(request):
#
#    feature_list_url = reverse('quality_control:feature_list')
#    html = f"<a href='{feature_list_url}'>Список запросов на улучшение</a>"
#    return HttpResponse(html)

#def bug_detail(request,bug_id):
#    ID = str(bug_id)
#    return HttpResponse("Детали бага "+ID)

#def feature_id_detail(request,feature_id):
#    ID=str(feature_id)
#    return HttpResponse("Детали улучшения "+ID)




#def bug_list(request):
#    Bugs = BugReport.objects.all()
#    bugs_html = '<h1>Список багов</h1><ul>'
#    for bug in Bugs:
#        bugs_html += f'<li><a href="{bug.id}/">{bug.title} - {bug.status}</a></li>'
#    bugs_html += "</ul>"
#    return HttpResponse(bugs_html)

from django.views import View

#def feature_list(request):
#    Features = FeatureRequest.objects.all()
#    feature_html = '<h1>Список запросов на улучшение</h1><ul>'
#    for Feature in Features:
#        feature_html += f'<li><a href="{Feature.id}/">{Feature.title} - {Feature.status}</a></li>'
#    feature_html += "</ul>"
#    return HttpResponse(feature_html)

#from django.views import View

#class IndexView(View):
#    def get(self, request, *args, **kwargs):
#        bugs_url = reverse('quality_control:bugs')
#        features_url = reverse('quality_control:features')
#
#        html = f"<h1>Система контроля качества</h1><a href='{bugs_url}'>Список всех багов</a><br><a href='{features_url}'>Запросы на улучшение</a>"
#        return HttpResponse(html)


#from django.views.generic import DetailView

#class BugReportView(DetailView):
#    model = BugReport
#    pk_url_kwarg = 'bug_id'

#    def get(self, request, *args, **kwargs):
#        self.object = self.get_object()
#        bug = self.object

#        response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p><p>{bug.status}</p><p>{bug.priority}</p><p>{bug.project}</p><p>{bug.task}</p>'
#        return HttpResponse(response_html)

#class FeatureReportView(DetailView):
#    model = FeatureRequest
#    pk_url_kwarg = 'features_id'

#    def get(self, request, *args, **kwargs):
#        self.object = self.get_object()
#        feature = self.object

#        response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p><p>{feature.status}</p><p>{feature.priority}</p><p>{feature.project}</p><p>{feature.task}</p>'
#        return HttpResponse(response_html)