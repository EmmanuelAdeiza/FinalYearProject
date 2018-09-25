# Source of text:
# https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents

Text = "Compatibility of systems of linear constraints over the set of natural numbers. \
Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and \
nonstrict inequations are considered. \
Upper bounds for components of a minimal set of solutions and \
algorithms of construction of minimal generating sets of solutions for all \
types of systems are given. \
These criteria and the corresponding algorithms for constructing \
a minimal supporting set of solutions can be used in solving all the \
considered types of systems and systems of mixed types."

# text = "Types of Computer Networks \
# Local Area Networks: LAN connects networking devices with in short spam of area, i.e. small offices, home, internet cafes etc. LAN uses TCP/IP network protocol for communication between computers. It is often but not always implemented as a single IP subnet. Since LAN is operated in short area so It can be control and administrate by single person or organization.\
# Wide Area Networks: As “word” Wide implies, WAN, wide area network cover large distance for communication between computers. The Internet itself is the biggest example of Wide area network, WAN, which is covering the entire earth. WAN is distributed collection of geographically LANs. A network connecting device router connects LANs to WANs. WAN used network protocols like ATM, and Frame Relay for long distance connectivity.\
# Wireless - Local Area Network: A LAN, local area networks based on wireless network technology mostly referred as Wi-Fi. Unlike LAN, in   WLAN no wires are used, but radio signals are the medium for communication. Wireless network cards are required to be installed in the systems for accessing any wireless network around. Mostly wireless cards connect to wireless routers for communication among computers or accessing WAN, internet.\
# Metropolitan Area Network: This kind of network is not mostly used but it has its own importance for some government bodies and organizations on larger scale. MAN, metropolitan area network falls in middle of LAN and WAN, It covers large span of physical area than LAN but smaller than WAN, such as a city.\
# Campus Area Network: Networking spanning with multiple LANs but smaller than a Metropolitan area network, MAN. This kind of network mostly used in relatively large universities or local business offices and buildings.\
# Storage Area Network: it is used for data storage and it has no use for most of the organization but data oriented organizations. Storage area network connects servers to data storage devices by using Fiber channel technology.\
# Network Topology\
# Network topology is the arrangement of the various elements (links, nodes, etc.) of a communication network. Network topology is the topological structure of a network and may be depicted physically or logically. The interconnections between computers whether logical or physical are the foundation of this classification.\
# Logical topology is the way a computer in a given network transmits information, not the way it looks or connected, along with the varying speeds of cables used from one network to another. On the other hand, the physical topology is affected by a number of factors: troubleshooting technique, installation cost, office layout and cables’ types. \
# The physical topology is figured out on the basis of a network’s capability to access media and devices, the fault tolerance desired and the cost of telecommunications circuits."


import string

import nltk
from nltk import word_tokenize


# nltk.download('punkt')

def clean(text):
    text = text.lower()
    printable = set(string.printable)
    text = filter(lambda x: x in printable, text)  # filter funny characters, if any.
    return text


Cleaned_text = clean(Text)

text = word_tokenize(Cleaned_text)

print("Tokenized Text: \n")
print(text)

# nltk.download('averaged_perceptron_tagger')

POS_tag = nltk.pos_tag(text)

print("Tokenized Text with POS tags: \n")
print(POS_tag)

# nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

adjective_tags = ['JJ', 'JJR', 'JJS']

lemmatized_text = []

for word in POS_tag:
    if word[1] in adjective_tags:
        lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0], pos="a")))
    else:
        lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0])))  # default POS = noun

print("Text tokens after lemmatization of adjectives and nouns: \n")
print(lemmatized_text)

POS_tag = nltk.pos_tag(lemmatized_text)

print("Lemmatized text with POS tags: \n")
print(POS_tag)

stopwords = []

wanted_POS = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS', 'VBG', 'FW']

for word in POS_tag:
    if word[1] not in wanted_POS:
        stopwords.append(word[0])

punctuations = list(str(string.punctuation))

stopwords = stopwords + punctuations

stopword_file = open("C:\\Users\\EmmaAdeiza\\PycharmProjects\\FinalYearProject\\long_stopwords.txt", "r")
# Source = https://www.ranks.nl/stopwords

lots_of_stopwords = []

