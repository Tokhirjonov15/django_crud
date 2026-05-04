from django.http import HttpResponseServerError
from django.shortcuts import render

# Sport Controller


def get_sports(request):
    try:
        events = [
            {
                'title': 'Morning Football Match',
                'date': 'Saturday, 09:00',
                'place': 'Central Stadium',
                'description': 'Friendly football match for students and local teams.',
            },
            {
                'title': 'Basketball Skills Night',
                'date': 'Tuesday, 18:30',
                'place': 'Indoor Arena',
                'description': 'Dribbling, shooting, and small team challenges.',
            },
            {
                'title': '5K Community Run',
                'date': 'Sunday, 07:30',
                'place': 'City Park',
                'description': 'Light running event for beginners and regular runners.',
            },
        ]
        return render(
            request,
            "sport.html",
            {'events': events, 'active_page': 'sport'},
            status=200,
        )
    
    except Exception as err:
        print("Error in get_sports:", err)
        return HttpResponseServerError("Something went wrong")
