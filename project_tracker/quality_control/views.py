from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bugs_url = reverse('quality_control:bugs')
    features_url = reverse('quality_control:features')

    html = f"<h1>Система контроля качества</h1><a href='{bugs_url}'>Список всех багов</a><br><a href='{features_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    html = f"<h1>Cписок отчетов об ошибках</h1>"
    return HttpResponse(html)

def feature_list(request):
    html = f"<h1>Список запросов на улучшение</h1>"
    return HttpResponse(html)

def bug_detail(request,bug_id):
    ID = str(bug_id)
    return HttpResponse("Детали бага "+ID)

def feature_id_detail(request,feature_id):
    ID=str(feature_id)
    return HttpResponse("Детали улучшения "+ID)