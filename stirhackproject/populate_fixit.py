import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
              'stirhackproject.settings')

import django
import random
django.setup()
from fixit.models import Issue


def populate():

    issues = [
        {"title": "Uni avenue pothole",
         "location_bdg": "N/A",
         "location_detail": "Outside main gate",
         "upvotes": "3",
         "images": "issue_images/Pothole.jpg",
            },

        {"title": "Slow PC",
         "location_bdg": "Boyd Orr",
         "location_detail": "Lvl 10, machine 5",
         "upvotes": "24",
         "images": "issue_images/Pothole.jpg",
            },

        {"title": "Broken door handle",
         "location_bdg": "Library",
         "location_detail": "Level 8 annex",
         "upvotes": "1",
         "images": "issue_images/Pothole.jpg",
            },

        {"title": "Heating not working",
         "location_bdg": "Adam Smith 1115",
         "location_detail": "top row",
         "upvotes": "9",
         "images": "issue_images/Pothole.jpg",
            },]

    for issue in issues:
        add_issue(issue["title"], issue["location_bdg"], issue["location_detail"], issue["upvotes"], issue["images"] )

def add_issue(title, location_bdg, location_detail, upvotes, images):
    i = Issue.objects.get_or_create(title=title, location_bdg=location_bdg, location_detail=location_detail, upvotes=upvotes, images=images)[0]
    i.save()
    return i

if __name__ == '__main__':
    print("Starting FixIt population script...")
    populate()
