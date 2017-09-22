#python

#this module handles relates to interactions with the user


class CallScreen:

    def __init__(self):
        self.data = []

    def dataget(self, date, you, installer, owner, gisnum, address, subdivision, systype):

        self.d = (date)
        self.y = (you)
        self.i = (installer)
        self.o = (owner)
        self.g = (gisnum)
        self.a = (address)
        self.s = (subdivision)
        self.t = (systype)

    def feedstats(self):
        wasteFlow = self.t * self.p
        BODLBS = self.t * self.p * self.s / 1000000 * 8.34
        gritLBS = self.t * self.p * self.g / 1000000 * 8.34
        print(" Wastewater influent is " + str(wasteFlow) + " GPD")
        print("BOD loading is: " + str(BODLBS) + "LBS/day")
        print("Grit Loading is" + str(gritLBS) + "LBS/day")