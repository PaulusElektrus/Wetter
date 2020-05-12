from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=30&API_KEY=4C576B97-355B-4913-8308-72EA96FF9206")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "0 - 50: Kein Risiko"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "51 - 100: Leicht erhöhte Werte"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "101 - 150: Risiko für empfindliche Menschen"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "151 - 200: Ungesund"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "201 - 300: Sehr ungesund"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "301 - 500: Quasi Tödlich"
            category_color = "hazardous"  

        return render(request, 'home.html', {
        'api': api, 
        'category_description': category_description, 
        'category_color': category_color})

    else:     

        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=96701&distance=30&API_KEY=4C576B97-355B-4913-8308-72EA96FF9206")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "0 - 50: Kein Risiko"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "51 - 100: Leicht erhöhte Werte"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "101 - 150: Risiko für empfindliche Menschen"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "151 - 200: Ungesund"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "201 - 300: Sehr ungesund"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "301 - 500: Quasi Tödlich"
            category_color = "hazardous"  

        return render(request, 'home.html', {
        'api': api, 
        'category_description': category_description, 
        'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})
