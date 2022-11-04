class Account:
    def __init__(self, owner, amount=0, *trans):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        if trans:
            for el in trans:
                self._transactions.append(el)

    def handle_transaction(self, transaction_amount):
        if self.amount + transaction_amount <= 0:
            raise ValueError('sorry cannot go in debt!')
        else:
            self.amount += transaction_amount
            self._transactions.append(transaction_amount)
            return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __add__(self, other):
        amount_sum = self.amount + other.amount
        trans_list = self._transactions + other._transactions
        return Account(f'{self.owner}&{other.owner}', amount_sum, *trans_list)

    def __gt__(self, other):
        return self.amount > other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount