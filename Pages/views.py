from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render
from Carts.models import Cart, CartItem
from Orders.models import Order, OrderItem
from Pages.models import *
from Products.models import Category, Product, Review
from django.http import JsonResponse
from Products.forms import ProductFilterForm
from django.contrib import messages
from django.utils import timezone
from django.db.models import Max, Min
from django.urls import reverse


from Users.forms import AddressForm, CustomUserForm, SignUpForm, LogInForm
from Users.models import Address, CustomUser
from django.contrib.auth import authenticate, login, logout

from django.db.models import Avg



# Create your views here.

def homeView(request, *args, **kwargs):
    categories = Category.objects.all()
    heros = Hero.objects.all()
    top_deals = TopDeals.objects.all()[0]
    cta1 = CTA1.objects.all()[0]
    pre_owned_deals = PreOwnedDeals.objects.all()[0]
    cta2 = CTA2.objects.all()[0]
    top_hardware = TopHardware.objects.all()[0].products.all()
    brands = Brands.objects.all()
    cta3 = CTA3.objects.all()[0]
    playstation_deals = PlaystationDeals.objects.all()[0]
    xbox_deals = XboxDeals.objects.all()[0]
    top_games = TopGames.objects.all()[0].products.all()
    featured_games = FeaturedGames.objects.all()[0]
    featured_games_cta = FeaturedGamesCTA.objects.all()
    featured_genres = FeaturedGenres.objects.all()[0]
    top_accessories = TopAccessories.objects.all()[0].products.all()
    cta4 = CTA4.objects.all()[0]

    return render(request, 'home.html', {
        "categories": categories,
        "heros": heros,
        "top_deals": top_deals,
        "CTA1": cta1,
        "pre_owned_deals": pre_owned_deals,
        "CTA2": cta2,
        "top_hardware": top_hardware,
        "brands": brands,
        "CTA3": cta3,
        "playstation_deals": playstation_deals,
        "xbox_deals": xbox_deals,
        "top_games": top_games,
        "featured_games": featured_games,
        "featured_games_cta": featured_games_cta,
        "featured_genres": featured_genres,
        "top_accessories": top_accessories,
        "CTA4": cta4,
    })

def productView(request, *args, **kwargs):
    product_id = kwargs.get('ID')  # Retrieve the ID from kwargs
    product = get_object_or_404(Product, id=product_id)  # Use get_object_or_404 to retrieve the product
    reviews = Review.objects.filter(product=product)
    
    # Calculate average rating
    average_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
    # Now you have access to the product object
    categories = Category.objects.all()
    return render(request, 'product.html', {"product": product, "categories": categories, "reviews": average_rating})

def catalogView(request, *args, **kwargs):
    form = ProductFilterForm()
    products = Product.objects.all()
    all_categories = Category.objects.all()

    # Retrieve maximum and minimum prices
    max_price = products.aggregate(Max('price'))['price__max']
    min_price = products.aggregate(Min('price'))['price__min']

    if request.method == "GET":
        form = ProductFilterForm(request.GET)
        sort_by = request.GET.get('sort_by') or "price_low_to_high"

        # Handle sorting by price low to high
        if sort_by == 'price_low_to_high':
            products = products.order_by('price')
        elif sort_by == 'price_high_to_low':
            products = products.order_by('-price')

        if form.is_valid():
            manufacturers = form.cleaned_data.get('manufacturer')
            categories = form.cleaned_data.get('category')
            genres = form.cleaned_data.get('genre')
            colors = form.cleaned_data.get('colors')
            sizes = form.cleaned_data.get('sizes')
            min_price_filter = form.cleaned_data.get('min_price')
            max_price_filter = form.cleaned_data.get('max_price')
            subcategories = form.cleaned_data.get('subcategory')  # Get selected subcategories

            if manufacturers:
                products = products.filter(manufacturer__in=manufacturers)

            if categories:
                products = products.filter(category__in=categories)

            if genres:
                products = products.filter(genre__in=genres)

            if colors:
                products = products.filter(colors__in=colors)

            if sizes:
                products = products.filter(sizes__in=sizes)

            if min_price_filter:
                products = products.filter(price__gte=min_price_filter)

            if max_price_filter:
                products = products.filter(price__lte=max_price_filter)

            if subcategories:  # Filter by selected subcategories
                products = products.filter(subcategories__in=subcategories)

    context = {
        "products": products,
        'form': form,
        "categories": all_categories,
        "min_price": min_price,
        "max_price": max_price,
    }
    return render(request, 'catalog.html', context)




