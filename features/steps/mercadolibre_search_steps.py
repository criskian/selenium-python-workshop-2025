from behave import given, when, then
from selenium import webdriver
from pages.mercadolibre_search_page import MercadoSearch
import re

@given('el usuario se encuentra en la pagina de inicio de mercadolibre')
def step_given_mercado_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.mercadolibre_search_page = MercadoSearch(context.driver)

@when('el usuario escribe el producto Iphone 13')
def step_when_mercado_search(context):
    context.mercadolibre_search_page.search("Iphone 13")

@then('aparecen resultados del producto')
def step_then_mercadolibre_search(context):
    assert "Iphone" in context.mercadolibre_search_page.isElementPresent()
