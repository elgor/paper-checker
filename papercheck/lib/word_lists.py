lstVague = (
    "a large number",
    "a lot",
    "almost",
    "few",
    "many",
    "most",
    "numerous",
    "some",
    "sometimes",
    "really",
    "several",
    "often",
    "very",
    "quite",
)


lstShouts = (
    "ah",
    "aha",
    "alas",
    "aw",
    "ay",
    "bah",
    "eh",
    "hurray",
    "oh",
    "oho",
    "oh-oh",
    "ooh",
    "oops",
    "ow",
    "oy",
    "phew",
    "ugh",
    "uh",
    "woah",
    "wow",
    "yay",
    "yow",
)


lstAcronyms = [
    "AC",
    "ACM",
    "CPU",
    "DDR",
    "FPGA",
    "FSM",
    "GNU",
    "GPS",
    "GUI",
    "HF",
    "HTML",
    "IEEE",
    "LED",
    "OS",
    "PC",
    "PCB",
    "PDF",
    "USB",
    "RAM",
    "RF",
    "ROM",
    "VR",
    "URL",
    "WIFI",
]


tabShortForms = [
    (r"(it[’']s)", "is not"),
    (r"\w+(n[’']t)", "not"),
    (r"\w+([’']re)", "are"),
    (r"\w+([’']ve)", "have"),
    (r"\w+([’']ll)", "will"),
]


tabNumbers = [
    ("0", "zero"),
    ("1", "one"),
    ("2", "two"),
    ("3", "three"),
    ("4", "four"),
    ("5", "five"),
    ("6", "six"),
    ("7", "seven"),
    ("8", "eight"),
    ("9", "nine"),
    ("10", "ten"),
    ("11", "eleven"),
    ("12", "twelve"),
]


tabRedundantPhrases = [
    ("all of the", "all"),
    ("all the", "all"),
    ("all in all", "overall"),
    ("approximately about", "about"),
    ("[Aa]t the moment", "currently"),
    ("[Aa]s a matter of fact", "in fact"),
    ("and so on", "etc."),
    ("ATM machines?", "ATM"),
    ("by means of", "by"),
    ("but however", "however"),
    ("but nevertheless", "nevertheless"),
    ("close proximity", "proximity"),
    ("combined together", "combined"),
    ("despite of", "despite"),
    ("despite the fact that", "although"),
    ("DNS servers?", "DNS"),
    ("due to the fact that", "because"),
    ("end result", "result"),
    ("(?:exact same|exactly the same)", "same"),
    ("[Ff]or the most part", "for most"),
    ("[Ff]or the purpose of", "to"),
    ("First of all", "First"),
    ("(?:have|has) the ability to", "can"),
    ("HIV virus", "HIV"),
    ("[Ii]n the case that", "in case"),
    ("[Ii]n terms of", "regarding"),
    ("in order to", "to"),
    ("[Ii]t is apparent", ""),
    ("[Ii]t is clear", ""),
    ("[Ii]t seems that", ""),
    ("[Ii]t can be seen that", ""),
    ("[Ii]n the process of", "while"),
    ("to such an extent", "insofar"),
    ("irregardless", "regardless"),
    ("LCD displays?", "LCD"),
    ("malicious attacks?", "attack"),
    ("more and more", "more"),
    ("not able", "unable"),
    ("not certain", "uncertain"),
    ("not many", "few"),
    ("not the same", "different"),
    ("(?:make|made) a decision about", "decide on"),
    ("[Oo]n the occasion of", "when"),
    ("[Oo]n the (?:one|other) hand", ""),
    ("of any of", "of"),
    ("originally discovered", "discovered"),
    ("over the time", "over time"),
    ("period (?:of|in) time", "period"),
    ("PIN number", "PIN"),
    ("reason why", "reason"),
    ("so therefore", "therefore"),
    ("(?:sufficient|adequate) enough", "sufficient"),
    ("that exists", ""),
    ("(?:a|the) type of", ""),
    ("USB bus", "USB"),
    ("whether or not", "whether"),
]


tabWrongCombinations = [
    ("could of", "could have"),
    ("de-factor", "de-facto"),
    ("last change", "last chance"),
    (r"(?:have|has|had) (?:the|a|no) change", "chance"),
    (r"(?:should|will) bee", "been"),
    ("insure that", "ensure that"),
    ("must to", "must"),
    ("to for", "for"),
    ("to here", "to hear"),
    ("in principal", "in principle"),
    ("network package", "network packet"),
    ("object orientated", "object oriented"),
    ("time point", "point in time"),
    ("software packet", "software package"),
    ("thread model", "threat model"),
    ("(?:some|certain) extend", "extent"),
    (r"resource[- ]constraint", "resource-constrained"),
]


