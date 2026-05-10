from model.handle_db import HandleAccounts #Traemas la DB para guardar las cuentas
from werkzeug.security import generate_password_hash #Esta es una libreria para encriptar la contra de la cuenta

class Account:
    data_account = {} #Guardar la informacion de la cuenta
    #Inicializadores de la cuenta
    def __init__(self, data_account):
        self.db = HandleAccounts()
        self.data_account = data_account
    #crear cuenta e insertarla en la base de datos
    def create_account(self):
        self._add_id_account()
        self._pass_encrypt()
        self.db.insert_account(self.data_account)
    #eliminar cuenta en la base de datos
    def delete_account(self):
        type_account = self.data_account["type_account"]
        self.db.delete_account(type_account)
    #Crear ID automatica a la cuenta para la BD
    def _add_id_account(self):
        account = self.db.get_all_accounts()
        one_account = account[-1]
        id_account = int(one_account[0])
        self.data_account["id_account"] = str(id_account + 1)
    #Encriptar la contra de la cuenta
    def _pass_encrypt(self): #Werkzeug usa PBKDF2 + SALT internamente, lo cual es muchísimo mejor que MD5 simple
        self.data_account["password_account"] = generate_password_hash(self.data_account["password_account"])