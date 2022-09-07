from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def reverse(request):
    source_text = request.GET['usertext']
    reverse_text = str(source_text)[::-1]
    return render(request, 'reverse.html', {'reverse_text':reverse_text})