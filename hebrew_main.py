import math
import random
from Word import Word

#import Word
# Hannah Sieber


# Hebrew!

# WHAT IF THEY TYPE THE WRONG THING - TELL THEM WHICH WASNT RECOGNIZED
# FINAL LETTERS - IF THERE ARE TWO OPTIONS AND ITS THE END, TAKE THE SECOND
# EDIT OR DELETE A WORD FROM THE DICTIONARY??
# add rest of letters!!!!!!
a = "\u05D0"
b = "\u05D1\u05BC"
d = "\u05D3"
g = "\u05D2"
h = "\u05D4"
v = "\u05D1"
va = "\u05D5"
z = "\u05D6"
ch = "\u05D7"
te = "\u05D8"
y = "\u05D9"
c = "\u05D9"
cha = "\u05D9"
l = "\u05D9"
m = "\u05D9"
n = "\u05E0"
s = "\u05D9"
ay = "\u05D9"
p = "\u05D9"
f = "\u05D9"
tz = "\u05D9"
k = "\u05D9"
r = "\u05D9"
sh = "\u05D9"
si = "\u05D9"
t = "\u05D9"
letter = {"A":a,"B":b,"H":h,"G":g,"N":n,"V":v, "D":d,"VA":va}
order = ["A","B","V","G","D","H","VA","Z","CH","TE","Y","C","CHA","L","M","N","S","AY","P","F","TZ","K","R","SH","SI","T"]
names = {"Alef":a,"Bet":b,"Vet":v,"Gimel":g,"Dalet":d}
vowel = {"a":"\u05B7","ah":"\u05C7","":"",".":"\u05B0","oh":"\u05B9"}
direction = "Type 'CREATE' followed by a Hebrew word, 'CODES' for the codes, 'DICTIONARY' for the words, 'TRANSLATE' followed by English words for sentence options, or 'EXIT' to finish\n"
dictionary = {}
def save(e,h,s,t):
    e = e.upper()
    f = open("all_words.txt",'a')
    f.write(e + ":" + h + ":" + s + ":" + t +"\n")
    si = True
    ma = True
    if (s == "FS"):
        ma = False
    elif (s == "MP"):
        si = False
    elif (s == "FP"):
        ma = False
        si = False
    w = Word(e,h,m,s,t)
    if (e in dictionary):
        dictionary[e] = dictionary[e].append(w)
    else:
        dictionary[e] = [w]
    f.close()

def t2h(word):
    word_array = word.split(" ")
    final = ""
    for sils in word_array:
        sound = sils.split("|")
        if (sound[0] in letter and sound[1] in vowel):
            final = final + letter[sound[0]] + vowel[sound[1]]
        else:
            print("That was not a valid transliteration for Hebrew")
            return False
    return final
    
def dictionaries():
    f = open("all_words.txt", 'r')
    content = f.read().splitlines()
    f.close()
    for line in content:
        parts = line.split(":")
        p0 = parts[0]
        p1 = parts[1]
        p2 = parts[2]
        p3 = parts[3]
        s = True
        m = True
        if (p2 == "FS"):
            m = False
        elif (p2 == "MP"):
            s = False
        elif (p2 == "FP"):
            m = False
            s = False
        w = Word(p0,p1,m,s,p3)
        if (p0 in dictionary):
            dictionary[p0] = dictionary[p0][len(dictionary[p0]):] = [w]
        else:
            dictionary[p0] = [w]

def specString(a,b):
    m = "Masculine"
    s = "Singular"
    if (not a):
        m = "Feminine"
    if (not s):
        s = "Plural"
    return (m + " and " + s)

def printE():
    for word_key in sorted(dictionary):
        for word in dictionary[word_key]:
            s = specString(word.male,word.single)
            print(word.wordE + " (" + s + ") = " + t2h(word.wordH))

def makeSentences(arr):
    MS = {"N":[],"V":[],"A":[]}
    MP = {"N":[],"V":[],"A":[]}
    FS = {"N":[],"V":[],"A":[]}
    FP = {"N":[],"V":[],"A":[]}
    for word in arr:
        print(word.wordType)
        if (word.male and word.single):
            MS[word.wordType].append(word)
        elif (word.male and not word.single):
            MP[word.wordType].append(word)
        elif (not word.male and word.single):
            FS[word.wordType].append(word)
        elif (not word.male and not word.single):
            FP[word.wordType].append(word)
    print("ms has " + str(FS['N']))
    printSent(MS)
    printSent(MP)
    printSent(FS)
    printSent(FP)


### WHEN DICTIONARY PRINTS IT PRINTS THE SAME OF THE TWO TALK NOT BOTH

def printSent(d):
    for noun in d['N']:
        for adj in d['A']:
            for verb in d['V']:
                print("The " + noun.wordE + " " + adj.wordE + " " + verb.wordE)
                print(t2h(addThe(noun.wordH)) + " " + t2h(adj.wordH) + " " + t2h(verb.wordH))

def addThe(word):
    result = "H|a " + word.wordH
    return result

def main():
    command = input(direction)
    while (command.upper() != "EXIT"):
        if (command.upper().startswith("CREATE")):
            word = command[7:]
            while (word == ""):
                word = input("What is the word?")
            final = t2h(word)
            if (final == False):
                main()
                break
            print(final + "\n")
            print("Would you like to save this word?\n")
            maybe = input("Type 'NO' or 'AS' followed by the English definition\n")
            while (maybe.upper() != "NO" and not maybe.upper().startswith("AS")):
                maybe = input("Type 'NO' or 'AS' followed by the English definition\n")
            if (maybe.upper().startswith('AS')):
		# what if they include spaces???
                eng = maybe[3:]
                while(len(eng.split(" ")) > 1):
                    print("English definitions must be a single word, no spaces.")
                    eng = input("Retype the English word\n")
                m = input("Type M for a masculine word, or F for a feminine word\n")
                while (m.upper() != "M" and m.upper() != "F"):
                    m = input("Type M for a masculine word, or F for a feminine word\n")
                s = input("Type S for a singular word, or P for a plural word\n")
                while (s.upper() != "S" and s.upper() != "P"):
                    s = input("Type S for a singular word, or P for a plural word\n")
                t = input("Type N for a noun, V for a verb, or A for an adjective\n")
                while (t.upper() != "N" and t.upper() != "V" and t.upper() != "A"):
                    t = input("Type N for a noun, V for a verb, or A for an adjective\n")    
                specs = m.upper() + s.upper();
                save(eng,word,specs,t.upper())
                print(final + " has been saved as " + eng + "\n")
        elif (command.upper() == "CODES"):
            print("LETTERS\n")
            for let in sorted(letter):
                print("Type " + let + " for " + letter[let] + ",   ")
            print("VOWELS\n")
            for vow in sorted(vowel):
                print("Type " + vow + " for  " + vowel[vow] + ",   ")
            print("\n")
        elif (command.upper() == "DICTIONARY"):
            printE()
        elif (command.upper().startswith("TRANSLATE")):
            english = command[10:]
            engs = english.split(" ")
            word_array = []
            for w in engs:
                w = w.upper()
                if (w in dictionary):
                    for wo in dictionary[w]:
                        word_array.append(wo)
                else:
                    print("The word " + w + " does not exist in the dictionary.\n")
                    print("The computer will still try to make a sentence\n")
            makeSentences(word_array)
        command = input(direction)
    print("Good-bye")

dictionaries()
main()
