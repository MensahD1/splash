class Metadata:
    def __init__(self,dict):
        self.dict = dict
        self.name = dict["name"]
        self.period = dict["active"]
        self.pos = dict["position"]
        self.height = dict["height"]
        self.weight = dict["weight"]
        self.nickname = dict["nicknames"]
        self.birthdate = dict["birthdate"]
        self.birthplace = dict["birthplace"]
        self.age = dict["age"]
        self.college = dict["college"]
        self.hand = dict["hand"]
        self.image = dict["image"]
        self.pick = dict["pick"]
        self.draftTeam = dict["draftTeam"]
        self.link = dict["link"]
        self.extra = []

    def getName(self):
        return self.name
    def getPeriod(self):
        return self.period
    def getPos(self):
        return self.pos
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight
    def getPeriod(self):
        return self.period
    def getNickname(self):
        return self.nickname
    def getDate(self):
        return self.birthdate
    def getPlace(self):
        return self.birthplace
    def getAge(self):
        return self.age
    def getCollege(self):
        return self.college
    def getHand(self):
        return self.hand
    def getPick(self):
        return self.pick
    def getImage(self):
        return self.image
    def getDraftTeam(self):
        return self.draftTeam
    def getAll(self):
        return self.dict
