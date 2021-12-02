from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ View that renders the shopping bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the number of rental weeks of the specified watch to the shopping bag """

    num_of_weeks = int(request.POST.get('num_of_weeks'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += num_of_weeks
    else:
        bag[item_id] = num_of_weeks

    request.session['bag'] = bag
    return redirect(redirect_url)