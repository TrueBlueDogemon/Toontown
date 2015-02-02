from toontown.suit.DistributedCashbotBossAI import DistributedCashbotBossAI


class DistributedBrutalCashbotBossAI(DistributedCashbotBossAI):
    notify = directNotify.newCategory('DistributedBrutalCashbotBoss')

    def removeToon(self, avId):
        av = self.air.doId2do.get(avId)

        if self.cranes is not None:
            for crane in self.cranes:
                crane.removeToon(avId)

        if self.safes is not None:
            for safe in self.safes:
                safe.removeToon(avId)

        if self.goons is not None:
            for goon in self.goons:
                goon.removeToon(avId)

        if avId in self.looseToons:
            self.looseToons.remove(avId)

        if avId in self.involvedToons:
            self.involvedToons.remove(avId)

        if avId in self.toonsA:
            self.toonsA.remove(avId)

        if avId in self.toonsB:
            self.toonsB.remove(avId)

        if avId in self.nearToons:
            self.nearToons.remove(avId)

        event = self.air.getAvatarExitEvent(avId)
        self.ignore(event)
        if not self.hasToons():
            taskMgr.doMethodLater(10, self.getBossDoneFunc(), self.uniqueName('BossDone'))