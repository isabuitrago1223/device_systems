from app.data.users_db import users_db


def get_users():
    return users_db


def get_user_by_id(user_id: int):
    return next((u for u in users_db if u["id"] == user_id), None)


def create_user(user_data):
    users_db.append(user_data)
    return user_data


def delete_user(user_id: int):
    global users_db
    users_db = [u for u in users_db if u["id"] != user_id]
    return True


def email_exists(email: str):
    return any(u["email"] == email for u in users_db)

def update_user(user_id: int, user_data: dict):
    user = get_user_by_id(user_id)

    if user:
        user.update(user_data)
        return user

    return None