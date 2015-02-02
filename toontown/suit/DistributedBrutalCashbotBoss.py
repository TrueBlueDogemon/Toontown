from toontown.suit.DistributedCashbotBoss import DistributedCashbotBoss


class DistributedBrutalCashbotBoss(DistributedCashbotBoss):
    notify = directNotify.newCategory('DistributedBrutalCashbotBoss')

    def announceGenerate(self):
        DistributedCashbotBoss.announceGenerate(self)

        base.localAvatar.setCanUseUnites(False)

    def disable(self):
        DistributedCashbotBoss.disable(self)

        base.localAvatar.setCanUseUnites(True)