tabConfusedVerbNoun = [
    ("affect", "effect"),
    ("ascend", "ascent"),
    ("build", "built"),
    ("constrain", "constraint"),
    ("descend", "descent"),
    ("extend", "extent"),
    ("grand", "grant"),
    ("reverse", "inverse"),
    ("live", "life"),
    ("practice", "practise"),
    ("prove", "proof"),
    ("set up", "setup"),
    ("save", "safe"),
    ("shut down", "shutdown"),
]


# ToDo: add false friends + explanation for words that are equally likely
tabFalseFriends = [
    (
        "ascend|ascent|assent",
        "ascend (V): increase height\nascent (N): process of increasing height\n assent (N): expression of approval",
    ),
    (
        "build|built",
        "build (V/N): to construct, software build\nbuilt (V): past of build",
    ),
    (
        "complaint|compliant",
        "complaint (N): dissatisfaction\ncompliant (J): in line with rules",
    ),
    (
        "historic|historical",
        "historical: refers exclusively to things that happened in the past.\nhistoric: can happen now but will have a profound impact on history",
    ),
    (
        "tenets|tenants",
        "tenets: guiding principles or beliefs.\ntenants: people who rent from you.",
    ),
    (
        "bowls?|bowels?",
        "bowl: round container for food.\nbowel: carries waste from the stomach.",
    ),
    (
        "affects?|effects?",
        "affect (verb): something gets changed.\neffect (noun): the change that is the result of an action.",
    ),
    (
        "principals?|principles?",
        "principal: first in order of importance.\nprinciple: foundation of beliefs.",
    ),
    ("lose|loose", "lose (V): cease to have.\nloose (Adj): not tight."),
    (
        "(?:assure|ensure|insure)(?:s|ed)?",
        "assure: to promise to someone\nensure: to make sure\ninsure: protect from damage costs",
    ),
    # PRECEDE-to come before PROCEED-to go forward
    # https://www.lexico.com/grammar/commonly-confused-words
]


tabSynonyms = [
    ("show", "illustrate", "demonstrate"),
    ("calculate", "determine"),
    ("analyze", "evaluate", "investigate"),
    ("precise", "concise"),
]


tabLatinPlural = [
    ("maximums", "maxima"),
    ("minimums", "minima"),
    ("indexes", "indices"),
    ("matrixes", "matrices"),
    ("formulas", "formulae"),
    ("radius", "radii"),
    ("focuses", "foci"),
]

tabBritishAmerican = [
    ("aeroplane", "airplane"),
    ("aluminium", "aluminum"),
    ("analyse", "analyze"),
    ("analogue", "analog"),
    ("catalogue", "catalog"),
    ("defence", "defense"),
    ("licence", "license"),
    ("centre", "center"),
    ("fibre", "fiber"),
    ("behaviour", "behavior"),
    ("neighbour", "neighbor"),
    ("colour", "color"),
    ("flavour", "flavor"),
    ("signalling", "signaling"),
    ("whilst", "while"),
    # (r'\w\wl')
]


## Non Scientific / Informal
## ===================================================


# maybe in medical/biology context
tabNonTechnicalWords = [("bee", "be")]

tabNonScientificVerbs = [
    ("adept", "adapt"),
    ("adopt", "adapt"),
    ("compere", "compare"),
    ("exorcise", "exercise"),
    ("defuse", "diffuse"),
    ("fray", ""),
    ("moan", "sign"),
    ("sing", "sign"),
    ("snag", ""),
]

