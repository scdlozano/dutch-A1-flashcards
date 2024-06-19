import random
"""
Flash cards
Other features I would add
[x] menu selection between sentences and translations
WIP: Make an OpenAI integration so that I could make AI-generated sentences 
[] Make a point system
[] Preview the words dictionary for revision
[] Generate list of words that need further revision
"""

words = {
    'nul':'zero',
    'een':'one',
    'twee':'three',
    'vier':'four',
    'vijf':'five',
    'zes':'six',
    'zeven':'seven',
    'acht':'eight',
    'negen':'nine',
    'tien':'ten',
    'elf':'eleven',
    'twaalf':'twelve',
    'dertien':'thirteen',
    'veertien':'fourteen',
    'vijftien':'fifteen',
    'zestien':'sixteen',
    'zeventien':'seventeen',
    'achttien':'eighteen',
    'negentien':'nineteen',
    'twintig':'twenty',
    'eenentwintig':'twenty-one',
    'tweeentwintig':'twenty-two',
    'dertig':'thirty',
    'veertig':'fourty',
    'vijftig':'fifty',
    'zestig':'sixty',
    'zeventig':'seventy',
    'tachtig':'eighty',
    'negentig':'ninety',
    'honderd':'hundred',
    'honderdvierentwintig':'one hundred twenty-four',
    'duizen':'thousand',

    'begroeten':'greetings',
    'goedemorgen':'good morning',
    'goedemiddag':'good afternoon',
    'goedenavond':'good evening',
    'goedendag':'good day',
    'dag':'hello / bye',
    'hoi':'hi/hello',
    'hallo':'hello',
    'doei':'bye',
    'tot zo':'see you soon',
    'tot straks':'see you later',
    'tot morgen':'see you tomorrow',
    'tot ziens':'good bye',

    'welkom (in)':'welcome (to)',
    'goedemorgen':'good morning',
    'allemaal':'all',
    'de cursus':'course',
    'de':'the',
    'Nederlands':'Dutch',
    'ik':'I',
    'zijn':'is',
    'jullie':'your (plural)',
    'de docent':'teacher',
    'jullie':'you (plural)',
    'hebben':'have',
    'twee':'two',
    'hij':'he',
    'lesgeven':'teaches',
    'de dag':'day',
    'drie':'three',
    'we':'we',
    'beginnen':'to begin / start',
    'met':'with',
    'kennismaken':'get to know',
    'wie':'who',
    'wat':'what',
    'de naam':'name',
    'mijn':'my',
    'dag':'day',
    'je / jouw':'your (singular)',
    'de voornaam':'first name',
    'de achternaam':'surname',
    'uit':'from',
    'welke (welk)':'which',
    'het land':'country',
    'Engeland':'England',
    'komen':'to come',
    'de buurman':'neighbour',
    'van':'of',
    'hoe':'how (what)',
    'hoe heet jij?':"what's your name?",
    'heten':'is called (name)',
    'waar vandaan':'where from',
    'waar':'where',
    'China':'China',
    'wonen':'to live',
    'nu':'now',
    'het adres':'address',
    'het nummer':'number',
    'het antwoord':'answer',
    'nee':'no',
    'de postcode':'postal code',
    'u':'you (formal)',
    'mevrouw':'Ms / Mrs',
    'wonen':'to live',
    'ook':'also',
    'in':'in',
    'zeg (zeggen)':'call (say)',
    'maar':'but (just)',
    'ja':'yes',
    'hier':'here',
    'al':'already',
    'twintig':'twenty',
    'het jaar':'year',
    'verdergaan':'go on (continue)',
    'de les':'lesson',
    'iedereen':'everyone',
    'het boek':'book',
    'het':'the',
    'de tekst':'text',
    'een':'one',
    'zitten':'sit',
    'de kantine':'canteen',
    'deze':'this',
    'de plaats':'seat / place',
    'vrije (vrij)':'free',
    'ja hoor':'yes',
    'zo':'okay I right',
    'een':'a(n)',
    'lekker':'nice / delicious',
    'het kopje (de kop)':'cup',
    'de koffie':'coffee',
    'al lang':'for a long time',
    'pas':'only',
    'of':'or',
    'eigenlijk':'actually I really',
    'vandaag':'today',
    'donderdag':'Thursday',
    'augustus':'August',
    'morgen':'tomorrow',
    'ik ben jarig (jarigzijn)':"it's my birthday",
    'wat leuk':'how nice',
    'december':'December',
    'dus':'so / therefore',
    'de winter':'winter',
    'krijgen':'get / receive',
    'nog':'any',
    'het bezoek':'visitor',
    'jonger (jong)':'younger',
    'maar':'but',
    'wel':'certainly',
    'langer (lang)':'taller',
    'nog meer':'any more',
    'nog':'as well',
    'kijken':'to look',
    'de foto':'photo',
    'goh':'Oh',
    'hele (heel)':'very',
    'andere (ander)':'different / other',
    'het type':'type',
    'kort':'short',
    'blond':'blonde',
    'het haar':'hair',
    'donker':'dark',

    'komen op bezoek (op bezoek komen)':'pay a visit',
    'op dit moment':'at the moment',
    'Indonesië':'Indonesia',
    'doen':'to do',
    'daar':'there',
    'op vakantie':'on holiday',
    'de vakantie':'holiday',
    'voor':'for',
    'zijn':'his',
    'het werk':'work',
    'het seizoen':'season',
    'wanneer':'when',
    'de zomer':'summer',
    'weet (weten)':'know',
    'niet':'not',
    'vertellen':'tell',
    'eens':'(usually untranslated)',
    'over':'about',
    'de familie':'family',
    'dat':'that',
    'wil (willen)':'want / would like',
    'laat':'late',
    '11.00 uur':"11 o'clock",
    'moeten':'should / have to',
    'weer':'again',
    'naar':'to',

    #Familierelaties
    'het gezin':'family (immediate)',
    'de ouders':'parents',
    'de vader':'father',
    'de moeder':'mother',
    'de man / de echtgenoot':'husband',
    'de vrouw / de echtgenote':'wife',
    'het kind':'child',
    'de zoon':'son',
    'de dochter':'daughter',
    'de broer':'brother',
    'de zus':'sister',
    'de familie':'family (incl.extended)',
    'de schoonzus':'sister in law',
    'de zwager':'brother in law',
    'de opa':'grandfather',
    'de oma':'grandmother',
    'het kleinkind':'grandchild',
    'de oom':'uncle',
    'de tante':'aunt',
    'de neef':'nephew / cousin',
    'de nicht':'niece / cousin',

    #De dagen van de week
    'eergisteren':'day before yesterday',
    'gisteren':'yesterday',
    'vandaag':'today',
    'morgen':'tomorrow',
    'overmorgen':'day after tomorrow',
    'maandag':'Monday',
    'dinsdag':'Tuesday',
    'woensdag':'Wednesday',
    'donderdag':'Thursday',
    'vrijdag':'Friday',
    'zaterdag':'Saturday',
    'zondag':'Sunday',

    # Maanden
    'de maand':'month',
    'januari':'January',
    'februari':'February',
    'maart':'March',
    'april':'April',
    'mei':'May',
    'juni':'June',
    'juli':'July',
    'augustus':'August',
    'september':'September',
    'oktober':'October',
    'november':'November',
    'december':'December',

    #De seizoenen
    'de winter':'winter',
    'de lente / het voorjaar':'spring',
    'de zomer':'summer',
    'de herfst / het najaar':'fall',

    #In het cafe
    'vieren':'to celebrate',
    'de verjaardag':'birthday',
    'het café':'café / pub',
    'samen':'together',
    'gefeliciteerd':'happy birthday',
    'dankje wel':'thank you',
    'dit is':'this is',
    'prettig met je kennis te maken':'pleased to meet you',
    'kennen':'know (people)',
    'elkaar':'one another',
    'drinken':'drink',
    'ik trakteer (trakteren)':"it's my treat",
    'graagwillen':'would like',
    'de cola':'cola',
    'biertje (het bier)':'beer',
    'nemen':'have (take)',
    'rode (rood)':'red',
    'de wijn':'wine',
    'roepen':'to call (a waiter)',
    'de Ober':'waiter',
    'mogen':'may',
    'bestellen':'order',
    'alstublieft':'please',
    'Franse (Frans)':'French',
    'Spaanse (Spaans)':'Spanish',
    'Zuid-Afrikaanse (Zuid-Afrikaans)':'South African',
    'de':'the',
    'nou':'well then',
    'proost':'cheers',
    'op je verjaardag':'happy birthday',
    'bedankt':'thanks',
    'het poosje':'short while',
    'later (laat)':'later',
    'zullen (zullen)':'shall',
    'nog een keer':'once more',
    'dat is':'that is',
    'goede (goed)':'good',
    'het idee':'idea',
    'hetzelfde':'the same',
    'ja, graag':'yes please',
    'dit':'this',
    'het rondje':'round',
    'betaal (betalen)':'pay',
    'geven':'give',
    'nog maar':'another',
    'het glas':'glass',
    'afrekenen':'pay / settle the bill',
    'alfes':'everything',
    'daarom':"that's why",

    #Rangtelwoorden
    'eerste':'first',
    'tweede':'second',
    'eerste':'first',
    'tweede':'second',
    'derde':'third',
    'vierde':'fourth',
    'vijfde':'fifth',
    'zesde':'sixth',
    'zevende':'seventh',
    'achtste':'eighth',
    'negende':'ninth',
    'tiende':'tenth',
    'elfde':'eleventh',
    'twaalfde':'twelvth',
    'dertiende':'thirteenth',
    'veertiende':'fourteenth',
    'vijftiende':'fifteenth',
    'zestiende':'sixteenth',
    'zeventiende':'seventeenth',
    'achttiende':'eighteenth',
    'negentiende':'nineteenth',
    'twintigste':'twenteeth',
    'eenentwintigste':'twenty-first',
    'honderdste':'hundredth',

    #Op de straat
    'de straat':'street',
    'de vriend':'friend',
    'tegenkomen':'meets',
    'hé':'hey',
    'geleden':'ago',
    'leuk':'nice',
    'prima':'wonderful',
    'het gaat wel':'all right',
    'het probleem':'problem',
    'de buurman':'neighbour',
    'de buuren':'neighbours',
    'niet zo':'not so',
    'belangrijke (belangrijk)':'important',
    'gaan':'go',
    'de week':'week',
    'een paar dagen':'a few days',
    'Venetië':'Venice',
    'wauw':'wow',
    'prachtige (prachtig)':'fine / splendid',
    'vele (veel)':'a lot',
    "foto's maken":'take photos',
    'sinds':'since',
    'nieuw':'new',
    'de camera':'camera',
    'romantische (romantisch)':'romantic',
    'de film':'film',
    'na':'after',
    'kijken naar':'to look at',
    'direct':'right now',
    'iets':'something',
    'afspreken':'set a date / make an appointment',
    'goed':'okay',
    'thuis':'at home',
    'de afspraak':'date / appointments',
    'maken':'to make',
    'de datum':'date / appointments',
    'dat lukt niet':"that doesn't work",
    'lukken':'to succeed',
    'dan':'then',
    'kunnen':'be able to',
    'blijven':'to stay',
    'eten':'to eat',
    'zullen':'will / shall',
    'de spaghetti':'spaghetti',
    'carbonara':'carbonara',
    'het plan':'plan',
    'schrijven':'to write',
    'de agenda':'diary',
    'hartstikke':'very / completely',
    'hartstikke leuk':'terrific / fantastic',
    'vind ik ook':'I think so too',
    'vinden':'to find',
    'ik moet ervandoor':'I have to go',
    'ervandoor':'away / off',
    'gauw':'quickly',
    'de winkel':'shop',
    'wensen':'to wish',
    'jullie':'you',
    'fijne (fijn)':'nice / good',
    'doe de groeten aan (de groeten doen aan)':'give my regards to',
    'volgende':'next',
    'tot dan':'until then',

    #Op de maarkt
    'boodschappen doen':'go shopping',
    'de markt':'market',
    'de groenteboer':'greengrocer',
    'er':'there',
    'wie is er aan de beurt':"who's next",
    'de beurt':'turn',
    'alsjeblieft':'please',
    'kleine (klein)':'small',
    'gele (gele)':'yellow',
    'mooie (mooi)':'nice',
    'altijd':'always',
    'sorry':'sorry',
    '(na)tuurlijk':'of course',
    'anders nog iets':'anything else',
    'typische (typisch)':'typical',
    'het gerecht':'dish',
    'de buitenlander':'foreigner',
    'de stamppot':'mashed potato and veggies',
    'spekjes (het spekje)':'bacon',
    'vaak':'often',
    'heerlijk':'delicious',
    'goedkope (goedkoop)':'cheap',
    'hoeveel':'how much',
    'nodig hebben':'need',
    'de persoon':'person',
    'ongeveer':'about',
    'halve (half)':'half',
    'de kilo':'kilo',
    'aardappels (de aardappel)':'potatoes',
    'de slager':'butcher',
    'het bakje (de bak)':'punnet',
    'het bosje (de bos)':'bunch',
    'verder nog iets?':'anything else',
    'verse (vers)':'fresh',
    'de euro':'euro',
    'wel':'quite',
    'genoeg':'enough',
    'waarnaartoe':'where to',
    'de cent':'cent',
    'erbij':'with it',
    'geeft niet':"doesn't matter",
    'prettige (prettig)':'nice',
    'het weekend':'weekend',

    #Groente
    'de courgette':'courgette',
    'de aubergine':'eggplant',
    'de paprika':'bell pepper',
    'de tomaat':'tomato',
    'de andijvie':'endive',
    'de aardappel':'potato',
    'de bloemkool':'cauliflower',
    'de champignon':'mushroom',
    'de peterselie':'parsley',
    'het boontje':'bean',
    'de sperzieboon':'green bean',
    'de knoflook':'garlic',
    'de komkommer':'cucumber',
    'de sla':'lettuce',
    'de broccoli':'broccoli',
    'de kool':'cabbage',
    'de witte kool':'white cabbage',
    'de rode kool':'red cabbage',
    'de boerenkool':'curly kale',
    'de zuurkool':'sauerkraut',
    'de ui':'onion',
    'de wortel':'carrot',

    #Vruchten
    'de aardbei':'strawberry',
    'de druif':'grape',
    'de perzik':'peach',
    'de pruim':'plum',
    'de kers':'cherry',
    'de appel':'apple',
    'de peer':'pear',
    'de sinaasappel':'orange',
    'de mandarijn':'mandarin',
    'de kiwi':'kiwi fruit',
    'de banaan':'banana',
    
    #In het restaurant
    'de vriendin':'girlfriend',
    'het restaurant':'restaurant',
    'de serveerster':'waitress',
    'de tafel':'table',
    'ons':'us',
    'bij':'at',
    'gaan zitten':'sit down',
    'de menukaart':'menu',
    'alvast':'in the meantime',
    'te':'to',
    'het mineraalwater':'mineral water',
    'ik heb dorst':"I'm thirsty",
    'de dorst':'thirst',
    'mij':'me',
    'alleen':'only / just',
    'het hoofdgerecht':'main course',
    'ik heb honger':"I'm hungry",
    'de honger':'hunger',
    'het voorgerecht':'starter',
    'misschien':'perhaps',
    'het nagerecht':'dessert',
    'de mosterdsoep':'mustard soup',
    'de mosterd':'mustard',
    'de soep':'soup',
    'erg':'very',
    'als':'as',
    'de biefstuk':'steak',
    'het frietje':'chip',
    'de frietjes':'chips',
    'eh':'um',
    'de salade':'salad',
    'de kip':'chicken',
    'de rijst':'rice',
    'o nee':'Oh no',
    'geen':'no',
    'het vlees':'meat',
    'toch':'after all',
    'vegetarische (vegetarisch)':'vegetarian',
    'de dagschotel':"today's special",
    'kiezen':'choose',
    'eet smakelijk':'bon appetit',
    'het mes':'knife',
    'de vork':'fork',
    'momentje (het moment)':'one moment',
    'de lepel':'spoon',
    'halen':'fetch',
    'beetje':'a little',
    'moeilijk':'difficult',
    'het gaat wel':"it's okay",
    'de soort':'kind',
    'de paella':'paella',
    'houden van':'to love',
    'de mosselen':'mussels',
    'proef (proeven)':'try',
    'wat':'a little, a bit',
    'een beetje':'a bit',
    'vet':'greasy / rich',
    'het toetje':'dessert',
    'het ijs':'ice cream',
    'de vrucht':'fruit',
    'de chocola':'chocolate',
    'de slagroom':'whipped cream',
    'zonder':'without',
    'alleen':'only',
    'de cappucino':'cappucino',
    'laat de rest maar zitten':'keep the change',
    'laten':'to leave',
    'dank u':'thank you',
    'de avond':'evening',

    #In de kledingzaak
    'normaal':'normally',
    'soms':'sometimes',
    'grote (groot)':'large',
    'de kleur':'color',
    'wat voor':'what kind of',
    'het model':'style',
    'lichte (licht)':'light (adj)',
    'lage (laag)':'low',
    'verschillende (verschillend)':'different',
    'het merk':'brand',
    'proberen':'to try on',
    'allebei':'both',
    'ergens':'somewhere',
    'passen':'to try on',
    'de paskamer':'changing room',
    'zitten':'fits (size)',
    'wijde (wijd)':'wide',
    'kleine (klein)':'small',
    'het spijt me':"I'm sorry",
    'kleinste':'smallest',
    'eventueel':'if necessary',
    'ruilen':'to return / exchange',
    'binnen':'within',
    'de bon':'receipt',
    'het T-shirt':'t-shirt',
    'liggen':'to lay',
    'allerlei':'all kinds of',
    'beslissen':'to decide',
    'staan het best':'suits the best',
    'het best':'the best',
    'pinnen':'pay by card',

    #Kleuren
    'witte (wit)':'white',
    'zwarte (zwart)':'black',
    'grijze (grijs)':'gray',
    'rode (rood)':'red',
    'blauwe (blauw)':'blue',
    'gele (geel)':'yellow',
    'groene (groen)':'green',
    'bruine (bruin)':'brown',
    'paarse (paars)':'purple',
    'roze':'pink',
    'oranje':'orange',
    'donkerblauw':'dark blue',
    'donkerbruin':'dark brown',
    'lichtgeel':'light yellow',
    'lichtgroen':'light green',
    'effen':'solid',
    'geruit':'checkered',
    'gebloemd':'floral',
    'gestreept':'striped',

    #Kleding
    'de broek':'trousers',
    'de spijkerbroek':'denim jeans',
    'de trui':'sweater',
    'de bloes':'blouse',
    'het overhemd':'shirt',
    'de rok':'skirt',
    'de jurk':'dress',
    'de jas':'de coat',
    'de schoenen':'shoes',
    'het pak':'suit',

    #Bij de makelaar
    "laten zien":"show", 
    "de computer":"computer",
    "derde":"third",
    "de verdieping":"floor/storey",
    "oude (oud)":"old",
    "de buurt":"neighborhood",
    "ver":"far",
    "het centrum":"city center",
    "dicht bij":"close to",
    "het park":"park",
    "de woonkamer":"living room",
    "de vierkante meter":"square meter",
    "vierkante (vierkant)":"square (adj.)",
    "de meter":"meter",
    "open":"open",
    "de keuken":"kitchen",
    "ruime (ruim)":"spacious",
    "het balkon":"balcony",
    "het westen":"west",
    "de gang":"passage(way)",
    "de wc":"toilet",
    "eenvoudige (eenvoudig)":"simple",
    "de badkamer":"bathroom",
    "de douche":"shower",
    "hoeven":"need",
    "het bad":"bath",
    "gebruiken":"use",
    "geschikte (geschikt)":"suitable",
    "huizen (het huis)":"houses",
    "want":"because",
    "te huur":"to let",
    "huren":"to rent",
    "het huisje (het huis)":"house",
    "verhuren":"to let out",
    "gemeubileerd":"furnished",
    "het bed":"bed",
    "de stoel":"chair",
    "het bureau":"desk",
    "de bank":"sofa/couch",
    "het voordeel":"advantage",
    "niets":"nothing",
    "zonnige (zonnig)":"sunny",
    "de kamer":"room",
    "benedewoning":"ground-floor flat",
    "dat lijkt me fantastisch":"that sounds great",
    "waar":"true",
    "overleggen":"discuss",
    "bel (bellen)":"call",
    "zo snel mogelijk":"as soon as possible",
    "nieuwe (nieuw)":"new",
    "een bepaald type woning":"a particular type of house",
    "de woning":"accomodation",
    "het huis":"house",
    "de flat":"flat",
    "het appartement":"appartment",
    "de bovenwoning":"upstairs flat",
    "de benedenwoning":"ground-floor flat",
    "in en bij het huis":"in and around the house",
    "de keuken":"kitchen",
    "ruime (ruim)":"spacious",
    "de slaapkamer":"bedroom",
    "het balkon":"balcony",
    "het westen":"west",
    "de gang":"passage(way)",
    "de wc":"toilet",
    "eenvoudige (eenvoudig)":"simple",
    "de badkamer":"bathroom",
    "de douche":"shower",
    "hoeven":"need",
    "het bad":"bath",
    "de deur":"door",
    "de tuin":"garden",
    "het schuurtje":"small shed",
    "de garage":"garage",
    "het raam":"window",
    "de tafel":"table",
    "het bed":"bed",
    "de kast":"cupboard",

    #H9 in the huisarts
    "meneer" : "Mr",
    "de doktor":"doctor / gp",
    "wat is er aan de hand?":"what is wrong?",
    "zoal":"as",
    "zit ik onder de bultjes":"I have a rash / lumps",
    "de bultjes (de bult)":"lumps",
    "de arm":"arm",
    "het been":"leg",
    "de buik":"stomach",
    "de rug":"back",
    "het gezicht":"face",
    "jeuken":"itch",
    "verschrikkelijke (verschrikkelijke)":"terrible",
    "van alles":"of everything",
    "helpen":"to help",
    "overdag":"during the day",
    "de voetbalverniging":"football club",
    "het wedstrijdje":"match (dim.)",
    "de wedstrijde":"match",
    "daarna":"after",
    "bijzonders (bijzonder)":"special",
    "afgelopen":"past / last few",
    "vergeten":"to forget",
    "denken":"to think",
    "o ja":"oh yes",
    "rijpe (rijp)":"ripe",
    "de emmer":"bucket",
    "volle (vol)":"full",
    "vorige (vorig)":"previous",
    "de klacht":"complaint",
    "lijken op":"looks like",
    "allergische (allergisch)":"allergic",
    "geeft me (mee geven)":"give me",
    "de zalf":"ointment",
    "tegen":"against",
    "anders":"otherwise",
    "krabben":"scratch",
    "kapot":"open (e.g wound)",
    "sterkte":"good luck",

    #Lichaamsdelen
    "het hoofd":"head",
    "de nek":"neck",
    "de buik":"stomach",
    "de rug":"back",
    "de arm":"arm",
    "de schouder":"shoulder",
    "de hand":"hand",
    "de vinger":"finger",

    "de knie":"knee",
    "de enkel":"ankle",
    "de voet":"foot",

    "de mond":"mouth",
    "het oog":"eye",
    "de neus":"nose",
    "het oor":"ear",

    #Dagdelen
    "gisterochtend / gistermorgen":"yesterday morning (6-12)",
    "de morgen":"morning",
    "vanochtend / vanmorgen":"today morning (6-12)",
    "morgenochtend":"tomorrow morning (6-12)",
    "'s ochtends / 's morgens":"each morning",

    "gistermiddag":"yesterday afternoon (12-18)",
    "de middag":" afternoon",
    "vanmiddag":"today afternoon (12-18)",
    "morgenmiddag":"tomorrow afternoon (12-18)",
    "'s middags":"each afternoon",

    "gisteravond":"yesterday evening (18-24)",
    "de avond":" evening",
    "vanavond":"today evening (18-24)",
    "morgenavond":"tomorrow evening (18-24)",
    "'s avonds":"each evening",

    "gisternacht":"yesterday night (0-6)",
    "de nacht":" evening",
    "vannacht":"today evening (0-6)",
    "morgennacht":"tomorrow evening (0-6)",
    "'s nachts":"each night",
}

