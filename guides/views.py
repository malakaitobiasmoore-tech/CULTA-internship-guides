from django.shortcuts import render

from django.conf import settings



GUIDES = {
    "guide1": {
        "title": "Microsoft Copilot",
        "description": """Microsoft Copilot is an AI-powered assistant that can help students generate ideas, explain difficult concepts, create study materials, and improve productivity. This guide explores practical ways neurodivergent students can use Copilot to support academic work while maintaining good academic practice.""",
        "pdf": "Student Guide - Copilot_Redesigned.pdf",
    },
    "guide2": {
        "title": "Gemini Notebook",
        "description": """Gemini Notebook is a research and note-taking tool that allows students to upload their own materials and ask questions based on those sources. This guide explains how it can support organisation, revision, and understanding of course content..""",
        "pdf": "Student Guide - Gemini Notebook_Redesigned.pdf",
    },
    "guide3": {
        "title": "Google Gemini",
        "description": """Google Gemini is a conversational AI tool that can assist with brainstorming, researching topics, explaining concepts, and creating study resources. This guide highlights ways students can incorporate Gemini into their learning workflow.""",
        "pdf": "Student Guide - Google Gemini_Redesigned.pdf",
    },
    "guide4": {
        "title": "LanguageTool",
        "description": """LanguageTool is a writing assistant that helps identify grammar, spelling, punctuation, and style issues. This guide explores how it can support academic writing and improve confidence in written work.""",
        "pdf": "Student Guide - LanguageTool_Redesigned.pdf",
    },
    "guide5": {
        "title": "Perplexity",
        "description": """Perplexity combines AI-powered responses with web search functionality, providing answers alongside referenced sources. This guide demonstrates how students can use it for research, fact-finding, and exploring new topics.""",
        "pdf": "Student Guide - Perplexity_Redesigned.pdf",
    },
    "guide6": {
        "title": "Quillbot",
        "description": """QuillBot offers tools for paraphrasing, summarising, and improving written text. This guide shows how students can use these features to support understanding, revision, and drafting academic work.""",
        "pdf": "Student Guide - Perplexity_Redesigned.pdf",
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
        {"title": "Microsoft Copilot", "slug": "guide1", 
         "description": "AI assistant for studying, planning and organisation."},
        {"title": "Gemini Notebook", "slug": "guide2",
        "description": "Research and revision using your own notes and sources."},
        {"title": "Google Gemini", "slug": "guide3",
        "description": "Generate ideas and explore complex topics."},
        {"title": "LanguageTool", "slug": "guide4",
        "description": "Improve grammar, spelling and writing clarity."},
        {"title": "Perplexity", "slug": "guide5",
        "description": "Focused research with accurate outputs and citaion." },
        {"title": "Quillbot", "slug": "guide6",
        "description": "Paraphrasing, summarising and improving written text."},
    ]
    return render(request, "guides/home.html", {"guides": guides})

def guide(request, name):
    guide_data = GUIDES.get(name)

    return render(request, "guides/guide.html", {
        "title": guide_data["title"],
        "description": guide_data["description"],
        "pdf_url": "/media/" + guide_data["pdf"],
    })

