from django.shortcuts import render
from .models import Listing

# Create your views here.

def listings(request):#打少t
    listings = Listing.objects.all()
    context = {"listings": listings}
    print("data : ", [listings] ,"--end  --")
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    return render(request, "listings/listing.html")