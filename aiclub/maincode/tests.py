from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

def create_user(username, password, email):
    try:
        # Create a new user using the provided information
        user = User.objects.create_user(username=username, password=password, email=email)
        return user
    except Exception as e:
        # Handle any exceptions that may occur during user creation
        return None


with open("combo.txt",'r') as reader:
    read = reader.read().splitlines()
    for combo in read:
        username, password = combo.split(':')
        print(f"Creating {username} with password {password}")
        _  = create_user(username,password,username+"@gmail.com")
        print(_)