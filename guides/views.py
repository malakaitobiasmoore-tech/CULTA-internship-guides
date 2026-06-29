from django.shortcuts import render

def home(request):

    guides = [
        {"title": "Guide 1", "description": "Description of Guide 1"},
        {"title": "Guide 2", "description": "Description of Guide 2"},
        {"title": "Guide 3", "description": "Description of Guide 3"},
        {"title": "Guide 4", "description": "Description of Guide 4"},
        {"title": "Guide 5", "description": "Description of Guide 5"},
        {"title": "Guide 6", "description": "Description of Guide 6"},
    ]

    return render(request, "guides/home.html", {
        "guides": guides
    })