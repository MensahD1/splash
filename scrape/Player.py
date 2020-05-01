class Player:
    additonals = []
    def __init__(self,metadata,seasons):
        self.metadata = metadata
        self.career = seasons


    def getMetadata(self):
        return self.metadata
    def getCareer(self):
        return self.career

    def getTotals(self):
        totals = {"GP":0,"MP":0,"3P":0,"3PA":0,"2P":0, "2PA":0,"FT":0,"FTA":0,
            "ORB":0,"DRB":0,"AST":0,"STL":0,"BLK":0,"TOV":0,"PF":0,"PTS":0}

        for season in self.career:
            totals["GP"] += season.getAll()["GP"]
            totals["MP"] += season.getAll()["MP"]
            totals["3P"] += season.getAll()["3P"]
            totals["3PA"] += season.getAll()["3PA"]
            totals["2P"] += season.getAll()["2P"]
            totals["2PA"] += season.getAll()["2PA"]
            totals["FT"] += season.getAll()["FT"]
            totals["FTA"] += season.getAll()["FTA"]
            totals["ORB"] += season.getAll()["ORB"]
            totals["DRB"] += season.getAll()["DRB"]
            totals["AST"] += season.getAll()["AST"]
            totals["STL"] += season.getAll()["STL"]
            totals["BLK"] += season.getAll()["BLK"]
            totals["TOV"] += season.getAll()["TOV"]
            totals["PF"] += season.getAll()["PF"]
            totals["PTS"] += season.getAll()["PTS"]
        return totals

    def getTotalPerGame(self):

        avgs = self.getTotals()
        numgames = avgs["GP"]

        for i in avgs.keys():
            avgs[i] = avg[i]/numgames

        return avgs

    def getTotalPerMin(self):

        avgs = self.getTotals()
        numMin = avgs["MP"]

        for i in avgs.keys():
            avgs[i] = avg[i]/numMin

        return avgs
