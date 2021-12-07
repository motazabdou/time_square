from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ View that renders the shopping bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the number of rental weeks of the specified watch to the shopping bag """

    product = Product.objects.get(pk=item_id)
    num_of_weeks = int(request.POST.get('num_of_weeks'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += num_of_weeks
    else:
        bag[item_id] = num_of_weeks
        messages.success(request, f'Added {product.name} to your shopping bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjusts the number of weeks to the specified number """

    num_of_weeks = int(request.POST.get('num_of_weeks'))
    bag = request.session.get('bag', {})

    if num_of_weeks > 0:
        bag[item_id] = num_of_weeks
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Removes item from shopping bag """

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)