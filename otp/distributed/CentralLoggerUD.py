from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class CentralLoggerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("CentralLoggertUD")

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

    def sendMessage(self, category, description, sender, receiver):
        self.air.writeServerEvent(category, sender, receiver, description)

    def logAIGarbage(self):
        pass
