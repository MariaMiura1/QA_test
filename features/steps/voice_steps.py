from behave import given, when, then
from src.voice_commands import process_command


@given("the assistant is ready")
def step_ready(context):
    context.last_response = None


@when('I say "{command}"')
def step_say(context, command):
    context.last_response = process_command(command)


@then('the response should be "{expected}"')
def step_expect(context, expected):
    assert context.last_response == expected
