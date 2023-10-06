class InputSeq:
    def __init__(self):
        self.filename = ""
        self.sequence2D = []
        self.inputSeq_041354279()

    def inputSeq_041354279(self):
        #To open and read the given file
        self.filename = input("Enter a file name: ")
        openfile = open(self.filename)
        for line in openfile:
            sequence = line.strip("\n")
            sequenceList = sequence.split(",")
            self.sequence2D.append(sequenceList)
        openfile.close()
        
        fileWrite = open("Output.txt","a")
        self.noCol = len(self.sequence2D[0])
        self.noRow = len(self.sequence2D)
        for row in range(self.noRow):
            outputseq=[]
            for col in range(self.noCol):
                outputseq.append(self.sequence2D[row][col])
            print('{:>2}'.format(row+1) , '{:>5}'.format(" ".join(outputseq)))
            fileWrite.write('{:>2}'.format(str(row+1)) + " " + '{:>5}'.format(" ".join(outputseq)) + "\n")
        fileWrite.close()
