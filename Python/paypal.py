from payment import Payment

class Paypal(Payment):
    email = str

    def Paypal(self, id, email):
        super.__init__(id)
        self.email = email
