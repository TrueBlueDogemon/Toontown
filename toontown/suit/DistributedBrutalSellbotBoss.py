from pandac.PandaModules import Point3

from toontown.suit.DistributedSellbotBoss import DistributedSellbotBoss
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.chat import ChatGlobals

from direct.interval.IntervalGlobal import *


class DistributedBrutalSellbotBoss(DistributedSellbotBoss):
    notify = directNotify.newCategory('DistributedBrutalSellbotBoss')

    ANIM_PLAYRATE = 3

    def announceGenerate(self):
        DistributedSellbotBoss.announceGenerate(self)

        base.localAvatar.setCanUseUnites(False)

    def disable(self):
        DistributedSellbotBoss.disable(self)

        base.localAvatar.setCanUseUnites(True)

    def makeIntroductionMovie(self, delayDeletes):
        track = Parallel()
        camera.reparentTo(render)
        camera.setPosHpr(0, 25, 30, 0, 0, 0)
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        dooberTrack = Parallel()

        if self.doobers:
            self._DistributedSellbotBoss__doobersToPromotionPosition(self.doobers[:4], self.battleANode)
            self._DistributedSellbotBoss__doobersToPromotionPosition(self.doobers[4:], self.battleBNode)
            turnPosA = ToontownGlobals.SellbotBossDooberTurnPosA
            turnPosB = ToontownGlobals.SellbotBossDooberTurnPosB
            self._DistributedSellbotBoss__walkDoober(self.doobers[0], 0, turnPosA, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[1], 4, turnPosA, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[2], 8, turnPosA, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[3], 12, turnPosA, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[7], 2, turnPosB, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[6], 6, turnPosB, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[5], 10, turnPosB, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[4], 14, turnPosB, dooberTrack, delayDeletes)

        toonTrack = Parallel()
        self._DistributedSellbotBoss__toonsToPromotionPosition(self.toonsA, self.battleANode)
        self._DistributedSellbotBoss__toonsToPromotionPosition(self.toonsB, self.battleBNode)
        delay = 0

        for toonId in self.toonsA:
            self._DistributedSellbotBoss__walkToonToPromotion(toonId, delay, self.toonsEnterA, toonTrack, delayDeletes)
            delay += 1

        for toonId in self.toonsB:
            self._DistributedSellbotBoss__walkToonToPromotion(toonId, delay, self.toonsEnterB, toonTrack, delayDeletes)
            delay += 1

        toonTrack.append(Sequence(Wait(delay), self.closeDoors))
        self.rampA.request('extended')
        self.rampB.request('extended')
        self.rampC.request('retracted')
        self.clearChat()
        self.cagedToon.clearChat()

        promoteDoobers = TTLocalizer.BrutalBossCogPromoteDoobers
        doobersAway = TTLocalizer.BrutalBossCogDoobersAway
        welcomeToons = TTLocalizer.BrutalBossCogWelcomeToons
        promoteToons = TTLocalizer.BrutalBossCogPromoteToons
        discoverToons = TTLocalizer.BrutalBossCogDiscoverToons
        attackToons = TTLocalizer.BrutalBossCogAttackToons
        interruptBoss = TTLocalizer.BrutalCagedToonInterruptBoss
        rescueQuery = TTLocalizer.BrutalCagedToonRescueQuery

        bossAnimTrack = Sequence(
            ActorInterval(self, 'Ff_speech', startTime=2, duration=10, loop=1),
            ActorInterval(self, 'ltTurn2Wave', duration=2),
            ActorInterval(self, 'wave', duration=4, loop=1),
            ActorInterval(self, 'ltTurn2Wave', startTime=2, endTime=0),
            ActorInterval(self, 'Ff_speech', duration=7, loop=1))
        track.append(bossAnimTrack)

        dialogTrack = Track(
            (0, Parallel(
                camera.posHprInterval(8, Point3(-22, -100, 35), Point3(-10, -13, 0), blendType='easeInOut'),
                IndirectInterval(toonTrack, 0, 18))),
            (5.6, Func(self.setChatAbsolute, promoteDoobers, ChatGlobals.CFSpeech)),
            (9, IndirectInterval(dooberTrack, 0, 9)),
            (10, Sequence(
                Func(self.clearChat),
                Func(camera.setPosHpr, -23.1, 15.7, 17.2, -160, -2.4, 0))),
            (12, Func(self.setChatAbsolute, doobersAway, ChatGlobals.CFSpeech)),
            (16, Parallel(
                Func(self.clearChat),
                Func(camera.setPosHpr, -25, -99, 10, -14, 10, 0),
                IndirectInterval(dooberTrack, 14),
                IndirectInterval(toonTrack, 30))),
            (18, Func(self.setChatAbsolute, welcomeToons, ChatGlobals.CFSpeech)),
            (22, Func(self.setChatAbsolute, promoteToons, ChatGlobals.CFSpeech)),
            (22.2, Sequence(
                Func(self.cagedToon.nametag3d.setScale, 2),
                Func(self.cagedToon.setChatAbsolute, interruptBoss, ChatGlobals.CFSpeech),
                ActorInterval(self.cagedToon, 'wave'),
                Func(self.cagedToon.loop, 'neutral'))),
            (25, Sequence(
                Func(self.clearChat),
                Func(self.cagedToon.clearChat),
                Func(camera.setPosHpr, -12, -15, 27, -151, -15, 0),
                ActorInterval(self, 'Ff_lookRt'))),
            (27, Sequence(
                Func(self.cagedToon.setChatAbsolute, rescueQuery, ChatGlobals.CFSpeech),
                Func(camera.setPosHpr, -12, 48, 94, -26, 20, 0),
                ActorInterval(self.cagedToon, 'wave'),
                Func(self.cagedToon.loop, 'neutral'))),
            (31, Sequence(
                Func(camera.setPosHpr, -20, -35, 10, -88, 25, 0),
                Func(self.setChatAbsolute, discoverToons, ChatGlobals.CFSpeech),
                Func(self.cagedToon.nametag3d.setScale, 1),
                Func(self.cagedToon.clearChat),
                ActorInterval(self, 'turn2Fb'))),
            (34, Sequence(
                Func(self.clearChat),
                self.loseCogSuits(self.toonsA, self.battleANode, (0, 18, 5, -180, 0, 0)),
                self.loseCogSuits(self.toonsB, self.battleBNode, (0, 18, 5, -180, 0, 0)))),
            (37, Sequence(
                self.toonNormalEyes(self.involvedToons),
                Func(camera.setPosHpr, -23.4, -145.6, 44.0, -10.0, -12.5, 0),
                Func(self.loop, 'Fb_neutral'),
                Func(self.rampA.request, 'retract'),
                Func(self.rampB.request, 'retract'),
                Parallel(self.backupToonsToBattlePosition(self.toonsA, self.battleANode),
                         self.backupToonsToBattlePosition(self.toonsB, self.battleBNode),
                         Sequence(
                             Wait(2),
                             Func(self.setChatAbsolute, attackToons, ChatGlobals.CFSpeech))))))
        track.append(dialogTrack)

        return Sequence(Func(self.stickToonsToFloor), track, Func(self.unstickToons), name=self.uniqueName('Introduction'))