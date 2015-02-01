from toontown.building.DistributedVPElevator import DistributedVPElevator
from toontown.toonbase import TTLocalizer


class DistributedBrutalVPElevator(DistributedVPElevator):
    def setupElevator(self):
        pass

    def getDestName(self):
        return TTLocalizer.ElevatorBrutalSellBotBoss
