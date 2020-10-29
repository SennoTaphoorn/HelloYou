import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["d", "D"]

Required = ("\nGebruik alleen A, B, of C\n")

def intro():
  print ("""\n\n  Je naam is Arts Abou, je woont in Syrië.
  En nadat je huis gebombardeerd is
  wil je een plan bedenken voor wat je nu wilt gaan doen:\n""")
  time.sleep(1)
  print ("""  A. Je begint een reis naar europa, lopend
  B. Zoek een nieuw huis
  C. Je gaat op zoek naar iemand die je kan helpen""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_101()
  elif choice in answer_B:
    print ("""Je vindt een nieuw huis!
    Maar hij wordt gebombardeerd, Je bent dood gegaan""")
    time.sleep(5)
    intro()
  elif choice in answer_C:
    optie_200()
  else:
    print (required)
    intro()

def optie_101():
  print ("\n  Je loopt dagen lang en komt uiteindelijk aan bij de grens:\n")
  time.sleep(1)
  print ("""  A. Je bent bang, en keert terug
  B. Probeer de grens over te steken""")
  choice = input(">>> ")
  if choice in answer_A:
    intro()
  elif choice in answer_B:
    print ("\nJe wordt gezien en neergeschoten, je bent dood gegaan\n")
    time.sleep(1)
    intro()
  else:
    print (required)
    optie_101()

def optie_200():
  print ("\n  Waar ga je zoeken?:\n")
  time.sleep(1)
  print ("""  A. Bij een groep mensen
  B. In een steeg
  C. In een huis dat nog overeind staat""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_300()
  elif choice in answer_B:
    print ("\nJe vindt niks")
    time.sleep(1)
    optie_200()
  elif choice in answer_C:
    print ("\nJe vindt niks")
    time.sleep(1)
    optie_200()
  else:
    print (required)
    optie_200()

def optie_300():
  print ("""\n  Je vraagt waarom de groep er staat, Je komt erachter dat ze een
  groep zijn die in een bus gaan vluchten naar Europa. Je vraagt of je mee kan
  Ze zeggen dat het kan omdat iemand niet was gekomen.
  Je stapt in de bus en rijdt totdat je bij een grens komt.
  Er wordt gevraagt of iemand nog uit wilt stappen of nog verder wil.
  Wat doe je?\n""")
  time.sleep(1)
  print ("""  A. Je blijft zitten
  B. Je verstopt je in de bus
  C. Je stapt uit""")
  choice = input(">>> ")
  if choice in answer_A:
    print("De bus wordt bij de grens gestopt, iedereen wordt gecheckt en je "
    "wordt vertelt terug te keren\n")
    intro()
  elif choice in answer_B:
    print ("\n  Je wordt gevonden en vermoord voor smokkeling\n")
    time.sleep(2)
    intro()
  elif choice in answer_C:
    optie_400()
  else:
    print (required)
    optie_300()

def optie_400():
  print ("""\n  De bus wordt gestopt en iedereen wordt gecheckt.
  Je ziet een kans om er langs te gaan en de grens over te gaan.
  Pak je die kans?\n""")
  time.sleep(1)
  print ("""  A. Nee
  B. Ja""")
  choice = input(">>> ")
  if choice in answer_A:
    print("je kiest ervoor het niet te wagen en keert terug\n")
    intro()
  elif choice in answer_B:
    optie_500()
  else:
    print (required)
    optie_400()

def optie_500():
  print ("""\n  Je loopt dagen op een rechte weg totdat je een kruispunt tegenkomt.
  Rechts zie je een bos. links een dorpje en rechtdoor niks.
  Welke kant ga je op?\n""")
  time.sleep(1)
  print ("""  A. Rechts
  B. Links
  C. Vooruit""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_501()
  elif choice in answer_B:
    optie_1600()
  elif choice in answer_C:
    optie_600()
  else:
    print (required)
    optie_500()

def optie_501():
  print ("""\n  Je loops richting het bos in het donker, Je hebt het koud
  en hebt enorme honger. Wanneer je diep in het bos komt kom je iets tegen.
  Je ziet dat je niet de enige bent die honger hebt. Er is een beer.
  Ga je?\n""")
  time.sleep(1)
  print ("""  A. Terug rennen
  B. Verder het bos in rennen
  C. Proberen te vechten""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_500()
  elif choice in answer_B:
    print("""Je bent de weg kwijt en rende toch the kant op
    Waar je vandaan kwam\n""")
    time.sleep(3)
    optie_500()
  elif choice in answer_C:
    print("""Je rent op de beer af en slaat hem op ze bek.
    Alleen doet het niks en bijt hij je hand eraf.
    Je rent gauw weg maar bloed uit.
    Je bent dood gegaan.\n""")
    time.sleep(3)
    intro()
  else:
    print (required)
    optie_501()

def optie_600():
  print ("""\n  Je loopt weer dagen zonder eten of drinken en valt bijna
  dood van de dorst. Opeens hoor je een auto achter je maar je weet niet
  of je ze kan vertrouwen. Wat doe je?\n""")
  time.sleep(1)
  print ("""  A. Houd ze aan
  B. Verstop je""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_700()
  elif choice in answer_B:
    print("""  Je vertopt je en ze rijden langs zonder te stoppen.
    Je loopt weer verder en komt nogsteeds niks tegen.
    Je valt dood neer\n""")
    time.sleep(3)
    intro()
  else:
    print (required)
    optie_600()

def optie_700():
  print ("""\n  Je houd ze aan en ze stoppen. Je vraagt wat ze hier doen.
  Ze zeggen dat ze naar Europa gaan om de vluchten. Wat een geluk!
  Je vraagt of je mee kan en ze zeggen ja. Ze hebben zelfs voedsel
  voor je! Niks kan meer fout gaan. Je rijdt dagen lang met jouw
  nieuwe vrienden en berijkt Europa. Alleen weet niemand precies
  in welk land je nou bent. Iemand in jouw groep vraagt rond en je
  komt erachter dat je in duitsland bent. Je vrienden vragen of je
  nog verder mee wilt of dat je hier wilt blijven.\n""")
  time.sleep(1)
  print ("""  A. Mee gaan
  B. Blijven""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_800()
  elif choice in answer_B:
    print("Je kiest ervoor om te blijven en je vrienden te verlaten.\n")
    optie_701()
  else:
    print (required)
    optie_700()

def optie_701():
  print ("""\n  Je loopt door een stadje heen.
   Wat ga je nu doen?\n""")
  time.sleep(1)
  print ("""  A. Naar een politiebureau
  B. Verder lopen en zien wat je tegen komt
  C. stelen""")
  choice = input(">>> ")
  if choice in answer_A:
    einde_100()
  elif choice in answer_B:
    print("""Je gaat lopen en staat verbaast te kijken naar hoe het er hier uitziet.
    Mensen die leven in vrede en alle winkels. Je zou hier wel willen wonen.\n""")
    einde_100()
  elif choice in answer_C:
    optie_750()
  else:
    print (required)
    optie_701()

def einde_100():
  print ("""\n  Je gaat naar een politiebureau om te vragen hoe je een
  inwoner kunt worden, je wordt naar een vluchtelingenkamp gebracht
  waar je de komende maanden zal leven. Veilig en met genoeg voedsel
  Eindelijk vrede\n""")
  time.sleep(2)
  print ("Badankt voor het spelen")
  time.sleep(10)
  intro()

def optie_750():
  print ("""\n  Je komt op het goede idee om iets te gaan stelen.
  Maar wat?""")
  time.sleep(1)
  print ("""  A. Geld
  B. Eten
  C. Nieuwe kleding
  D. Toch een slecht idee""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_751()
  elif choice in answer_B:
    optie_752()
  elif choice in answer_C:
    print("""Je ziet een kleding winkel en gaat naar binnen.
    Je kiest een mooi outfitje en rent ermee naar buiten.
    Er rent een beveiliger mega snel achter je aan. hij grijpt je
    En haalt de politie erbij\n""")
    time.sleep(5)
    einde_200()
  elif choice in answer_D:
    optie_701()
  else:
    print (required)
    optie_750()

def optie_751():
  print ("""\n  Je ziet een vrouw met een handtas die er duur uit ziet.
  Je rent snel op haar af en pakt de handtas af. Je rent snel weer weg
  en komt in een steegje uit. Daar ben je goed mee weggekomen.
  Je vindt 30 euro in de tas.
  wat ga je nu doen?\n""")
  time.sleep(1)
  print ("""  A. Eten kopen
  B. Eten stelen
  C. Kleding kopen
  D. Kleding stelen""")
  choice = input(">>> ")
  if choice in answer_A:
    print("""Je vindt een supermarkt en gaat naar binnen.
    Je kiest zoveel voedsel als je kan betalen.
    Maar wanneer je staat af te rekenen komt er politie binnen die je
    arresteren.\n""")
    time.sleep(5)
    einde_200()
  elif choice in answer_B:
    optie_752()
  elif choice in answer_C:
    print("""Je ziet een kleding winkel en gaat naar binnen.
    Je komt erachter dat je niks kunt vinden voor 30 euro.
    Terwijl je nog aan het zoeken bent komt er politie naar binnen
    en die arresteren je.\n""")
    time.sleep(5)
    einde_200()
  elif choice in answer_D:
    einde_200()
  else:
    print (required)
    optie_751()

def optie_752():
  print ("""\n  Je ziet een supermarkt en gaat naar binnen.
  Je merkt dat je in de gaten gehouden wordt.
  Wat ga je stelen?\n""")
  time.sleep(1)
  print ("""  A. Brood
  B. Water
  C. Een koekje""")
  choice = input(">>> ")
  if choice in answer_A:
    print("""Je pakt een stuk brood en rent snel weer naar buiten.
    Je rent snel weg en eet hem op in een park.
    Doordat je je brood eet zie je niet dat er politie aankomt\n""")
    einde_200()
  elif choice in answer_B:
    print("""Je pakt een flesje water en rent snel weer naar buiten.
    Je rent snel weg en eet hem op in een park.
    Je ziet politie aankomen en rent snel weer weg\n""")
    optie_701()
  elif choice in answer_C:
    print("""Je pakt een koekje en rent snel weer naar buiten.
    Je rent snel weg en eet hem op in een park.
    Je ziet politie aankomen en rent snel weer weg\n""")
    optie_701()
  else:
    print (required)
    optie_752()

def einde_200():
  print ("""\n  Je wordt opgepakt en naar de gevangenis gestuurd waar je vast zit
  voor diefstal waar je voor de komende maanden vast zit\n""")
  time.sleep(2)
  print ("Badankt voor het spelen")
  time.sleep(10)
  intro()

def optie_1600():
  print ("""\nJe komt in een dropje terecht aan het water en ziet dat er bijna
  niks van het dorpje over is. Je ziet wat beweging bij het water.
  Er zijn mensen met een boot, en een auto. Je vraagt waar ze naartoe gaan
  Het zijn ook vluchtelingen, ze gaan varen tot ze land tegekomen.
  Je ziet ook nog een auto aankomen, Misshien is dat veiliger.
  Wat doe je?\n""")
  time.sleep(1)
  print ("""  A. Met de boot
  B. Houd de auto tegen
  C. Je vertrouwt het niet en loopt verder""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_1700()
  elif choice in answer_B:
    optie_700()
  elif choice in answer_C:
    optie_600()
  else:
    print (required)
    optie_1600()

def optie_1700():
  print ("""\n  Je klimt in de boot en gaat varen. Er is genoeg eten voor een
  Maand. Dus je moet voorzichtig met het eten zijn. Hoeveel ga je per dag eten?\n""")
  time.sleep(1)
  print ("""  A. minder dan 1 keer per dag
  B. 2 keer per dag
  C. 5 keer per dag""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("""Je eet veel te weinig en sterft uit van de honger.
    Je bent dood gegaan. probeer het opnieuw\n""")
    time.sleep(5)
    intro()
  elif choice in answer_B:
    optie_1800()
  elif choice in answer_C:
    print("""Je eet goed en voelt je veel beter. Het is een pret op die boot
    en je denkt dat er niks meer fout kan gaan. Je droomt al over de toekomst
    Een vrouw, mooi huis, kinderen, een fijn vredig leven in welk land je dan
    ook zult komen..... Alleen kom je er nooit omdat het voedsel op is en je
    Uitsterft van de honger
    Probeer het opnieuw\n""")
    time.sleep(20)
    intro()
  else:
    print (required)
    optie_1700()

def optie_1800():
  print ("""\n  Je hebt je voedsel goed verdeeld en heb zelfs nog wat over
  wanneer je land bereikt. Maar welk land nou precies? Je nieuwe vrienden
  vertellen je dat je in italie bent, en dat ze weer vervoer hebben geregeld.
  Maar je kunt ook in italie blijven.
  Wat doe je?\n""")
  time.sleep(1)
  print ("""  A. Je gaat mee
  B. Je blijft
  C. Je keert terug""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_800()
  elif choice in answer_B:
    optie_701()
  elif choice in answer_C:
    print("""Je vraagt of je terug kan en wordt vaag aangekeken.
    Na een lange stilte wordt je vertelt.... nee\n""")
    time.sleep(3)
    optie_1800()
  else:
    print (required)
    optie_1800()

def optie_800():
  print ("""\n  Je hebt de keuze gemaakt om weer met de auto te gaan.
  Onderweg raakt de benzine op maar hebben geen geld voor nieuwe.
  Er is wel een tankstation verderop.
  Wat ga je doen?\n""")
  time.sleep(1)
  print ("""  A. Benzine stelen
  B. Om benzine vragen
  C. Je vrienden verlaten en lopen""")
  choice = input(">>> ")
  if choice in answer_A:
    print("""Je vult de tank en rijdt hard weg.
    Onderweg hoor je opeens een sirene achter je.
    Het is de politie en je wordt aangehouden.\n""")
    time.sleep(5)
    einde_200()
  elif choice in answer_B:
    print("""Je loopt naar binnen en vraagt om benzine en zegt dat je een
    vluchteling bent. Hij is zelf ook een vluchteling geweest.
    Dus hij wilt je wel helpen en geeft je gratis benzine\n""")
    optie_900()
  elif choice in answer_C:
    print("""Je loopt verder en komt in een stadje terecht\n""")
    time.sleep(1)
    optie_701()
  else:
    print (required)
    optie_800()

def optie_900():
  print ("""\n  Je komt aan in een stad met grachten en veel fietsen
  Je vraagt rond naar waar je bent.
  Nederland, wordt je vertelt. En je wordt gewezen naar een politiebureau voorzicht
  wat je nu zou kunnen doen.
  Wat ga je doen?\n""")
  time.sleep(1)
  print ("""  A. Naar het politiebureau
  B. De stad in
  C. Blijven staan""")
  choice = input(">>> ")
  if choice in answer_A:
    optie_1000()
  elif choice in answer_B:
    optie_701()
  elif choice in answer_C:
    print("""Je komt op het idee om stil te blijven staan omdat je er helemaal
    klaar mee bent dus je gaat maar wachten..""")
    time.sleep(5)
    print("en wachten..")
    time.sleep(5)
    print("en wachten..")
    time.sleep(5)
    print("en wachten..")
    time.sleep(5)
    print("en wachten..")
    time.sleep(5)
    print("en wachten..")
    time.sleep(5)
    print("Je valt in slaap en wordt naar het politiebureau gebracht\n")
    optie_600()
  else:
    print (required)
    optie_900()

def optie_1000():
  print ("""\n  Je komt in het politiebureau en wordt vertelt dat nu al een
  paspoort kunt krijgen en een nederlandse inwoner kunt worden
  Je krijgt een baan, een goedkoop huisje, en heb dan eindelijk
  het ding waarvoor je al die tijd gereisd had.
  Maar, accepteer je het?\n""")
  time.sleep(1)
  print ("""  A. Ja
  B. Nee""")
  choice = input(">>> ")
  if choice in answer_A:
    einde_300()
  elif choice in answer_B:
    einde_400()
  else:
    print (required)
    optie_1000()

def einde_300():
  print ("5")
  time.sleep(1)
  print ("Jaar")
  time.sleep(1)
  print ("Later")
  time.sleep(1)
  print ("""  En je hebt een vrouw met een kind. Je hebt eindelijk het leven
  waarvan je gedroomt hebt. Je heb ook nog contact met je vrienden die je
  tijdens je reis ontmoet had.\n""")
  time.sleep(10)
  print ("Badankt voor het spelen")
  time.sleep(10)
  intro()

def einde_400():
  print ("""  Je zegt nee. Ze kijken verbaasd en leiden je de deur uit.
  Je loopt langs de grachten en denkt aan het avontuur die je beleeft heb.
  Daarna val je in de gracht en verdrink je omdat je niet kunt zwemmen...\n""")
  time.sleep(10)
  print ("Badankt voor het spelen")
  time.sleep(10)
  intro()

intro()
