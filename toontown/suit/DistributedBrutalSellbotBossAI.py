from toontown.suit.DistributedSellbotBossAI import DistributedSellbotBossAI
from toontown.toon import NPCToons

import random


class DistributedBrutalSellbotBossAI(DistributedSellbotBossAI):
    notify = directNotify.newCategory('DistributedBrutalSellbotBossAI')

    def __init__(self, air):
        DistributedSellbotBossAI.__init__(self, air)

        self.cagedToonNpcId = random.choice(NPCToons.BrutalSellbotNPCS.keys())
