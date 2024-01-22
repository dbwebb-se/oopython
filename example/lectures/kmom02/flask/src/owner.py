"""
Contain bank owner class
"""
class Owner:
    """
    represents an Account owner in bank
    """
    def __init__(self, name, ssn, adress):
        print(name)
        self.name = name
        self._ssn = ssn
        self.adress = adress
        self.accounts = []

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
