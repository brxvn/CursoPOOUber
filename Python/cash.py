from payment import Payment

class Cash(Payment):
    id = int 

    def Cash(self, id):
        super.__init__(id)
        