tabNonScientificWords = [
    ("altars?", "alter"),
    ("airs", "air"),
    ("angels?", "angle"),
    ("ass", "as"),
    ("avid", "avoid"),
    ("awl", "all"),
    ("bale", "able"),
    ("ballets?", "ballot"),
    ("bellow", "below"),
    ("bites?", "byte"),
    ("bloc", "block"),
    ("blocs", "blocks"),
    ("butt", "but"),
    ("botch", "both"),
    ("bloody", "blood"),
    ("boar", "board"),
    ("bough", "bought"),
    ("breach", "breech"),
    ("breaches", "breeches"),
    ("bye", "by"),
    ("cam", "can, camera"),
    ("cant", "cannot"),
    ("cashed", "cached"),
    ("canvass", "canvas"),
    ("cheek", "check"),
    ("coarse", "course"),
    ("curse", "course"),
    ("compliments?", "complement"),
    ("collars?", "caller"),
    ("corrals?", "coral"),
    ("cor", "core"),
    ("contend", "content"),
    ("cousin", "cosine"),
    ("curry", "carry"),
    ("currant", "current"),
    ("curries", "carries"),
    ("curtain", "certain"),
    ("fir", "for"),
    ("feces?", "fence"),
    ("fur", "for"),
    ("foe", "for"),
    ("fife", "five"),
    ("fist", "first"),
    ("Fist,", "first"),
    ("fuck", ""),
    ("damn", "dam"),
    ("discreet", "discrete"),
    ("desert", ""),
    ("dessert", ""),
    ("dome", "done"),
    ("duel", "dual"),
    ("goof", "good"),
    ("ether", "either"),
    ("ere", "here"),
    ("hail", "hall"),
    ("heir", "here"),
    ("hew", "he"),
    ("hight", "height"),
    ("hog", "hot"),
    ("hut", "hot"),
    ("jest", "just"),
    ("juts", "just"),
    ("jib", "job"),
    ("junk", ""),
    ("kelp", "help"),
    ("ken", "keen"),
    ("kid", "kit"),
    ("kidding", "kitting"),
    ("knot", "not"),
    ("knights?", "night"),
    ("loch", "lock"),
    ("lodes?", "load"),
    ("lark", "lack"),
    ("lawn", "law"),
    ("lees?", "less"),
    ("lest", "least"),
    ("litter", "little"),
    ("lusts?", "list"),
    ("maize", "maze"),
    ("marital", "material"),
    ("massages?", "message"),
    ("mayor", "major"),
    ("merry", "marry"),
    ("milks?", "mill"),
    ("minuets?", "minute"),
    ("mist", "must"),
    ("moans?", "mean"),
    ("mowed", "mode"),
    ("mob", "mod"),
    ("mom", "non"),
    ("mow", "now"),
    ("muck", "much"),
    ("mum", "min"),
    ("nit", "not"),
    ("nun", "non"),
    ("ore", "or"),
    ("oar", "or"),
    ("palate", "palette"),
    ("par", "part"),
    ("pie", "pi"),
    ("peaces?", "piece"),  # evil entry
    ("peeks?", "peak"),
    ("planing", "planning"),
    ("poop", "pop"),
    ("pope", "pop"),
    ("prostrate", "prostate"),
    ("ploy", "play"),
    ("precious", "precise"),
    ("principal", "principle"),
    ("pubic", "public"),
    ("puns?", "pin"),
    ("rants?", "rent"),
    ("realty", "reality"),
    ("revenge", "revenue"),
    ("rime", "time"),
    ("rite", "write"),
    ("rise", "raise"),
    ("routs?", "route"),
    ("sad", "said"),
    ("sadden", "sudden"),
    ("saga", "stage"),
    ("sage", "stage"),
    ("sake", "sale"),
    ("sate", "state"),
    ("scum", "scam"),
    ("seams", "seems"),
    ("sew", "see"),
    ("shed", "she"),
    ("shit", "shift"),
    ("sheikh", "shake"),
    ("sleight", "slight"),
    ("slut", "slot"),
    ("sic", "six"),
    ("sigh", "sight"),
    ("sire", "sure"),
    ("smug", ""),
    ("snug", ""),
    ("sod", "rod"),
    ("sow", "show"),
    ("sown", "shown"),
    ("spout", "spot"),
    ("stale", "stake"),
    ("stationery", "stationary"),
    ("steal", "steel"),
    ("steak", "stake"),
    ("stiles?", "style"),
    ("sties", "sites"),
    ("streight", "straight"),
    ("strait", "straight"),
    ("sty", "stay"),
    ("stying", "staying"),
    ("sword", "word"),
    ("temper", "tamper"),
    ("testes", "tests"),
    ("theses", "these"),
    ("thy", "why"),
    ("treaty", "treat"),
    ("trinity", "triple"),
    ("toad", "to"),
    ("tome", "tone"),
    ("vat", "vast"),
    ("vet", ""),
    ("vicious", "viscous"),
    ("vicar", "vice"),
    ("vile", "file"),
    # ("valve", "value"),
    ("wade", "ware"),
    ("wand", "want"),
    ("wee", "we"),
    ("wend", "went"),
    ("wax", "way"),
    ("woks?", "work"),
    ("widow", "window"),
    ("witch", "which"),
    ("wildly", "widely"),
    ("withing", "within"),
    ("wit", "with"),
    ("wive", "wife"),
    ("whore", "wore"),
    ("wont", "will not! 'wont' means 'habit'"),
    ("wren", "when"),
    ("wring", "wrong"),
    ("writ", "write"),
    ("wright", "right"),
    ("ye", "you"),
]


