from recept import Recept 
from ingredient import Ingredient
from stap import Stap

def maak_recepten():
    recepten = []

    
    recept1 = Recept("Tagliatelle pesto", "Een romige pasta met kip en pesto voor 1 persoon.")

    recept1.voeg_ingredient_toe(Ingredient("kip", 100, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("pesto", 100, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("uitje", 1, ""))
    recept1.voeg_ingredient_toe(Ingredient("tagliatelle", 150, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("kookroom", 100, "milliliter"))
    recept1.voeg_ingredient_toe(Ingredient("cherry tomaatjes", 250, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("peper en zout", 1, "snuf"))
    recept1.voeg_ingredient_toe(Ingredient("olijfolie", 1, "scheutje"))
    recept1.voeg_ingredient_toe(Ingredient("geraspte kaas", 1, "handje"))
    recept1.voeg_ingredient_toe(Ingredient("knoflook", 1, "teentje"))

    recept1.voeg_stap_toe(Stap("Snipper het uitje en knoflook en fruit even aan in een scheut olijfolie. Voeg de blokjes kip toe en bak ongeveer 5 minuten. Kook ondertussen de tagliatelle gaar."))
    recept1.voeg_stap_toe(Stap("Voeg de (zelfgemaakte) pesto en room toe aan de kip en roer goed door. Proef nog even of er nog peper of zout bij moet."))
    recept1.voeg_stap_toe(Stap("Laat de pestosaus een paar minuutjes zachtjes pruttelen. Voeg dan de gekookte tagliatelle toe en schep er doorheen."))
    recept1.voeg_stap_toe(Stap("Snijd de cherry tomaatjes door de helft en verwarm deze nog een minuutje mee. Serveer de tagliatelle pesto op een bord, eventueel met wat geraspte kaas."))

    recepten.append(recept1)

    recept2 = Recept("Quesadillas met gehakt", "Heerlijke quesadillas met gehakt voor 1 persoon.")

    recept2.voeg_ingredient_toe(Ingredient("gehakt", 175, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("tortilla's", 2, "stuks"))
    recept2.voeg_ingredient_toe(Ingredient("paprika", 1, ""))
    recept2.voeg_ingredient_toe(Ingredient("uitje", 1, "klein"))
    recept2.voeg_ingredient_toe(Ingredient("maïs", 140, "gram uit blik"))
    recept2.voeg_ingredient_toe(Ingredient("zure room", 125, "milliliter"))
    recept2.voeg_ingredient_toe(Ingredient("geraspte kaas", 1, "handje"))
    recept2.voeg_ingredient_toe(Ingredient("peper en zout", 1, "snuf"))
    recept2.voeg_ingredient_toe(Ingredient("komijn", 1, "snuf"))
    recept2.voeg_ingredient_toe(Ingredient("paprikapoeder", 1, "snuf"))
    recept2.voeg_ingredient_toe(Ingredient("tomatenpuree", 1, "eetlepel"))
    recept2.voeg_ingredient_toe(Ingredient("guacamole", 2, "eetlepels"))

    recept2.voeg_stap_toe(Stap("Doe de tomatenpuree met de komijn, paprikapoeder en gehakt in een pan en bak een paar minuutjes. Voeg eventueel een klein scheutje water toe om het mengsel iets smeuïger te maken."))
    recept2.voeg_stap_toe(Stap("Snijd de puntpaprika in kleine blokjes, laat de maïs uitlekken en snipper de rode ui."))
    recept2.voeg_stap_toe(Stap("Neem een wrap en bestrijk deze met zure room. Verdeel een deel van het gehaktmengsel er over."))
    recept2.voeg_stap_toe(Stap("Verdeel dan ook een deel van de blokjes paprika, maïs, rode ui en geraspte kaas er over."))
    recept2.voeg_stap_toe(Stap("Leg de tweede wrap er bovenop en druk deze een beetje aan. Bak de quesadilla in een droge koekenpan op middelhoog vuur totdat de onderkant goudbruin is. Draai hem voorzichtig om en bak ook de andere kant goudbruin."))
    recept2.voeg_stap_toe(Stap("Dek de wrap af met een andere wrap en bak de quesadilla in een contactgrill of in een droge koekenpan licht krokant."))
    recept2.voeg_stap_toe(Stap("Snijd de quesadilla in vieren en serveer met guacamole en zure room."))

    recepten.append(recept2)

    recept3 = Recept("Carrot cake voor één", "Heerlijke warme carrot cake voor 1 persoon.")

    recept3.voeg_ingredient_toe(Ingredient("geraspte wortel", 25, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("suiker", 50, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("gesmolten boter", 30, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("eidooier", 1, "stuk"))
    recept3.voeg_ingredient_toe(Ingredient("bloem", 30, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("gemalen kaneel", 0.3, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("vanille-extract", 0.6, "milliliter"))
    recept3.voeg_ingredient_toe(Ingredient("zout", 1, "snuf"))
    recept3.voeg_ingredient_toe(Ingredient("melk", 15, "milliliter"))
    recept3.voeg_ingredient_toe(Ingredient("gehakte pecannoten", 8, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("bakpoeder", 1.25, "gram"))

    recept3.voeg_ingredient_toe(Ingredient("roomkaas (zacht)", 30, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("boter (zacht)", 15, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("poedersuiker", 30, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("vanille-extract (frosting)", 1.25, "milliliter"))


    recept3.voeg_stap_toe(Stap("Verwarm de oven voor op 177°C en vet een klein ovenschaaltje (ca. 300 ml) licht in met boter."))
    recept3.voeg_stap_toe(Stap("Meng de suiker, gesmolten boter, eidooier en vanille in een middelgrote kom met een vork tot een glad mengsel (ongeveer 45 seconden)."))
    recept3.voeg_stap_toe(Stap("Klop in een andere kom de bloem, het bakpoeder, de kaneel en het zout door elkaar."))
    recept3.voeg_stap_toe(Stap("Voeg de droge ingrediënten geleidelijk toe aan het natte mengsel en roer tot het net is gecombineerd."))
    recept3.voeg_stap_toe(Stap("Giet de melk erbij en meng tot een glad beslag."))
    recept3.voeg_stap_toe(Stap("Spatel de geraspte wortel en gehakte pecannoten er voorzichtig doorheen."))
    recept3.voeg_stap_toe(Stap("Giet het beslag in het ovenschaaltje en bak gedurende 20-23 minuten tot een prikker in het midden er schoon uitkomt. Laat de cake volledig afkoelen."))

    recept3.voeg_stap_toe(Stap("Meng voor de frosting de zachte roomkaas en zachte boter in een kleine kom tot een glad mengsel."))
    recept3.voeg_stap_toe(Stap("Voeg de poedersuiker en vanille toe en meng tot een gladde frosting."))
    recept3.voeg_stap_toe(Stap("Verdeel de frosting gelijkmatig over de bovenkant van de afgekoelde cake."))


    recepten.append(recept3)

    return recepten

def toon_overzicht(recepten):
    print("Lekkere recepten voor 1")
    for index, recept in enumerate(recepten, start=1):
        print(f"{index}. {recept.get_naam()}")

def toon_recept(recept):
    print(f"\n{recept.get_naam()}")
    print(recept.get_omschrijving())

    print("\nIngrediënten:")
    for ingredient in recept.get_ingredienten():
        print(f"- {ingredient}")

    print("\nStappen:")
    for volgnummer, stap in enumerate(recept.get_stappen(), start=1):
        print(f"{volgnummer}. {stap}")

def kies_recept(recepten):
     keuze = input("\nKies een receptnummer (of 'q' om te stoppen): ").strip()

     
     if keuze.lower() == "q":
        return None
 
     if not keuze.isdigit() or not (1 <= int(keuze) <= len(recepten)):
        print("Recept niet gevonden.")
        return "opnieuw"
 
     return recepten[int(keuze) - 1]
 
 
def main():
    recepten = maak_recepten()
 
    while True:
        toon_overzicht(recepten)
        resultaat = kies_recept(recepten)
 
        if resultaat is None:
            print("Tot ziens!")
            break
 
        if resultaat == "opnieuw":
            continue
 
        toon_recept(resultaat)
    
if __name__ == "__main__":
    main()
