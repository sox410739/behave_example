from behave import given, when, then
from src.product import Product
from src.shoppingCart import ShoppingCart

@given('一個 10 元的餅乾')
def step_impl(context):
    context.biscuit = Product('biscuit', 10)

@given('一個 2 元的糖果')
def step_impl(context):
    context.candy = Product('candy', 2)

@when('餅乾和糖果被加進購物車')
def step_impl(context):
    context.shopping_cart = ShoppingCart()
    context.shopping_cart.add_product(context.biscuit)
    context.shopping_cart.add_product(context.candy)

@then('購物車內的總金額是 12 元')
def step_impl(context):
    assert context.shopping_cart.get_total_price() == 12
    
@then('購物車內有 2 樣商品')
def step_impl(context):
    assert context.shopping_cart.get_quantity_of_product() == 2


@given('一個 {product1_price:d} 元的 {product1_name}')
def step_impl(context, product1_price, product1_name):
    context.product1 = Product(product1_name, product1_price)

@given('一個 {product2_price:d} 元的 {product2_name}')
def step_impl(context, product2_price, product2_name):
    context.product2 = Product(product2_name, product2_price)

@when('兩樣商品被加進購物車')
def step_impl(context):
    context.shopping_cart = ShoppingCart()
    context.shopping_cart.add_product(context.product1)
    context.shopping_cart.add_product(context.product2)

@then('購物車內的總金額是 {total_price:d} 元')
def step_impl(context, total_price):
    assert context.shopping_cart.get_total_price() == total_price

