class CreditCard:
    """
    create new credit card instance
    """
    def __init__(self, customer, bank, account, limit):
        """
        The initial balance is zero

        customer - The name of the customer ('Dawa')
        bank - The name of the bank ("BOB")
        account - The account number ("1234556")
        limit - credit limit (measured in Nu)
        """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0 

    def get_customer(self):
        """
        Return name of the customer
        """
        return self._customer

    def get_bank(self):
        """
        Return name of the bank
        """
        return self._bank

    def get_account(self):
        """
        Return account name
        """
        return self._account

    def get_limit(self):
        """
        return credit limit
        """
        return self._limit

    def get_balance(self):
        """
        Return the credit balance
        """
        return self._balance
    
    def charge(self, price):
        """
        Charge given price, assuming sufficient credit limit
        Return True if charge is processed, otherwise False
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """
        process customer payment that reduces balance
        """
        self._balance -= amount

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard("Dawa", "BOB", "34235245", 110))
    wallet.append(CreditCard("Pema", "BNB", "000045", 120))
    wallet.append(CreditCard("Namgay", "BDB", "56758245", 150))

    for val in range(1, 30):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New Balance =", wallet[c].get_balance())
        print()
