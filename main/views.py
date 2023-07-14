from django.shortcuts import render
def index (request):
    data = {
        'title': 'Музей УГТУ' }
    return render(request, 'main/index.html', data)
def authentication (resuest):
    return render(resuest, 'main/authentication.html')
def gallery(request):
    return render(request, 'main/gallery.html')
def itm(request):
    return render(request, 'main/itm.html')
def excursion(request):
    return render(request, 'main/excursion.html')
def about(request):
    return render(request, 'main/about.html')