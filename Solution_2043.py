class Bank:

    def __init__(self, balance: List[int]):
        self.balance = {}
        for i,x in enumerate(balance):
            self.balance[i + 1] = x

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.balance or account2 not in self.balance:
            return False
        if self.balance[account1] < money:
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.balance:
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.balance:
            return False
        if self.balance[account] < money:
            return False
        self.balance[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)