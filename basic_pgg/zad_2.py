# = -> jest operatorem przypisania, wkłada to co po prawej stronie, do tego co po lewej

# PEP - Python Enhancement Proposal
# Konwencje nazewnicze
#
imie_psa = "Burek"
# imiePsa = "Burek" # tak nie robimy w pythonie

podstawa_1 = 3
podstawa_2 = 9
wysokosc_trapezu = 6.5

pole_trapezu = 0.5 * (podstawa_1 + podstawa_2) * wysokosc_trapezu

print(pole_trapezu)
print("Pole trapezu wynosi: " + str(pole_trapezu))
print("Pole trapezu wynosi:", str(pole_trapezu)) # jezeli podajemy kilka argumentow do wyświetlenia, są one rozdzielane spacją
print("Pole trapezu wynosi:", pole_trapezu) # tutaj nie musze zmieniac typu, tym sie zajmie funkcja print

