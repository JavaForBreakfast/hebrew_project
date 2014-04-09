class Word:
    'Class for all Hebrew words for the program'
    
    def __init__(self,wordE,wordH,male,single,wordType):
        self.wordE = wordE
        self.wordH = wordH
        self.male = male
        self.single = single
        self.wordType = wordType

    def displayWordHebrew(self):
        gend = "Feminine"
        if (self.male):
            gend = "Masculine"
        sing = "Plural"
        if (self.single):
            gend = "Singular"
        print("The word " + self.wordH + " is " + gend + " and " + sing + " and means " + self.wordE)

    def displayWordEnglish(self):
        gend = "Feminine"
        if (self.male):
            gend = "Masculine"
        sing = "Plural"
        if (self.single):
            gend = "Singular"
        print(self.wordE + " means " + self.wordH + ", which is " + gend + " and " + sing)
