class Transaction:
    def __init__(self, transaction: str) -> None:
        self._who, self._when, self._amount = transaction.split()

    def who(self):
        return self._who

    def when(self):
        return self._when

    def amount(self):
        return float(self._amount)

    def equals(self, that):
        return (
            self.who() == that.who()
            and self.when() == that.when()
            and self.amount() == that.amount()
        )

    def __lt__(self, that):  # fluent python
        return self.amount() < that.amount()

    def __gt__(self, that):  # fluent python
        return self.amount() > that.amount()

    def __eq__(self, that):  # fluent python
        return self.amount() == that.amount()

    def __str__(self) -> str:
        return self.who() + "\t" + self.when() + "\t" + str(self.amount())
