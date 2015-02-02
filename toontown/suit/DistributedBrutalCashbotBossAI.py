from toontown.suit.DistributedCashbotBossAI import DistributedCashbotBossAI
from toontown.coghq.DistributedCashbotBossCraneAI import DistributedCashbotBossCraneAI
from toontown.toonbase import ToontownGlobals


class DistributedBrutalCashbotBossAI(DistributedCashbotBossAI):
    notify = directNotify.newCategory('DistributedBrutalCashbotBoss')

    def __init__(self, air):
        DistributedCashbotBossAI.__init__(self, air)

        self.bossMaxDamage = ToontownGlobals.BrutalCashbotBossMaxDamage
        self.setMakeBattleFreeObjects(self.newMakeBattleThreeObjects)

    def generateSuits(self, battleNumber):
        return self.invokeSuitPlanner(20, 0)

    def newMakeBattleThreeObjects(self):
        if self.cranes is None:
            self.cranes = []
            for index in xrange(len(ToontownGlobals.CashbotBossCranePosHprs)):
                crane = DistributedCashbotBossCraneAI(self.air, self, index)
                crane.generateWithRequired(self.zoneId)
                self.cranes.append(crane)

        if self.goons is None:
            self.goons = []

    def recordHit(self, damage):
        avId = self.air.getAvatarIdFromSender()

        if not self.validate(avId, avId in self.involvedToons, 'recordHit from unknown avatar'):
            return

        if self.state != 'BattleThree':
            return

        self.b_setBossDamage(self.bossDamage + damage)

        if self.bossDamage >= self.bossMaxDamage:
            self.b_setState('Victory')

        self.b_setAttackCode(ToontownGlobals.BossCogNoAttack)

    def waitForNextHelmet(self):
        pass

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