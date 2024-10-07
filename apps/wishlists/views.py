from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from apps.wishlists.models import Wishlist

def wishlist_page(request):
    context = {
        'wishlists': Wishlist.objects.filter()
    }
    return render(request=request, template_name="wishlist.html", context=context)


def view_wishlist(request):
    geting_wish = request.session.get('wishlist')
    wish = request.session['wishlist'] = geting_wish
    context = {
           'wishlists': wish
    }
    # geting_wish.append()
    # get_obj = request.session['wishlist'] = geting_wish
    # if get_obj:
        #
        # return redirect(request.META['HTTP_REFERER'])
    # context ={
    #     'wishlist': get_obj,
    # }
    return redirect(request.META['HTTP_REFERER'], context)
# def search(request):
#     search = request.POST.get('search')
#     request.session['search'] = search
#     return redirect(request.META['HTTP_REFERER'])
