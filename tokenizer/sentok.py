#! /usr/bin/python

import sys
import nltk

def main():
    """ 
    Reads text from standard input and outputs sentenses to standard output.
    """

    tab="\t";
    space=" ";

    text = sys.stdin.readlines()
    text = space.join(text)
    sentences = nltk.tokenize.sent_tokenize(text)
    
    # printSentences(sentences)

    questions = xtractQuestions(sentences)
    
    printSentences(questions)


def isQuestion(sentence):
    feature = '?'
    if feature in sentence:
        return True
    else:
        return False

def xtractQuestions(sentences):
    questions = []
    for sent in sentences:
        if isQuestion(sent):
            questions.append(sent)
    
    return questions

def printSentences(sentences):
    for sent in sentences:
        print (sent)
    print("There are " + str(len(sent)) +" sentences.")

def test():
    text = """At eight o'clock on Thursday morning Arthur didn't feel very good. Why he is so sick ? """
    sentences = nltk.tokenize.sent_tokenize(text)
    for sent in sentenses:
        print (sent)

if __name__ == '__main__':
    main()

