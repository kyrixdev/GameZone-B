
from django.contrib import admin
from django.urls import path, reverse_lazy
from Pages.views import homeView, loginView, logoutView, productView, catalogView, filterProducts, profileView, registerView, update_profile, cartView, delete_cart_item,register, logIn, add_to_cart, checkoutView, add_address, update_cart_item_quantity, forgetPasswordView, checkEmailView, cancelOrderView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name="home"),
    path('product/<int:ID>', productView, name="product"),
    path('catalog/', catalogView, name="catalog"),
    path('filter/', filterProducts, name='filter_products'),
    path('profile/<str:val>/', profileView, name='profile'),
    path('profile/', profileView, name='profile'),
    path('update-profile/', update_profile, name='update_profile'),
    path('cart/', cartView, name='cart'),
    path('delete-cart-item/', delete_cart_item, name='delete_cart_item'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('register/', registerView, name='register'),
    path('registerf/', register, name='registerf'),
    path('loginf/', logIn, name='loginf'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkoutView, name='checkout'),
    path('add_address/', add_address, name='add_address'),
    path('update-cart-item-quantity/', update_cart_item_quantity, name='update-cart-item-quantity'),
    path('forgetPassword/', forgetPasswordView, name='forgetPassword'),
    path('checkEmail/', checkEmailView, name='checkEmail'),
    path('cancel-order/<int:order_id>/', cancelOrderView, name='cancel_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="forgetPassword.html", success_url=reverse_lazy('password_reset_sent')), name="reset_password"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="checkEmail.html"), name="password_reset_sent"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class = SetPasswordForm, template_name="newPassword.html", success_url=reverse_lazy('password_reset_complete')), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="resetComplete.html"), name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)