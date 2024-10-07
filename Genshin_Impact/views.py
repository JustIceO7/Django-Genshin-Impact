from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def home(request):
    return render(request, "home.html")

def set_theme_mode(request):
    if request.method == 'POST':
        theme_mode = request.POST.get('theme_mode')
        request.session['theme_mode'] = theme_mode 
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)