from django.shortcuts import render
from .forms import ImageUploadForm

from .models import image_classification, nearest_neighbors
# Create your views here.
img_path = "static/img.jpg"
def handle_uploaded_file(f):
    with open(img_path,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home_view(request):

    return render(request, "home.html",{} )

def image_process(request):
    form = ImageUploadForm(request.POST,request.FILES)
    if form.is_valid():


        handle_uploaded_file(request.FILES['image'])
        res = image_classification(img_path)
        img_names = nearest_neighbors(img_path,10)
        print(res[0])
    return render(request, "result.html",{'label':res[0][1],'prob':res[0][0],'res':res[1:],'img_names1':img_names[0:5],'img_names2':img_names[5:]})
