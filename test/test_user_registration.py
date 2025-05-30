import sys
import os

# Add parent directory to path so we can import auth.*
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from auth.user_manager import UserManager



um = UserManager()
response = um.register("james", "securepass123")
print(response)
users = um._load_users()
print("Current users:", users)