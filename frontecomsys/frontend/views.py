from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import requests
from django.http import JsonResponse

from django.views.generic import TemplateView
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
import requests

from django.views.generic import TemplateView
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests

class RegistrationView(TemplateView):
    template_name = 'registration.html'

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')  

        response = requests.post('http://127.0.0.1:8003/api/register/', data={
            'username': username,
            'email': email,
            'password': password,
            'phone_number': phone_number  
        })

        if response.status_code == 201:
            messages.success(request, 'Đăng ký thành công.')
            return HttpResponseRedirect(reverse('login'))
        else:
            error_message = response.json().get('error', 'Đã xảy ra lỗi khi đăng ký.')
            messages.error(request, error_message)
            return render(request, self.template_name)



class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        response = requests.post('http://127.0.0.1:8003/api/login/', json={
            'username': username,
            'password': password
        })

        if response.status_code == 200:
            messages.success(request, 'Đăng nhập thành công.')
            user_data = response.json()
            user_id = user_data.get('id')
            request.session['user_id'] = user_id
            return HttpResponseRedirect(reverse('home'))
        else:
            error_message = response.json().get('error', 'Đã xảy ra lỗi khi đăng nhập.')
            messages.error(request, error_message)
            return render(request, self.template_name)

class UserProfileView(TemplateView):
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.session.get('user_id')
        if user_id:
            response = requests.get(f'http://127.0.0.1:8003/api/users/{user_id}/')
            if response.status_code == 200:
                context['user'] = response.json()
        print(context['user'])
        return context

    def post(self, request):
        user_id = self.request.session.get('user_id')
        address_data = request.POST.get('address')
        address_parts = address_data.split(' ')
        fullname_data = request.POST.get('fullname')
        fullname_parts = fullname_data.split(' ')
        if user_id:
            data = {
                'birthday': request.POST.get('birthday'),
                'email': request.POST.get('email'),
                'phone_number': request.POST.get('phone_number'),
                'full_name': {
                    'first_name': fullname_parts[0].strip(),
                    'last_name': fullname_parts[1].strip()
                },
                'address': {
                    'street': address_parts[0].strip(),
                    'city': address_parts[1].strip(),
                    'state': address_parts[2].strip(),
                    'country': address_parts[3].strip(),
                },
                'account': {
                    'username': request.POST.get('username'),
                    'password': request.POST.get('password')
                }
            }

            response = requests.put(f'http://127.0.0.1:8003/api/users/{user_id}/', json=data)
            if response.status_code == 200:
                messages.success(request, 'User information has been updated successfully.')
            else:
                error_message = response.json().get('error', 'An error occurred while updating user information.')
                messages.error(request, error_message)
        
        # Redirect to the user profile page after updating the information
        return HttpResponseRedirect(reverse('user_profile'))

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        response_books = requests.get('http://127.0.0.1:8001/api/books/')
        if response_books.status_code == 200:
            context['books'] = response_books.json()


        response_clothes = requests.get('http://127.0.0.1:8001/api/clothes/')
        if response_clothes.status_code == 200:
            context['clothes'] = response_clothes.json()

        response_mobiles = requests.get('http://127.0.0.1:8001/api/mobiles/')
        if response_mobiles.status_code == 200:
            context['mobiles'] = response_mobiles.json()

        return context

from django.views.generic import TemplateView
import requests

class SearchView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        keyword = self.request.GET.get('q', '')

        response = requests.get(f'http://127.0.0.1:8006/api/search/?q={keyword}&category=all')

        if response.status_code == 200:
            search_results = response.json()
            context['books'] = search_results.get('books', [])
            context['clothes'] = search_results.get('clothes', [])
            context['mobiles'] = search_results.get('mobiles', [])

        return context




from django.http import JsonResponse
class AddToCartView(TemplateView):
    template_name = 'home.html'
    def post(self, request, *args, **kwargs):
        user_id = self.request.session.get('userId')
        product_type = request.POST.get('product_type')
        product_id = request.POST.get('product_id')
        price = request.POST.get('price')
        api_url = 'http://127.0.0.1:8004/api/cart/add_to_cart/'
        data = {
            'user_id': user_id,
            'product_type': product_type,
            'product_id': product_id,
            'price': price,
        }

        response = requests.post(api_url, data=data)

        if response.status_code == 201:
            return JsonResponse({}, status=201)
        else:
            return JsonResponse({'status': 'error'}, status=500)

