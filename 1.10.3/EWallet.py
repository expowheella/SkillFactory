class Wallet:
    def __init__(self, clients_full_name, balance):
        self.clients_full_name = clients_full_name
        self.balance = balance

    def get_account_info(self):
        return f'Клиент "{self.clients_full_name}".', \
               f'Баланс: {self.balance} руб.'