class Person:
    "Beskriver en person"
    def __init__(self, fornavn:str, etternavn:str, fødselsår:int, høyde:int, vekt:int) -> None:
        self.Fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselsår
        self.høyde = høyde
        self.vekt = vekt

sigurd = Person("Sigurd", "Fareth", 2005, 185, 65)
