from toontown.suit.DistributedSellbotBossAI import DistributedSellbotBossAI
from toontown.suit import BrutalSellbotBossGlobals
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
