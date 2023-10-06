class OutputMatrices:
    
    #write 1D matrix accept matrix 
    def writeTotal(self, label, total):
        filew = open("Output.txt","a")
        print(label , total)
        filew.write(label + str(total))
        
    def write1DmatrixReal(self,mtxName,leftLabel=[],mtx=[]):
        #write to file and print
        filew = open("Output.txt","a")
        print("\n\n" , mtxName)
        filew.write("\n\n" + mtxName + "\n")
        for line in range (len(mtx)):
            print(leftLabel[line] , "{:.4f}".format(mtx[line]))
            filew.write(leftLabel[line]+" "+"{:.4f}".format(mtx[line])+"\n")
        filew.close()

    #write 2D matrix accept matrix with integer
    def write2Dmatrixint(self,mtxName,topLabel=[],leftLabel=[],mtx=[]):
        filew = open("Output.txt","a")
        print("\n\n" , mtxName)
        filew.write("\n\n" + mtxName)
        print("{:4s}".format("")),
        filew.write("\n"+"{:4s}".format(""))
        for c in range(len(topLabel)):
            print("{:4s}".format(topLabel[c]))
            filew.write("{:4s}".format(topLabel[c]))
        for r in range(len(leftLabel)):
            print("\n",leftLabel[r]),
            filew.write("\n"+leftLabel[r])
            for c in range(len(topLabel)):
                print("{:4}".format(mtx[r][c])),
                filew.write("{:4}".format(mtx[r][c]))
        filew.close()

    #write 2D matrix accept matrix with real numbers
    def write2DmatrixReal(self,mtxName,topLabel=[],leftLabel=[],mtx=[]):
        filew = open("Output.txt","a")
        print("\n\n" , mtxName)
        filew.write("\n\n" + mtxName)
        print("{:5s}".format("")),
        filew.write("\n"+"{:5s}".format(""))
        for c in range(len(topLabel)):
            print("{:7s}".format(topLabel[c])),
            filew.write("{:7s}".format(topLabel[c]))
        for r in range(len(mtx)):
            print("\n", leftLabel[r]),
            filew.write("\n"+leftLabel[r])
            for c in range(len(mtx)):
                print("{:7.4f}".format(mtx[r][c])),
                filew.write("{:7.4f}".format(mtx[r][c]))
        filew.close()
