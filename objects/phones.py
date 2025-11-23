class Phone:
    def __init__(self, arpa: str, fx: str):
        self.arpa = arpa # symbol from CMU
        self.fx = fx # fauxnetic from config
        self.lexical_set = ""

    def __str__(self):
        return self.fx
    
    def __repr__(self):
        return self.fx