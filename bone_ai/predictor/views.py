from django.shortcuts import render
from .predict import predict_image
from django.core.files.storage import FileSystemStorage

def index(request):
    result = None
    prob = None
    image_url = None

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        filepath = fs.path(filename)

        result, prob = predict_image(filepath)

    return render(request, 'index.html', {
        'result': result,
        'prob': prob,
        'image_url': image_url
    })