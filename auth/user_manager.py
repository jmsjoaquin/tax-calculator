import json
import os
import hashlib

class UserManager:
    def __init__(self, db_file="data/users.json"):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.db_file = os.path.join(base_dir, db_file)

        os.makedirs(os.path.dirname(self.db_file), exist_ok=True)

        if not os.path.exists(self.db_file):
            with open(self.db_file, "w") as f:
                json.dump([], f)

    def _load_users(self):
        with open(self.db_file, "r") as f:
            return json.load(f)

    def _save_users(self, users):
        with open(self.db_file, "w") as f:
            json.dump(users, f, indent=2)

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str) -> dict:
        users = self._load_users()

        if any(user["username"] == username for user in users):
            return {"status": "fail", "message": "Username already exists."}

        hashed_password = self.hash_password(password)

        users.append({
            "username": username,
            "password": hashed_password
        })

        self._save_users(users)
        return {"status": "success", "message": "User registered successfully."}
    
    def login(self, username: str, password: str) -> dict:
        users = self._load_users()
        hashed_input = self.hash_password(password)

        for user in users:
            if user["username"] == username and user["password"] == hashed_input:
                return {
                "status": "success",
                "message": f"Welcome back, {username}!"
            }

        return {
        "status": "fail",
        "message": "Invalid username or password."
    }

