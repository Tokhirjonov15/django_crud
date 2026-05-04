from django.http import HttpResponseServerError
from django.shortcuts import render

# Tour Controller


def get_tours(request):
    try:
        tours = [
            {
                'title': 'Mountain Weekend',
                'date': 'May 18',
                'place': 'Chimgan Mountains',
                'description': 'Fresh air, short hiking routes, and sunset views.',
            },
            {
                'title': 'Historic City Walk',
                'date': 'June 2',
                'place': 'Old Town',
                'description': 'A calm walking tour through local history and architecture.',
            },
            {
                'title': 'Lake Picnic Trip',
                'date': 'June 15',
                'place': 'Charvak Reservoir',
                'description': 'A relaxed travel day with food, photos, and open water views.',
            },
        ]
        return render(
            request,
            "tour.html",
            {'tours': tours, 'active_page': 'tour'},
            status=200,
        )
    
    except Exception as err:
        print("Error in get_tours:", err)
        return HttpResponseServerError("Something went wrong")
