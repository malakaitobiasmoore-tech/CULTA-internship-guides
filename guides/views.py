from django.shortcuts import render

from django.conf import settings



GUIDES = {
    "guide1": {
        "title": "Copilot",
        "description": "Guide for Microsoft Copilot.",
        "pdf": "Student Guide - Copilot_Redesigned.pdf",
    },
    "guide2": {
        "title": "Gemini Notebook",
        "description": "Guide for Gemini Notebook.",
        "pdf": "Student Guide - Gemini Notebook_Redesigned.pdf",
    },
    "guide3": {
        "title": "Google Gemini",
        "description": "Guide for Google Gemini.",
        "pdf": "Student Guide - Google Gemini_Redesigned.pdf",
    },
    "guide4": {
        "title": "LanguageTool",
        "description": "Guide for LanguageTool.",
        "pdf": "Student Guide - LanguageTool_Redesigned.pdf",
    },
    "guide5": {
        "title": "Perplexity",
        "description": "Guide for Perplexity.",
        "pdf": "Student Guide - Perplexity_Redesigned.pdf",
    },
    "guide6": {
        "title": "Quillbot",
        "description": "Guide for Quillbot.",
        "pdf": "Student Guide - Quillbot_Redesigned.pdf",
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
        "pdf_url": "/media/" + guide_data["pdf"],
    })

