from model.handle_db import HandleAccounts
from lib.check_password import check_account

def less_money_account(money_account, type_account, password_account, type_transaction):
    account = HandleAccounts()
    
    filter_money = account.get_only_money_account(type_account) #Dinero original
    first_money = int(filter_money[0])
    money_transaction = int(money_account) #Dinero consignacion
    
    verify_password = check_account(type_account, password_account)
    if verify_password:
        if type_transaction == "N":
            if first_money > money_transaction:
                final_money = first_money - money_transaction
                account.update_account(final_money,type_account)
                account = account.get_only_account(type_account)
                return account
            else:
                return None
        elif type_transaction == "Y":
            if first_money > money_transaction:
                final_money = first_money - money_transaction
                iva = 7090
                if final_money >= iva:
                    final_money -= iva
                    account.update_account(final_money,type_account)
                    account = account.get_only_account(type_account)
                    return account
                else:
                    return None
            else:
                return None
    elif verify_password == False:
        return False
    
def more_money_account(money_account, type_account, password_account):
    account = HandleAccounts()
    
    filter_money = account.get_only_money_account(type_account) #Dinero original
    first_money = int(filter_money[0])
    money_transaction = int(money_account) #Dinero que mete
    
    verify_password = check_account(type_account, password_account)
    if verify_password:
        final_money = first_money + money_transaction
        account.update_account(final_money,type_account)
        account = account.get_only_account(type_account)
        return account
    elif verify_password == False:
        return False