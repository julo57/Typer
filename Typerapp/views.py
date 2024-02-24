from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
    text_content = read_file(request)
    return render(request, 'Typerapp/main.html', {'title': 'Main', 'text_content': text_content})


    
def base(request):
    return render(request, 'Typerapp/base.html', {'title': 'Base'})


def read_file(request):
   
    file_path = 'Typerapp/static/tekst/przyklad.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    return text_content


def read_file2(request):
    file_path = 'Typerapp/static/tekst/przyklad.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    return text_content



def test(request):
    text_content = read_file2(request)
    return render(request, 'Typerapp/test.html',  {'text_content': text_content , 'title': 'Test'})
