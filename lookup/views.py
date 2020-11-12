from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":

        values = []

        title = request.POST['Filmtitel']
        
        api_request = requests.get("http://www.omdbapi.com/?t=" + title + "&apikey=eb280a88")

        api = json.loads(api_request.content)

        if api.get("Response") == "False":
            api = "Error2"

        return render(request, 'home.html', {
        'api': api
        })

    else:

        values = []

        api_request = requests.get("http://www.omdbapi.com/?t=Matrix&apikey=eb280a88")

        try:
            api = json.loads(api_request.content)

        except:
            api = "Error1"

        return render(request, 'home.html', {
        'api': api
        })

def about(request):
    return render(request, 'about.html', {})
