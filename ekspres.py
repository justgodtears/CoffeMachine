#ekspres.py

class EkspresDoKawy:
    def __init__(self, woda, ziarno):
        self.woda = woda
        self.ziarno = ziarno

    def zrobkawe(self, rodzaj):
        if rodzaj == "espresso":
            potrzebna_woda, potrzebna_ziarno = 30, 15
        elif rodzaj == "latte":
            potrzebna_woda, potrzebna_ziarno = 150, 20
        else:
            print("Nie mamy tego w ofercie")
            return

        if self.woda >= potrzebna_woda and self.ziarno >= potrzebna_ziarno:
            self.woda -= potrzebna_woda
            self.ziarno -= potrzebna_ziarno
            print("Odbierz swoją kawę")
        else:
            print("Brakuje zasobów")

    def uzupelnij(self, woda, ziarno):
        self.woda += woda
        self.ziarno += ziarno

    def __str__(self):
        return f"Stan wody: {self.woda}ml, ziarna: {self.ziarno}g"


class EkspresPro(EkspresDoKawy):
    def __init__(self, woda, ziarno, mleko):
        super().__init__(woda, ziarno)
        self.mleko = mleko


    def zrobkawe(self, rodzaj):
        if rodzaj == "cappucino":
            potrzebna_woda, potrzebna_ziarno, potrzebne_mleko = 200, 25, 100

            if self.woda >= 200 and self.ziarno >= 25 and self.mleko >= 100:
                self.woda -= potrzebna_woda
                self.ziarno -= potrzebna_ziarno
                self.mleko -= potrzebne_mleko
            else:
                print("Brak zasobów")

        else:
            super().zrobkawe(rodzaj)