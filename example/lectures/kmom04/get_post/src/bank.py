from src.owner import Owner
from src.account import Account

class Bank():

    def __init__(self, data):
        # data = {
        # "accounts": []
        # "owners":  []
        #}
        self.owners = [Owner.from_dict(owner_data) for owner_data in data["owners"]]
        self.accounts = [Account.from_dict(acc_data) for acc_data in data["accounts"]]
    
    def to_dict(self):
        return {
            "accounts": [acc.to_dict() for acc in self.accounts],
            "owners": [owner.to_dict() for owner in self.owners],
        }

