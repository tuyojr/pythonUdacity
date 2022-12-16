# © Faustina Maria Giaquinta
class Category:

    # create a method that initializes the name of the budget category, and an empty ledger that takes a list of spend details
    def __init__(self, name):
        self.name = name.title()
        self.ledger = []

    # a method that creates a dictionary that describes the deposit details and appends it to the ledger created in the __init__ method
    def deposit(self, amount, description=''):
        deposit_ = {
            'amount': amount,
            'description': description
        }
        self.ledger.append(deposit_)

    # this method checks if the user has sufficient amount in his ledger, and if it has, creates a dictionary displays the amount withdrawn (in -ve) and what it is used for, this is also appended to the ledger
    def withdraw(self, amount, description=''):
        sufficient_funds = self.check_funds(amount)
        if sufficient_funds:
            withdrawal_ = {
                'amount': -amount,
                'description': description
            }
            self.ledger.append(withdrawal_)

        return sufficient_funds

    # this method returns the user's balance. which is the sum of the amount value in the ledger
    def get_balance(self):
        balance = sum([spend['amount'] for spend in self.ledger])

        return balance

    # this method allows for withdrawal and transfer from the legder
    def transfer(self, amount, category):
        withdraw_description = f"Transfer to {category.name}"
        transfer_description = f"Transfer from {self.name}"
        operation = self.check_funds(amount)

        if operation:
            self.withdraw(amount, withdraw_description)
            category.deposit(amount, transfer_description)

        return operation

    # this method allows us to get the balance using the get_balance() method.
    def check_funds(self, amount):
        balance = self.get_balance()

        return amount <= balance

    # we want to create a method that returns a string expression
    def __repr__(self):
        line_len = 30
        side_len = '*' * ((line_len - len(self.name)) // 2)
        title_line = f"{side_len}{self.name}{side_len}"
        expenses = [title_line]
        for i in self.ledger:
            amount = f"{i['amount']:.2f}"
            description = i['description'][:23]

            expenses.append(
                f"{description.ljust(line_len - len(amount), ' ')}{amount}")

        funds = self.get_balance()
        expenses.append(f"Total: {funds:.2f}")

        category_str = '\n'.join(expenses)

        return category_str

# This function creates a spend chart by percentage
def create_spend_chart(categories):
    cat_ledgers = [cat.ledger for cat in categories]
    withdrawals = [-sum([exp['amount'] for exp in ledger_ if exp['amount'] < 0])
                   for ledger_ in cat_ledgers]
    total_withdrawals = sum(withdrawals)
    withdrawals_idx = [
        10 - int(i * 100 // total_withdrawals) // 10 for i in withdrawals]

    num_cat = len(categories)
    inner_space = num_cat - 1
    cats_str = num_cat * '{}  '
    cat_names = [cat.name for cat in categories]
    cat_names = [cat.ljust(len(max(cat_names, key=len)), ' ')
                 for cat in cat_names]

    percentages = list(range(100, -10, -10))
    chart_str = ['Percentage spent by category']

    for idx, i in enumerate(percentages):
        cat_percentages = ' ' + cats_str.format(
            *['o' if wi <= idx else ' ' for wi in withdrawals_idx])
        chart_str.append(f"{str(i).rjust(3, ' ')}|" + cat_percentages)
        if not i:
            chart_str.append(' ' * 4 + f"-{'-'*num_cat}{'--'*inner_space}--")
            for i in range(len(max(cat_names, key=len))):
                chart_str.append(' ' * 5 + cats_str.format(*
                                                           [cat[i] for cat in cat_names]))

    chart_str = '\n'.join(chart_str)

    return chart_str