from django.shortcuts import render

GUIDES = {
    "guide1": {
        "title": "1st Guide",
        "description": "This is a test for the 1st guide.",
        "pdf": "media/guides/guide1.pdf",
    },
    "guide2": {
        "title": "2nd Guide",
        "description": "This is a test for the 2nd guide.",
        "pdf": "media/guides/guide2.pdf",
    },
    "guide3": {
        "title": "3rd Guide",
        "description": "This is a test for the 3rd guide.",
        "pdf": "media/guides/guide3.pdf",
    },
    "guide4": {
        "title": "4th Guide",
        "description": "This is a test for the 4th guide.",
        "pdf": "media/guides/guide4.pdf",
    },
    "guide5": {
        "title": "5th Guide",
        "description": "This is a test for the 5th guide.",
        "pdf": "media/guides/guide5.pdf",
    },
    "guide6": {
        "title": "6th Guide",
        "description": "This is a test for the 6th guide.",
        "pdf": "media/guides/guide6.pdf",
    },
}

GUIDE_TITLES = {
    "guide1": "1st Guide",
    "guide2": "2nd Guide",
    "guide3": "3rd Guide",
    "guide4": "4th Guide",
    "guide5": "5th Guide",
    "guide6": "6th Guide",
}

def home(request):
    guides = [
        {"title": "Guide 1", "slug": "guide1"},
        {"title": "Guide 2", "slug": "guide2"},
        {"title": "Guide 3", "slug": "guide3"},
        {"title": "Guide 4", "slug": "guide4"},
        {"title": "Guide 5", "slug": "guide5"},
        {"title": "Guide 6", "slug": "guide6"},
    ]
    return render(request, "guides/home.html", {"guides": guides})

def guide(request, name):
    guide_data = GUIDES.get(name)

    return render(request, "guides/guide.html", {
        "title": guide_data["title"],
        "description": guide_data["description"],
        "pdf_url": "/" + guide_data["pdf"],
    })

