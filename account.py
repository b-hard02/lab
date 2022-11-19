class Account:
    """
    A class representing an account object.
    """
    def __init__(self, name: str):
        """
        Constructor to create the initial state of an account object.
        :param name: Name of the account.
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float):
        """
        Function to increase the balance of an account and determine if the deposit was successful.
        :param amount: Numeric value
        :return: Success of the transaction.
        """
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float):
        """
        Function to decrease the balance of an account and determine if the withdrawal was successful.
        :param amount: Numeric value.
        :return: Success of the transaction.
        """
        if 0 < amount < self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """
        Function to retrieve the balance of an account.
        :return: Account balance.
        """
        return self.account_balance

    def get_name(self):
        """
        Function to retrieve the name of an account.
        :return: Account name.
        """
        return self.account_name
