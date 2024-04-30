from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest

def index(request):
    bugs_url = reverse('quality_control:bugs')
    features_url = reverse('quality_control:features')

    html = f"<h1>Система контроля качества</h1><a href='{bugs_url}'>Список всех багов</a><br><a href='{features_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    bug_list_url = reverse('tasks:bug_list')
    html = f"<a href='{bug_list_url}'>Список багов</a>"
    return HttpResponse(html)

def feature_list(request):

    feature_list_url = reverse('tasks:feature_list')
    html = f"<a href='{feature_list_url}'>Список запросов на улучшение</a>"
    return HttpResponse(html)

def bug_detail(request,bug_id):
    ID = str(bug_id)
    return HttpResponse("Детали бага "+ID)

def feature_id_detail(request,feature_id):
    ID=str(feature_id)
    return HttpResponse("Детали улучшения "+ID)




def bug_list(request):
    Bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in Bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title} - {bug.status}</a></li>'
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)

from django.views import View

def feature_list(request):
    Features = FeatureRequest.objects.all()
    feature_html = '<h1>Список запросов на улучшение</h1><ul>'
    for Feature in Features:
        feature_html += f'<li><a href="{Feature.id}/">{Feature.title} - {Feature.status}</a></li>'
    feature_html += "</ul>"
    return HttpResponse(feature_html)

from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_url = reverse('quality_control:bugs')
        features_url = reverse('quality_control:features')

        html = f"<h1>Система контроля качества</h1><a href='{bugs_url}'>Список всех багов</a><br><a href='{features_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)


from django.views.generic import DetailView

class BugReportView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object

        response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p><p>{bug.status}</p><p>{bug.priority}</p><p>{bug.project}</p><p>{bug.task}</p>'
        return HttpResponse(response_html)

class FeatureReportView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'features_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object

        response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p><p>{feature.status}</p><p>{feature.priority}</p><p>{feature.project}</p><p>{feature.task}</p>'
        return HttpResponse(response_html)