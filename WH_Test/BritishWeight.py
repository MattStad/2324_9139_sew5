class BritishWeight:
    """ Doctest
    >>> b1 = BritishWeight(13)
    >>> b2 = BritishWeight(16)
    >>> print(b1)
    13 lb
    >>> print(b2)
    1 st 2 lb
    >>> b3 = b1 + b2
    >>> print(b3)
    2 st 1 lb
    """

    def __init__(self,stones,pounds):
        self.pound=pounds+stones*14

    def __str__(self):
        if self.pound//14==0:
            return str(self.pound)+" lb"
        else:
            return str(self.pound//14) +" st "+str(self.pound%14)+" lb"

    def __add__(self, other):
        return BritishWeight(self.pound+other.pound)