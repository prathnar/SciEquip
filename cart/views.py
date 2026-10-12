from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.core.mail import send_mail
from django.conf import settings
from .emails import send_order_emails
from orders.models import Order,OrderItem
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product.quantity = quantity
        product.subtotal = product.price * quantity
        total += product.subtotal
        products.append(product)

    context = {
        'products': products,
        'total': total
    }

    return render(request, 'cart/cart.html', context)

@login_required(login_url="login")
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart

    return redirect('view_cart')


@login_required(login_url="login")
def remove_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('view_cart')


@login_required(login_url="login")
def decrease_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('view_cart')

# CHCKOUT ITEM 
@login_required(login_url="login")
def checkout(request):
    total = 0
    products = []
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('product_list')
    
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product.quantity = quantity
        product.subtotal = product.price * quantity
        total += product.subtotal
        products.append(product)

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        payment_method = request.POST.get("payment_method", "cash on delivery")

        total = 0

        # calculate total price
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            total += product.price * quantity

        # create order
        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            payment_method=payment_method,
            total_amount=total
        )

        # create order items
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

      

        
        send_order_emails(order)
        # clear cart
        request.session['cart'] = {}

        return redirect("checkout_success")

    return render(request, "cart/checkout.html" , {"products" :products , "total" :total})

@login_required
def checkout_success(request):
    return render(request, 'cart/checkout_success.html')
