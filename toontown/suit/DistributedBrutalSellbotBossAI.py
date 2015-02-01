from toontown.suit.DistributedSellbotBossAI import DistributedSellbotBossAI
from toontown.suit import BrutalSellbotBossGlobals
from toontown.toonbase import ToontownGlobals
from toontown.toon import NPCToons

import random


class DistributedBrutalSellbotBossAI(DistributedSellbotBossAI):
    notify = directNotify.newCategory('DistributedBrutalSellbotBossAI')

    SOS_AMOUNT = 2

    def __init__(self, air):
        DistributedSellbotBossAI.__init__(self, air)

        self.cagedToonNpcId = random.choice(NPCToons.BrutalSellbotNPCS.keys())
        self.numPies = 0

    def enterBattleThree(self):
        DistributedSellbotBossAI.enterBattleThree(self)

        self.numPies = BrutalSellbotBossGlobals.PieCount[self.getToonDifficulty()-1]

    def hitToon(self, toonId):
        pass

    def zapToon(self, x, y, z, h, p, r, bpx, bpy, attackCode, timestamp):
        avId = self.air.getAvatarIdFromSender()

        if not self.validate(avId, avId in self.involvedToons, 'zapToon from unknown avatar'):
            return

        if attackCode == ToontownGlobals.BossCogLawyerAttack and self.dna.dept != 'l':
            self.notify.warning('got lawyer attack but not in CJ boss battle')
            return

        toon = simbase.air.doId2do.get(avId)
        if toon:
            self.d_showZapToon(avId, x, y, z, h, p, r, attackCode, timestamp)

            damage = BrutalSellbotBossGlobals.getDamageFromAttackCode(attackCode)
            self.damageToon(toon, damage)

            currState = self.getCurrentOrNextState()

            if attackCode == ToontownGlobals.BossCogElectricFence and (currState == 'RollToBattleTwo' or currState == 'BattleThree'):
                if bpy < 0 and abs(bpx / bpy) > 0.5:
                    if bpx < 0:
                        self.b_setAttackCode(ToontownGlobals.BossCogSwatRight)
                    else:
                        self.b_setAttackCode(ToontownGlobals.BossCogSwatLeft)

    def generateSuits(self, battleNumber):
        if battleNumber == 1:
            return self.invokeSuitPlanner(18, 0, randomRevives=True)
        else:
            return self.invokeSuitPlanner(19, 0)

    def touchCage(self):
        avId = self.air.getAvatarIdFromSender()
        currState = self.getCurrentOrNextState()
        if currState != 'BattleThree' and currState != 'NearVictory':
            return
        if not self.validate(avId, avId in self.involvedToons, 'touchCage from unknown avatar'):
            return
        toon = simbase.air.doId2do.get(avId)
        if toon:
            if self.hasToonTouchedCage(toon):
                return
            toon.b_setNumPies(self.numPies)
            self.setToonTouchedCage(toon)
            self.toonDidGoodJump(avId)

    def removeToon(self, avId):
        av = self.air.doId2do.get(avId)

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