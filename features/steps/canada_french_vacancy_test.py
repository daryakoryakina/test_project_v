import time

from behave import *

from features.pages.home_page import HomePage


@when("I open Home Page")
def step_impl(context):
    context.driver.get("https://careers.veeam.com/")


@then("I click on the country field")
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.select_country()


@then("I choosing a '{country}'country")
def step_impl(context, country):
    home_page = HomePage(context.driver)
    home_page.country_choice(country)


@step("I see '{country}'")
def step_impl(context, country):
    home_page = HomePage(context.driver)
    assert country in home_page.ret_f(country)


@then("I click to the '{language}' field")
def step_impl(context, language):
    home_page = HomePage(context.driver)
    home_page.language_field_open()


@then("I click to language '{language}', '{param}' checkbox")
def step_impl(context, language, param):
    home_page = HomePage(context.driver)
    home_page.language_choice(param)


@step("I see the '{language}' on the language's field")
def step_impl(context, language):
    home_page = HomePage(context.driver)
    assert language in home_page.language_in_field(language)


@step("I click to apply button")
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.apply_button()


@then("I check count of vacancies card with '{language}' and '{country}' parameters in the vacancies block")
def step_impl(context, language, country):
    home_page = HomePage(context.driver)
    count_country_in_cart = str(home_page.count_active_vacancy_cart_country(country)) + " jobs found"
    count_language_in_cart = str(home_page.count_active_vacancy_cart_language(language)) + " jobs found"
    quantity = home_page.active_vacancy_block_h3()
    if count_country_in_cart != count_language_in_cart != quantity:
        print("country in cart is  ," + count_country_in_cart, "language in cart is  ," + count_language_in_cart, quantity)
    assert count_country_in_cart == count_language_in_cart == quantity


@step("I print quantity vacancies")
def step_impl(context):
    home_page = HomePage(context.driver)
    print(home_page.active_vacancy_block_h3())


@step("I clear filter")
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.clear_filter()
