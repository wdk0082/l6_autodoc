def say_hello(name):
    """
    This is a function to say hello (return a hello str).

    Parameters:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a str")
    
    return f"hello, {name}!"