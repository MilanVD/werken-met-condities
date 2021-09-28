#kaas,kaas
if input("Is de kaas geel? (J/N) : ") == "J":
    if input("Zitten er gaten in? (J/N) : ") == "J":
        if input("Is de kaas belachelijk duur? (J/N) : ") == "J":
            print("Dan is het Emmenthaler")
        else:
            print("Dan is het Leerdammer")
    else:
        if input("Is de kaas zo hard als steen? (J/N) : ") == "J":
            print("Dan is het Pamigiano Reggiano")
        else:
            print("Dan is het Goudse kaas")
else:
    if input("Heeft de kaas blauwe schimmels? (J/N) : ") == "J":
        if input("Heeft de kaas een korst? (J/N) : ") == "J":
            print("Dan is het Blue de Rochbaron")
        else:
            print("Dan is het Foume d'Ambert")
    else:

        if input("Heeft de kaas een korst? (J/N) : ") == "J":
            print("Dan is het Camenbert")
        else:
            print("Dan is het Mozzarella")
