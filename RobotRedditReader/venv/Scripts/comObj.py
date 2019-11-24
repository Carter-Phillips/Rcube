class comObj:

    def __init__(self, comString, userName, date):
        self.comString = comString
        self.userName = userName
        self.permission = False
        self.date = date

    def getUser(self):
        return self.userName

    def getCom(self):
        return self.comString

    def setPerm(self, perm):
        self.permission = perm;

    def save(self):
        f = open(str(self.date + " " + self.userName) + ".txt", "w+")
        f.seek(0)
        f.truncate()
        f.write(str(self.permission) + "\n")
        f.write(str(self.date) + "\n")
        f.write(self.userName + "\n")
        f.write(self.comString)