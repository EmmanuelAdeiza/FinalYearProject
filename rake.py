import operator
import re

debug = False
test = False


def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


def load_stop_words(stop_word_file):
    """
    Utility function to load stop words from a file and return as a list of words
    @param stop_word_file Path and file name of a file containing stop words.
    @return list A list of stop words.
    """
    stop_words = []
    for line in open(stop_word_file):
        if line.strip()[0:1] != "#":
            for word in line.split():  # in case more than one per line
                stop_words.append(word)
    return stop_words


def separate_words(text, min_word_return_size):
    """
    Utility function to return a list of all words that are have a length greater than a specified number of characters.
    @param text The text that must be split in to words.
    @param min_word_return_size The minimum no of characters a word must have to be included.
    """
    splitter = re.compile('[^a-zA-Z0-9_\\+\\-/]')
    words = []
    for single_word in splitter.split(text):
        current_word = single_word.strip().lower()
        # leave numbers in phrase, but don't count as words, since they tend to invalidate scores of their phrases
        if len(current_word) > min_word_return_size and current_word != '' and not is_number(current_word):
            words.append(current_word)
    # print(words)
    return words


def split_sentences(text):
    """
    Utility function to return a list of sentences.
    @param text The text that must be split in to sentences.
    """
    sentence_delimiters = re.compile(u'[\\[\\]\n.!?,;:\t\\-\\"\\(\\)\\\'\u2019\u2013]')
    sentences = sentence_delimiters.split(text)
    return sentences


def build_stop_word_regex(stop_word_file_path):
    stop_word_list = load_stop_words(stop_word_file_path)
    stop_word_regex_list = []
    for word in stop_word_list:
        word_regex = '\\b' + word + '\\b'
        stop_word_regex_list.append(word_regex)
    stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
    return stop_word_pattern


def generate_candidate_keywords(sentence_list, stopword_pattern, min_char_length=1, max_words_length=4):
    phrase_list = []
    for s in sentence_list:
        tmp = re.sub(stopword_pattern, '|', s.strip())
        phrases = tmp.split("|")
        for phrase in phrases:
            phrase = phrase.strip().lower()
            if phrase != "" and is_acceptable(phrase, min_char_length, max_words_length):
                phrase_list.append(phrase)
    # print(phrase_list)
    return phrase_list


def is_acceptable(phrase, min_char_length, max_words_length):
    # a phrase must have a min length in characters
    if len(phrase) < min_char_length:
        return 0

    # a phrase must have a max number of words
    words = phrase.split()
    if len(words) > max_words_length:
        return 0

    digits = 0
    alpha = 0
    for i in range(0, len(phrase)):
        if phrase[i].isdigit():
            digits += 1
        elif phrase[i].isalpha():
            alpha += 1

    # a phrase must have at least one alpha character
    if alpha == 0:
        return 0

    # a phrase must have more alpha than digits characters
    if digits > alpha:
        return 0
    return 1


def calculate_word_scores(phraseList):
    word_frequency = {}
    word_degree = {}
    for phrase in phraseList:
        word_list = separate_words(phrase, 0)
        word_list_length = len(word_list)
        word_list_degree = word_list_length - 1
        # if word_list_degree > 3: word_list_degree = 3 #exp.
        for word in word_list:
            word_frequency.setdefault(word, 0)
            word_frequency[word] += 1
            word_degree.setdefault(word, 0)
            word_degree[word] += word_list_degree  # orig.
            # word_degree[word] += 1/(word_list_length*1.0) #exp.
    for item in word_frequency:
        word_degree[item] = word_degree[item] + word_frequency[item]

    # Calculate Word scores = deg(w)/frew(w)
    word_score = {}
    for item in word_frequency:
        word_score.setdefault(item, 0)
        word_score[item] = word_degree[item] / (word_frequency[item] * 1.0)  # orig.
    # word_score[item] = word_frequency[item]/(word_degree[item] * 1.0) #exp.
    # print(word_frequency)
    return word_frequency


def generate_candidate_keyword_scores(phrase_list, word_score, min_keyword_frequency=1):
    keyword_candidates = {}

    for phrase in phrase_list:
        if min_keyword_frequency > 1:
            if phrase_list.count(phrase) < min_keyword_frequency:
                continue
        keyword_candidates.setdefault(phrase, 0)
        word_list = separate_words(phrase, 0)
        candidate_score = 0
        for word in word_list:
            candidate_score += word_score[word]
        keyword_candidates[phrase] = candidate_score
    return keyword_candidates


class Rake(object):
    def __init__(self, stop_words_path, min_char_length=1, max_words_length=3, min_keyword_frequency=1):
        self.__stop_words_path = stop_words_path
        self.__stop_words_pattern = build_stop_word_regex(stop_words_path)
        self.__min_char_length = min_char_length
        self.__max_words_length = max_words_length
        self.__min_keyword_frequency = min_keyword_frequency

    def run(self, text):
        sentence_list = split_sentences(text)

        phrase_list = generate_candidate_keywords(sentence_list, self.__stop_words_pattern, self.__min_char_length,
                                                  self.__max_words_length)

        word_scores = calculate_word_scores(phrase_list)

        keyword_candidates = generate_candidate_keyword_scores(phrase_list, word_scores, self.__min_keyword_frequency)

        sorted_keywords = sorted(keyword_candidates.items(), key=operator.itemgetter(1), reverse=True)

        return sorted_keywords

