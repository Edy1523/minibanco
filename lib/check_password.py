from model.handle_db import HandleUsers, HandleAccounts
from werkzeug.security import check_password_hash

def check_user(username, password_user):
    user = HandleUsers()
    filter_user = user.get_only_user(username)
    if filter_user:
        same_password = check_password_hash(filter_user[5], password_user)
        if same_password:
            return filter_user
    return None

def check_account(type_account, password_account):
    account = HandleAccounts()
    filter_account = account.get_only_account(type_account)
    if filter_account: #Si existe la cuenta
        same_password = check_password_hash(filter_account[3], password_account)
        if same_password:
            return filter_account
    return False #Si no exite la cuenta