def main():
    print("Welkom bij Flashcards!")
    new_word = input_new_word()
    while new_word == "j":
        random_key = pick_word()
        print_dutch_word(random_key)
        NL_response = input_NL_response()
        test_NL_response(random_key, NL_response)
        input_new_word()

def input_new_word():
    new_word = input("(Her)starten? (j/n)")
    if new_word == "j":
       return new_word
    else:
      print("Dankje wel voor gebruiken!")
      quit()  

#Selects a random key
def pick_word():
    random_key = random.choice(list(words.keys()))
    return random_key

#Accesses the corresponding value for the selected random_key
def print_dutch_word(random_key):
    print(words[random_key])

#Asks for the NL response
def input_NL_response():
    NL_response = input("NL: ")
    return NL_response

#Checks correctness of NL response with the corresponding key
def test_NL_response(random_key, NL_response):
    if NL_response == random_key:
        print("Goed!")
    else:
        print(f"Fout! De juiste antwoord is: {random_key}")
        NL_response_retest = input("Opnieuw: ")
        if NL_response_retest == random_key:
            print("Goed!")
        else:
            print("Nee! Probeer het nog eens!")
            while NL_response_retest != random_key:
                print("Fout!")
                NL_response_retest = input("Opnieuw: ")
                if NL_response_retest == random_key:
                    print("Goed!")
                    break

if __name__ == '__main__':
    main()