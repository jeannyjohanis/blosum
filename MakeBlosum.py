from InputSeq import *
from OutputMatrices import *
import math

class MakeBlosum:
    def __init__(self):
        self.seqIn = InputSeq()
        #outFile = OutputMatrices()
        self.inputArray = self.seqIn.sequence2D
        self.numAA = 20;
        self.aaList = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
        self.aaCountTotalInCols =[] 
        self.aaMargProb = [] 
        self.aaFreqSub = [[]] 
        self.aaCountSubs = [[]] 
        self.aaProbSub = [[]] 
        self.aaExpectSubst = [[]] 
        self.oddsRatio = [[]]
        self.logsOddsRatio = [[]] 
        self.colList = ['0','1','2','3','4','5','6','7','8']
                
        #initialize values inside 1D matrix to 0 or 0.0
        self.aaCountTotalInCols = [0 for i in range(self.numAA)]
        self.aaMargProb = [0.0 for i in range(self.numAA)]

        #initialize values inside 2D matrix to 0 or 0.0
        self.aaCountSubs = [[0 for col in range(self.numAA)] for row in range(self.numAA)]
        self.aaExpectSubst = [[0.0 for col in range(self.numAA)] for row in range(self.numAA)]
        self.aaProbSub = [[0.0 for col in range(self.numAA)] for row in range(self.numAA)]
        self.oddsRatio = [[0.0 for col in range(self.numAA)] for row in range(self.numAA)]
        self.logsOddsRatio = [[0.0 for col in range(self.numAA)] for row in range(self.numAA)]

    def calcfreqAAsub(self):
        #create and initialize values inside 20x9 matrix to 0
        self.aaFreqSub = [[0 for col in range(self.seqIn.noCol)] for row in range(self.numAA)]
        #count frequency of amino acids substitutions
        for i1 in range(self.seqIn.noRow):
            for i2 in range(self.seqIn.noCol):
                for c1 in range(self.numAA):
                    if(self.inputArray[i1][i2]==self.aaList[c1]):
                        self.aaFreqSub[c1][i2]=self.aaFreqSub[c1][i2]+1
                        break
        #write to file
        OutputMatrices().write2Dmatrixint("Amino Acid Frequency Substitution", self.colList, self.aaList, self.aaFreqSub)

    def calcProbsAAsub(self):
        #count amino acid substitution
        totalI = 0
        for i1 in range (self.numAA):
            for i2 in range (i1+1):
                for c1 in range (self.seqIn.noCol):
                    if i1==i2:
                        self.aaCountSubs[i1][i2] = self.aaCountSubs[i1][i2]+(self.aaFreqSub[i1][c1]*(self.aaFreqSub[i1][c1]-1))/2
                    else:
                        self.aaCountSubs[i1][i2] = self.aaCountSubs[i1][i2]+(self.aaFreqSub[i1][c1])*(self.aaFreqSub[i2][c1])
        #write to file
        OutputMatrices().write2Dmatrixint("Amino Acid Counted Substitution", self.aaList, self.aaList, self.aaCountSubs)
        #count overall amino acid substitution and change from type int to type double
        for i1 in range(0,self.numAA):
            for i2 in range(0,i1+1):
                totalI = totalI + self.aaCountSubs[i1][i2]
        totalD = float(totalI)
        OutputMatrices().writeTotal("\nTotal substitution count = " ,totalI)
        #count probability of amino acid substitution
        for i1 in range (0,self.numAA):
            for i2 in range (0,i1+1):
                self.aaProbSub[i1][i2] = self.aaCountSubs[i1][i2]/totalD
        #write to file
        OutputMatrices().write2DmatrixReal("Amino Acid Probability Substitution", self.aaList, self.aaList, self.aaProbSub)

    def calcAAMargProb(self):
        aaGrandTotal = 0
        #count sum for each amino acids across all columns
        for i1 in range(self.numAA):
            for i2 in range(len(self.colList)):
                self.aaCountTotalInCols[i1] += self.aaFreqSub[i1][i2]
        #count grand total of amino acids across all columns
        for i1 in range (self.numAA):
            aaGrandTotal += self.aaCountTotalInCols[i1]
        #change grand total to type double
        dblTotal = float(aaGrandTotal)
        OutputMatrices().writeTotal("\nGrand Total Amino Acid = " ,aaGrandTotal)
        #count marginal probability
        for i1 in range(self.numAA):
            self.aaMargProb[i1] = self.aaCountTotalInCols[i1]/dblTotal
        #write to file
        OutputMatrices().write1DmatrixReal("Amino Acid Marginal Prob",self.aaList,self.aaMargProb)

    def calcExpectedSubs(self):
        #calculate expected substitution rate
        for i in range(self.numAA):
            for j in range(i+1):
                if i==j:
                    self.aaExpectSubst[i][j] = self.aaMargProb[i]*self.aaMargProb[j]
                else:
                    self.aaExpectSubst[i][j] = 2*self.aaMargProb[i]*self.aaMargProb[j]
        #write to file
        OutputMatrices().write2DmatrixReal("Amino Acid Expected Substitution Rate", self.aaList, self.aaList, self.aaExpectSubst)

    def calcOddsRatio(self):
        #calculate odd ratio
        for i1 in range(self.numAA):
            for i2 in range (i1+1):
                if self.aaProbSub[i1][i2] != 0 and self.aaExpectSubst[i1][i2] != 0:
                    self.oddsRatio[i1][i2] = self.aaProbSub[i1][i2] / self.aaExpectSubst[i1][i2]
        #write to file
        OutputMatrices().write2DmatrixReal("Amino Acid Odds Ratio", self.aaList, self.aaList, self.oddsRatio)

    def calcLogOddRatio(self):
        #calculate log odd ratio
        for i1 in range(self.numAA):
            for i2 in range(i1+1):
                if self.oddsRatio[i1][i2] !=0:
                    self.logsOddsRatio[i1][i2] = 2 * (math.log(self.oddsRatio[i1][i2],2))
                else:
                    self.logsOddsRatio[i1][i2] = -9.9900;
        #write to file
        OutputMatrices().write2DmatrixReal("Amino Acid Log(Odds Ratio)", self.aaList, self.aaList, self.logsOddsRatio)

    def main(self):
        self.calcfreqAAsub()
        self.calcProbsAAsub()
        self.calcAAMargProb()
        self.calcExpectedSubs()
        self.calcOddsRatio()
        self.calcLogOddRatio()
        print("\nBLOSUM has completed!")

