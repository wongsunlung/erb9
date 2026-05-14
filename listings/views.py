from django.shortcuts import render

# Create your views here.
def listings(request):#打少t
    return render(request, "listings/listings.html")

def listing(request, listing_id):
    return render(request, "listings/listing.html")