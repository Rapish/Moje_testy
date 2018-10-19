from behave import given, when, then
import Calculator
from hamcrest import *

@given('I have entered {number1:d} into the calculator')
def enter_number1(context, number1):
    context.number1 = number1


@given('I have also entered {number2:d} into the calculator')
def enter_number2(context, number2):
    context.number2 = number2


@when('I press add')
def press_add(context):

    context.r = Calculator.Add(context.number1, context.number2)


@then('the sum should be {result:d}')
def check_result(context, result):
    assert_that(result is 8)




    "assert_that(context.result, equal_to(result))"