class Season:
    def __init__(self,dict):

        self.dict = dict
        self.year = dict["year"]
        self.age = dict["age"]
        self.team = dict["team"]
        self.position = dict["position"]
        self.GP = dict["GP"]
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
        self.link = dict["link"]
        self.games = dict["games"]
        self.salary = dict["salary"]
        self.roster = dict["roster"]
        self.wentPlayoffs = dict["wentPlayoffs"]
        self.wasChamp = dict["wasChamp"]
        self.extra = []

    def getYear(self):
        return self.year
    def getAge(self):
        return self.age
    def getTeam(self):
        return self.team
    def getPosition(self):
        return self.position
    def getGP(self):
        return self.GP
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
    def getLink(self):
        return self.link
    def getGames(self):
        return self.games
    def getSalary(self):
        return self.salary
    def getRoster(self):
        return self.roster
    def isPlayoffs(self):
        return self.wentPlayoffs
    def isChamp(self):
        return self.wasChamp
    def getAll(self):
        return self.dict
