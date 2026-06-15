# test_data.py

# Sample user data (list of dictionaries)
users = [
    {
        "username": "admin_user",
        "password": "Admin@123",
        "role": "admin",
        "expected_result": "success"
    },
    {
        "username": "normal_user",
        "password": "User@123",
        "role": "user",
        "expected_result": "success"
    },
    {
        "username": "invalid_user",
        "password": "Wrong@123",
        "role": "user",
        "expected_result": "failure"
    }
]

# API test data
api_test_data = [
    {
        "endpoint": "/login",
        "method": "POST",
        "payload": {"username": "admin_user", "password": "Admin@123"},
        "expected_status": 200
    },
    {
        "endpoint": "/login",
        "method": "POST",
        "payload": {"username": "wrong", "password": "wrong"},
        "expected_status": 401
    }
]

# Environment config
config = {
    "base_url": "https://example.com",
    "timeout": 30,
    "retry": 2
}