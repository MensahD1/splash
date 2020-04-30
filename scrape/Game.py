class Game:
    def __init__(self,dict):

        self.dict = dict
        self.date = dict["date"]
        self.wasHome = dict["wasHome"]
        self.rival = dict["opponent"]
        self.wasWin = dict["wasWin"]
        self.netScore = dict["netScore"]
        self.MP = dict["MP"]
        self.threeP = dict["3P"]
        self.threePA= dict["3PA"]
        self.twoP = dict["2P"]
        self.twoPA= dict["2PA"]
        self.FT = dict["FT"]
        self.FTA= dict["FTA"]
        self.ORB = dict["ORB"]
        self.DRB = dict["DRB"]
        self.AST = dict["AST"]
        self.STL = dict["STL"]
        self.BLK = dict["BLK"]
        self.TOV = dict["TOV"]
        self.PF = dict["PF"]
        self.PTS = dict["PTS"]
        self.rivalRoster = dict["opponentRoster"]
        self.wasPlayoff = dict["wasPlayoff"]
        self.extra = []

    def getGame(self):
        return self.date
    def getOpponent(self):
        return self.rival
    def wasHome(self):
        return self.wasHome
    def wasWin(self):
        return self.wasWin
    def getMP(self):
        return self.MP
    def get3P(self):
        return self.threeP
    def get3PA(self):
        return self.threePA
    def get3PP(self):
        return self.threeP/self.threePA
    def get2P(self):
        return self.twoP
    def get2PA(self):
        return self.twoPA
    def get2PP(self):
        return self.twoP/self.twoPA
    def getFG(self):
        return self.threeP + self.twoP
    def getFGA(self):
        return self.threePA + self.twoPA
    def getFGP(self):
        return self.getFG()/self.getFGA()
    def getFT(self):
        return self.FT
    def getFTA(self):
        return self.FTA
    def getFTP(self):
        return self.FT/self.FTA
    def getORB(self):
        return self.ORB
    def getDRB(self):
        return self.DRB
    def getTRB(self):
        return self.DRB + self.ORB
    def getAST(self):
        return self.AST
    def getSTL(self):
        return self.STL
    def getBLK(self):
        return self.BLK
    def getTOV(self):
        return self.TOV
    def getPF(self):
        return self.PF
    def getPTS(self):
        return self.PTS
    def wasPlayoff(self):
        return self.wasPlayoff
    def getRivalRoster(self):
        return self.rivalRoster
    def getAll(self):
        return self.dict
