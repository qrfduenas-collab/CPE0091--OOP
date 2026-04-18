from Character import Character

class Novice:
    def __init__(self, username):
        self.username = username
        self.hp = 100
        self.damage = 10
        self.str = 0
        self.vit = 0
        self.int = 0
        self.agi = 0

    def getUsername(self):
        return self.username

    def getHp(self):
        return self.hp

    def setHp(self, value):
        self.hp = value

    def getDamage(self):
        return self.damage

    def reduceHp(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def addHp(self, value):
        self.hp += value


    def setStr(self, value):
        self.str = value

    def getStr(self):
        return self.str

    def setVit(self, value):
        self.vit = value

    def getVit(self):
        return self.vit

    def setInt(self, value):
        self.int = value

    def getInt(self):
        return self.int

    def setAgi(self, value):
        self.agi = value

    def getAgi(self):
        return self.agi  
    
#character1 = Novice("Your Username")
#print(character1.getUsername())
#print(character1.getHp())