def filterProducts(request):
    if request.method == "POST":
        form = ProductFilterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('valid form')
            # Fetching data from the form
            manufacturer = form.cleaned_data.get('manufacturer')
            category = form.cleaned_data.get('category')
            genre = form.cleaned_data.get('genre')
            colors = form.cleaned_data.get('colors')
            sizes = form.cleaned_data.get('sizes')
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            sort_by = request.POST.get('sort_by')


            # Printing the fetched data
            print("Manufacturer:", manufacturer)
            print("Category:", category)
            print("Genre:", genre)
            print("Colors:", colors)
            print("Sizes:", sizes)
            print("Min Price:", min_price)
            print("Max Price:", max_price)
            print("sort_by:", sort_by)

            # Fetching products based on the filters
            products = Product.objects.all()

            if manufacturer:
                products = products.filter(manufacturer__in=manufacturer)

            if category:
                products = products.filter(category__in=category)

            if genre:
                products = products.filter(genre__in=genre)

            if colors:
                products = products.filter(colors__in=colors)

            if sizes:
                products = products.filter(sizes__in=sizes)

            if min_price:
                products = products.filter(price__gte=min_price)

            if max_price:
                products = products.filter(price__lte=max_price)

            if sort_by:
                if sort_by == 'price-low-to-high':
                    products = products.order_by('price')
                elif sort_by == 'price-high-to-low':
                    products = products.order_by('-price')

            # Serializing products to JSON
            products_data = [{
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'manufacturer': product.manufacturer.name if product.manufacturer else None,
                'category': product.category.name if product.category else None,
                'colors': [color.name for color in product.colors.all()],
                'sizes': [size.name for size in product.sizes.all()],
                'price': str(product.price),  
                'availability': product.availability,
                'quantity': product.quantity,
                'discount_percentage': product.discount_percentage,
                'image_url': product.image.url if product.image else None,
            } for product in products]

            return JsonResponse({'products': products_data}, safe=False)
    
    # Return an empty list if no valid data or request is not AJAX
    return JsonResponse({'products': []}, safe=False)



def profileView(request, val=None):
    categories = Category.objects.all()
    user = CustomUser.objects.get(user=request.user)
    form = CustomUserForm(instance=user)
    orders = user.order_set.all().order_by('-created_at')
    receipts = user.receipt_set.all()
    return render(request, 'profile.html', {'profileForm': form, 'orders': orders, "receipts": receipts, "categories": categories, "val": val})

def update_profile(request):
    user_profile = CustomUser.objects.get(user=request.user)

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            # Return form errors if the form is not valid
            return JsonResponse({'errors': form.errors, 'success': False})

    else:
        # If the request is not POST, return a 405 Method Not Allowed status
        return JsonResponse({'error': 'Method Not Allowed', 'success': False})





def delete_cart_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        try:
            # Retrieve the cart item
            cart_item = CartItem.objects.get(pk=item_id)
            # Delete the cart item
            cart_item.delete()

            user_cart = None
            try:
                user_cart = Cart.objects.filter(user=CustomUser.objects.get(user=request.user))[0]
            except:
                print ("Cart does not exist")
            if user_cart:
                # Access the items related to the cart using the related name 'cart_items'
                items = user_cart.cart_items.all()
                total_price = user_cart.calculate_total_price()
                ultimate_total = int(total_price) + 7
                total_items = user_cart.cart_items.count()
                print(total_price)
                print("items exists")
            else:
                print("items doesn't exist")
                items = []

            return JsonResponse({'success': True, 'message': 'Item deleted successfully', "total_price": total_price, "ultimate_total":ultimate_total, "total_items": total_items})
        except CartItem.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found'})
    else:
        return JsonResponse({'error': 'bad request'})
    





def registerView(request):
    signUpForm = SignUpForm()
    return render(request, 'register.html', {"signUpForm":signUpForm})

def loginView(request):
    logInForm = LogInForm()
    return render(request, 'login.html', {"logInForm":logInForm})

def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username, password=password1)
            print("Register Test")
            if user is not None:
                login(request, user)
                messages.success(request, "Registered and logged in successfully.")
                # Update CustomUser with telephone number
                custom_user = CustomUser.objects.get(user=user)
                custom_user.tel = form.cleaned_data['tel']
                custom_user.first_name = form.cleaned_data['first_name']
                custom_user.last_name = form.cleaned_data['last_name']
                custom_user.save()
                if not custom_user.address:
                    return JsonResponse({'success': True, 'redirect': True})
                
            return JsonResponse({'success': True, 'redirect': False})  # Return success response
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors, 'redirect': False})  # Return error response
    else:
        return redirect('register')
    


