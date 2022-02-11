from fastapi import FastAPI

app = FastAPI()


class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


users = [User("user1@mail.com", "user1"), User("user2@mail.com", "user2"), User("user1@mail.com", "user2")]
success_response = {"authenticated": "true"}
fail_response = {"authenticated": "false"}


@app.get("/auth")
async def get_all_users(email: str, password: str):
    for user in users:
        if user.email == email and user.password == password:
            return success_response
    return fail_response
