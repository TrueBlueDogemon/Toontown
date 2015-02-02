from toontown.suit.DistributedCashbotBoss import DistributedCashbotBoss
from toontown.toonbase import ToontownGlobals


class DistributedBrutalCashbotBoss(DistributedCashbotBoss):
    notify = directNotify.newCategory('DistributedBrutalCashbotBoss')

    ANIM_PLAYRATE = 1.5

    def __init__(self, cr):
        DistributedCashbotBoss.__init__(self, cr)

        self.bossMaxDamage = ToontownGlobals.BrutalCashbotBossMaxDamage

    def announceGenerate(self):
        DistributedCashbotBoss.announceGenerate(self)

        base.localAvatar.setCanUseUnites(False)

    def disable(self):
        DistributedCashbotBoss.disable(self)

        base.localAvatar.setCanUseUnites(True)
