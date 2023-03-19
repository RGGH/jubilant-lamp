""" example for GitHub Actions with Sphinx """

def hello_world():
    """
    do the hello world shizz

    :return: Hello World
    :rtype: String
    """
    return "hello world!! :) "

def greeter_msg(greeter :str)->str:
    """
    Custom greeting

    :param greeter: name of person message will be from
    :type greeter: str
    :return: a greeting from the greeter
    :rtype: str
    """
    return (f"Hello to you from {greeter}")