tabInformalWords = [
    ("Also,?", "Furthermore,"),
    ("[Aa]nyways?", "nevertheless"),
    ("a couple of", "several"),
    ("and so on", "etc."),
    ("a bit", "slightly"),
    ("a little bit", "slightly"),
    # ('about '+reNum, 'approximately'),
    ("all right", "acceptable"),
    ("bad", "negative"),
    ("big", "major"),
    ("do away", "remove"),
    ("bug", "fault"),
    ("buyer", "purchaser"),
    ("to know (?:an?|the|this)", "obtain"),
    ("But,?", "However,"),
    ("cheap", "inexpensive"),
    ("classical", "conventional"),
    ("cool", "great"),
    ("cute", "great"),
    ("deal with", "manage"),
    ("decent", "proper"),
    ("easy", "simple"),
    ("enough", "sufficient"),
    ("fat", "heavy"),
    ("good", "positive"),
    ("kinds", "types"),
    ("kind of", "rather"),
    ("like(?! to)", "such as"),
    ("looks", "appears"),
    ("sort of", "rather"),
    ("heaps of", "many"),
    ("huge", "large"),
    ("mess", "chaos"),
    ("nice", "attractive"),
    # ("normal", "general"),  # conventional
    ("places?", "location"),
    ("pity", ""),
    ("plenty", "many"),
    ("pretty", "rather"),
    # ("rotations", "evolutions"),
    ("rough(?:ly)?", "approximately"),
    ("so", "Therefore,"),
    ("something", "?"),
    # ("speed", "velocity"),
    ("silly", "inappropriate"),
    ("stuff", "things"),
    ("stupid", "inappropriate"),
    # ('then', 'subsequently'),
    ("things?", "object"),
    ("though", "although"),
    ("tough", "difficult"),
    ("thou", "you"),
    ("thee", "you"),
    ("thine", "your"),
    ("trendy", "modern"),
    ("trifle", "nuance"),
    ("trusty", "trustworthy"),
    ("untrue", "false"),
    ("wonderful", "great"),
    ("weird", "strange"),
    ("quite", "rather"),
    ("vain", "useless"),
    ("whole", "entire"),
    ("whim", "madness"),
    ("wholly", "entirely"),
    # ('wrong', 'incorrect'),
    ("Well,?", ""),
    ("[Yy]ou", "one"),
    ("[Yy]our", "one's"),
]


################################################################################################


tabInformalVerbs = [
    ("admire[sd]?", ""),
    ("amuse[sd]?", ""),
    ("annoy(?:s|ed|ing)?", "unpleasant"),
    # ("ask", "request"),
    # ("asked", "requested"),
    ("bake", ""),
    ("bang", ""),
    ("blush", ""),
    ("buy", "purchase"),
    ("bought", "purchased"),
    ("comes? back", "return"),
    ("check", "test"),
    ("cut down", "reduce"),
    ("dare", ""),
    ("(?:get|got) rid of", "eliminate"),
    # ("got", "obtain"),
    ("go", ""),
    ("give", "provide"),
    ("guess", "estimate"),
    ("happen(?:s|ed|ing)?", "occur"),
    ("help(?:s|ed|ing)? out", "assist"),
    ("keep", "preserve"),
    # ("let us", "permit"),
    ("look(?:s|ed|ing)? into", "investigate"),
    ("look(?:s|ed|ing)? like", "appears similar to"),
    # ('make', 'render'),
    ("mess", ""),
    ("open(?:s|ed|ing)? up", "enable"),
    ("pick(?:s|ed|ing)? up ", "collect"),
    ("put", ""),
    ("put(?:s|ting)? together", "assembled"),
    ("points? out", "indicate"),
    ("reckon", "think"),
    # ("see", "observe"),
    ("seems?", "appear"),
    ("seemed", "appeared"),
    ("speed(?:s|ed|ing)? up", "accelerate"),
    ("stay(?:s|ed|ing)?", "remain"),
    ("think(?:s|ing)? about", "consider"),
    ("(?:takes|took|taken)? apart", "disassemble"),
    ("take a (?:closer )?look", "investigate"),
    ("take(?:s|ing)? place", "occurs"),
    ("talk(?:ed|ing)? about", "consider"),
    ("wipe(?:s|d)? out", "eliminate"),
    ("[Ww]e got", "we obtain"),
    # give it a go, we will not "go into"
    # on the go, on the fly
    # It is out of discussion
]


