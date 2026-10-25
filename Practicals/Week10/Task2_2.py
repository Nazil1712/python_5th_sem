def authenticate(func):
    def wrapper(user, *args, **kwargs):
        if user.is_authenticated:
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("Access denied. User is not authenticated.")
    return wrapper

class User:
    def __init__(self, username, is_authenticated=False):
        self.username = username
        self.is_authenticated = is_authenticated

@authenticate
def view_sensitive_data(user, data):
    return f"{user.username} is viewing sensitive data: {data}"

# Create a user
user = User("Alice", is_authenticated=True)

# Access the sensitive data with authentication
result = view_sensitive_data(user, "Some confidential information")
print(result)