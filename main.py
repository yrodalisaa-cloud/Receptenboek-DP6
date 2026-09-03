from recept import Recept 
from ingredient import Ingredient
from stap import Stap

def main():
    recepten = []

    
    recept1 = Recept("Pasta Pesto", "Een romige pasta met kip en pesto voor 1 persoon.")

    recept1.voeg_ingredient_toe(Ingredient("kip", 100, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("pesto", 1, "eetlepels"))
    recept1.voeg_ingredient_toe(Ingredient("ui", 1, "kwart"))
    recept1.voeg_ingredient_toe(Ingredient("pasta", 75, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("kookroom", 62.5, "milliliter"))
    recept1.voeg_ingredient_toe(Ingredient("cherry tomaatjes", 62.5, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("peper en zout", 0.25, "snuf"))
    recept1.voeg_ingredient_toe(Ingredient("olijfolie", 1, "klein scheutje"))
    recept1.voeg_ingredient_toe(Ingredient("geraspte kaas", 1, "handje"))

    recept1.voeg_stap_toe(Stap("Snipper het uitje en fruit even aan in een scheutje olijfolie. Voeg de blokjes kip toe en bak ongeveer 5 minuten. Kook ondertussen de pasta gaar."))
    recept1.voeg_stap_toe(Stap("Voeg de (zelfgemaakte) pesto en room toe aan de kip en roer goed door. Proef nog even of er nog peper of zout bij moet."))
    recept1.voeg_stap_toe(Stap("Laat de pestosaus een paar minuutjes zachtjes pruttelen. Voeg dan de gekookte pasta toe en schep er doorheen."))
    recept1.voeg_stap_toe(Stap("Snijd de cherry tomaatjes door de helft en verwarm deze nog een minuutje mee. Serveer de pasta pesto op een bord, eventueel met wat geraspte kaas."))

    recepten.append(recept1)

    recept2 = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")

    

if __name__ == "__main__":
    main()