informalVerbs = [
    "back",
    "bathe",
    "bare",
    "beg",
    "bless",
    "blot",
    "boast",
    "bore",
    "bruise",
    "bubble",
    "cheer",
    "chew",
    "comb",
    "cough",
    "cry",
    "dam",
    "dare",
    "drum",
    "dust",
    "embarrass",
    "fancy",
    "flower",
    "gaze",
    "grease",
    "groan",
    "harass",
    "hug",
    "itch",
    "jail",
    "jam",
    "jog",
    "juggle",
    "kiss",
    "like",
    "laugh",
    "love",
    "marry",
    "meddle",
    "mend",
    "mess",
    "moan",
    "mourn",
    "nail",
    "nod",
    "paddle",
    "pat",
    "peck",
    "pine",
    "poke",
    "pray",
    "preach",
    "prick",
    "rhyme",
    "rob",
    "rot",
    "shiver",
    "soothe",
    "scold",
    "scorch",
    "scribble",
    "shave",
    "shrug",
    "sigh",
    "sin",
    "ski",
    "smile",
    "sneeze",
    "snore",
    "squeak",
    "squeal",
    "stuff",
    "tame",
    "tremble",
    "trot",
    "tug",
    "tumble",
    "untidy",
    "wail",
    "whine",
    "whip",
    "wobble",
    "yawn",
    "yell",
]


