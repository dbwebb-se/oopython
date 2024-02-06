"""
Contain bank owner class
"""

from src.account import Account
class Owner:
    """
    represents an Account owner in bank
    """
    def __init__(self, name, ssn, adress):
        self.name = name
        self._ssn = ssn
        self.adress = adress
        self.accounts = []

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data["name"],
            data["ssn"],
            data["adress"]
        )
        obj.accounts = [Account.from_dict(acc_data) for acc_data in data["accounts"]]
        # tmp_list = []
        # for acc_data in data["accounts"]:
        #     tmp_list.append(Account.from_dict(acc_data, obj))

        return obj

    def to_dict(self):
        return {
            "name": self.name,
            "ssn": self._ssn,
            "adress": self.adress,
            "accounts": [acc.to_dict() for acc in self.accounts],
        }

        # tmp_list = []
        # for acc in self.accounts:
        #     tmp_list.append(acc.to_dict())
        

    def get_ssn(self):
        """
        Return private attribute ssn
        """
        return self._ssn

    def get_account(self, name):
        """
        Find and return specific accont based on name
        """
        for account in self.accounts:
            if account.name == name:
                return account
        return None
