from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Jane')

        self.a2.account_balance = 100

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

        assert self.a2.get_name() == 'Jane'
        assert self.a2.get_balance() == 100

    def test_deposit(self):
        assert self.a1.deposit(100) is True
        assert self.a1.get_balance() == 100
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 100
        assert self.a1.deposit(-1) is False
        assert self.a1.get_balance() == 100

    def test_withdraw(self):
        assert self.a2.withdraw(200) is False
        assert self.a2.get_balance() == 100
        assert self.a2.withdraw(0) is False
        assert self.a2.get_balance() == 100
        assert self.a2.withdraw(50) is True
        assert self.a2.get_balance() == 50