class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.session.get('userId')  
        
        api_url = f'http://127.0.0.1:8004/api/cart/{user_id}/'
        response = requests.get(api_url)

        if response.status_code == 200:
            cart_items = response.json()

            total_price = 0
            if cart_items:
                for item in cart_items:
                    product_type = item.get('product_type')
                    product_id = item.get('product_id')

                    product_api_url = f'http://127.0.0.1:8001/api/{product_type}/{product_id}/'
                    product_response = requests.get(product_api_url)

                    if product_response.status_code == 200:
                        product_data = product_response.json()
                        item.update(product_data)

                        price = float(item.get('price'))
                        quantity = int(item.get('quantity'))
                        item_total = price * quantity
                        total_price += item_total  

            context['cart_items'] = cart_items
            context['total_price'] = total_price 
        else:
            context['error'] = 'Failed to fetch cart items'

        return context

    def post(self, request, *args, **kwargs):
        form = request.POST
        user_id = self.request.session.get('userId')  
        product_type = form.get('product_type')
        product_id = form.get('product_id')
        action = form.get('action')
        
        response = None
        if action == 'add':
            data={
                'user_id': user_id,
                'product_type': product_type,
                'product_id': product_id,
                'price': 0,  
            }

            response = requests.post('http://127.0.0.1:8004/api/cart/add/', data={
                'user_id': user_id,
                'product_type': product_type,
                'product_id': product_id,
                'price': 0, 
            })
        elif action == 'remove':
            response = requests.post('http://127.0.0.1:8004/api/cart/remove/', data={
                'user_id': user_id,
                'product_type': product_type,
                'product_id': product_id,
            })
        elif action == 'removeAll':
            response = requests.post('http://127.0.0.1:8004/api/cart/remove_from_cart/', data={
                'user_id': user_id,
                'product_type': product_type,
                'product_id': product_id,
            })

        if response and response.status_code == 201:
            return HttpResponseRedirect(reverse('cart'))

        return super().get(request, *args, **kwargs)

class CreateOrderView(TemplateView):
    template_name = 'create_order.html'

    def post(self, request):
        user_id = self.request.session.get('userId')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        if not user_id:
            return render(request, self.template_name, {"error": "Bạn cần đăng nhập để tạo đơn hàng."})

        response = requests.post('http://127.0.0.1:8002/api/orders/create/', json={
            'userId': user_id,
            'shipment': address,
            'payment': payment_method
        })

        if response.status_code == 201:
            messages.success(request, 'Đã tạo đơn hàng thành công.')
            return HttpResponseRedirect(reverse('home'))
        else:
            error_message = response.json().get('error', 'Đã xảy ra lỗi khi tạo đơn hàng.')
            messages.error(request, error_message)
            return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OrderListView(TemplateView):
    template_name = 'order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.session.get('userId')  
        order_api_url = f'http://127.0.0.1:8002/api/order/{user_id}/'
        response = requests.get(order_api_url)
        if response.status_code == 200:
            orders = response.json()
            context['orders'] = []

            for order in orders:
                order_items = order.get('items', [])
                order_datetime = order.get('order_datetime')
                if order_datetime:
                    time = order_datetime[:10]
                    order['order_datetime'] = time
                for item in order_items:
                    product_type = item.get('product_type')
                    product_id = item.get('product_id')

                    product_api_url = f'http://127.0.0.1:8001/api/{product_type}/{product_id}/'
                    product_response = requests.get(product_api_url)

                    if product_response.status_code == 200:
                        product_data = product_response.json()
                        item.update(product_data)
                        context['orders'].append(order)
        print(context)
        return context

    



from django import forms

class CartItemForm(forms.Form):
    user_id = forms.IntegerField()
    product_type = forms.CharField(max_length=100)
    product_id = forms.IntegerField()
    action = forms.CharField(max_length=10)

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
import requests

class CreateReviewView(TemplateView):
    template_name = 'create_review.html'

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product_type = request.POST.get('product_type')
        star = request.POST.get('star')
        comment = request.POST.get('comment')

        api_url = 'http://127.0.0.1:8008/api/create-review/'
        data = {
            'product_id': product_id,
            'product_type': product_type,
            'star': star,
            'comment': comment
        }
        print(data)
        response = requests.post(api_url, data=data)
        if response.status_code == 201:
            # Đánh giá đã được tạo thành công
            return HttpResponseRedirect('/')
        else:
            # Xử lý lỗi nếu cần
            return HttpResponse("Đã xảy ra lỗi khi tạo đánh giá")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_id'] = self.request.GET.get('product_id')
        context['product_type'] = self.request.GET.get('product_type')
        return context
import requests
from django.views.generic import TemplateView
from django.conf import settings

class ProductReviewView(TemplateView):
    template_name = 'product_reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['product_id']
        product_type = self.kwargs['product_type']
        
        api_url = f'http://127.0.0.1:8008/api/get-review/{product_id}/{product_type}/'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            reviews = response.json()
        else:
            reviews = []

        context['reviews'] = reviews
        context['product_id'] = product_id
        context['product_type'] = product_type
        print(context)
        return context
