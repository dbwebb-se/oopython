"""
Show code for a Aaccount and BannedAccounts based on UML diagram in an article.
"""

class Account:
    """
    A account
    """

    def __init__(self, name, password, active):
        self.name = name
        self.password = password
        self.active = active


    def login(self):
        """
        Login account on service
        """
        pass

    def logout(self):
        """
        Logut account from service
        """
        pass

    def set_active(self, active):
        """
        Activare or de-activate account
        """
        pass



class BannedAccounts:
    """
    A class for banned accounts
    """

    def __init__(self, reason, date):
        self.generated = date
        self.reason = reason
        self.accounts = []

    def ban_accounts(self, accounts):
        """
        Ban accounts
        """
        pass

    def get_details(self):
        """
        Return the details about the banned accounts
        """
        pass