for line in stopword_file.readlines():
    lots_of_stopwords.append(str(line.strip()))

stopwords_plus = []
stopwords_plus = stopwords + lots_of_stopwords
stopwords_plus = set(stopwords_plus)

# Stopwords_plus contain total set of all stopwords


processed_text = []
for word in lemmatized_text:
    if word not in stopwords_plus:
        processed_text.append(word)
print(processed_text)

vocabulary = list(set(processed_text))
print(vocabulary)

import numpy as np
import math

vocab_len = len(vocabulary)

weighted_edge = np.zeros((vocab_len, vocab_len), dtype=np.float32)

score = np.zeros((vocab_len), dtype=np.float32)
window_size = 3
covered_coocurrences = []

for i in xrange(0, vocab_len):
    score[i] = 1
    for j in xrange(0, vocab_len):
        if j == i:
            weighted_edge[i][j] = 0
        else:
            for window_start in xrange(0, (len(processed_text) - window_size)):

                window_end = window_start + window_size

                window = processed_text[window_start:window_end]

                if (vocabulary[i] in window) and (vocabulary[j] in window):

                    index_of_i = window_start + window.index(vocabulary[i])
                    index_of_j = window_start + window.index(vocabulary[j])

                    # index_of_x is the absolute position of the xth term in the window
                    # (counting from 0)
                    # in the processed_text

                    if [index_of_i, index_of_j] not in covered_coocurrences:
                        weighted_edge[i][j] += 1 / math.fabs(index_of_i - index_of_j)
                        covered_coocurrences.append([index_of_i, index_of_j])

inout = np.zeros((vocab_len), dtype=np.float32)

for i in xrange(0, vocab_len):
    for j in xrange(0, vocab_len):
        inout[i] += weighted_edge[i][j]

MAX_ITERATIONS = 50
d = 0.85
threshold = 0.0001  # convergence threshold

for iter in xrange(0, MAX_ITERATIONS):
    prev_score = np.copy(score)

    for i in xrange(0, vocab_len):

        summation = 0
        for j in xrange(0, vocab_len):
            if weighted_edge[i][j] != 0:
                summation += (weighted_edge[i][j] / inout[j]) * score[j]

        score[i] = (1 - d) + d * (summation)

    if np.sum(np.fabs(prev_score - score)) <= threshold:  # convergence condition
        print("Converging at iteration " + str(iter) + "....")
        break

for i in xrange(0, vocab_len):
    print("Score of " + vocabulary[i] + ": " + str(score[i]))

phrases = []

phrase = " "
for word in lemmatized_text:

    if word in stopwords_plus:
        if phrase != " ":
            phrases.append(str(phrase).strip().split())
        phrase = " "
    elif word not in stopwords_plus:
        phrase += str(word)
        phrase += " "

print("Partitioned Phrases (Candidate Keyphrases): \n")
print(phrases)

unique_phrases = []

for phrase in phrases:
    if phrase not in unique_phrases:
        unique_phrases.append(phrase)

print("Unique Phrases (Candidate Keyphrases): \n")
print(unique_phrases)

for word in vocabulary:
    # print word
    for phrase in unique_phrases:
        if (word in phrase) and ([word] in unique_phrases) and (len(phrase) > 1):
            # if len(phrase)>1 then the current phrase is multi-worded.
            # if the word in vocabulary is present in unique_phrases as a single-word-phrase
            # and at the same time present as a word within a multi-worded phrase,
            # then I will remove the single-word-phrase from the list.
            unique_phrases.remove([word])

print("Thinned Unique Phrases (Candidate Keyphrases): \n")
print(unique_phrases)

phrase_scores = []
keywords = []
for phrase in unique_phrases:
    phrase_score = 0
    keyword = ''
    for word in phrase:
        keyword += str(word)
        keyword += " "
        phrase_score += score[vocabulary.index(word)]
    phrase_scores.append(phrase_score)
    keywords.append(keyword.strip())

i = 0
for keyword in keywords:
    print("Keyword: '" + str(keyword) + "', Score: " + str(phrase_scores[i]))
    i += 1

sorted_index = np.flip(np.argsort(phrase_scores), 0)

keywords_num = 10

print("Keywords:\n")

for i in xrange(0, keywords_num):
    print(str(keywords[sorted_index[i]]) + ", ", )
