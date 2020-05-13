from django.shortcuts import render

# ! Die Home Page !

def home(request):
    import json # ! Für die API Abfrage, .json Dateiformat !
    import requests # ! Für API Abfrage !

    if request.method == "POST": # ! Wenn eine Abfrage per Suche kommt, dann
        zipcode = request.POST['zipcode']
        
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode +"&distance=30&API_KEY=4C576B97-355B-4913-8308-72EA96FF9206")

        try:
            api = json.loads(api_request.content)

            if api[0]['Category']['Name'] == "Good":
                category_description = "0 - 50: Kein Risiko"
                category_color = "good"
                category_name = "gut"
            elif api[0]['Category']['Name'] == "Moderate":
                category_description = "51 - 100: Leicht erhöhte Werte"
                category_color = "moderate"
                category_name = "moderat"
            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                category_description = "101 - 150: Risiko für empfindliche Menschen sehr hoch"
                category_color = "usg"
                category_name = "ungesund für empfindliche Menschen"
            elif api[0]['Category']['Name'] == "Unhealthy":
                category_description = "151 - 200: Ungesund"
                category_color = "unhealthy"
                category_name = "ungesund"
            elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_description = "201 - 300: Sehr ungesund"
                category_color = "veryunhealthy"
                category_name = "sehr ungesund"
            elif api[0]['Category']['Name'] == "Hazardous":
                category_description = "301 - 500: Quasi Tödlich"
                category_color = "hazardous"
                category_name = "verheerend"  # ! Darstellung der Wetter Ergebnisse !
        except:
            api = "Error2" # ! Error Handling Modul !
            category_description = "-"
            category_color = "-"
            category_name = "-"


        return render(request, 'home.html', {
        'api': api, 
        'category_description': category_description, 
        'category_color': category_color,
        'category_name': category_name}) # ! Ausgabe der Homepage --> templates !

    else:     # ! Normale Homepage, ohne speziellen Zip-Code, Standardabfrage !

        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=96701&distance=30&API_KEY=4C576B97-355B-4913-8308-72EA96FF9206")

        try:
            api = json.loads(api_request.content)

            if api[0]['Category']['Name'] == "Good":
                category_description = "0 - 50: Kein Risiko"
                category_color = "good"
                category_name = "gut"
            elif api[0]['Category']['Name'] == "Moderate":
                category_description = "51 - 100: Leicht erhöhte Werte"
                category_color = "moderate"
                category_name = "moderat"
            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                category_description = "101 - 150: Risiko für empfindliche Menschen sehr hoch"
                category_color = "usg"
                category_name = "ungesund für empfindliche Menschen"
            elif api[0]['Category']['Name'] == "Unhealthy":
                category_description = "151 - 200: Ungesund"
                category_color = "unhealthy"
                category_name = "ungesund"
            elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_description = "201 - 300: Sehr ungesund"
                category_color = "veryunhealthy"
                category_name = "sehr ungesund"
            elif api[0]['Category']['Name'] == "Hazardous":
                category_description = "301 - 500: Quasi Tödlich"
                category_color = "hazardous"
                category_name = "verheerend"  # ! Darstellung der Wetter Ergebnisse !
        except:
            api = "Error1" # ! Error Handling Modul !
            category_description = "-"
            category_color = "-"
            category_name = "-"

        

        return render(request, 'home.html', {
        'api': api, 
        'category_description': category_description, 
        'category_color': category_color,
        'category_name': category_name})  # ! Ausgabe der Homepage !

# ! Die About Seite !

def about(request):
    return render(request, 'about.html', {})    # ! Ausgabe des Impressum --> templates !
