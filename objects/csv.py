from datetime import date

class CSV:
    def __init__(
            self,
            word: str,
            sets: str,
            source: str,
            checked: int = 0,
            score: int = 0,
            synonyms: int = 1,
            generated: bool = True,
            added: date = date.today()
    ):
        self.word = word
        self.sets = sets
        self.source = source
        self.checked = checked
        self.score = score
        self.synonyms = synonyms
        self.generated = generated
        self.added = added