#
# text = """
# A Computer network or data network is a digital telecommunications network which allows nodes
# (computers, terminals, and communications devices) to share resources.
# In computer networks, networked computing devices exchange data with each other using a data link.
# The connections between nodes are established using either cable media or wireless media.
# Nodes can include hosts such as personal computers, phones, servers as well as networking hardware.
# Computer networks support an enormous number of applications and services such as access to the World Wide Web,
# digital video, digital audio, shared use of application and storage servers, printers, and fax machines, and
# use of email and instant messaging applications as well as many others. The best-known computer network is the Internet
# """
#
#
# # text = """
# # Types of Computer Networks
# # Local Area Networks: LAN connects networking devices with in short spam of area, i.e. small offices, home, internet cafes etc. LAN uses TCP/IP network protocol for communication between computers. It is often but not always implemented as a single IP subnet. Since LAN is operated in short area so It can be control and administrate by single person or organization.
# # Wide Area Networks: As “word” Wide implies, WAN, wide area network cover large distance for communication between computers. The Internet itself is the biggest example of Wide area network, WAN, which is covering the entire earth. WAN is distributed collection of geographically LANs. A network connecting device router connects LANs to WANs. WAN used network protocols like ATM, X.25, and Frame Relay for long distance connectivity.
# # Wireless - Local Area Network: A LAN, local area networks based on wireless network technology mostly referred as Wi-Fi. Unlike LAN, in   WLAN no wires are used, but radio signals are the medium for communication. Wireless network cards are required to be installed in the systems for accessing any wireless network around. Mostly wireless cards connect to wireless routers for communication among computers or accessing WAN, internet.
# # Metropolitan Area Network: This kind of network is not mostly used but it has its own importance for some government bodies and organizations on larger scale. MAN, metropolitan area network falls in middle of LAN and WAN, It covers large span of physical area than LAN but smaller than WAN, such as a city.
# # Campus Area Network: Networking spanning with multiple LANs but smaller than a Metropolitan area network, MAN. This kind of network mostly used in relatively large universities or local business offices and buildings.
# # Storage Area Network: it is used for data storage and it has no use for most of the organization but data oriented organizations. Storage area network connects servers to data storage devices by using Fiber channel technology.
# # Network Topology
# # Network topology is the arrangement of the various elements (links, nodes, etc.) of a communication network. Network topology is the topological structure of a network and may be depicted physically or logically. The interconnections between computers whether logical or physical are the foundation of this classification.
# # Logical topology is the way a computer in a given network transmits information, not the way it looks or connected, along with the varying speeds of cables used from one network to another. On the other hand, the physical topology is affected by a number of factors: troubleshooting technique, installation cost, office layout and cables’ types.
# # The physical topology is figured out on the basis of a network’s capability to access media and devices, the fault tolerance desired and the cost of telecommunications circuits.
# #
# # """
#
# # Split text into sentences
# sentenceList = split_sentences(text)
# # print(sentenceList)
# # #stoppath = "FoxStoplist.txt" #Fox stoplist contains "numbers", so it will not find "natural numbers" like in Table 1.1
# stoppath = 'C:\\Users\\EmmaAdeiza\\PycharmProjects\\needed_project_main\\Ok_keyword-rake-master\\SmartStoplist.txt'  # SMART stoplist misses some of the lower-scoring keywords in Figure 1.5, which means that the top 1/3 cuts off one of the 4.0 score words in Table 1.1
# stopwordpattern = build_stop_word_regex(stoppath)
# #
# # generate candidate keywords
# phraseList = generate_candidate_keywords(sentenceList, stopwordpattern)
# #
# # # calculate individual word scores
# wordscores = calculate_word_scores(phraseList)
#
# # generate candidate keyword scores
# keywordcandidates = generate_candidate_keyword_scores(phraseList, wordscores)
# if debug: print(keywordcandidates)
#
# sortedKeywords = sorted(keywordcandidates.items(), key=operator.itemgetter(1), reverse=True)
# if debug: print(sortedKeywords)
#
# totalKeywords = len(sortedKeywords)
# if debug: print(totalKeywords)
# # print (sortedKeywords[0:(totalKeywords / 3)])
# # using 12 as the specified number of keywords
# import pprint as pp
#
# pp = pp.PrettyPrinter(indent=4)
# pp.pprint('----------------------------------------------------------------------------------')
# pp.pprint('----------------------------------------------------------------------------------')
# # print('Input File')
# pp.pprint('----------------------------------------------------------------------------------')
# # pp.pprint(text)
# pp.pprint('----------------------------------------------------------------------------------')
# pp.pprint('Keywords with highest scores', )
# pp.pprint('----------------------------------------------------------------------------------')
# pp.pprint(len(sortedKeywords[0:12]))



# rake = Rake('C:\\Users\\EmmaAdeiza\\PycharmProjects\\needed_project_main\\Ok_keyword-rake-master\\SmartStoplist.txt')
# keywords = rake.run(text)
# print (keywords)
