import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from auth.user_manager import UserManager

um = UserManager()

# Test successful login
response = um.login("james", "securepass123")
print("Login test (correct):", response)

# Test invalid password
response = um.login("james", "wrongpass")
print("Login test (wrong password):", response)

# Test nonexistent user
response = um.login("unknown", "something")
print("Login test (unknown user):", response)