def logIn(request, *args, **kwargs):
    print("rrrrrrrrrrr")
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                messages.success(request, 'Logged In successfully')
                login(request, user)
                custom_user = CustomUser.objects.get(user=user)
                if not custom_user.address:
                    return JsonResponse({'success': True, 'redirect': True})
                return JsonResponse({'success': True, 'error': "User logged in", 'redirect': False})
            else:
                return JsonResponse({'success': False, 'error': "User not found", 'redirect': False})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'error': errors, 'redirect': False})
        

        


def add_to_cart(request, product_id):
    # Get the product object
    product = get_object_or_404(Product, id=product_id)

    # Get the user's cart or create one if it doesn't exist
    user_cart, created = Cart.objects.get_or_create(user=CustomUser.objects.get(user=request.user))

    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=user_cart, product=product)

    if not item_created:
        # If the item already exists in the cart, increment its quantity
        cart_item.quantity += 1
        cart_item.save()

    # Set the created_at timestamp for the cart if it's newly created
    if created:
        user_cart.created_at = timezone.now()
        user_cart.save()

    # Redirect the user to the cart page
    return redirect('cart')  # You need to define the 'cart' URL in your urls.py




def checkoutView(request):
    """ user = CustomUser.objects.get(user=request.user)
    
    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=user)
    
    # Check if the cart is empty
    if cart.cart_items.exists():
        # Create an order for the user
        order = Order.objects.create(user=user)
        
        # Create order items for each item in the cart
        for cart_item in cart.cart_items.all():
            # You need to modify this line according to your actual model structure
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
            )
        
        # Clear the cart after creating the order
        cart.cart_items.all().delete()
        
        # Redirect the user to the 'cart' page after checkout
        return redirect('profile', val="orders")
    else:
        # If the cart is empty, redirect the user to some page indicating that the cart is empty """
    return render(request, 'checkout.html', {})
    



def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            # Retrieve the CustomUser instance associated with the current user
            custom_user = CustomUser.objects.get(user=request.user)
            custom_user.address = address
            custom_user.save()
            return redirect('home')  # Redirect to the home page after successfully adding the address
    else:
        form = AddressForm()
    return render(request, 'add_address.html', {'form': form})






def update_cart_item_quantity(request):
    if request.method == "POST":
        itemId = request.POST.get('itemId')
        quantity = request.POST.get('quantity')
        item = get_object_or_404(CartItem, id=itemId)
        item.quantity = quantity
        item.save()

        cart = Cart.objects.get(user = CustomUser.objects.get(user=request.user))  # You need to implement this function
        if cart:
            total_price = cart.calculate_total_price()
            ultimate_total = int(total_price) + 7
            print(total_price)

        return JsonResponse({'success': True, "total_price": total_price, "ultimate_total":ultimate_total})
    return JsonResponse({'success': False, 'error': "bad request"})











def cartView(request):
        # Retrieve the user's cart
    user_cart = None
    categories = Category.objects.all()
    try:
        user_cart = Cart.objects.filter(user=CustomUser.objects.get(user=request.user))[0]
    except:
        print ("Cart does not exist")
    if user_cart:
        # Access the items related to the cart using the related name 'cart_items'
        items = user_cart.cart_items.all()
        total_price = user_cart.calculate_total_price()
        ultimate_total = int(total_price) + 7
        total_items = user_cart.cart_items.count()
        print(total_price)
        print("items exists")
        context = {'cart': user_cart, 'items': items, "categories": categories, "total_price": total_price, "ultimate_total":ultimate_total, "total_items": total_items}
    else:
        print("items doesn't exist")
        items = []
        context = {'cart': user_cart, 'items': items, "categories": categories, "total_price": 0, "ultimate_total":0, "total_items": 0}
    print(context)
    return render(request, 'newCart.html', context)

def forgetPasswordView(request):
    return render(request, 'forgetPassword.html', {})

def checkEmailView(request):
    return render(request, 'checkEmail.html', {})


def cancelOrderView(request, order_id):
    if request.method == 'POST':
        print("test")
        order = get_object_or_404(Order, id=order_id)
        order.status = 'cancelled'
        order.save()
        return JsonResponse({'success': True, 'message': 'Order cancelled successfully'})
    else:
        return JsonResponse({'success': False, 'error': "bad request"})
    

def logoutView(request):
    logout(request)
    return redirect(reverse('home'))