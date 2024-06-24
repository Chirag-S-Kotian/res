from django.shortcuts import render
from .models import Restaurant
from fuzzywuzzy import process

# Create your views here.
def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        all_restaurants = Restaurant.objects.all()
        names = [restaurant.items for restaurant in all_restaurants]
        best_match = process.extractOne(query, names)
        if best_match:
            best_match_restaurant = Restaurant.objects.filter(items__icontains=best_match[0])
            results = best_match_restaurant

    return render(request, 'search/search.html', {'results': results, 'query': query})
