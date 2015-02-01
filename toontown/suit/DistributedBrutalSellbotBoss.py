from toontown.suit.DistributedSellbotBoss import DistributedSellbotBoss


class DistributedBrutalSellbotBoss(DistributedSellbotBoss):
    notify = directNotify.newCategory('DistributedBrutalSellbotBoss')

    ANIM_PLAYRATE = 3

    def announceGenerate(self):
        DistributedSellbotBoss.announceGenerate(self)

        base.localAvatar.setCanUseUnites(False)

    def disable(self):
        DistributedSellbotBoss.disable(self)

        base.localAvatar.setCanUseUnites(True)
