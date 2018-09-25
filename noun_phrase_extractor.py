import nltk
from nltk.corpus import stopwords

# text = """
# Types of Computer Networks
# Local Area Networks: LAN connects networking devices with in short spam of area, i.e. small offices, home, internet cafes etc. LAN uses TCP/IP network protocol for communication between computers. It is often but not always implemented as a single IP subnet. Since LAN is operated in short area so It can be control and administrate by single person or organization.
# Wide Area Networks: As “word” Wide implies, WAN, wide area network cover large distance for communication between computers. The Internet itself is the biggest example of Wide area network, WAN, which is covering the entire earth. WAN is distributed collection of geographically LANs. A network connecting device router connects LANs to WANs. WAN used network protocols like ATM, X.25, and Frame Relay for long distance connectivity.
# Wireless - Local Area Network: A LAN, local area networks based on wireless network technology mostly referred as Wi-Fi. Unlike LAN, in   WLAN no wires are used, but radio signals are the medium for communication. Wireless network cards are required to be installed in the systems for accessing any wireless network around. Mostly wireless cards connect to wireless routers for communication among computers or accessing WAN, internet.
# Metropolitan Area Network: This kind of network is not mostly used but it has its own importance for some government bodies and organizations on larger scale. MAN, metropolitan area network falls in middle of LAN and WAN, It covers large span of physical area than LAN but smaller than WAN, such as a city.
# Campus Area Network: Networking spanning with multiple LANs but smaller than a Metropolitan area network, MAN. This kind of network mostly used in relatively large universities or local business offices and buildings.
# Storage Area Network: it is used for data storage and it has no use for most of the organization but data oriented organizations. Storage area network connects servers to data storage devices by using Fiber channel technology.
# Network Topology
# Network topology is the arrangement of the various elements (links, nodes, etc.) of a communication network. Network topology is the topological structure of a network and may be depicted physically or logically. The interconnections between computers whether logical or physical are the foundation of this classification.
# Logical topology is the way a computer in a given network transmits information, not the way it looks or connected, along with the varying speeds of cables used from one network to another. On the other hand, the physical topology is affected by a number of factors: troubleshooting technique, installation cost, office layout and cables’ types.
# The physical topology is figured out on the basis of a network’s capability to access media and devices, the fault tolerance desired and the cost of telecommunications circuits.
#
# """

text = '''
Canadian Ben Johnson left the Olympics today “in a
complete state of shock,” accused of cheating with drugs
in the world’s fastest 100-meter dash and stripped of
his gold medal. The prize went to American Carl
Lewis. Many athletes accepted the accusation that Johnson
used a muscle-building but dangerous and illegal anabolic
steroid called stanozolol as confirmation of what
they said they know has been going on in track and field.
Two tests of Johnson’s urine sample proved positive and
his denials of drug use were rejected today. “This is
a blow for the Olympic Games and the Olympic movement,”
said International Olympic Committee President
Juan Antonio Samaranch.
'''

sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)
toks = nltk.regexp_tokenize(text, sentence_re)
postoks = nltk.tag.pos_tag(toks)
print (postoks)
tree = chunker.parse(postoks)
stopwords = stopwords.words('english')

def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    # word = stemmer.stem_word(word) #if we consider stemmer then results comes with stemmed word, but in this case word will not match with comment
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword. We can increase the length if we want to consider large phrase"""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted

def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term

terms = get_terms(tree)
yu = []
for term in terms:
    yu1 = ''
    for word in term:
        # print (word)
        yu1 = ' ' + word
        # print(yu1)
    yu.append(yu1)
    print()
# print(yu)