schoenmaat2voetlengte = lambda schoenmaat: 2/3 * schoenmaat -1.5
voetlengte2schoenmaat = lambda voetlengte: round(3/2 * (voetlengte + 1.5))

schoenmaat = 47
voetlengte = schoenmaat2voetlengte(schoenmaat)

print("Mijn schoenmaat is {:d}. Mijn voetlengte is dus {:.2f} cm.".format(
    schoenmaat,
    voetlengte
))

print("Check: de voetlengte van {:.2f} cm komt overeen met schoenmaat {:d}.".format(
    voetlengte,
    voetlengte2schoenmaat(voetlengte)
))