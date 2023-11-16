class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.starting_amount = amount

    def handle_transaction(self, transaction_amount: int):
        if transaction_amount <= self.amount:
            self.amount -= transaction_amount
            return f"New balance: {self.amount}"
        raise ValueError("sorry cannot go in debt!")

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        if amount + self.amount >= 0:
            self.amount += amount
            self._transactions.append(amount)
            return f"New balance: {self.amount}"
        raise ValueError("sorry cannot go in debt!")

    @property
    def balance(self):
        return self.amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __add__(self, other):
        if isinstance(other, Account):
            new_owner = f"{self.owner}&{other.owner}"
            new_starting_amount = self.starting_amount + other.starting_amount
            new_transactions = self._transactions + other._transactions
            new_account = Account(new_owner, new_starting_amount)
            new_account._transactions.extend(new_transactions)
            return new_account


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
