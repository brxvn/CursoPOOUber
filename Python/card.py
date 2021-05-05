from payment import Payment

class Card(Payment):
    cardNumber = int 
    cvv = int
    cardDate = str

    def Card(self, id, cardNumber, cvv, cardDate):
        super.__init__(id)
        self.cardNumber = cardNumber
        self.cvv = cvv
        self.cardDate = cardDate