tabInformalAdjectives = [
    ("apt", "appropriate"),
    ("austere", "strict"),
    ("awesome", "great"),
    ("awful", "negative"),
    ("awkward", "negative"),
    ("babyish", ""),
    ("baggy", ""),
    ("barren", "unproductive"),
    ("bogus", " counterfeit"),
    ("bony", ""),
    ("bossy", ""),
    ("bubbly", ""),
    ("bulky", "large"),
    ("bumpy", ""),
    ("cheery", ""),
    ("chubby", ""),
    ("colossal", "large"),
    ("crazy", ""),
    ("creepy", ""),
    ("cuddly", ""),
    ("cumbersome", "attractive"),
    ("cute", "attractive"),
    ("dear", ""),
    ("drab", ""),
    ("drafty", ""),
    ("dreary", ""),
    ("droopy", ""),
    ("dull", "tedious"),
    ("evil", "bad"),
    ("fancy", "sophisticated"),
    ("feisty", "spirited"),
    ("fickle", "vacillating"),
    ("filthy", "polluted"),
    ("firm", "inflexible"),
    ("flaky", "inflexible"),
    ("flashy", ""),
    ("flimsy", ""),
    ("flippant", ""),
    ("fluffy", ""),
    ("fond", "affectionate"),
    ("foolish", ""),
    ("frank", "honest"),
    ("frilly", ""),
    ("frizzy", ""),
    ("funny", "humorous"),
    ("fussy", "meticulous"),
    ("giant", "large"),
    ("giddy", ""),
    ("gloomy", "dark"),
    ("glum", "depressed"),
    ("grave", "serious"),
    ("grim", "hopeless"),
    ("gross", "large"),
    ("grouchy", "complaining"),
    ("grumpy", "angry"),
    ("happy", ""),
    ("hasty", "abrupt"),
    ("hearty", ""),
    ("heavenly", ""),
    ("hefty", "large"),
    ("hoarse", ""),
    ("husky", "deep"),
    ("icky", "disgusting"),
    ("impish", ""),
    ("intent", "determined"),
    ("jaunty", ""),
    ("jolly", ""),
    ("klutzy", ""),
    ("knobby", ""),
    ("knotty", ""),
    ("kooky", ""),
    ("lanky", ""),
    ("lavish", ""),
    ("lazy", "slow"),
    ("lovely", "attractive"),
    ("lucky", ""),
    ("lumpy", ""),
    ("mad", "bad"),
    ("merry", "good"),
    ("measly", ""),
    ("meaty", ""),
    ("mediocre", ""),
    ("meek", ""),
    ("mellow", ""),
    ("messy", ""),
    ("minty", ""),
    ("miserly", ""),
    ("misty", ""),
    ("muddy", ""),
    ("murky", ""),
    ("mushy", ""),
    ("nasty", "negative"),
    ("naughty", "negative"),
    ("neat", "attractive"),
    ("needy", ""),
    ("nice", "attractive"),
    ("nifty", ""),
    ("nimble", ""),
    ("nippy", ""),
    ("nutty", ""),
    ("obese", "corpulent"),
    ("ornery", ""),
    ("ornate", ""),
    ("paltry", "insignificant"),
    ("peppery", ""),
    ("perky", ""),
    ("pesky", ""),
    ("petty", "trivial"),
    ("plump", ""),
    ("plush", "luxurious"),
    ("portly", "corpulent"),
    ("posh", "luxurious"),
    ("pretty", "attractive"),
    ("prickly", ""),
    ("pristine", "clean"),
    ("prudent", ""),
    ("proud", ""),
    ("pungent", ""),
    ("puny", "small"),
    ("pushy", ""),
    ("putrid", ""),
    ("quaint", ""),
    ("queasy", ""),
    ("quirky", ""),
    ("rash", ""),
    ("regal", ""),
    ("repentant", ""),
    ("ripe", ""),
    ("rotten", ""),
    ("rowdy", ""),
    ("ruddy", ""),
    ("runny", ""),
    ("rusty", ""),
    ("sad", ""),
    ("scaly", ""),
    ("scarce", "limited"),
    ("scary", ""),
    ("scratchy", ""),
    ("scrawny", ""),
    ("serene", ""),
    ("shabby", ""),
    ("shadowy", ""),
    ("shady", ""),
    ("shiny", ""),
    ("shoddy", ""),
    ("showy", ""),
    ("shrill", ""),
    ("shy", ""),
    ("silly", "negative"),
    ("skinny", ""),
    ("sleepy", ""),
    ("slushy", ""),
    ("smoggy", ""),
    ("smug", ""),
    ("snappy", ""),
    ("sneaky", ""),
    ("snoopy", ""),
    ("soggy", ""),
    ("somber", ""),
    ("soupy", ""),
    ("speedy", ""),
    ("spicy", ""),
    ("spiffy", ""),
    ("spry", "agile"),
    ("squeaky", ""),
    ("squiggly", ""),
    ("stale", ""),
    ("starchy", ""),
    ("starry", ""),
    ("stingy", ""),
    ("stormy", ""),
    ("strident", ""),
    ("stupid", ""),
    ("stylish", ""),
    ("sugary", ""),
    ("sunny", ""),
    ("svelte", ""),
    ("sweaty", ""),
    ("sweet", ""),
    ("swift", "abrupt"),
    ("tame", ""),
    ("tan", ""),
    ("tart", "bitter"),
    ("tasty", ""),
    ("taut", "tense"),
    ("tender", "fragile"),
    ("tepid", ""),
    ("testy", ""),
    ("thinkable", "possible"),
    ("thirsty", ""),
    ("thorny", ""),
    ("thrifty", ""),
    ("tidy", ""),
    ("timely", ""),
    ("torn", ""),  # also verb?
    ("trusty", ""),
    ("tricky", ""),
    ("tubby", ""),
    ("ugly", "negative"),
    ("uneasy", "difficult"),
    ("unhappy", "negative"),
    ("unkempt", ""),
    ("unlucky", ""),
    ("unpractical", "impractical"),
    ("unripe", ""),
    ("unruly", ""),
    ("unselfish", ""),
    ("unsightly", ""),
    ("unsung", ""),
    ("untidy", ""),
    ("untimely", ""),
    ("unwieldy", ""),
    ("upbeat", ""),
    ("upset", ""),
    ("utter", "pure"),
    ("vapid", ""),
    ("wan", ""),
    ("watery", ""),
    ("wary", "careful"),
    ("weary", ""),
    ("wee", ""),
    ("weepy", ""),
    ("weighty", ""),
    ("weird", "strange"),
    ("wiggly", ""),
    ("windy", ""),
    ("wiry", ""),
    ("witty", ""),
    ("wobbly", ""),
    ("woozy", ""),
    ("wordy", ""),
    ("worldly", ""),
    ("wry", ""),
    ("yummy", ""),
    ("zany", ""),
    ("zesty", ""),
]
