from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        context = {
            "name": request.POST['name'],
            "location": request.POST['location'],
            "favLang": request.POST['favLang'],
            "travel": request.POST['travel'],
            "music": request.POST['music'],
            "comment": request.POST['comment'],
        }
    return render(request, 'result.html', context)


# def some_function(request):
#     if request.method == "POST":
#         val_from_field_one = request.POST["one"]
#     	  val_from_field_two = request.POST["two"]

# def processForm(request):
#     print(f"printing the request method which is: {request.method}")
#     #the information from the form is represented by request.POST
#     print(request.POST)     #request.POST is a dictionary that has mkey values
#     print(request.POST['favshow'])
#     context = {
#         'formInfo':request.POST
#     }
#     return render(request, 'result.html', context)

def catch_all(request, url):        #The catch all view, "url" must be passed in
    return HttpResponse("There is no page here. You have made an error.")