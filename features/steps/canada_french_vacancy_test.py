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


@then("I click to language '{language}' checkbox")
def step_impl(context, language):
    home_page = HomePage(context.driver)
    home_page.language_choice()


@step("I see the '{language}' on the language's field")
def step_impl(context, language):
    home_page = HomePage(context.driver)
    assert language in home_page.language_in_field(language)


@step("I click to apply button")
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.apply_button()


@when("I check count of vacancies card in the vacancies block")
def step_impl(context):
    home_page = HomePage(context.driver)
    assert str(home_page.count_active_vacancy_cart()) + " jobs found" == home_page.active_vacancy_block_h3()


@then("I print quantity of active vacancies")
def step_impl(context):
    home_page = HomePage(context.driver)
    print("On the page is " + str(home_page.count_active_vacancy_cart()), " active vacancy")
