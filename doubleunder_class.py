class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    # def __str__(self):
    #     return f"{self.model} avtomobile"

    def __repr__(self):
        return f"{self.model} avtomobile"

    def __eq__(self, other):
        return self.narh == other.narh

    def __lt__(self, other):
        if isinstance(other, Avto):
            return self.narh < other.narh

        return "Avto classiga oid obyectni solishtiring"

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass


